/* Python Study – dynamic site (auto-detects folders from files.json) */

const KNOWN_META = {
  exams: { title: "Exams", icon: "📝", desc: "Past tentor by date" },
  labs: { title: "Labs", icon: "🔬", desc: "Labbar & solutions" },
  exercises: { title: "Exercises", icon: "✏️", desc: "Practice exercises" },
  seminars: { title: "Seminars", icon: "💬", desc: "Seminar examples" },
  lectures: { title: "Lectures", icon: "📚", desc: "Lecture notes & code" },
  projects: { title: "Projects", icon: "🚀", desc: "Project materials" },
};

let SECTIONS = [];
let lastView = "home";
let currentCode = "";
let cache = {};
let loaded = false;

function $(id) {
  return document.getElementById(id);
}

function metaFor(key) {
  if (KNOWN_META[key]) return KNOWN_META[key];
  const title = key.charAt(0).toUpperCase() + key.slice(1).replace(/[-_]/g, " ");
  return { title, icon: "📁", desc: title + " materials" };
}

async function loadData() {
  for (const url of ["assets/files.json", "files.json"]) {
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
    "</div></div>";
  btn.onclick = function () {
    openFile(path, name);
  };
  return btn;
}

function escapeHtml(s) {
  return String(s)
    .replace(/&/g, "&")
    .replace(/</g, "<")
    .replace(/>/g, ">")
    .replace(/"/g, """);
}

async function openFile(path, name) {
  showView("viewer");
  $("viewer-title").textContent = name || path;
  const raw = $("raw-link");
  if (raw) {
    raw.href = path;
    raw.setAttribute("download", name || "");
  }
  $("code-content").textContent = "Loading…";
  currentCode = "";
  try {
    const res = await fetch(path);
    if (!res.ok) throw new Error("Not found (" + res.status + ")");
    const text = await res.text();
    currentCode = text;
    $("code-content").innerHTML = highlight(text, path);
  } catch (e) {
    $("code-content").textContent =
      "Could not load:\n" + path + "\n\n" + e.message;
  }
}

function highlight(code, path) {
  const escaped = code
    .replace(/&/g, "&")
    .replace(/</g, "<")
    .replace(/>/g, ">");
  if (!/\.py$/i.test(path || "")) return escaped;
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
  if (!currentCode) return;
  navigator.clipboard.writeText(currentCode).then(function () {
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

async function boot() {
  wireSearch();
  wireToggle();
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
