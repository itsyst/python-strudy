/* Python Study – dynamic site + in-browser Python playground */

const KNOWN_META = {
  exams: { title: "Exams", icon: "📝", desc: "Past tentor by date — edit & run" },
  labs: { title: "Labs", icon: "🔬", desc: "Labbar & solutions — Discord for codes" },
  exercises: { title: "Exercises", icon: "✏️", desc: "Practice exercises — edit & run" },
  seminars: { title: "Seminars", icon: "💬", desc: "Seminar examples — edit & run" },
  lectures: { title: "Lectures", icon: "📚", desc: "Lecture notes & code" },
  projects: { title: "Projects", icon: "🚀", desc: "Project materials" },
};

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
  return { title, icon: "📁", desc: title + " materials" };
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
        "<h2>" + m.icon + " " + m.title + "</h2>" +
        "<p>" + m.desc + "</p>" +
        "</header>" +
        '<div id="' + sec + '-list" class="file-grid"></div>';
      host.appendChild(section);
    });
  }
}

function renderHome() {
  const box = $("home-cards");
  if (!box) return;
  box.innerHTML = "";
  if (!SECTIONS.length) {
    box.innerHTML =
      '<p class="empty">No sections found. Add folders and run <code>python update_files.py</code>.</p>';
    return;
  }
  SECTIONS.forEach(function (sec) {
    const m = metaFor(sec);
    const n = countFiles(cache[sec]);
    const card = document.createElement("button");
    card.className = "card";
    card.type = "button";
    card.onclick = function () { showSection(sec); };
    card.innerHTML =
      '<div class="card-icon">' + m.icon + "</div>" +
      "<h3>" + m.title + "</h3>" +
      "<p>" + m.desc + "</p>" +
      '<span class="count">' + (n ? n + " files" : "Open →") + "</span>";
    box.appendChild(card);
  });
}

function renderSection(sec, filter) {
  filter = filter || "";
  const el = $(sec + "-list");
  if (!el) return;
  el.innerHTML = "";
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
  const icon = path.endsWith(".md")
    ? "📘"
    : path.endsWith(".txt")
    ? "📃"
    : "📄";
  btn.innerHTML =
    '<div class="icon">' +
    icon +
    '</div><div class="meta"><div class="name">' +
    escapeHtml(name) +
    '</div><div class="path">' +
    escapeHtml(path) +
    "</div></div>" +
    (isPy ? '<span class="run-chip">▶ Run</span>' : "");
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

async function openFile(path, name) {
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
      termLine("sys", "File loaded. Press Run, then use the prompt like a local shell.");
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
    termLine("sys", "$ python " + currentName);
    bindIO(stdin);
    pyodide.globals.set("_user_src", src);
    pyodide.globals.set("_user_file", currentName);
    await pyodide.runPythonAsync(
      "_playground_ns = {'__name__': '__main__', '__file__': _user_file}\nexec(_user_src, _playground_ns)"
    );
  } catch (err) {
    termLine("err", (err && err.message) || String(err));
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
  termLine("sys", "Reset to the original file. Press Run to execute again.");
}

async function runRepl(src) {
  src = String(src || "").replace(/\s+$/, "");
  if (!src || running) return;
  running = true;
  try {
    await warmupPyodide();
    termLine("in", ">>> " + src);
    bindIO(($("stdin-box") && $("stdin-box").value) || "");
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
  } catch (err) {
    termLine("err", (err && err.message) || String(err));
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
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      const input = $("term-in");
      if (!input) return;
      const src = input.value;
      input.value = "";
      runRepl(src);
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
