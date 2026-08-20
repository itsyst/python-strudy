# Python Study

Student website for **TDDE24** — exams, labs, exercises and seminars.

Open any `.py` file to **edit and run it in the browser** (editor + terminal). No Node, npm, or Vite.

**Live:** https://itsyst.github.io/python-strudy/

**Discord (lab codes):** https://discord.gg/mR9JByCr7  
**Support:** [Ko-fi](https://ko-fi.com/itsyst) · [Patreon](https://www.patreon.com/c/itsyst)

## Local

```powershell
cd python-strudy
git pull
python update_files.py
python -m http.server 8000
```

Open http://localhost:8000 — not `npx vite`.

## Labs lock

Labs stay closed until a one-time passcode.

1. Open `admin.html` on your computer
2. Set a PIN (encrypted in this browser)
3. Generate codes and post them on Discord
4. A code is valid 3 days unused. Using it **burns it** on that device (and IP, as far as the browser can see) and unlocks Labs for 3 days. The code is dropped from the teacher vault on that machine.

There is no server. A second browser on the same PC is a different store — that is a limit of GitHub Pages, not a missing setting.

Teacher desk: http://localhost:8000/admin.html

## Folders

| Folder | Menu |
|--------|------|
| `exams/` | Exams (open) |
| `labs/` | Labs (passcode) |
| `exercises/` | Exercises (open) |
| `seminars/` | Seminars (open) |

Lab 8 needs `cal_abstraction.py`, `settings.py`, `cal_booking.py` and `cal_ui.py` next to `labb_8a.py` (they are in `labs/labb-8/`).

```bash
python update_files.py
git add .
git commit -m "Add material"
git push
```

© 2026 [itsyst](https://github.com/itsyst)
