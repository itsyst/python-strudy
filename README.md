# Python Study 🐍

Student website for **TDDE24** — exams, labs, exercises and seminars.

Open any `.py` file to **edit and run it in the browser** (editor + terminal). No local Python install. No Node, npm, or Vite.

**Live:** https://itsyst.github.io/python-strudy/

**Discord (lab codes):** https://discord.gg/mR9JByCr7  
**Support:** [Ko-fi](https://ko-fi.com/itsyst) · [Patreon](https://www.patreon.com/c/itsyst)

## Local (static site — do not run Vite)

This repo is only HTML + JS. **Do not** run `npx vite`, `npm install`, or `npm run dev`.

```powershell
cd python-strudy
python update_files.py
python -m http.server 8000
```

Open http://localhost:8000

## Labs lock + teacher codes

Labs stay closed until a student enters a one-time passcode.

1. Open [`admin.html`](admin.html) on **your** computer.
2. Set a teacher PIN (stored as a hash; the code vault is AES-GCM encrypted in this browser).
3. Generate codes (`ABCD-EFGH`). Copy them into Discord.
4. A code is valid **3 days** if unused. Redeeming it **burns it on that device** and unlocks Labs for 3 days.

There is no server and no database. Codes cannot be globally deleted for every student the instant one person uses them — that needs a backend. This design keeps honest students out of Labs and keeps PIN/codes off disk in plaintext.

Teacher desk: http://localhost:8000/admin.html

## Folders

| Folder | Menu |
|--------|------|
| `exams/` | Exams (open) |
| `labs/` | Labs (passcode) |
| `exercises/` | Exercises (open) |
| `seminars/` | Seminars (open) |

```bash
python update_files.py
git add .
git commit -m "Add material"
git push
```

## In-browser Python

`.py` files open in a split editor / terminal. **Run** executes the file. First load downloads the Python runtime (~10s).

## GitHub Pages

Settings → Pages → Branch `main` → `/ (root)`  
The repository must be **public** on a free GitHub account.

© 2026 [itsyst](https://github.com/itsyst)
