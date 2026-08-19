# Python Study 🐍

Student website for **TDDE24** — exams, labs, exercises and seminars.

Open any `.py` file to **edit and run it in the browser** (editor + terminal, powered by Pyodide). No local Python install needed.

**Live:** https://itsyst.github.io/python-strudy/

**Discord (lab codes):** https://discord.gg/mR9JByCr7  
**Support:** [Ko-fi](https://ko-fi.com/itsyst) · [Patreon](https://www.patreon.com/c/itsyst)

## Local

```bash
git pull
python update_files.py    # refresh file list after adding files / folders
python -m http.server 8000
```

Open http://localhost:8000

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
