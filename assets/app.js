/* Python Study – fully dynamic (no hardcoded file lists)
   New files under lectures/ or exams/ appear automatically after you push.
*/

const OWNER = "itsyst";
const REPO = "python-strudy";
const BRANCH = "main";

let lastView = "home";
let currentCode = "";
let lecturesCache = [];
let examsCache = []; // { group, items: [{name, path}] }

function $(id) { return document.getElementById(id); }

/* ---------- GitHub API helpers ---------- */
async function apiList(path) {
  const url = `https://api.github.com/repos/${OWNER}/${REPO}/contents/${path}?ref=${BRANCH}`;
  const res = await fetch(url, {
    headers: { Accept: "application/vnd.github+json" }
  });
  if (!res.ok) {
    if (res.status === 403 || res.status === 404) {
      throw new Error("API_LIMIT_OR_PRIVATE");
    }
    throw new Error(`HTTP ${res.status}`);
  }
  return res.json();
}

async function loadLectures() {
  const items = await apiList("lectures");
  return items
    .filter(f => f.type === "file" && f.name.endsWith(".py"))
    .sort((a, b) => a.name.localeCompare(b.name, undefined, { numeric: true }))
    .map(f => ({
      name: prettyName(f.name),
      path: f.path,
      icon: "📄"
    }));
}

async function loadExams() {
  const top = await apiList("exams");
  const dirs = top
    .filter(f => f.type === "dir")
    .sort((a, b) => b.name.localeCompare(a.name)); // newest first

  const groups = [];
  for (const dir of dirs) {
    const files = await apiList(dir.path);
    const pyFiles = files
      .filter(f => f.type === "file" && f.name.endsWith(".py"))
      .sort((a, b) => a.name.localeCompare(b.name, undefined, { numeric: true }))
      .map(f => ({
        name: f.name.replace(/\.py$/, ""),
        path: f.path
      }));
    if (pyFiles.length) {
      groups.push({ group: dir.name, items: pyFiles });
    }
  }
  return groups;
}

function prettyName(filename) {
  return filename
    .replace(/\.py$/, "")
    .replace(/_/g, " ")
    .replace(/^(\d+)\s/, "$1 · ");
}

/* ---------- UI ---------- */
function showView(name) {
  document.querySelectorAll(".view").forEach(v => v.classList.remove("active"));
  $(`view-${name}`).classList.add("active");
  document.querySelectorAll(".nav-btn").forEach(b => {
    b.classList.toggle("active", b.dataset.view === name);
  });
}

function showHome() {
  lastView = "home";
  showView("home");
  $("search").value = "";
}

async function showSection(section) {
  lastView = section;
  showView(section);
  $("search").value = "";
  await ensureData();
  renderLists();
}

function goBack() {
  showSection(lastView === "viewer" ? "home" : lastView);
}

async function ensureData() {
  if (lecturesCache.length || examsCache.length) return;
  try {
    $("lectures-list").innerHTML = "<p class='loading'>Loading…</p>";
    $("exams-list").innerHTML = "<p class='loading'>Loading…</p>";
    lecturesCache = await loadLectures();
    examsCache = await loadExams();
  } catch (e) {
    const msg = e.message === "API_LIMIT_OR_PRIVATE"
      ? "Could not list files. Make the repo <strong>public</strong> (needed for dynamic listing) or check rate limits."
      : `Failed to load file list: ${e.message}`;
    $("lectures-list").innerHTML = `<p class="error">${msg}</p>`;
    $("exams-list").innerHTML = `<p class="error">${msg}</p>`;
  }
}

function renderLists(filter = "") {
  const q = filter.toLowerCase().trim();

  // Lectures
  const lecEl = $("lectures-list");
  lecEl.innerHTML = "";
  const lecs = lecturesCache.filter(f =>
    !q || f.name.toLowerCase().includes(q) || f.path.toLowerCase().includes(q)
  );
  if (!lecs.length) {
    lecEl.innerHTML = "<p class='empty'>No lectures found. Add .py files under <code>lectures/</code> and push.</p>";
  } else {
    lecs.forEach(f => lecEl.appendChild(makeFileBtn(f.name, f.path, f.icon)));
  }

  // Exams
  const exEl = $("exams-list");
  exEl.innerHTML = "";
  let any = false;
  examsCache.forEach(group => {
    const items = group.items.filter(f =>
      !q || f.name.toLowerCase().includes(q) || group.group.includes(q) || f.path.toLowerCase().includes(q)
    );
    if (!items.length) return;
    any = true;
    const title = document.createElement("div");
    title.className = "group-title";
    title.textContent = group.group;
    exEl.appendChild(title);
    items.forEach(f => exEl.appendChild(makeFileBtn(f.name, f.path, "📝")));
  });
  if (!any) {
    exEl.innerHTML = "<p class='empty'>No exams found. Add folders + .py files under <code>exams/</code> and push.</p>";
  }
}

function makeFileBtn(name, path, icon) {
  const btn = document.createElement("button");
  btn.className = "file-item";
  btn.innerHTML = `
    <div class="icon">${icon}</div>
    <div class="meta">
      <div class="name">${name}</div>
      <div class="path">${path}</div>
    </div>`;
  btn.onclick = () => openFile(path, name);
  return btn;
}

async function openFile(path, name) {
  showView("viewer");
  $("viewer-title").textContent = name || path;
  $("code-content").textContent = "Loading…";
  currentCode = "";

  try {
    // Relative path → works on GitHub Pages and local Live Server
    const res = await fetch(path);
    if (!res.ok) throw new Error("Not found");
    const text = await res.text();
    currentCode = text;
    $("code-content").innerHTML = highlightPython(text);
  } catch (e) {
    $("code-content").textContent = `Could not load:\n${path}\n\n${e.message}`;
  }
}

function highlightPython(code) {
  const escaped = code
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
  return escaped
    .replace(/(#.*)$/gm, '<span class="cmt">$1</span>')
    .replace(/("[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*')/g, '<span class="str">$1</span>')
    .replace(/\b(def|class|return|if|elif|else|for|while|import|from|as|try|except|finally|with|assert|lambda|True|False|None|in|not|and|or|pass|break|continue|raise|yield|async|await)\b/g, '<span class="kw">$1</span>')
    .replace(/\b(\d+\.?\d*)\b/g, '<span class="num">$1</span>')
    .replace(/\b([a-zA-Z_][a-zA-Z0-9_]*)\s*(?=\()/g, '<span class="fn">$1</span>');
}

function copyCode() {
  if (!currentCode) return;
  navigator.clipboard.writeText(currentCode).then(() => {
    const btn = document.querySelector(".copy-btn");
    btn.textContent = "Copied!";
    btn.classList.add("copied");
    setTimeout(() => {
      btn.textContent = "Copy";
      btn.classList.remove("copied");
    }, 1500);
  });
}

/* Search */
$("search").addEventListener("input", (e) => {
  const q = e.target.value;
  const onList =
    $("view-lectures").classList.contains("active") ||
    $("view-exams").classList.contains("active");
  if (onList) {
    renderLists(q);
  } else if (q) {
    showSection("lectures").then(() => renderLists(q));
  }
});

/* Init */
showHome();
// Preload in background so first click is fast
ensureData().then(() => renderLists()).catch(() => {});
