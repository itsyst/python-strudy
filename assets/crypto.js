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

  const DEVICE_KEY = "ps.v1.device";
  const COOKIE_USED = "ps_used";

  function getDeviceId() {
    let id = localStorage.getItem(DEVICE_KEY);
    if (!id) {
      id = b64(crypto.getRandomValues(new Uint8Array(16)));
      localStorage.setItem(DEVICE_KEY, id);
    }
    return id;
  }

  async function getIp() {
    try {
      const r = await fetch("https://api.ipify.org?format=json", { cache: "no-store" });
      if (!r.ok) throw new Error("ip");
      const j = await r.json();
      return String(j.ip || "unknown");
    } catch (_) {
      return "unknown";
    }
  }

  function setCookie(name, value, ms) {
    const exp = new Date(Date.now() + ms).toUTCString();
    document.cookie =
      name + "=" + encodeURIComponent(value) + "; expires=" + exp + "; path=/; SameSite=Lax";
  }

  function getCookie(name) {
    const parts = document.cookie.split(";");
    for (let i = 0; i < parts.length; i++) {
      const p = parts[i].trim();
      if (p.indexOf(name + "=") === 0) return decodeURIComponent(p.slice(name.length + 1));
    }
    return "";
  }

  function readUsed() {
    try {
      const arr = JSON.parse(localStorage.getItem(USED_KEY) || "[]");
      if (!Array.isArray(arr)) return [];
      const now = Date.now();
      return arr
        .map(function (x) {
          if (typeof x === "string") return { hash: x, at: now };
          return x;
        })
        .filter(function (x) { return x && x.hash && now - (x.at || 0) < TTL_MS * 4; });
    } catch (_) {
      return [];
    }
  }

  function writeUsed(arr) {
    localStorage.setItem(USED_KEY, JSON.stringify(arr.slice(-200)));
  }

  async function hasLabSession() {
    try {
      const match = await bindingMatches();
      if (!match.ok) return false;
      const blob = JSON.parse(localStorage.getItem(SESSION_KEY) || "null");
      const sess = await unwrapWithPepper(blob);
      if (!sess || !sess.until) return false;
      if (Date.now() > sess.until) {
        localStorage.removeItem(SESSION_KEY);
        return false;
      }
      if (sess.device && match.bind.deviceId && sess.device !== match.bind.deviceId) return false;
      if (sess.ip && match.bind.ip && sess.ip !== "unknown" && match.bind.ip !== "unknown" && sess.ip !== match.bind.ip) {
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
    const match = await bindingMatches();
    if (!match.ok) return { ok: false, error: "Confirm this device and IP first." };
    const checked = await verifyIssuedCode(raw);
    if (!checked.ok) return checked;
    const hash = await sha256Hex(checked.code);
    const issued = await loadIssuedPublic();
    const row = issued.find(function (x) {
      return x && x.hash === hash && Date.now() <= (x.expires || 0);
    });
    if (!row) {
      return { ok: false, error: "This code was not issued by the GitHub owner." };
    }
    const device = match.bind.deviceId;
    const ip = match.bind.ip;
    const ipBind = await sha256Hex(hash + "|ip|" + ip);
    const deviceBind = await sha256Hex(hash + "|dev|" + device);
    const used = readUsed();
    const cookie = getCookie(COOKIE_USED);
    const ledger = await fetchUsedLedger();
    const already =
      used.some(function (u) {
        return u.hash === hash || u.ipBind === ipBind || u.deviceBind === deviceBind;
      }) ||
      ledger.indexOf(hash) !== -1 ||
      (cookie && cookie.split(".").indexOf(hash.slice(0, 12)) !== -1);
    if (already) {
      return { ok: false, error: "This code was already used on this device, IP, or ledger." };
    }
    used.push({
      hash: hash, ipBind: ipBind, deviceBind: deviceBind, ip: ip, device: device,
      kind: match.bind.kind, browser: match.bind.browser, at: Date.now(),
    });
    writeUsed(used);
    writeLog({
      at: Date.now(), ip: ip, deviceId: device, kind: match.bind.kind,
      browser: match.bind.browser, hash: hash.slice(0, 12),
    });
    const stamp = hash.slice(0, 12);
    const prev = cookie ? cookie.split(".").filter(Boolean) : [];
    if (prev.indexOf(stamp) === -1) prev.push(stamp);
    setCookie(COOKIE_USED, prev.join("."), TTL_MS);
    const until = Date.now() + TTL_MS;
    const blob = await wrapWithPepper({
      until: until, hash: hash, ip: ip, device: device,
      kind: match.bind.kind, browser: match.bind.browser,
    });
    localStorage.setItem(SESSION_KEY, JSON.stringify(blob));
    return { ok: true, until: until, bind: match.bind };
  }

  function lockLabs() {
    localStorage.removeItem(SESSION_KEY);
  }

  const GATE_SALT = enc.encode("python-strudy-teacher-v1");
  let teacherGateCache = null;

  async function loadTeacherGate() {
    if (teacherGateCache && teacherGateCache.hash) return teacherGateCache;
    const res = await fetch("assets/teacher-gate.json", { cache: "no-store" });
    if (!res.ok) throw new Error("Teacher PIN is not registered in the repo.");
    teacherGateCache = await res.json();
    return teacherGateCache;
  }

  async function hashTeacherPin(pin) {
    return sha256Hex(pepper() + "|teacher-gate|" + String(pin || ""));
  }

  async function pinMatchesPublished(pin) {
    const gate = await loadTeacherGate();
    const got = await hashTeacherPin(pin);
    return !!(gate && gate.hash && got === gate.hash);
  }

  function hasTeacherPin() {
    return true;
  }

  async function setTeacherPin() {
    return { ok: false, error: "PIN is registered in GitHub, not in this browser." };
  }

  async function unlockTeacher(pin) {
    try {
      if (!(await pinMatchesPublished(pin))) return { ok: false, error: "Wrong PIN." };
    } catch (e) {
      return { ok: false, error: e.message || "Teacher gate missing." };
    }
    const key = await deriveAesKey(String(pin), GATE_SALT, ["encrypt", "decrypt"]);
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

  async function exportTeacherGate(newPin) {
    newPin = String(newPin || "");
    if (newPin.length < 12) return { ok: false, error: "New PIN must be at least 12 characters." };
    const hash = await hashTeacherPin(newPin);
    return {
      ok: true,
      gate: {
        v: 1,
        algo: "sha256-pepper",
        hash: hash,
        note: "SHA-256 of the teacher PIN. The PIN itself is not stored in this repo. Replace this file to reset.",
      },
    };
  }

  async function changeTeacherPin(oldPin, newPin) {
    const unlocked = await unlockTeacher(oldPin);
    if (!unlocked.ok) return unlocked;
    const exported = await exportTeacherGate(newPin);
    if (!exported.ok) return exported;
    const salt = GATE_SALT;
    const key = await deriveAesKey(String(newPin), salt, ["encrypt"]);
    const blob = await aesEncrypt(key, unlocked.vault);
    localStorage.setItem(VAULT_KEY, JSON.stringify(blob));
    return { ok: true, gate: exported.gate };
  }

  const OWNER = "itsyst";
  const REPO = "python-strudy";
  const ISSUED_PATH = "assets/issued.json";

  /* ---------- Teacher backend (no browser tokens) ---------- */
  const TEACHER_JWT_KEY = "ps.v1.teacherJwt";
  let apiBaseCache = null;

  function captureTeacherJwt() {
    const h = location.hash || "";
    if (h.indexOf("#ts=") === 0) {
      sessionStorage.setItem(TEACHER_JWT_KEY, decodeURIComponent(h.slice(4)));
      history.replaceState({}, "", location.pathname + location.search);
    }
  }

  function teacherHeaders(extra) {
    captureTeacherJwt();
    const headers = Object.assign({}, extra || {});
    const tok = sessionStorage.getItem(TEACHER_JWT_KEY);
    if (tok) headers.Authorization = "Bearer " + tok;
    return headers;
  }

  async function getApiBase() {
    if (apiBaseCache !== null) return apiBaseCache;
    try {
      const res = await fetch("assets/teacher-api.json", { cache: "no-store" });
      if (!res.ok) {
        apiBaseCache = "";
        return "";
      }
      const data = await res.json();
      apiBaseCache = String(data.apiBase || "").replace(/\/$/, "");
      return apiBaseCache;
    } catch (_) {
      apiBaseCache = "";
      return "";
    }
  }

  async function teacherLoginUrl() {
    const base = await getApiBase();
    if (!base) throw new Error("Teacher backend not configured (assets/teacher-api.json).");
    const next = encodeURIComponent(location.href.split("?")[0]);
    return base + "/auth/github?next=" + next;
  }

  async function teacherSession() {
    const base = await getApiBase();
    if (!base) return { ok: false, error: "Backend not configured." };
    try {
      const res = await fetch(base + "/api/session", {
        credentials: "include",
        cache: "no-store",
        headers: teacherHeaders(),
      });
      if (res.status === 401) return { ok: false, error: "" };
      if (!res.ok) return { ok: false, error: "Session check failed." };
      const data = await res.json();
      if (!data.ok || !data.login) return { ok: false, error: "" };
      return { ok: true, login: data.login, name: data.name || data.login, avatar: data.avatar || "" };
    } catch (e) {
      return { ok: false, error: "Cannot reach teacher backend. Is it deployed?" };
    }
  }

  async function teacherLogout() {
    const base = await getApiBase();
    sessionStorage.removeItem("ps.v1.lastcodes");
    sessionStorage.removeItem(TEACHER_JWT_KEY);
    if (!base) return;
    try {
      await fetch(base + "/api/logout", { method: "POST", credentials: "include", headers: teacherHeaders() });
    } catch (_) {}
  }

  /* Browser must never hold a GitHub token. These stubs reject any attempt. */
  function githubSession() {
    return null;
  }
  function githubSignOut() {
    teacherLogout();
  }
  async function githubSignIn() {
    return {
      ok: false,
      error: "Personal access tokens are disabled. Deploy teacher-server and sign in with GitHub OAuth.",
    };
  }

  async function loadIssuedPublic() {
    try {
      const res = await fetch("assets/issued.json", { cache: "no-store" });
      if (!res.ok) return [];
      const data = await res.json();
      return Array.isArray(data.issued) ? data.issued : [];
    } catch (_) {
      return [];
    }
  }

  async function generateOwnerCodes(count) {
    const base = await getApiBase();
    if (!base) {
      return { ok: false, error: "Teacher backend not configured (set apiBase in teacher-api.json)." };
    }
    count = Math.max(1, Math.min(20, Number(count) || 1));
    try {
      const res = await fetch(base + "/api/codes", {
        method: "POST",
        credentials: "include",
        headers: teacherHeaders({ "Content-Type": "application/json" }),
        body: JSON.stringify({ count: count }),
      });
      const data = await res.json().catch(function () {
        return {};
      });
      if (!res.ok) {
        return { ok: false, error: data.error || "Code generation failed (" + res.status + ")." };
      }
      const codes = Array.isArray(data.codes) ? data.codes : [];
      sessionStorage.setItem("ps.v1.lastcodes", JSON.stringify(codes));
      return { ok: true, codes: codes };
    } catch (e) {
      return { ok: false, error: "Cannot reach teacher backend: " + (e.message || "network error") };
    }
  }

  async function listIssuedPublic() {
    const now = Date.now();
    const rows = (await loadIssuedPublic()).filter(function (x) {
      return x && x.hash && now <= (x.expires || 0);
    });
    return { ok: true, codes: rows };
  }

  async function generateCodes() {
    return {
      ok: false,
      error: "Sign in with GitHub via the teacher backend to generate codes. Browser tokens are disabled.",
    };
  }

  async function listVault() {
    return listIssuedPublic();
  }

  const BIND_KEY = "ps.v1.bind";
  const LOG_KEY = "ps.v1.log";
  const VAULT_SALT = enc.encode("python-strudy-labs-vault-v1");

  function parseBrowser(ua) {
    ua = ua || "";
    if (/Edg\//.test(ua)) return "Edge";
    if (/Chrome\//.test(ua) && !/Edg\//.test(ua)) return "Chrome";
    if (/Firefox\//.test(ua)) return "Firefox";
    if (/Safari\//.test(ua) && !/Chrome\//.test(ua)) return "Safari";
    return "Browser";
  }

  async function canvasStamp() {
    try {
      const c = document.createElement("canvas");
      c.width = 200;
      c.height = 50;
      const x = c.getContext("2d");
      x.textBaseline = "top";
      x.font = "14px Arial";
      x.fillStyle = "#3dd6c6";
      x.fillRect(0, 0, 200, 50);
      x.fillStyle = "#000";
      x.fillText("python-strudy", 4, 8);
      return (await sha256Hex(c.toDataURL())).slice(0, 16);
    } catch (_) {
      return "nocanvas";
    }
  }

  async function probeDevice() {
    const ip = await getIp();
    const ua = navigator.userAgent || "";
    const touch = navigator.maxTouchPoints || 0;
    const mobile = /Mobi|Android|iPhone|iPad/i.test(ua) || touch > 2;
    const screenInfo =
      (window.screen && window.screen.width) + "x" +
      (window.screen && window.screen.height) + "@" +
      (window.devicePixelRatio || 1);
    const fpSrc = [
      ua, navigator.platform || "", navigator.language || "",
      Intl.DateTimeFormat().resolvedOptions().timeZone || "",
      screenInfo, navigator.hardwareConcurrency || "", touch,
      navigator.deviceMemory || "", await canvasStamp(),
    ].join("|");
    return {
      ip: ip,
      mac: "blocked-by-browser",
      deviceId: (await sha256Hex("fp|" + fpSrc)).slice(0, 20),
      kind: mobile ? "mobile" : "pc",
      browser: parseBrowser(ua),
      screen: screenInfo,
      tz: Intl.DateTimeFormat().resolvedOptions().timeZone || "",
      ua: ua.slice(0, 180),
      at: Date.now(),
    };
  }

  function readBind() {
    try { return JSON.parse(localStorage.getItem(BIND_KEY) || "null"); }
    catch (_) { return null; }
  }

  async function confirmDevice() {
    const probe = await probeDevice();
    localStorage.setItem(BIND_KEY, JSON.stringify(probe));
    setCookie("ps_bind", probe.deviceId, TTL_MS * 4);
    return probe;
  }

  function deviceConfirmed() {
    const b = readBind();
    return !!(b && b.deviceId && b.ip);
  }

  async function bindingMatches() {
    const b = readBind();
    if (!b) return { ok: false, reason: "not-confirmed" };
    const now = await probeDevice();
    if (now.deviceId !== b.deviceId) return { ok: false, reason: "device", now: now, bind: b };
    if (now.kind !== b.kind) return { ok: false, reason: "kind", now: now, bind: b };
    if (now.browser !== b.browser) return { ok: false, reason: "browser", now: now, bind: b };
    if (now.ip !== "unknown" && b.ip !== "unknown" && now.ip !== b.ip) {
      return { ok: false, reason: "ip", now: now, bind: b };
    }
    return { ok: true, now: now, bind: b };
  }

  function readLog() {
    try {
      const arr = JSON.parse(localStorage.getItem(LOG_KEY) || "[]");
      return Array.isArray(arr) ? arr : [];
    } catch (_) { return []; }
  }

  function writeLog(entry) {
    const arr = readLog();
    arr.push(entry);
    localStorage.setItem(LOG_KEY, JSON.stringify(arr.slice(-100)));
  }

  async function labsVaultKey() {
    return deriveAesKey(pepper() + "|labs-vault", VAULT_SALT, ["decrypt"]);
  }

  let labsVaultCache = null;
  async function loadLabsVault() {
    if (labsVaultCache) return labsVaultCache;
    const res = await fetch("assets/labs-vault.json", { cache: "no-store" });
    if (!res.ok) throw new Error("Labs vault missing");
    labsVaultCache = await res.json();
    return labsVaultCache;
  }

  async function decryptLabFile(path) {
    const pack = await loadLabsVault();
    const item = pack.files && pack.files[path];
    if (!item) return null;
    const key = await labsVaultKey();
    const raw = await crypto.subtle.decrypt(
      { name: "AES-GCM", iv: unb64(item.iv) },
      key,
      unb64(item.data),
    );
    return dec.decode(raw);
  }

  async function fetchUsedLedger() {
    try {
      const res = await fetch("assets/used-ledger.json", { cache: "no-store" });
      if (!res.ok) return [];
      const data = await res.json();
      return Array.isArray(data.used) ? data.used : [];
    } catch (_) { return []; }
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
    exportTeacherGate: exportTeacherGate,
    generateCodes: generateCodes,
    listVault: listVault,
    githubSignIn: githubSignIn,
    githubSignOut: githubSignOut,
    githubSession: githubSession,
    generateOwnerCodes: generateOwnerCodes,
    listIssuedPublic: listIssuedPublic,
    getApiBase: getApiBase,
    teacherLoginUrl: teacherLoginUrl,
    teacherSession: teacherSession,
    teacherLogout: teacherLogout,
    probeDevice: probeDevice,
    confirmDevice: confirmDevice,
    deviceConfirmed: deviceConfirmed,
    bindingMatches: bindingMatches,
    readBind: readBind,
    readLog: readLog,
    decryptLabFile: decryptLabFile,
    loadLabsVault: loadLabsVault,
  };
})(window);
