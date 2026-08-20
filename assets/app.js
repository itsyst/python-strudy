/* Python Study – dynamic site + in-browser Python playground */

const KNOWN_META = {
  exams: { title: "Exams", icon: "exams", desc: "Past tentor by date — edit and run" },
  labs: { title: "Labs", icon: "labs", desc: "Labbar — locked until a Discord passcode" },
  exercises: { title: "Exercises", icon: "exercises", desc: "Practice exercises — edit and run" },
  seminars: { title: "Seminars", icon: "seminars", desc: "Seminar examples — edit and run" },
  lectures: { title: "Lectures", icon: "exams", desc: "Lecture notes and code" },
  projects: { title: "Projects", icon: "exams", desc: "Project materials" },
};

const ICON_SVG = {
  exams:
    '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>',
  labs:
    '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M9 3h6M10 9h4M10 3v6L6.2 18.2A2 2 0 0 0 8 21h8a2 2 0 0 0 1.8-2.8L14 9V3"/></svg>',
  exercises:
    '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4 12.5-12.5z"/></svg>',
  seminars:
    '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 15a2 2 0 0 1-2 2H8l-5 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
  lock:
    '<svg class="lock-ico" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>',
};

function iconSvg(key) {
  return ICON_SVG[key] || ICON_SVG.exams;
}

const PYODIDE_INDEX = "https://cdn.jsdelivr.net/pyodide/v0.27.5/full/";

let SECTIONS = [];
let lastView = "home";
let currentCode = "";
let originalCode = "";
let currentPath = "";
let currentName = "";
let cache = {};
let loaded = false;
let pyodide = null;
let pyodideLoading = null;
let running = false;

function $(id) {
  return document.getElementById(id);
}

function metaFor(key) {
  if (KNOWN_META[key]) return KNOWN_META[key];
  const title = key.charAt(0).toUpperCase() + key.slice(1).replace(/[-_]/g, " ");
  return { title: title, icon: "exams", desc: title + " materials" };
}

async function loadData() {
  for (const url of ["files.json", "assets/files.json"]) {
    try {
      const res = await fetch(url, { cache: "no-store" });
      if (!res.ok) continue;
      const data = await res.json();
      cache = data || {};
      SECTIONS = Object.keys(cache);
      loaded = true;
      return;
    } catch (_) {}
  }
  try {
    const OWNER = "itsyst", REPO = "python-strudy", BRANCH = "main";
    async function apiList(path) {
      const r = await fetch(
        "https://api.github.com/repos/" + OWNER + "/" + REPO + "/contents/" + path + "?ref=" + BRANCH,
        { headers: { Accept: "application/vnd.github+json" } }
      );
      if (!r.ok) throw new Error("api");
      return r.json();
    }
    const root = await apiList("");
    const dirs = root
      .filter(function (f) {
        return f.type === "dir" && f.name !== "assets" && f.name !== ".github" && f.name.charAt(0) !== ".";
      })
      .map(function (f) { return f.name; });
    const preferred = ["exams", "labs", "exercises", "seminars", "lectures", "projects"];
    const finalOrder = preferred.filter(function (p) { return dirs.indexOf(p) !== -1; });
    dirs.filter(function (d) { return preferred.indexOf(d) === -1; }).sort().forEach(function (d) {
      finalOrder.push(d);
    });

    cache = {};
    for (let i = 0; i < finalOrder.length; i++) {
      const sec = finalOrder[i];
      const top = await apiList(sec);
      const subdirs = top
        .filter(function (f) { return f.type === "dir"; })
        .sort(function (a, b) { return b.name.localeCompare(a.name); });
      const groups = [];
      for (let j = 0; j < subdirs.length; j++) {
        const d = subdirs[j];
        const files = await apiList(d.path);
        const items = files
          .filter(function (f) {
            return f.type === "file" && /\.(py|txt|md)$/i.test(f.name);
          })
          .map(function (f) { return { name: f.name, path: f.path }; });
        if (items.length) groups.push({ group: d.name, items: items });
      }
      const loose = top
        .filter(function (f) {
          return f.type === "file" && /\.(py|txt|md)$/i.test(f.name);
        })
        .map(function (f) { return { name: f.name, path: f.path }; });
      if (loose.length) groups.unshift({ group: "(root)", items: loose });
      cache[sec] = groups;
    }
    SECTIONS = Object.keys(cache);
    loaded = true;
  } catch (e) {
    throw e;
  }
}

function ensureData() {
  if (loaded) return Promise.resolve();
  return loadData();
}

function showView(name) {
  document.querySelectorAll(".view").forEach(function (v) {
    v.classList.remove("active");
  });
  const el = $("view-" + name);
  if (el) el.classList.add("active");
  document.querySelectorAll(".nav-btn").forEach(function (b) {
    b.classList.toggle("active", b.dataset.view === name);
  });
  const links = $("nav-links");
  if (links) links.classList.remove("open");
}

function showHome() {
  lastView = "home";
  showView("home");
  const s = $("search");
  if (s) s.value = "";
  renderHome();
}

async function showSection(section) {
  lastView = section;
  await ensureData();
  showView(section);
  if (section === "labs" && window.PSCrypto && !(await PSCrypto.hasLabSession())) {
    renderLabsLock();
    return;
  }
  renderSection(section, ($("search") && $("search").value) || "");
}

function goBack() {
  if (lastView === "home") showHome();
  else showSection(lastView);
}

function countFiles(groups) {
  return (groups || []).reduce(function (n, g) {
    return n + ((g.items && g.items.length) || 0);
  }, 0);
}

function buildUI() {
  const nav = $("nav-links");
  if (nav) {
    nav.innerHTML = "";
    const homeBtn = document.createElement("button");
    homeBtn.className = "nav-btn active";
    homeBtn.dataset.view = "home";
    homeBtn.textContent = "Home";
    homeBtn.onclick = showHome;
    nav.appendChild(homeBtn);

    SECTIONS.forEach(function (sec) {
      const m = metaFor(sec);
      const btn = document.createElement("button");
      btn.className = "nav-btn";
      btn.dataset.view = sec;
      btn.textContent = m.title;
      if (sec === "labs") {
        btn.insertAdjacentHTML("beforeend", ICON_SVG.lock);
      }
      btn.onclick = function () { showSection(sec); };
      nav.appendChild(btn);
    });
  }

  const host = $("dynamic-sections");
  if (host) {
    host.innerHTML = "";
    SECTIONS.forEach(function (sec) {
      const m = metaFor(sec);
      const section = document.createElement("section");
      section.id = "view-" + sec;
      section.className = "view";
      section.innerHTML =
        '<header class="section-header">' +
        "<h2>" + m.title + "</h2>" +
        "<p>" + m.desc + "</p>" +
        "</header>" +
        '<div id="' + sec + '-list" class="file-grid"></div>' +
        (sec === "labs" ? '<div id="labs-lock" class="labs-lock" hidden></div>' : "");
      host.appendChild(section);
    });
  }
}

async function renderHome() {
  const box = $("home-cards");
  if (!box) return;
  box.innerHTML = "";
  if (!SECTIONS.length) {
    box.innerHTML =
      '<p class="empty">No sections found. Add folders and run <code>python update_files.py</code>.</p>';
    return;
  }
  const labsOpen = window.PSCrypto ? await PSCrypto.hasLabSession() : false;
  SECTIONS.forEach(function (sec) {
    const m = metaFor(sec);
    const n = countFiles(cache[sec]);
    const card = document.createElement("button");
    card.className = "card";
    card.type = "button";
    card.onclick = function () { showSection(sec); };
    const locked = sec === "labs" && !labsOpen;
    card.innerHTML =
      '<div class="card-top">' +
      '<span class="card-icon">' + iconSvg(m.icon) + "</span>" +
      (locked
        ? '<span class="card-lock">' + ICON_SVG.lock + " Discord</span>"
        : '<span class="count">' + (n ? n + " files" : "Open") + "</span>") +
      "</div>" +
      "<h3>" + m.title + "</h3>" +
      "<p>" + m.desc + "</p>";
    box.appendChild(card);
  });
}

function renderSection(sec, filter) {
  filter = filter || "";
  const el = $(sec + "-list");
  if (!el) return;
  const lock = $("labs-lock");
  if (sec === "labs" && lock) lock.hidden = true;
  el.innerHTML = "";
  if (sec === "labs" && window.PSCrypto) {
    const bar = document.createElement("div");
    bar.className = "unlocked-bar";
    bar.innerHTML = '<span>Labs unlocked on this device</span><button type="button" class="tool-btn" id="relock">Lock again</button>';
    el.appendChild(bar);
    const btn = bar.querySelector("#relock");
    if (btn) {
      btn.onclick = function () {
        PSCrypto.lockLabs();
        showSection("labs");
        renderHome();
      };
    }
  }
  const q = filter.toLowerCase().trim();
  const groups = cache[sec] || [];
  let any = false;
  groups.forEach(function (group) {
    const items = group.items.filter(function (f) {
      return (
        !q ||
        f.name.toLowerCase().indexOf(q) !== -1 ||
        group.group.toLowerCase().indexOf(q) !== -1 ||
        f.path.toLowerCase().indexOf(q) !== -1
      );
    });
    if (!items.length) return;
    any = true;
    const title = document.createElement("div");
    title.className = "group-title";
    title.textContent = group.group;
    el.appendChild(title);
    items.forEach(function (f) {
      el.appendChild(makeFileBtn(f.name, f.path));
    });
  });
  if (!any) {
    el.innerHTML =
      '<p class="empty">No files found. Add files under <code>' +
      sec +
      "</code>, run <code>python update_files.py</code>, then refresh.</p>";
  }
}

function makeFileBtn(name, path) {
  const btn = document.createElement("button");
  btn.className = "file-item";
  btn.type = "button";
  const isPy = /\.py$/i.test(path);
  const ext = (name.split(".").pop() || "file").slice(0, 3).toLowerCase();
  btn.innerHTML =
    '<div class="icon">' +
    escapeHtml(ext) +
    '</div><div class="meta"><div class="name">' +
    escapeHtml(name) +
    '</div><div class="path">' +
    escapeHtml(path) +
    "</div></div>" +
    (isPy ? '<span class="run-chip">Run</span>' : "");
  btn.onclick = function () {
    openFile(path, name);
  };
  return btn;
}

function escapeHtml(s) {
  const d = document.createElement("div");
  d.textContent = String(s);
  return d.innerHTML.replace(/"/g, String.fromCharCode(38) + "quot;");
}

function isPython(path) {
  return /\.py$/i.test(path || "");
}

function isLabsPath(path) {
  return /^labs\//i.test(path || "");
}

function renderLabsLock() {
  const list = $("labs-list");
  const lock = $("labs-lock");
  if (list) list.innerHTML = "";
  if (!lock) return;
  lock.hidden = false;
  lock.innerHTML =
    '<div class="lock-card">' +
    '<div class="lock-mark">' + ICON_SVG.lock + "</div>" +
    "<h3>Labs are locked</h3>" +
    "<p>Join Discord for a one-time passcode. Each code works once on this device and IP, then it is erased. Unused codes expire after 3 days.</p>" +
    '<a class="tool-btn run-btn discord-btn" href="https://discord.gg/mR9JByCr7" target="_blank" rel="noopener">Join Discord to get a passcode</a>' +
    '<form id="lab-unlock-form" class="unlock-form" autocomplete="off">' +
    '<label class="field">One-time passcode' +
    '<input id="lab-code" type="text" inputmode="text" autocapitalize="characters" spellcheck="false" placeholder="XXXX-XXXX" aria-label="Lab passcode" required />' +
    "</label>" +
    '<p class="form-error" id="lab-err" hidden></p>' +
    '<button class="tool-btn run-btn" type="submit">Unlock Labs</button>' +
    "</form>" +
    '<div class="support-box"><p>Labs take time to prepare. If they help you, a coffee keeps them coming.</p>' +
    '<div class="btn-row">' +
    '<a class="tool-btn" href="https://ko-fi.com/itsyst" target="_blank" rel="noopener">Ko-fi</a>' +
    '<a class="tool-btn" href="https://www.patreon.com/c/itsyst" target="_blank" rel="noopener">Patreon</a>' +
    "</div></div></div>";
  const form = $("lab-unlock-form");
  if (form) {
    form.addEventListener("submit", async function (e) {
      e.preventDefault();
      const err = $("lab-err");
      err.hidden = true;
      const res = await PSCrypto.redeemCode($("lab-code").value);
      if (!res.ok) {
        err.hidden = false;
        err.textContent = res.error;
        return;
      }
      lock.hidden = true;
      renderSection("labs", ($("search") && $("search").value) || "");
      renderHome();
    });
  }
}

async function openFile(path, name) {
  if (isLabsPath(path) && window.PSCrypto && !(await PSCrypto.hasLabSession())) {
    showSection("labs");
    return;
  }
  showView("viewer");
  currentPath = path;
  currentName = name || path;
  $("viewer-title").textContent = currentName;
  const raw = $("raw-link");
  if (raw) {
    raw.href = path;
    raw.setAttribute("download", name || "");
  }
  currentCode = "";
  originalCode = "";
  const play = $("playground");
  const block = $("code-block");
  const runBtn = $("run-btn");
  const resetBtn = $("reset-btn");
  if (isPython(path)) {
    if (play) play.hidden = false;
    if (block) block.hidden = true;
    if (runBtn) runBtn.hidden = false;
    if (resetBtn) resetBtn.hidden = false;
    const editor = $("code-editor");
    if (editor) editor.value = "Loading…";
    if ($("editor-name")) $("editor-name").textContent = currentName;
    if ($("stdin-box")) $("stdin-box").value = "";
    termClear();
    termLine("sys", "Loading file…");
    warmupPyodide();
  } else {
    if (play) play.hidden = true;
    if (block) block.hidden = false;
    if (runBtn) runBtn.hidden = true;
    if (resetBtn) resetBtn.hidden = true;
    $("code-content").textContent = "Loading…";
  }
  try {
    const res = await fetch(path);
    if (!res.ok) throw new Error("Not found (" + res.status + ")");
    const text = await res.text();
    currentCode = text;
    originalCode = text;
    if (isPython(path)) {
      const editor = $("code-editor");
      if (editor) editor.value = text;
      const details = $("stdin-details");
      if (details) details.open = /\binput\s*\(/.test(text);
      termClear();
      termLine("sys", "File loaded. Run, or type:  python this.py   ·  ls   ·  help");
    } else {
      $("code-content").innerHTML = highlight(text, path);
    }
  } catch (e) {
    const msg = "Could not load:\n" + path + "\n\n" + e.message;
    if (isPython(path)) termLine("err", msg);
    else $("code-content").textContent = msg;
  }
}

function highlight(code, path) {
  const escaped = escapeHtml(code);
  if (!isPython(path)) return escaped;
  return escaped
    .replace(/(#.*)$/gm, '<span class="cmt">$1</span>')
    .replace(
      /("[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*')/g,
      '<span class="str">$1</span>'
    )
    .replace(
      /\b(def|class|return|if|elif|else|for|while|import|from|as|try|except|finally|with|assert|lambda|True|False|None|in|not|and|or|pass|break|continue|raise|yield|async|await|global|nonlocal|match|case)\b/g,
      '<span class="kw">$1</span>'
    )
    .replace(/\b(\d+\.?\d*)\b/g, '<span class="num">$1</span>')
    .replace(
      /\b([a-zA-Z_][a-zA-Z0-9_]*)\s*(?=\()/g,
      '<span class="fn">$1</span>'
    );
}

function copyCode() {
  const editor = $("code-editor");
  const text = editor && !$("playground").hidden ? editor.value : currentCode;
  if (!text) return;
  navigator.clipboard.writeText(text).then(function () {
    const btn = document.querySelector(".copy-btn");
    if (!btn) return;
    btn.textContent = "Copied!";
    btn.classList.add("copied");
    setTimeout(function () {
      btn.textContent = "Copy";
      btn.classList.remove("copied");
    }, 1500);
  });
}

function termClear() {
  const out = $("term-out");
  if (out) out.innerHTML = "";
}

function termLine(kind, text) {
  const out = $("term-out");
  if (!out) return;
  const pre = document.createElement("pre");
  pre.className = "t-" + kind;
  pre.textContent = text;
  out.appendChild(pre);
  out.scrollTop = out.scrollHeight;
}

function setPyStatus(text, ok) {
  const el = $("py-status");
  if (!el) return;
  el.textContent = text;
  el.classList.toggle("ok", !!ok);
}

function loadScript(src) {
  return new Promise(function (resolve, reject) {
    if (document.querySelector('script[data-pyodide="1"]')) {
      if (window.loadPyodide) return resolve();
    }
    const s = document.createElement("script");
    s.src = src;
    s.async = true;
    s.dataset.pyodide = "1";
    s.onload = function () { resolve(); };
    s.onerror = function () { reject(new Error("Failed to load Python runtime.")); };
    document.head.appendChild(s);
  });
}

function warmupPyodide() {
  if (pyodide || pyodideLoading) return pyodideLoading;
  setPyStatus("loading Python…", false);
  pyodideLoading = loadScript(PYODIDE_INDEX + "pyodide.js")
    .then(function () {
      return window.loadPyodide({ indexURL: PYODIDE_INDEX });
    })
    .then(function (py) {
      pyodide = py;
      return py.runPythonAsync("_playground_ns = {'__name__': '__main__'}");
    })
    .then(function () {
      setPyStatus("python ready", true);
      return pyodide;
    })
    .catch(function (err) {
      setPyStatus("load failed", false);
      termLine("err", err.message || String(err));
      throw err;
    });
  return pyodideLoading;
}

function bindIO(stdinText) {
  const lines = stdinText ? stdinText.split(/\r?\n/) : [];
  let i = 0;
  pyodide.setStdout({
    batched: function (t) { if (t) termLine("out", t); },
  });
  pyodide.setStderr({
    batched: function (t) { if (t) termLine("err", t); },
  });
  pyodide.setStdin({
    isatty: false,
    stdin: function () {
      if (i < lines.length) return lines[i++] + "\n";
      const extra = window.prompt("Python is waiting for input():");
      if (extra === null) return;
      return extra + "\n";
    },
  });
}

function dirname(path) {
  const i = String(path || "").lastIndexOf("/");
  return i === -1 ? "" : path.slice(0, i);
}

function allItems() {
  const out = [];
  (SECTIONS || []).forEach(function (sec) {
    (cache[sec] || []).forEach(function (g) {
      (g.items || []).forEach(function (f) {
        out.push({ name: f.name, path: f.path, group: g.group, section: sec });
      });
    });
  });
  return out;
}

function filesInDir(dir) {
  return allItems().filter(function (f) {
    return dirname(f.path) === dir && /\.py$/i.test(f.name);
  });
}

function aliasNames(name) {
  const extras = [];
  const m = String(name).match(/^labb[_-]?(\d+[a-z]?)\.py$/i);
  if (m) {
    extras.push("lab" + m[1].toLowerCase() + ".py");
    extras.push("labb" + m[1].toLowerCase() + ".py");
  }
  const u = String(name).match(/^uppgift[_-]?(\d+[a-z]?)\.py$/i);
  if (u) extras.push("uppgift" + u[1].toLowerCase() + ".py");
  return extras;
}

function importedModuleFiles(src) {
  const names = [];
  const re = /(?:^|\n)\s*(?:from|import)\s+([A-Za-z_][A-Za-z0-9_]*)/g;
  let m;
  while ((m = re.exec(src || ""))) {
    const n = m[1];
    if (
      [
        "sys", "os", "math", "re", "json", "typing", "abc", "copy", "random",
        "itertools", "functools", "collections", "datetime", "unittest",
        "argparse", "traceback", "importlib", "pathlib", "numpy", "cv2",
      ].indexOf(n) === -1
    ) {
      names.push(n + ".py");
    }
  }
  return names;
}

function findFiles(query) {
  const raw = String(query || "").trim();
  if (!raw) return [];
  const q = raw.toLowerCase().replace(/\s+/g, "");
  const q2 = q.replace(/\.py$/, "");
  const num = q2.replace(/^(uppgift|labbar|labb|labs|lab)/, "");
  const dir = dirname(currentPath);
  return allItems()
    .filter(function (f) { return /\.py$/i.test(f.name); })
    .map(function (f) {
      const name = f.name.toLowerCase();
      const base = name.replace(/\.py$/, "");
      const path = f.path.toLowerCase();
      let s = 0;
      if (name === q || name === q + ".py" || base === q2) s = 100;
      else if (dir && dirname(f.path) === dir && (base.indexOf(q2) !== -1 || q2.indexOf(base) !== -1)) s = 80;
      else if (base.indexOf(q2) !== -1) s = 50;
      else if (path.indexOf(q2) !== -1) s = 40;
      else if (num && (base.indexOf(num) !== -1 || path.indexOf("labb-" + num) !== -1 || path.indexOf("labb_" + num) !== -1)) s = 30;
      return { f: f, s: s };
    })
    .filter(function (x) { return x.s > 0; })
    .sort(function (a, b) { return b.s - a.s; })
    .map(function (x) { return x.f; });
}

async function fetchText(path) {
  const res = await fetch(path);
  if (!res.ok) return null;
  return res.text();
}

async function mountProject(mainPath, mainSrc) {
  const dir = dirname(mainPath);
  const mainName = (mainPath.split("/").pop() || "main.py");
  const siblings = filesInDir(dir);
  try {
    pyodide.FS.mkdirTree("/work");
  } catch (_) {}
  const written = {};
  async function write(name, text) {
    pyodide.FS.writeFile("/work/" + name, text);
    written[name] = true;
    aliasNames(name).forEach(function (alias) {
      if (!written[alias]) {
        pyodide.FS.writeFile("/work/" + alias, text);
        written[alias] = true;
      }
    });
  }
  await write(mainName, mainSrc);
  for (let i = 0; i < siblings.length; i++) {
    const f = siblings[i];
    if (f.path === mainPath) continue;
    try {
      const text = await fetchText(f.path);
      if (text != null) await write(f.name, text);
    } catch (_) {}
  }
  const hints = importedModuleFiles(mainSrc);
  for (let i = 0; i < hints.length; i++) {
    const name = hints[i];
    if (written[name]) continue;
    const tries = dir
      ? [dir + "/" + name, dirname(dir) + "/" + name, name]
      : [name];
    for (let t = 0; t < tries.length; t++) {
      try {
        const text = await fetchText(tries[t]);
        if (text != null) {
          await write(name, text);
          break;
        }
      } catch (_) {}
    }
  }
  return Object.keys(written);
}

function formatPyError(err) {
  const msg = (err && err.message) || String(err);
  const m = msg.match(/ModuleNotFoundError: No module named '([^']+)'/);
  if (!m) return msg;
  const mod = m[1];
  const dir = dirname(currentPath) || "this folder";
  return (
    msg +
    "\n\nThe file " +
    mod +
    ".py is not next to " +
    (currentName || "this script") +
    ".\nPut " +
    mod +
    ".py in " +
    dir +
    "/ (same as a local project), refresh, then Run again.\n" +
    "In the terminal you can also:  ls   or   python other_file.py"
  );
}

async function runPlayground() {
  if (running) return;
  const editor = $("code-editor");
  if (!editor) return;
  running = true;
  const runBtn = $("run-btn");
  if (runBtn) runBtn.textContent = "Running…";
  try {
    await warmupPyodide();
    const src = editor.value;
    currentCode = src;
    const stdin = ($("stdin-box") && $("stdin-box").value) || "";
    const fileName = currentName || "main.py";
    termLine("sys", "$ python " + fileName);
    bindIO(stdin);
    const mounted = await mountProject(currentPath || fileName, src);
    pyodide.globals.set("_user_file", fileName);
    await pyodide.runPythonAsync(
      "import sys, os, runpy\n" +
        "os.chdir('/work')\n" +
        "if '/work' not in sys.path:\n" +
        "    sys.path.insert(0, '/work')\n" +
        "for _n, _m in list(sys.modules.items()):\n" +
        "    _f = getattr(_m, '__file__', '') or ''\n" +
        "    if _f.startswith('/work/'):\n" +
        "        del sys.modules[_n]\n" +
        "ns = runpy.run_path(_user_file, run_name='__main__')\n" +
        "globals()['_playground_ns'] = ns\n"
    );
    if (mounted.length > 1) {
      termLine("sys", "loaded " + mounted.filter(function (n) { return n.endsWith(".py"); }).join(", "));
    }
  } catch (err) {
    termLine("err", formatPyError(err));
  } finally {
    running = false;
    if (runBtn) runBtn.textContent = "▶ Run";
  }
}

function resetPlayground() {
  const editor = $("code-editor");
  if (editor) editor.value = originalCode;
  currentCode = originalCode;
  if ($("stdin-box")) $("stdin-box").value = "";
  termClear();
  termLine("sys", "Reset to the original file. Press Run, or type: python other.py");
}

function printHelp() {
  termLine(
    "sys",
    "Terminal (like a local shell)\n" +
      "  ls                  list files in this folder\n" +
      "  clear               clear the terminal\n" +
      "  python labb_8a.py   run a file\n" +
      "  uppgift 8a          jump to a matching lab/exam file\n" +
      "  help                this text\n" +
      "After Run, type Python as usual:  add(2, 3)"
  );
}

function printLs() {
  const dir = dirname(currentPath);
  const files = (dir ? filesInDir(dir) : []).map(function (f) { return f.name; });
  if (!files.length) {
    termLine("sys", "No .py files in this folder. Open a file first.");
    return;
  }
  termLine("sys", (dir || ".") + "\n  " + files.join("\n  "));
}

async function openAndRun(item) {
  if (!item) return;
  await openFile(item.path, item.name);
  await runPlayground();
}

async function runNamedFile(query) {
  const hits = findFiles(query);
  if (!hits.length) {
    termLine("err", "No file matching '" + query + "'. Try  ls");
    return;
  }
  if (hits.length > 1 && hits[0].name.toLowerCase() !== String(query).toLowerCase() &&
      hits[0].name.toLowerCase() !== String(query).toLowerCase() + ".py") {
    termLine(
      "sys",
      "Several matches for '" + query + "':\n  " +
        hits.slice(0, 8).map(function (f) { return f.path; }).join("\n  ") +
        "\nType: python " + hits[0].name
    );
    return;
  }
  await openAndRun(hits[0]);
}

async function evalPython(src) {
  pyodide.globals.set("_repl_src", src);
  await pyodide.runPythonAsync(
    "import ast as _ast\n" +
      "_src = _repl_src\n" +
      "try:\n" +
      "    _tree = _ast.parse(_src, mode='eval')\n" +
      "    _val = eval(compile(_tree, '<stdin>', 'eval'), _playground_ns)\n" +
      "    if _val is not None:\n" +
      "        print(repr(_val))\n" +
      "except SyntaxError:\n" +
      "    exec(_src, _playground_ns)\n"
  );
}

async function runRepl(src) {
  src = String(src || "").replace(/\s+$/, "");
  if (!src || running) return;
  running = true;
  try {
    await warmupPyodide();
    const t = src.trim();
    if (/^(clear|cls)$/i.test(t)) {
      termClear();
      return;
    }
    termLine("in", "❯ " + src);
    bindIO(($("stdin-box") && $("stdin-box").value) || "");
    if (/^(help|\?)$/i.test(t)) {
      printHelp();
      return;
    }
    if (/^(ls|dir)$/i.test(t)) {
      printLs();
      return;
    }
    const runm = t.match(/^(python3?|py|run)\s+(.+)$/i);
    if (runm) {
      running = false;
      await runNamedFile(runm[2].replace(/^["']|["']$/g, ""));
      return;
    }
    if (/^[A-Za-z0-9_./-]+\.py$/i.test(t)) {
      running = false;
      await runNamedFile(t);
      return;
    }
    if (/^(uppgift|labbar|labb|labs|lab)\s*\d+[a-z]?\s*$/i.test(t)) {
      running = false;
      await runNamedFile(t);
      return;
    }
    try {
      await evalPython(t);
    } catch (err) {
      const hits = findFiles(t);
      if (hits.length === 1) {
        running = false;
        await openAndRun(hits[0]);
        return;
      }
      if (hits.length > 1) {
        termLine(
          "sys",
          "Not Python — matching files:\n  " +
            hits.slice(0, 8).map(function (f) { return f.path; }).join("\n  ") +
            "\nType: python " + hits[0].name
        );
        return;
      }
      termLine("err", formatPyError(err));
      termLine("sys", "Tip:  ls  ·  python labb_8a.py  ·  help");
    }
  } catch (err) {
    termLine("err", formatPyError(err));
  } finally {
    running = false;
  }
}

function wireSearch() {
  const input = $("search");
  if (!input) return;
  input.addEventListener("input", function (e) {
    const q = e.target.value;
    const active = SECTIONS.find(function (s) {
      const v = $("view-" + s);
      return v && v.classList.contains("active");
    });
    if (active) renderSection(active, q);
    else if (q && SECTIONS[0]) {
      showSection(SECTIONS[0]).then(function () {
        renderSection(SECTIONS[0], q);
      });
    }
  });
}

function wireToggle() {
  const toggle = $("nav-toggle");
  if (toggle) {
    toggle.onclick = function () {
      const links = $("nav-links");
      if (links) links.classList.toggle("open");
    };
  }
}

function wirePlayground() {
  const form = $("repl-form");
  const termIn = $("term-in");
  function submitTerm(e) {
    if (e) e.preventDefault();
    const input = $("term-in");
    if (!input) return;
    const src = input.value;
    input.value = "";
    runRepl(src);
  }
  if (form) form.addEventListener("submit", submitTerm);
  if (termIn) {
    termIn.addEventListener("keydown", function (e) {
      if (e.key === "Enter" && !e.shiftKey) submitTerm(e);
    });
  }
  const editor = $("code-editor");
  if (editor) {
    editor.addEventListener("keydown", function (e) {
      if ((e.metaKey || e.ctrlKey) && e.key === "Enter") {
        e.preventDefault();
        runPlayground();
        return;
      }
      if (e.key !== "Tab") return;
      e.preventDefault();
      const start = editor.selectionStart;
      const end = editor.selectionEnd;
      editor.value = editor.value.slice(0, start) + "    " + editor.value.slice(end);
      editor.selectionStart = editor.selectionEnd = start + 4;
    });
  }
}

async function boot() {
  wireSearch();
  wireToggle();
  wirePlayground();
  showHome();
  try {
    await ensureData();
    buildUI();
    renderHome();
  } catch (e) {
    console.warn(e);
    const box = $("home-cards");
    if (box) {
      box.innerHTML =
        '<p class="error">Could not load file list. Run <code>python update_files.py</code> and refresh.</p>';
    }
  }
}

boot();
