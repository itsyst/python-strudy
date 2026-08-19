# Python Study 🐍

Student website for **TDDE24** — exams, labs, exercises and seminars.

Open any `.py` file to **edit and run it in the browser** (editor + terminal). No local Python install needed. No Node, npm, or Vite.

**Live:** https://itsyst.github.io/python-strudy/

**Discord (lab codes):** https://discord.gg/mR9JByCr7  
**Support:** [Ko-fi](https://ko-fi.com/itsyst) · [Patreon](https://www.patreon.com/c/itsyst)

## Local (static site — do not run Vite)

This repo is only HTML + JS. **Do not** run `npx vite`, `npm install`, or `npm run dev`. Those tools belong to a different kind of project and will fail on this one.

```bash
git pull
python update_files.py    # refresh file list after adding files / folders
python -m http.server 8000
```

Then open http://localhost:8000 in your browser.

On Windows PowerShell:

```powershell
python -m http.server 8000
```

## Folders

| Folder | Menu |
|--------|------|
| `exams/` | Exams |
| `labs/` | Labs |
| `exercises/` | Exercises |
| `seminars/` | Seminars |

Any other top-level folder with `.py` / `.txt` / `.md` files is detected automatically.

```bash
python update_files.py
git add .
git commit -m "Add material"
git push
```

## In-browser Python

`.py` files open in a split editor / terminal. **Run** executes the file, the prompt works like a local REPL, and a stdin box feeds `input()`. First load downloads the Python runtime (~10s).

## GitHub Pages

Settings → Pages → Branch `main` → `/ (root)`  
The repository must be **public** on a free GitHub account.

© 2026 [itsyst](https://github.com/itsyst)
