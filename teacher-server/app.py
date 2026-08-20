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
USED_PATH = "assets/used-ledger.json"
REVOKED_PATH = "assets/revoked-jti.json"
LABS_REPO = _env("GITHUB_LABS_REPO", "python-strudy-labs")
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



def _get_json_file(token: str, repo: str, path: str) -> tuple[dict, str | None]:
    url = f"https://api.github.com/repos/{OWNER}/{repo}/contents/{path}"
    r = requests.get(url, headers=_gh_headers(token), timeout=20)
    if r.status_code == 404:
        return {}, None
    if r.status_code >= 400:
        raise RuntimeError(f"Read {path} failed ({r.status_code}): {r.text[:200]}")
    data = r.json()
    content = base64.b64decode(data["content"]).decode("utf-8")
    parsed = json.loads(content) if content.strip() else {}
    if not isinstance(parsed, dict):
        parsed = {}
    return parsed, data.get("sha")


def _put_json_file(token: str, repo: str, path: str, obj: dict, sha: str | None, message: str) -> None:
    body = json.dumps(obj, indent=2) + "\n"
    payload: dict[str, Any] = {
        "message": message,
        "content": base64.b64encode(body.encode("utf-8")).decode("ascii"),
    }
    if sha:
        payload["sha"] = sha
    url = f"https://api.github.com/repos/{OWNER}/{repo}/contents/{path}"
    r = requests.put(url, headers=_gh_headers(token), json=payload, timeout=20)
    if r.status_code >= 400:
        raise RuntimeError(f"Write {path} failed ({r.status_code}): {r.text[:240]}")


def _get_lab_file(token: str, path: str) -> tuple[str, str]:
    rel = str(path or "").replace("\\", "/").lstrip("/")
    if not rel.startswith("labs/") or ".." in rel or rel.endswith("/"):
        raise ValueError("Invalid lab path")
    url = f"https://api.github.com/repos/{OWNER}/{LABS_REPO}/contents/{rel}"
    r = requests.get(url, headers=_gh_headers(token), timeout=20)
    if r.status_code == 404:
        raise FileNotFoundError(rel)
    if r.status_code >= 400:
        raise RuntimeError(f"Lab fetch failed ({r.status_code}): {r.text[:200]}")
    data = r.json()
    raw = base64.b64decode(data["content"])
    # text if decodes, else base64 for images
    try:
        text = raw.decode("utf-8")
        if "\x00" not in text:
            return "text", text
    except UnicodeDecodeError:
        pass
    return "base64", base64.b64encode(raw).decode("ascii")


def normalize_code(raw: str) -> str:
    s = "".join(ch for ch in str(raw or "").upper() if ch.isalnum())
    if len(s) != 8:
        return ""
    return s[:4] + "-" + s[4:]


def _teacher_jwt(login: str, name: str, avatar: str) -> str:
    now = int(time.time())
    return jwt.encode(
        {
            "login": login,
            "name": name,
            "avatar": avatar,
            "role": "teacher",
            "jti": secrets.token_urlsafe(18),
            "iat": now,
            "exp": now + 12 * 3600,
            "iss": "python-strudy-teacher",
        },
        app.secret_key,
        algorithm="HS256",
    )


def _student_jwt(code_hash: str) -> str:
    now = int(time.time())
    return jwt.encode(
        {
            "role": "student",
            "hash": code_hash,
            "jti": secrets.token_urlsafe(18),
            "iat": now,
            "exp": now + 3 * 24 * 3600,
            "iss": "python-strudy-student",
        },
        app.secret_key,
        algorithm="HS256",
    )


_revoked_cache: tuple[float, set[str]] | None = None


def _revoked_jtis() -> set[str]:
    global _revoked_cache
    now = time.time()
    if _revoked_cache and now - _revoked_cache[0] < 30:
        return _revoked_cache[1]
    try:
        token = _installation_token()
        data, _sha = _get_json_file(token, REPO, REVOKED_PATH)
        rows = data.get("revoked") if isinstance(data, dict) else []
        out = set()
        cutoff = int(now)
        if isinstance(rows, list):
            for x in rows:
                if isinstance(x, str):
                    out.add(x)
                elif isinstance(x, dict) and x.get("jti") and int(x.get("exp") or 0) >= cutoff:
                    out.add(str(x["jti"]))
        _revoked_cache = (now, out)
        return out
    except Exception:
        return _revoked_cache[1] if _revoked_cache else set()


def _bearer_payload() -> dict | None:
    auth = request.headers.get("Authorization") or ""
    if not auth.lower().startswith("bearer "):
        return None
    raw = auth.split(" ", 1)[1].strip()
    try:
        data = jwt.decode(raw, app.secret_key, algorithms=["HS256"])
    except Exception:
        return None
    jti = str(data.get("jti") or "")
    if jti and jti in _revoked_jtis():
        return None
    return data


def teacher_identity() -> dict[str, str] | None:
    login = str(session.get("github_login") or "").lower()
    if login == TEACHER_LOGIN:
        return {
            "login": login,
            "name": str(session.get("github_name") or login),
            "avatar": str(session.get("github_avatar") or ""),
        }
    data = _bearer_payload()
    if not data or data.get("role") not in (None, "teacher"):
        if data and data.get("role") != "teacher":
            return None
    if data:
        login = str(data.get("login") or "").lower()
        if login == TEACHER_LOGIN:
            return {
                "login": login,
                "name": str(data.get("name") or login),
                "avatar": str(data.get("avatar") or ""),
            }
    return None


def student_identity() -> dict | None:
    data = _bearer_payload()
    if not data or data.get("role") != "student":
        return None
    return data


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
    data = None
    auth = request.headers.get("Authorization") or ""
    if auth.lower().startswith("bearer "):
        raw = auth.split(" ", 1)[1].strip()
        try:
            data = jwt.decode(raw, app.secret_key, algorithms=["HS256"], options={"verify_exp": False})
        except Exception:
            data = None
    if data and data.get("jti"):
        try:
            token = _installation_token()
            doc, sha = _get_json_file(token, REPO, REVOKED_PATH)
            rows = doc.get("revoked") if isinstance(doc, dict) else []
            if not isinstance(rows, list):
                rows = []
            now = int(time.time())
            rows = [x for x in rows if isinstance(x, dict) and int(x.get("exp") or 0) >= now]
            rows.append({"jti": str(data["jti"]), "exp": int(data.get("exp") or now + 12 * 3600)})
            _put_json_file(token, REPO, REVOKED_PATH, {"revoked": rows[-400:]}, sha, "Revoke teacher/student session")
            global _revoked_cache
            _revoked_cache = None
        except Exception:
            pass
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



@app.post("/api/redeem")
def api_redeem():
    if not _origin_ok():
        return jsonify({"ok": False, "error": "Origin not allowed."}), 403
    body = request.get_json(silent=True) or {}
    code = normalize_code(body.get("code") or "")
    if not code:
        return jsonify({"ok": False, "error": "Use a code like ABCD-EFGH."}), 400
    payload, check = code[:4], code[5:]
    now_ms = int(time.time() * 1000)
    bucket = now_ms // TTL_MS
    valid_bucket = None
    for b in (bucket, bucket - 1):
        if b < 0:
            continue
        if _checksum(payload, b) == check:
            valid_bucket = b
            break
    if valid_bucket is None:
        return jsonify({"ok": False, "error": "Invalid or expired code."}), 400
    code_hash = _sha256_hex(code)
    try:
        token = _installation_token()
        issued_doc, _ = _get_json_file(token, REPO, ISSUED_PATH)
        issued = issued_doc.get("issued") if isinstance(issued_doc, dict) else []
        row = None
        if isinstance(issued, list):
            for x in issued:
                if isinstance(x, dict) and x.get("hash") == code_hash and now_ms <= int(x.get("expires") or 0):
                    row = x
                    break
        if not row:
            return jsonify({"ok": False, "error": "This code was not issued by the GitHub owner."}), 400
        used_doc, used_sha = _get_json_file(token, REPO, USED_PATH)
        used = used_doc.get("used") if isinstance(used_doc, dict) else []
        if not isinstance(used, list):
            used = []
        hashes = {str(x.get("hash") if isinstance(x, dict) else x) for x in used}
        if code_hash in hashes:
            return jsonify({"ok": False, "error": "This code was already used."}), 409
        used.append({"hash": code_hash, "at": now_ms})
        _put_json_file(
            token,
            REPO,
            USED_PATH,
            {"used": used[-2000:], "note": "Hashes of redeemed lab codes. Global one-time ledger."},
            used_sha,
            "Record redeemed lab code",
        )
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 502
    until = (valid_bucket + 1) * TTL_MS
    tok = _student_jwt(code_hash)
    return jsonify({"ok": True, "token": tok, "until": until})


@app.get("/api/student")
def api_student():
    ident = student_identity()
    if not ident:
        return jsonify({"ok": False}), 401
    return jsonify({"ok": True, "until": ident.get("exp", 0) * 1000})


@app.get("/api/labs/file")
def api_lab_file():
    ident = student_identity()
    if not ident:
        return jsonify({"ok": False, "error": "Unlock labs with a passcode first."}), 401
    path = request.args.get("path") or ""
    try:
        token = _installation_token()
        kind, body = _get_lab_file(token, path)
    except FileNotFoundError:
        return jsonify({"ok": False, "error": "Lab file not found."}), 404
    except ValueError as e:
        return jsonify({"ok": False, "error": str(e)}), 400
    except Exception as e:
        msg = str(e)
        if "404" in msg or "Not Found" in msg:
            return jsonify({
                "ok": False,
                "error": "Lab store is private. Install GitHub App python-strudy-teacher on itsyst/python-strudy-labs.",
            }), 503
        return jsonify({"ok": False, "error": msg}), 502
    return jsonify({"ok": True, "path": path, "kind": kind, "content": body})



if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
