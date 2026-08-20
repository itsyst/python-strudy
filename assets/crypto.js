/* python-strudy — Web Crypto helpers (no server, no database)
   Teacher vault + student session are AES-GCM.
   Lab codes are one-time on this browser and expire after 3 days unused.
*/

(function (global) {
  const TTL_MS = 3 * 24 * 60 * 60 * 1000;
  const ITER = 120000;
  const ALPH = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
  const META_KEY = "ps.v1.meta";
  const VAULT_KEY = "ps.v1.vault";
  const SESSION_KEY = "ps.v1.session";
  const USED_KEY = "ps.v1.used";
  const PEPPER_PARTS = ["TDDE24", "python-strudy", "lab-gate", "2026"];

  const enc = new TextEncoder();
  const dec = new TextDecoder();

  function pepper() {
    return PEPPER_PARTS.join("|");
  }

  function b64(bytes) {
    let s = "";
    const arr = bytes instanceof Uint8Array ? bytes : new Uint8Array(bytes);
    for (let i = 0; i < arr.length; i++) s += String.fromCharCode(arr[i]);
    return btoa(s);
  }

  function unb64(str) {
    const bin = atob(str);
    const out = new Uint8Array(bin.length);
    for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
    return out;
  }

  function bytesToCodeChars(bytes, n) {
    let out = "";
    for (let i = 0; i < n; i++) out += ALPH[bytes[i % bytes.length] % ALPH.length];
    return out;
  }

  async function sha256Bytes(text) {
    return new Uint8Array(await crypto.subtle.digest("SHA-256", enc.encode(text)));
  }

  async function sha256Hex(text) {
    const buf = await sha256Bytes(text);
    return Array.from(buf)
      .map(function (x) {
        return x.toString(16).padStart(2, "0");
      })
      .join("");
  }

  function timeBucket(ts) {
    return Math.floor((ts || Date.now()) / TTL_MS);
  }

  async function deriveAesKey(secret, salt, usages) {
    const material = await crypto.subtle.importKey(
      "raw",
      enc.encode(secret),
      "PBKDF2",
      false,
      ["deriveKey"],
    );
    return crypto.subtle.deriveKey(
      { name: "PBKDF2", salt: salt, iterations: ITER, hash: "SHA-256" },
      material,
      { name: "AES-GCM", length: 256 },
      false,
      usages,
    );
  }

  async function aesEncrypt(key, obj) {
    const iv = crypto.getRandomValues(new Uint8Array(12));
    const data = await crypto.subtle.encrypt(
      { name: "AES-GCM", iv: iv },
      key,
      enc.encode(JSON.stringify(obj)),
    );
    return { iv: b64(iv), data: b64(data) };
  }

  async function aesDecrypt(key, blob) {
    const raw = await crypto.subtle.decrypt(
      { name: "AES-GCM", iv: unb64(blob.iv) },
      key,
      unb64(blob.data),
    );
    return JSON.parse(dec.decode(raw));
  }

  async function wrapWithPepper(obj) {
    const salt = await sha256Bytes(pepper() + "|wrap");
    const key = await deriveAesKey(pepper(), salt, ["encrypt"]);
    return aesEncrypt(key, obj);
  }

  async function unwrapWithPepper(blob) {
    if (!blob || !blob.iv || !blob.data) return null;
    try {
      const salt = await sha256Bytes(pepper() + "|wrap");
      const key = await deriveAesKey(pepper(), salt, ["decrypt"]);
      return await aesDecrypt(key, blob);
    } catch (_) {
      return null;
    }
  }

  function normalizeCode(raw) {
    const s = String(raw || "")
      .toUpperCase()
      .replace(/[^A-Z0-9]/g, "");
    if (s.length !== 8) return "";
    return s.slice(0, 4) + "-" + s.slice(4);
  }

  async function checksumFor(payload, bucket) {
    const digest = await sha256Bytes(pepper() + "|code|" + payload + "|" + bucket);
    return bytesToCodeChars(digest, 4);
  }

  async function mintCode(now) {
    now = now || Date.now();
    const rnd = crypto.getRandomValues(new Uint8Array(8));
    const payload = bytesToCodeChars(rnd, 4);
    const bucket = timeBucket(now);
    const check = await checksumFor(payload, bucket);
    const code = payload + "-" + check;
    return {
      code: code,
      hash: await sha256Hex(code),
      created: now,
      expires: (bucket + 1) * TTL_MS,
    };
  }

  async function verifyIssuedCode(raw) {
    const code = normalizeCode(raw);
    if (!code) return { ok: false, error: "Use a code like ABCD-EFGH." };
    const payload = code.slice(0, 4);
    const check = code.slice(5);
    const bucket = timeBucket(Date.now());
    for (let b = bucket; b >= bucket - 1; b--) {
      if (b < 0) continue;
      if ((await checksumFor(payload, b)) === check) {
        return { ok: true, code: code, bucket: b, expires: (b + 1) * TTL_MS };
      }
    }
    return { ok: false, error: "Invalid or expired code." };
  }

  function readUsed() {
    try {
      const arr = JSON.parse(localStorage.getItem(USED_KEY) || "[]");
      return Array.isArray(arr) ? arr : [];
    } catch (_) {
      return [];
    }
  }

  function writeUsed(arr) {
    localStorage.setItem(USED_KEY, JSON.stringify(arr.slice(-200)));
  }

  async function hasLabSession() {
    try {
      const blob = JSON.parse(localStorage.getItem(SESSION_KEY) || "null");
      const sess = await unwrapWithPepper(blob);
      if (!sess || !sess.until) return false;
      if (Date.now() > sess.until) {
        localStorage.removeItem(SESSION_KEY);
        return false;
      }
      return true;
    } catch (_) {
      return false;
    }
  }

  async function sessionUntil() {
    try {
      const blob = JSON.parse(localStorage.getItem(SESSION_KEY) || "null");
      const sess = await unwrapWithPepper(blob);
      return sess && sess.until ? sess.until : 0;
    } catch (_) {
      return 0;
    }
  }

  async function redeemCode(raw) {
    const checked = await verifyIssuedCode(raw);
    if (!checked.ok) return checked;
    const hash = await sha256Hex(checked.code);
    const used = readUsed();
    if (used.indexOf(hash) !== -1) {
      return { ok: false, error: "This code was already used on this device." };
    }
    used.push(hash);
    writeUsed(used);
    const until = Date.now() + TTL_MS;
    const blob = await wrapWithPepper({ until: until, hash: hash });
    localStorage.setItem(SESSION_KEY, JSON.stringify(blob));
    return { ok: true, until: until };
  }

  function lockLabs() {
    localStorage.removeItem(SESSION_KEY);
  }

  function teacherMeta() {
    try {
      return JSON.parse(localStorage.getItem(META_KEY) || "null");
    } catch (_) {
      return null;
    }
  }

  function hasTeacherPin() {
    const m = teacherMeta();
    return !!(m && m.salt && m.verify);
  }

  async function setTeacherPin(pin) {
    pin = String(pin || "");
    if (pin.length < 6) return { ok: false, error: "PIN must be at least 6 characters." };
    const salt = crypto.getRandomValues(new Uint8Array(16));
    const key = await deriveAesKey(pin, salt, ["encrypt"]);
    const verify = await sha256Hex(pepper() + "|pin|" + pin);
    const empty = await aesEncrypt(key, { codes: [] });
    localStorage.setItem(
      META_KEY,
      JSON.stringify({ v: 1, salt: b64(salt), verify: verify }),
    );
    localStorage.setItem(VAULT_KEY, JSON.stringify(empty));
    return { ok: true };
  }

  async function unlockTeacher(pin) {
    const meta = teacherMeta();
    if (!meta) return { ok: false, error: "No teacher PIN on this browser yet." };
    const verify = await sha256Hex(pepper() + "|pin|" + pin);
    if (verify !== meta.verify) return { ok: false, error: "Wrong PIN." };
    const key = await deriveAesKey(pin, unb64(meta.salt), ["encrypt", "decrypt"]);
    let vault = { codes: [] };
    try {
      vault = await aesDecrypt(key, JSON.parse(localStorage.getItem(VAULT_KEY)));
    } catch (_) {
      vault = { codes: [] };
    }
    return { ok: true, key: key, vault: vault };
  }

  async function saveVault(key, vault) {
    const blob = await aesEncrypt(key, vault);
    localStorage.setItem(VAULT_KEY, JSON.stringify(blob));
  }

  async function changeTeacherPin(oldPin, newPin) {
    const unlocked = await unlockTeacher(oldPin);
    if (!unlocked.ok) return unlocked;
    newPin = String(newPin || "");
    if (newPin.length < 6) return { ok: false, error: "New PIN must be at least 6 characters." };
    const salt = crypto.getRandomValues(new Uint8Array(16));
    const key = await deriveAesKey(newPin, salt, ["encrypt"]);
    const verify = await sha256Hex(pepper() + "|pin|" + newPin);
    const blob = await aesEncrypt(key, unlocked.vault);
    localStorage.setItem(
      META_KEY,
      JSON.stringify({ v: 1, salt: b64(salt), verify: verify }),
    );
    localStorage.setItem(VAULT_KEY, JSON.stringify(blob));
    return { ok: true };
  }

  async function generateCodes(pin, count) {
    const unlocked = await unlockTeacher(pin);
    if (!unlocked.ok) return unlocked;
    count = Math.max(1, Math.min(20, Number(count) || 1));
    const now = Date.now();
    const fresh = [];
    for (let i = 0; i < count; i++) fresh.push(await mintCode(now));
    const vault = unlocked.vault || { codes: [] };
    vault.codes = (vault.codes || []).concat(fresh);
    await saveVault(unlocked.key, vault);
    return { ok: true, codes: fresh, vault: vault };
  }

  async function listVault(pin) {
    const unlocked = await unlockTeacher(pin);
    if (!unlocked.ok) return unlocked;
    const now = Date.now();
    const codes = (unlocked.vault.codes || []).map(function (c) {
      return {
        code: c.code,
        hash: c.hash,
        created: c.created,
        expires: c.expires,
        expired: now > c.expires,
      };
    });
    return { ok: true, codes: codes };
  }

  global.PSCrypto = {
    TTL_MS: TTL_MS,
    normalizeCode: normalizeCode,
    hasLabSession: hasLabSession,
    sessionUntil: sessionUntil,
    redeemCode: redeemCode,
    lockLabs: lockLabs,
    hasTeacherPin: hasTeacherPin,
    setTeacherPin: setTeacherPin,
    unlockTeacher: unlockTeacher,
    changeTeacherPin: changeTeacherPin,
    generateCodes: generateCodes,
    listVault: listVault,
  };
})(window);
