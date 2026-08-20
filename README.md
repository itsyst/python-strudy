# Python Study

Student website for **TDDE24**. Live: https://itsyst.github.io/python-strudy/

First visit: confirm **IP + device ID** (browsers cannot read a MAC address). Labs stay locked until a Discord passcode. Lab files on the website are served from an **encrypted vault** (`assets/labs-vault.json`), not from a raw `/labs/` fetch.

```powershell
cd python-strudy
git pull
python update_files.py
python -m http.server 8000
```

Teacher: http://localhost:8000/admin.html

Rebuild the labs vault after adding lab files:

```powershell
node scripts/build-labs-vault.mjs
```

© 2026 [itsyst](https://github.com/itsyst)
