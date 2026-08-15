# Python Study 🐍

Student website for Python **lectures** and **exams (Tentor)**.

## Live site

After enabling GitHub Pages (Settings → Pages → main branch):

**https://itsyst.github.io/python-strudy/**

## How it works (dynamic)

The site **automatically discovers** every `.py` file under:

- `lectures/`
- `exams/<date>/`

**No hardcoded lists.**  
Just add a file, push, refresh the site → it appears.

```bash
# Example: new exam exercise
mkdir -p exams/2026-08-15
# write exams/2026-08-15/ex6.py in VS Code
git add exams/2026-08-15/ex6.py
git commit -m "Add ex6"
git push
# → website shows it after a few seconds
```

> **Note:** The repo must be **public** for the live file list (GitHub API). File content still works when served by Pages.

## Local preview

```bash
# VS Code: install "Live Server" → right-click index.html → Open with Live Server
# Or:
python -m http.server 8000
# open http://localhost:8000
```

## Structure

```
lectures/          # lecture examples
exams/             # tentor by date (YYYY-MM-DD)
  2024-01-09/
  2025-08-19/
  ...
assets/            # website CSS + JS
index.html
```

## Requirements

- Python 3.8+
- Public repo recommended for the dynamic website
