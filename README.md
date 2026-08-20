# Python Study

Student website for **TDDE24**. Live: https://itsyst.github.io/python-strudy/

**For study only** — practice materials to help you prepare and pass the exam. Not an official course site.

If this helps you, please **star the repo** ★ — it keeps the project visible and motivates updates.

First visit: confirm **IP + device ID** (browsers cannot read a MAC address). Labs stay locked until a Discord passcode. Lab **source files are not in this public repo**. They live in the private `itsyst/python-strudy-labs` repository and are served only after a one-time Discord passcode, via the teacher backend.

```powershell
cd python-strudy
git pull
python update_files.py
python -m http.server 8000
```

Teacher: [admin.html](https://itsyst.github.io/python-strudy/admin.html) — **no personal access tokens in the browser**. Deploy [`teacher-server/`](teacher-server/) (GitHub OAuth + GitHub App), then set `apiBase` in `assets/teacher-api.json`.

Rebuild the labs vault after adding lab files:

```powershell
node scripts/build-labs-vault.mjs
```

---

© 2026 [itsyst](https://github.com/itsyst)

**Support** · [Ko-fi](https://ko-fi.com/itsyst) · [Patreon](https://www.patreon.com/c/itsyst)

**Star the repo** if you find it useful: [github.com/itsyst/python-strudy](https://github.com/itsyst/python-strudy)
