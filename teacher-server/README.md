# Teacher backend for python-strudy

Removes **all** personal access tokens from the browser.

```
Browser  →  this Flask app (OAuth session)  →  GitHub App installation token  →  assets/issued.json
```

Only GitHub user **`itsyst`** can open the desk and mint codes. Everyone else is rejected after OAuth.

## 1. Revoke any old PAT

If a token was ever pasted into `admin.html`:

1. GitHub → Settings → Developer settings → Personal access tokens → **Revoke**.
2. Check the repository audit log.

Never put a token in HTML, JS, `sessionStorage`, or `localStorage`.

## 2. Create a GitHub App (writes)

1. GitHub → Settings → Developer settings → **GitHub Apps** → New.
2. Name: e.g. `python-strudy-teacher`.
3. Homepage URL: your backend URL (or the Pages URL for now).
4. Webhook: disable (uncheck active).
5. Repository permissions:
   - **Contents**: Read and write
   - Everything else: No access
6. Where can this App be installed? **Only on this account**.
7. Create → generate a **private key** → download the `.pem`.
8. Install the App **only** on `itsyst/python-strudy`.
9. Note:
   - **App ID**
   - **Installation ID** (from the install URL: `.../installations/12345678`)
   - Private key PEM contents

## 3. Create a GitHub OAuth App (identity only)

1. GitHub → Settings → Developer settings → **OAuth Apps** → New.
2. Application name: `python-strudy-teacher-login`.
3. Homepage URL: `https://itsyst.github.io/python-strudy/`
4. Authorization callback URL: `https://YOUR-BACKEND.onrender.com/auth/callback`
5. Note **Client ID** and generate a **Client secret**.

Scope used: `read:user` only. The OAuth token is never given repository write access.

## 4. Deploy this folder

Any free host that runs Python works (Render, Railway, Fly.io, …).

Example **Render** free web service:

- Build: `pip install -r requirements.txt`
- Start: `gunicorn -b 0.0.0.0:$PORT app:app`
- Root directory: `teacher-server`

Set environment variables:

| Variable | Value |
|---|---|
| `FLASK_SECRET_KEY` | long random string |
| `GITHUB_OAUTH_CLIENT_ID` | from OAuth App |
| `GITHUB_OAUTH_CLIENT_SECRET` | from OAuth App |
| `GITHUB_APP_ID` | numeric App ID |
| `GITHUB_PRIVATE_KEY` | full PEM, newlines as `\n` |
| `GITHUB_INSTALLATION_ID` | installation id |
| `GITHUB_OWNER` | `itsyst` |
| `GITHUB_REPO` | `python-strudy` |
| `FRONTEND_ORIGIN` | `https://itsyst.github.io` |
| `PUBLIC_BASE_URL` | `https://YOUR-BACKEND.onrender.com` |
| `TEACHER_LOGIN` | `itsyst` (optional) |

After deploy, open `/health` — it should report `"configured": true`.

## 5. Point the static site at the backend

Edit `assets/teacher-api.json` on the Pages site:

```json
{
  "apiBase": "https://YOUR-BACKEND.onrender.com",
  "note": "Deployed teacher-server URL"
}
```

Commit and push. Open `admin.html` → **Sign in with GitHub**.

## Security model

| What | Where |
|---|---|
| OAuth client secret | server env only |
| GitHub App private key | server env only |
| Installation token | short-lived, server only |
| Teacher session cookie | HttpOnly + Secure + SameSite=None |
| Personal access token | **never used** |
| Plaintext codes | returned once to the teacher session, never stored in the repo |
| Code hashes | published to `assets/issued.json` |

Students only ever see public hashes. Forging a code requires knowing the pepper and matching a published hash.
