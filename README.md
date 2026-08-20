# Python Study

Student website for **TDDE24**. Live: https://itsyst.github.io/python-strudy/

**For study only** — practice materials to help you prepare and pass the exam. Not an official course site.

First visit: confirm **IP + device ID** (browsers cannot read a MAC address). Labs stay locked until a Discord passcode. Lab files on the website are served from an **encrypted vault** (`assets/labs-vault.json`), not from a raw `/labs/` fetch.

```powershell
cd python-strudy
git pull
python update_files.py
python -m http.server 8000
```

Teacher: [admin.html](https://itsyst.github.io/python-strudy/admin.html) — only GitHub user **@itsyst** (repo owner). Sign in with a GitHub token; generated codes are published as hashes in `assets/issued.json`. Other GitHub accounts are rejected.

Rebuild the labs vault after adding lab files:

```powershell
node scripts/build-labs-vault.mjs
```

---

© 2026 [itsyst](https://github.com/itsyst)

**Support** · [Ko-fi](https://ko-fi.com/itsyst) · [Patreon](https://www.patreon.com/c/itsyst)
