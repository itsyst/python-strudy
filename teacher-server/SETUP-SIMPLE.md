# Teacher backend — simple setup (click by click)

You only need to do this **once**. After that, open `admin.html` and sign in with GitHub.

---

## A. Create the two GitHub apps (5 minutes)

### A1 — GitHub App (writes codes to the repo)

1. Open: https://github.com/settings/apps/new
2. **GitHub App name:** `python-strudy-teacher` (any unique name)
3. **Homepage URL:** `https://itsyst.github.io/python-strudy/`
4. Uncheck **Webhook** → Active
5. Under **Repository permissions** → **Contents** → **Read and write**
6. **Where can this GitHub App be installed?** → Only on this account
7. Click **Create GitHub App**
8. On the next page click **Generate a private key** → download the `.pem` file (save it)
9. Note the **App ID** (number at the top)
10. Click **Install App** (left sidebar) → Install → only select **python-strudy**
11. After install, the URL looks like:
    `https://github.com/settings/installations/12345678`
    → the number is your **Installation ID**

### A2 — OAuth App (login only)

1. Open: https://github.com/settings/developers → **OAuth Apps** → **New OAuth App**
2. **Application name:** `python-strudy-teacher-login`
3. **Homepage URL:** `https://itsyst.github.io/python-strudy/`
4. **Authorization callback URL:**  
   `https://YOUR-VERCEL-URL.vercel.app/auth/callback`  
   (you will fix this after Vercel deploy in step B)
5. Register → note **Client ID** → **Generate a new client secret** → copy it once

---

## B. Deploy on Vercel (you click Deploy)

1. Open: https://vercel.com/new
2. Import **itsyst/python-strudy**
3. **Root Directory** → `teacher-server` → Edit → select folder
4. Framework: leave automatic / Other
5. **Environment Variables** — add all of these (Production + Preview):

| Name | Value |
|------|--------|
| `FLASK_SECRET_KEY` | any long random string (e.g. mash keyboard 40 chars) |
| `GITHUB_OAUTH_CLIENT_ID` | from OAuth App |
| `GITHUB_OAUTH_CLIENT_SECRET` | from OAuth App |
| `GITHUB_APP_ID` | numeric App ID |
| `GITHUB_PRIVATE_KEY` | open the `.pem` in a text editor, paste **all** of it (including BEGIN/END lines). On Vercel you can paste multi-line. |
| `GITHUB_INSTALLATION_ID` | number from install URL |
| `GITHUB_OWNER` | `itsyst` |
| `GITHUB_REPO` | `python-strudy` |
| `FRONTEND_ORIGIN` | `https://itsyst.github.io` |
| `PUBLIC_BASE_URL` | `https://YOUR-PROJECT.vercel.app` (the URL Vercel shows after deploy) |
| `TEACHER_LOGIN` | `itsyst` |

6. Click **Deploy**
7. Copy your live URL, e.g. `https://ps-teacher-desk.vercel.app`
8. Go back to the OAuth App → edit **Callback URL** to  
   `https://YOUR-PROJECT.vercel.app/auth/callback` → Update
9. In Vercel, set `PUBLIC_BASE_URL` to the same URL → Redeploy if needed

Test: open `https://YOUR-PROJECT.vercel.app/health`  
You want: `{"ok":true,"configured":true}`

---

## C. Point the student site at the backend

Edit `assets/teacher-api.json` in the repo:

```json
{
  "apiBase": "https://YOUR-PROJECT.vercel.app",
  "note": "Vercel teacher backend"
}
```

Commit and push. Wait ~1 minute for GitHub Pages.

Open: https://itsyst.github.io/python-strudy/admin.html  
→ **Sign in with GitHub** as **@itsyst**.

---

## D. Revoke old PATs (important)

https://github.com/settings/tokens → delete any token you ever pasted into the teacher page.

---

If something fails, send me the `/health` JSON and the error on `admin.html`.
