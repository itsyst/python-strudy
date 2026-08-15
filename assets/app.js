/* Python Study – simple SPA */

const lectures = [
  { name: "01 Data Structures", path: "lectures/01_data_structures.py", icon: "📦" },
  { name: "02 Factorial", path: "lectures/02_factorial.py", icon: "🔢" },
  { name: "03 Strings", path: "lectures/03_strings.py", icon: "🔤" },
  { name: "04 FizzBuzz", path: "lectures/04_fizzbuzz.py", icon: "buzz" },
  { name: "05 Control Flow", path: "lectures/05_control_flow.py", icon: "🔀" },
  { name: "06 Functions", path: "lectures/06_functions.py", icon: "ƒ" },
  { name: "07 Exceptions", path: "lectures/07_exceptions.py", icon: "⚠️" },
  { name: "08 Char Frequency", path: "lectures/08_char_frequency.py", icon: "📊" },
  { name: "09 Numbers", path: "lectures/09_numbers.py", icon: "➕" },
  { name: "10 Type Conversion", path: "lectures/10_type_conversion.py", icon: "🔄" },
];

const exams = [
  { group: "2014-01-14", items: [
    { name: "ex1 · Find notes", path: "exams/2014-01-14/ex1.py" },
  ]},
  { group: "2024-01-09", items: [
    { name: "ex1 · Cumulative sums", path: "exams/2024-01-09/ex1.py" },
    { name: "ex2 · Merge sorted lists", path: "exams/2024-01-09/ex2.py" },
  ]},
  { group: "2025-03-18", items: [
    { name: "ex1 · Doors (stub)", path: "exams/2025-03-18/ex1.py" },
  ]},
  { group: "2025-08-19", items: [
    { name: "ex1", path: "TENTOR/2025-08-19/ex1.py" },
    { name: "ex2", path: "TENTOR/2025-08-19/ex2.py" },
    { name: "ex3a", path: "TENTOR/2025-08-19/ex3a.py" },
    { name: "ex3b", path: "TENTOR/2025-08-19/ex3b.py" },
    { name: "ex4", path: "TENTOR/2025-08-19/ex4.py" },
    { name: "ex5a", path: "TENTOR/2025-08-19/ex5a.py" },
    { name: "ex5b", path: "TENTOR/2025-08-19/ex5b.py" },
    { name: "ex6a", path: "TENTOR/2025-08-19/ex6a.py" },
    { name: "ex6b", path: "TENTOR/2025-08-19/ex6b.py" },
  ]},
  { group: "2026-01-14", items: [
    { name: "ex1", path: "TENTOR/2026-01-14/ex1.py" },
    { name: "ex2", path: "TENTOR/2026-01-14/ex2.py" },
    { name: "ex3", path: "TENTOR/2026-01-14/ex3.py" },
    { name: "ex4", path: "TENTOR/2026-01-14/ex4.py" },
    { name: "ex5", path: "TENTOR/2026-01-14/ex5.py" },
    { name: "ex6a", path: "TENTOR/2026-01-14/ex6a.py" },
    { name: "ex6b", path: "TENTOR/2026-01-14/ex6b.py" },
  ]},
];

let lastView = "home";
let currentCode = "";

function $(id) { return document.getElementById(id); }

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

function showSection(section) {
  lastView = section;
  showView(section);
  $("search").value = "";
  renderLists();
}

function goBack() {
  showSection(lastView === "viewer" ? "home" : lastView);
}

function renderLists(filter = "") {
  const q = filter.toLowerCase().trim();

  // Lectures
  const lecEl = $("lectures-list");
  lecEl.innerHTML = "";
  lectures
    .filter(f => !q || f.name.toLowerCase().includes(q) || f.path.toLowerCase().includes(q))
    .forEach(f => {
      lecEl.appendChild(makeFileBtn(f.name, f.path, f.icon || "📄"));
    });

  // Exams
  const exEl = $("exams-list");
  exEl.innerHTML = "";
  exams.forEach(group => {
    const items = group.items.filter(f =>
      !q || f.name.toLowerCase().includes(q) || group.group.includes(q) || f.path.toLowerCase().includes(q)
    );
    if (!items.length) return;
    const title = document.createElement("div");
    title.className = "group-title";
    title.textContent = group.group;
    exEl.appendChild(title);
    items.forEach(f => {
      exEl.appendChild(makeFileBtn(f.name, f.path, "📝"));
    });
  });
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
    const res = await fetch(path);
    if (!res.ok) throw new Error("Not found");
    const text = await res.text();
    currentCode = text;
    $("code-content").innerHTML = highlightPython(text);
  } catch (e) {
    $("code-content").textContent = `Could not load file:\n${path}\n\nMake sure the file exists in the repository.`;
  }
}

function highlightPython(code) {
  // very light highlighter
  const escaped = code
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");

  return escaped
    .replace(/(#.*)$/gm, '<span class="cmt">$1</span>')
    .replace(/("[^"]*"|'[^']*')/g, '<span class="str">$1</span>')
    .replace(/\b(def|class|return|if|elif|else|for|while|import|from|as|try|except|finally|with|assert|lambda|True|False|None|in|not|and|or|pass|break|continue|raise|yield)\b/g, '<span class="kw">$1</span>')
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

// Search
$("search").addEventListener("input", (e) => {
  const q = e.target.value;
  if (document.getElementById("view-lectures").classList.contains("active") ||
      document.getElementById("view-exams").classList.contains("active")) {
    renderLists(q);
  } else if (q) {
    // from home → show both filtered
    showSection("lectures");
    renderLists(q);
    // also show exams section briefly? just switch to lectures for simplicity
  }
});

// Init
renderLists();
showHome();
