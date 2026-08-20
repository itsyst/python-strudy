from __future__ import annotations

import base64
import hashlib
import json
import os
import secrets
import time
from typing import Any

import jwt
import requests
from pathlib import Path as _Path
from flask import Flask, jsonify, redirect, request, session, send_from_directory


def _env(name: str, default: str = "") -> str:
    return (os.environ.get(name) or default).strip()


app = Flask(__name__)
app.secret_key = _env("FLASK_SECRET_KEY") or secrets.token_hex(32)
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="None",
    SESSION_COOKIE_SECURE=True,
)

OWNER = _env("GITHUB_OWNER", "itsyst")
REPO = _env("GITHUB_REPO", "python-strudy")
TEACHER_LOGIN = _env("TEACHER_LOGIN", OWNER).lower()
INSTALLATION_ID = int(_env("GITHUB_INSTALLATION_ID", "0") or "0")
FRONTEND_ORIGIN = _env("FRONTEND_ORIGIN", "https://itsyst.github.io").rstrip("/")
PUBLIC_BASE_URL = _env("PUBLIC_BASE_URL").rstrip("/")
OAUTH_CLIENT_ID = _env("GITHUB_OAUTH_CLIENT_ID")
OAUTH_CLIENT_SECRET = _env("GITHUB_OAUTH_CLIENT_SECRET")
APP_ID = _env("GITHUB_APP_ID")
PRIVATE_KEY_PEM = _env("GITHUB_PRIVATE_KEY").replace("\\n", "\n")

ISSUED_PATH = "assets/issued.json"
HERE = _Path(__file__).resolve().parent
TTL_MS = 3 * 24 * 60 * 60 * 1000
ALPH = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
PEPPER = "TDDE24|python-strudy|lab-gate|2026"


@app.after_request
def add_cors(resp):
    origin = request.headers.get("Origin", "")
    allowed_local = origin.startswith("http://localhost") or origin.startswith("http://127.0.0.1")
    if origin == FRONTEND_ORIGIN or origin.startswith(FRONTEND_ORIGIN + "/") or allowed_local:
        resp.headers["Access-Control-Allow-Origin"] = origin
        resp.headers["Access-Control-Allow-Credentials"] = "true"
        resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        resp.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        resp.headers["Vary"] = "Origin"
    return resp


@app.route("/api/<path:_any>", methods=["OPTIONS"])
@app.route("/auth/<path:_any>", methods=["OPTIONS"])
def options_ok(_any=None):
    return "", 204


def _sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _bytes_to_code_chars(data: bytes, n: int) -> str:
    out = []
    for i in range(n):
        out.append(ALPH[data[i % len(data)] % len(ALPH)])
    return "".join(out)


def _time_bucket(ts_ms: int) -> int:
    return ts_ms // TTL_MS


def _checksum(payload: str, bucket: int) -> str:
    digest = hashlib.sha256(f"{PEPPER}|code|{payload}|{bucket}".encode("utf-8")).digest()
    return _bytes_to_code_chars(digest, 4)


def mint_code(now_ms: int | None = None) -> dict[str, Any]:
    now_ms = now_ms or int(time.time() * 1000)
    rnd = secrets.token_bytes(8)
    payload = _bytes_to_code_chars(rnd, 4)
    bucket = _time_bucket(now_ms)
    check = _checksum(payload, bucket)
    code = f"{payload}-{check}"
    return {
        "code": code,
        "hash": _sha256_hex(code),
        "created": now_ms,
        "expires": (bucket + 1) * TTL_MS,
    }


def _app_jwt() -> str:
    if not APP_ID or not PRIVATE_KEY_PEM:
        raise RuntimeError("GITHUB_APP_ID / GITHUB_PRIVATE_KEY not configured")
    now = int(time.time())
    payload = {"iat": now - 60, "exp": now + 9 * 60, "iss": APP_ID}
    return jwt.encode(payload, PRIVATE_KEY_PEM, algorithm="RS256")


def _installation_token() -> str:
    if not INSTALLATION_ID:
        raise RuntimeError("GITHUB_INSTALLATION_ID not configured")
    token_jwt = _app_jwt()
    r = requests.post(
        f"https://api.github.com/app/installations/{INSTALLATION_ID}/access_tokens",
        headers={
            "Authorization": f"Bearer {token_jwt}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
        timeout=20,
    )
    if r.status_code >= 400:
        raise RuntimeError(f"Installation token failed ({r.status_code}): {r.text[:200]}")
    return r.json()["token"]


def _gh_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def _get_issued(token: str) -> tuple[list[dict], str | None]:
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{ISSUED_PATH}"
    r = requests.get(url, headers=_gh_headers(token), timeout=20)
    if r.status_code == 404:
        return [], None
    if r.status_code >= 400:
        raise RuntimeError(f"Read issued.json failed ({r.status_code}): {r.text[:200]}")
    data = r.json()
    content = base64.b64decode(data["content"]).decode("utf-8")
    parsed = json.loads(content)
    issued = parsed.get("issued") if isinstance(parsed, dict) else []
    if not isinstance(issued, list):
        issued = []
    return issued, data.get("sha")


def _put_issued(token: str, issued: list[dict], sha: str | None) -> None:
    body = json.dumps({"issued": issued}, indent=2) + "\n"
    payload: dict[str, Any] = {
        "message": "Issue lab passcodes (teacher-server)",
        "content": base64.b64encode(body.encode("utf-8")).decode("ascii"),
    }
    if sha:
        payload["sha"] = sha
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{ISSUED_PATH}"
    r = requests.put(url, headers=_gh_headers(token), json=payload, timeout=20)
    if r.status_code >= 400:
        raise RuntimeError(f"Publish issued.json failed ({r.status_code}): {r.text[:240]}")


def _teacher_jwt(login: str, name: str, avatar: str) -> str:
    now = int(time.time())
    return jwt.encode(
        {
            "login": login,
            "name": name,
            "avatar": avatar,
            "iat": now,
            "exp": now + 12 * 3600,
            "iss": "python-strudy-teacher",
        },
        app.secret_key,
        algorithm="HS256",
    )


def teacher_identity() -> dict[str, str] | None:
    login = str(session.get("github_login") or "").lower()
    if login == TEACHER_LOGIN:
        return {
            "login": login,
            "name": str(session.get("github_name") or login),
            "avatar": str(session.get("github_avatar") or ""),
        }
    auth = request.headers.get("Authorization") or ""
    if auth.lower().startswith("bearer "):
        raw = auth.split(" ", 1)[1].strip()
        try:
            data = jwt.decode(raw, app.secret_key, algorithms=["HS256"])
        except Exception:
            return None
        login = str(data.get("login") or "").lower()
        if login == TEACHER_LOGIN:
            return {
                "login": login,
                "name": str(data.get("name") or login),
                "avatar": str(data.get("avatar") or ""),
            }
    return None


def require_teacher() -> bool:
    return teacher_identity() is not None


def _oauth_redirect_uri() -> str:
    base = PUBLIC_BASE_URL or request.url_root.rstrip("/")
    return f"{base}/auth/callback"


def _allowed_frontends() -> list[str]:
    out = []
    if PUBLIC_BASE_URL:
        out.append(PUBLIC_BASE_URL)
    if FRONTEND_ORIGIN:
        out.append(FRONTEND_ORIGIN)
    out.append("https://python-strudy-backend.vercel.app")
    # unique, stripped
    seen = []
    for u in out:
        u = u.rstrip("/")
        if u and u not in seen:
            seen.append(u)
    return seen


def _safe_next(url: str | None) -> str:
    default = f"{PUBLIC_BASE_URL}/desk" if PUBLIC_BASE_URL else f"{FRONTEND_ORIGIN}/python-strudy/admin.html"
    if not url:
        return default
    url = str(url).strip().split("#")[0]
    for base in _allowed_frontends():
        if url == base or url.startswith(base + "/") or url.startswith(base + "?"):
            return url
    return default


def _origin_ok() -> bool:
    origin = (request.headers.get("Origin") or "").rstrip("/")
    referer = request.headers.get("Referer") or ""
    allowed = _allowed_frontends()
    if origin:
        return origin in allowed
    return any(referer.startswith(base) for base in allowed)



@app.get("/desk")
@app.get("/admin")
@app.get("/admin.html")
def desk():
    return send_from_directory(HERE, "desk.html")


@app.get("/")
def index():
    return jsonify(
        {
            "service": "python-strudy-teacher",
            "owner": OWNER,
            "repo": REPO,
            "auth": "/auth/github",
            "session": "/api/session",
            "codes": "POST /api/codes",
        }
    )


@app.get("/health")
def health():
    missing = []
    if not OAUTH_CLIENT_ID:
        missing.append("GITHUB_OAUTH_CLIENT_ID")
    if not OAUTH_CLIENT_SECRET:
        missing.append("GITHUB_OAUTH_CLIENT_SECRET")
    if not APP_ID:
        missing.append("GITHUB_APP_ID")
    if not PRIVATE_KEY_PEM:
        missing.append("GITHUB_PRIVATE_KEY")
    if not INSTALLATION_ID:
        missing.append("GITHUB_INSTALLATION_ID")
    if not PUBLIC_BASE_URL:
        missing.append("PUBLIC_BASE_URL")
    ok = len(missing) == 0
    return jsonify({"ok": ok, "configured": ok, "missing": missing}), (200 if ok else 503)


@app.get("/auth/github")
def github_login():
    if not OAUTH_CLIENT_ID:
        return jsonify({"error": "OAuth not configured (GITHUB_OAUTH_CLIENT_ID)"}), 503
    state = secrets.token_urlsafe(32)
    session["oauth_state"] = state
    next_url = _safe_next(request.args.get("next"))
    session["oauth_next"] = next_url
    params = {
        "client_id": OAUTH_CLIENT_ID,
        "redirect_uri": _oauth_redirect_uri(),
        "state": state,
        "scope": "read:user",
    }
    q = "&".join(f"{k}={requests.utils.quote(str(v))}" for k, v in params.items())
    return redirect(f"https://github.com/login/oauth/authorize?{q}")


@app.get("/auth/callback")
def github_callback():
    if request.args.get("state") != session.pop("oauth_state", None):
        return "Invalid OAuth state", 400
    code = request.args.get("code")
    if not code:
        return "Missing code", 400
    token_r = requests.post(
        "https://github.com/login/oauth/access_token",
        headers={"Accept": "application/json"},
        data={
            "client_id": OAUTH_CLIENT_ID,
            "client_secret": OAUTH_CLIENT_SECRET,
            "code": code,
            "redirect_uri": _oauth_redirect_uri(),
        },
        timeout=20,
    )
    if token_r.status_code >= 400:
        return f"Token exchange failed: {token_r.text[:200]}", 502
    token_data = token_r.json()
    access_token = token_data.get("access_token")
    if not access_token:
        return f"No access_token: {token_data}", 502
    user_r = requests.get("https://api.github.com/user", headers=_gh_headers(access_token), timeout=20)
    if user_r.status_code >= 400:
        return "Could not read GitHub user", 502
    user = user_r.json()
    login = str(user.get("login") or "").lower()
    name = str(user.get("name") or login)
    avatar = str(user.get("avatar_url") or "")
    next_url = _safe_next(session.pop("oauth_next", None))
    if login != TEACHER_LOGIN:
        session.clear()
        sep = "&" if "?" in next_url else "?"
        return redirect(f"{next_url}{sep}err=forbidden&login={login}")
    session["github_login"] = login
    session["github_name"] = name
    session["github_avatar"] = avatar
    desk_token = _teacher_jwt(login, name, avatar)
    return redirect(f"{next_url}#ts={desk_token}")


@app.get("/api/session")
def api_session():
    ident = teacher_identity()
    if not ident:
        return jsonify({"ok": False, "login": None}), 401
    return jsonify({"ok": True, **ident})


@app.post("/api/logout")
def api_logout():
    session.clear()
    return jsonify({"ok": True})


@app.get("/api/issued")
def api_issued():
    if not require_teacher():
        return jsonify({"ok": False, "error": "Sign in required."}), 401
    now = int(time.time() * 1000)
    try:
        token = _installation_token()
        existing, _sha = _get_issued(token)
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 502
    live = [
        x
        for x in existing
        if isinstance(x, dict) and x.get("hash") and now <= int(x.get("expires") or 0)
    ]
    return jsonify({"ok": True, "codes": live})


@app.post("/api/codes/revoke")
def api_revoke():
    if not require_teacher() or not _origin_ok():
        return jsonify({"ok": False, "error": f"Forbidden — only @{TEACHER_LOGIN} can revoke codes."}), 403
    body = request.get_json(silent=True) or {}
    hashes = body.get("hashes") or []
    if body.get("hash"):
        hashes = list(hashes) + [body.get("hash")]
    hashes = {str(h).strip().lower() for h in hashes if h}
    all_of = bool(body.get("all"))
    now = int(time.time() * 1000)
    try:
        token = _installation_token()
        existing, sha = _get_issued(token)
        kept = []
        for x in existing:
            if not isinstance(x, dict) or not x.get("hash"):
                continue
            if now > int(x.get("expires") or 0):
                continue
            if all_of or str(x.get("hash") or "").lower() in hashes:
                continue
            kept.append(x)
        _put_issued(token, kept, sha)
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 502
    return jsonify({"ok": True, "codes": kept})


@app.post("/api/codes")
def api_codes():
    if not require_teacher() or not _origin_ok():
        return jsonify(
            {"ok": False, "error": f"Forbidden — only @{TEACHER_LOGIN} can generate codes."}
        ), 403
    body = request.get_json(silent=True) or {}
    try:
        count = int(body.get("count", 5))
    except (TypeError, ValueError):
        count = 5
    count = max(1, min(20, count))
    now = int(time.time() * 1000)
    fresh = [mint_code(now) for _ in range(count)]
    try:
        token = _installation_token()
        existing, sha = _get_issued(token)
        merged = [
            x
            for x in existing
            if isinstance(x, dict) and x.get("hash") and now <= int(x.get("expires") or 0)
        ]
        for c in fresh:
            merged.append({"hash": c["hash"], "expires": c["expires"], "at": now})
        _put_issued(token, merged, sha)
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 502
    return jsonify(
        {
            "ok": True,
            "codes": [{"code": c["code"], "expires": c["expires"], "hash": c["hash"]} for c in fresh],
            "issued": merged,
        }
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
