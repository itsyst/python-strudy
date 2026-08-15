# Python Study 🐍

Student website for **TDDE24** — exams, labs, exercises and seminars.

**Live:** https://itsyst.github.io/python-strudy/

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

## GitHub Pages

Settings → Pages → Branch `main` → `/ (root)`

© 2026 [itsyst](https://github.com/itsyst)
