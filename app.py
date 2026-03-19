<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>FocusFit — Schedule Manager</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700&family=Instrument+Sans:wght@300;400;500&display=swap" rel="stylesheet"/>
<style>
/* ── THEME VARIABLES ── */
[data-theme="dark"] {
  --bg: #0c0d0f;
  --surface: #141518;
  --surface2: #1c1d21;
  --surface3: #242529;
  --border: rgba(255,255,255,0.06);
  --border2: rgba(255,255,255,0.12);
  --text: #eceae4;
  --text2: #9a9890;
  --text3: #5a5956;
  --fit: #b8f058;
  --fit-dim: rgba(184,240,88,0.1);
  --fit-border: rgba(184,240,88,0.22);
  --foc: #5eb8ff;
  --foc-dim: rgba(94,184,255,0.1);
  --foc-border: rgba(94,184,255,0.22);
  --danger: #ff6b6b;
  --warn: #ffb347;
  --warn-dim: rgba(255,179,71,0.1);
  --success: #4ecb71;
}
[data-theme="light"] {
  --bg: #f2f0eb;
  --surface: #ffffff;
  --surface2: #f7f5f0;
  --surface3: #eeece8;
  --border: rgba(0,0,0,0.07);
  --border2: rgba(0,0,0,0.14);
  --text: #1a1916;
  --text2: #6b6a65;
  --text3: #b0aea8;
  --fit: #4a8a0a;
  --fit-dim: rgba(74,138,10,0.08);
  --fit-border: rgba(74,138,10,0.2);
  --foc: #0a6abf;
  --foc-dim: rgba(10,106,191,0.08);
  --foc-border: rgba(10,106,191,0.2);
  --danger: #d63030;
  --warn: #c47a00;
  --warn-dim: rgba(196,122,0,0.08);
  --success: #1e8c3e;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: 15px; scroll-behavior: smooth; }
body {
  background: var(--bg);
  color: var(--text);
  font-family: 'Instrument Sans', sans-serif;
  font-weight: 400;
  min-height: 100vh;
  transition: background 0.3s, color 0.3s;
}
h1,h2,h3,.logo { font-family: 'Syne', sans-serif; }

/* ── LAYOUT ── */
.app { display: grid; grid-template-columns: 260px 1fr; min-height: 100vh; }

/* ── SIDEBAR ── */
.sidebar {
  background: var(--surface);
  border-right: 1px solid var(--border);
  padding: 1.5rem 1.25rem;
  display: flex; flex-direction: column; gap: 1.75rem;
  position: sticky; top: 0; height: 100vh; overflow-y: auto;
}
.logo-row { display: flex; align-items: center; justify-content: space-between; }
.logo { font-size: 1.4rem; font-weight: 700; letter-spacing: -0.02em; }
.logo em { color: var(--fit); font-style: normal; }
.theme-btn {
  width: 32px; height: 32px; border-radius: 8px;
  border: 1px solid var(--border2); background: var(--surface2);
  color: var(--text2); font-size: 15px; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: all 0.15s;
}
.theme-btn:hover { background: var(--surface3); }

/* Streak */
.streak-card {
  background: var(--warn-dim);
  border: 1px solid rgba(255,179,71,0.2);
  border-radius: 12px; padding: 14px;
  display: flex; align-items: center; gap: 12px;
}
[data-theme="light"] .streak-card { border-color: rgba(196,122,0,0.2); }
.streak-icon { font-size: 2rem; line-height: 1; }
.streak-num { font-family: 'Syne', sans-serif; font-size: 1.6rem; font-weight: 700; color: var(--warn); line-height: 1; }
.streak-lbl { font-size: 11px; color: var(--text2); margin-top: 2px; }

/* Progress */
.progress-block { display: flex; flex-direction: column; gap: 10px; }
.prog-row { display: flex; flex-direction: column; gap: 5px; }
.prog-label { display: flex; justify-content: space-between; font-size: 12px; color: var(--text2); }
.prog-track { height: 6px; background: var(--surface3); border-radius: 4px; overflow: hidden; }
.prog-fill { height: 100%; border-radius: 4px; transition: width 0.5s cubic-bezier(0.4,0,0.2,1); }
.prog-fit { background: var(--fit); }
.prog-foc { background: var(--foc); }

/* Filter */
.section-label { font-size: 10px; text-transform: uppercase; letter-spacing: 0.08em; color: var(--text3); margin-bottom: 6px; }
.filter-list { display: flex; flex-direction: column; gap: 2px; }
.fbtn {
  background: transparent; border: none; color: var(--text2);
  font-family: inherit; font-size: 13px; padding: 8px 10px;
  border-radius: 8px; text-align: left; cursor: pointer;
  display: flex; align-items: center; gap: 8px; transition: all 0.15s;
}
.fbtn:hover { background: var(--surface2); color: var(--text); }
.fbtn.active { background: var(--surface2); color: var(--text); border: 1px solid var(--border2); }
.fdot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }

/* ── MAIN ── */
.main { display: flex; flex-direction: column; gap: 0; overflow: hidden; }

/* Tab bar */
.tabs {
  display: flex; gap: 2px; padding: 1rem 1.5rem 0;
  border-bottom: 1px solid var(--border);
  background: var(--surface);
}
.tab {
  font-family: 'Syne', sans-serif; font-size: 13px; font-weight: 500;
  padding: 10px 16px; border: none; background: transparent;
  color: var(--text2); cursor: pointer; border-radius: 8px 8px 0 0;
  border-bottom: 2px solid transparent; transition: all 0.15s;
}
.tab:hover { color: var(--text); }
.tab.active { color: var(--text); border-bottom-color: var(--fit); }

/* Content panels */
.panel { display: none; flex-direction: column; gap: 1.5rem; padding: 1.5rem; overflow-y: auto; }
.panel.active { display: flex; }

/* ── ADD FORM ── */
.add-card {
  background: var(--surface); border: 1px solid var(--border2);
  border-radius: 14px; padding: 1.25rem;
}
.type-toggle {
  display: grid; grid-template-columns: 1fr 1fr; gap: 6px;
  background: var(--surface2); padding: 4px; border-radius: 10px;
  margin-bottom: 1rem;
}
.tbtn {
  background: transparent; border: none; color: var(--text2);
  font-family: 'Syne', sans-serif; font-size: 13px; font-weight: 500;
  padding: 8px; border-radius: 8px; cursor: pointer; transition: all 0.2s;
  display: flex; align-items: center; justify-content: center; gap: 5px;
}
.tbtn.af { background: var(--fit-dim); color: var(--fit); box-shadow: inset 0 0 0 1px var(--fit-border); }
.tbtn.ac { background: var(--foc-dim); color: var(--foc); box-shadow: inset 0 0 0 1px var(--foc-border); }
.form-row { display: grid; grid-template-columns: 1fr 110px 110px 100px; gap: 8px; margin-bottom: 8px; }
.form-row2 { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 8px; }
.form-row input, .form-row select,
.form-row2 input, .form-row2 select, .notes-input {
  background: var(--surface2); border: 1px solid var(--border);
  border-radius: 8px; color: var(--text); font-family: inherit;
  font-size: 13px; padding: 9px 11px; outline: none; width: 100%;
  transition: border 0.15s;
}
.form-row input::placeholder, .notes-input::placeholder { color: var(--text3); }
.form-row input:focus, .form-row select:focus,
.form-row2 input:focus, .notes-input:focus { border-color: var(--border2); }
.form-row select option, .form-row2 select option { background: var(--surface2); color: var(--text); }
.notes-input { resize: none; height: 60px; margin-bottom: 8px; }
.add-btn {
  width: 100%; padding: 10px; border-radius: 8px; font-family: 'Syne', sans-serif;
  font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.15s;
  border: 1px solid var(--fit-border); background: var(--fit-dim); color: var(--fit);
}
.add-btn:hover { background: rgba(184,240,88,0.18); }
.add-btn.fm { border-color: var(--foc-border); background: var(--foc-dim); color: var(--foc); }
.add-btn.fm:hover { background: rgba(94,184,255,0.18); }

/* ── CALENDAR ── */
.cal-grid {
  display: grid; grid-template-columns: repeat(7, 1fr); gap: 10px;
}
.cal-day {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 12px; padding: 12px 10px; min-height: 120px;
}
.cal-day.today { border-color: var(--fit-border); }
.cal-day-name {
  font-family: 'Syne', sans-serif; font-size: 11px; font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.06em; color: var(--text2);
  margin-bottom: 8px;
}
.cal-day.today .cal-day-name { color: var(--fit); }
.cal-task-chip {
  font-size: 10px; padding: 3px 7px; border-radius: 5px;
  margin-bottom: 4px; white-space: nowrap; overflow: hidden;
  text-overflow: ellipsis; cursor: default;
}
.chip-fit { background: var(--fit-dim); color: var(--fit); }
.chip-foc { background: var(--foc-dim); color: var(--foc); }
.chip-done { opacity: 0.45; text-decoration: line-through; }

/* ── TASK LIST ── */
.task-list { display: flex; flex-direction: column; gap: 8px; }
.task-item {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 12px; padding: 13px 14px;
  display: flex; align-items: flex-start; gap: 12px;
  cursor: grab; transition: opacity 0.2s, border-color 0.15s, transform 0.15s;
  animation: fadeIn 0.25s ease;
}
.task-item:hover { border-color: var(--border2); }
.task-item.done { opacity: 0.38; }
.task-item.dragging { opacity: 0.4; transform: scale(0.98); cursor: grabbing; }
.task-item.drag-over { border-color: var(--fit-border); background: var(--fit-dim); }
@keyframes fadeIn { from { opacity:0; transform:translateY(-5px); } to { opacity:1; transform:translateY(0); } }
.drag-handle { color: var(--text3); font-size: 14px; cursor: grab; flex-shrink: 0; padding-top: 2px; user-select: none; }
.task-icon {
  width: 34px; height: 34px; border-radius: 9px; flex-shrink: 0;
  display: flex; align-items: center; justify-content: center; font-size: 15px;
}
.ti-fit { background: var(--fit-dim); }
.ti-foc { background: var(--foc-dim); }
.task-body { flex: 1; min-width: 0; }
.task-name {
  font-size: 14px; font-weight: 500; color: var(--text);
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.task-name.struck { text-decoration: line-through; color: var(--text3); }
.task-notes { font-size: 12px; color: var(--text2); margin-top: 3px; }
.task-tags { display: flex; gap: 5px; flex-wrap: wrap; margin-top: 6px; }
.tag {
  font-size: 10px; padding: 2px 8px; border-radius: 20px; font-weight: 500;
}
.tg-fit { background: var(--fit-dim); color: var(--fit); }
.tg-foc { background: var(--foc-dim); color: var(--foc); }
.tg-time { background: var(--surface3); color: var(--text2); }
.tg-high { background: rgba(255,107,107,0.1); color: var(--danger); }
.tg-mid  { background: var(--surface3); color: var(--text2); }
.tg-low  { background: var(--fit-dim); color: var(--fit); }
.tg-day  { background: var(--surface3); color: var(--text2); }
.task-actions { display: flex; gap: 5px; flex-shrink: 0; align-items: flex-start; }
.act {
  font-size: 11px; font-weight: 500; padding: 5px 11px;
  border-radius: 7px; border: 1px solid var(--border); background: transparent;
  color: var(--text2); cursor: pointer; font-family: inherit; transition: all 0.15s;
}
.act:hover { border-color: var(--border2); color: var(--text); }
.act.done-act { border-color: var(--fit-border); color: var(--fit); background: var(--fit-dim); }
.act.del-act:hover { background: rgba(255,107,107,0.08); color: var(--danger); border-color: rgba(255,107,107,0.3); }

/* ── POMODORO ── */
.pomo-wrap { display: flex; flex-direction: column; align-items: center; gap: 1.5rem; padding: 1rem 0; }
.pomo-ring-wrap { position: relative; width: 200px; height: 200px; }
.pomo-svg { transform: rotate(-90deg); }
.pomo-bg { fill: none; stroke: var(--surface3); stroke-width: 10; }
.pomo-arc { fill: none; stroke-width: 10; stroke-linecap: round; transition: stroke-dashoffset 1s linear, stroke 0.3s; }
.pomo-time {
  position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%);
  text-align: center;
}
.pomo-time .mins { font-family: 'Syne', sans-serif; font-size: 2.4rem; font-weight: 700; line-height: 1; }
.pomo-time .phase { font-size: 11px; color: var(--text2); text-transform: uppercase; letter-spacing: 0.06em; margin-top: 4px; }
.pomo-controls { display: flex; gap: 10px; }
.pomo-btn {
  font-family: 'Syne', sans-serif; font-size: 13px; font-weight: 600;
  padding: 10px 24px; border-radius: 10px; cursor: pointer; transition: all 0.15s;
  border: 1px solid var(--border2); background: var(--surface2); color: var(--text);
}
.pomo-btn.primary { background: var(--fit-dim); border-color: var(--fit-border); color: var(--fit); }
.pomo-btn:hover { border-color: var(--border2); background: var(--surface3); }
.pomo-settings { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; width: 100%; max-width: 360px; }
.pomo-set { background: var(--surface2); border: 1px solid var(--border); border-radius: 10px; padding: 10px; text-align: center; }
.pomo-set label { font-size: 10px; color: var(--text2); text-transform: uppercase; letter-spacing: 0.05em; display: block; margin-bottom: 6px; }
.pomo-set input { background: transparent; border: none; color: var(--text); font-family: 'Syne', sans-serif; font-size: 1.1rem; font-weight: 600; text-align: center; width: 100%; outline: none; }
.pomo-session-count { font-size: 13px; color: var(--text2); }
.pomo-session-count span { color: var(--fit); font-weight: 600; }

/* Toast */
#toast {
  position: fixed; bottom: 20px; right: 20px;
  background: var(--surface); border: 1px solid var(--border2);
  color: var(--text); font-size: 13px; padding: 11px 16px;
  border-radius: 10px; opacity: 0; transform: translateY(8px);
  transition: all 0.25s; pointer-events: none; z-index: 999;
}
#toast.show { opacity: 1; transform: translateY(0); }

.empty-msg { text-align: center; padding: 2.5rem; color: var(--text2); font-size: 13px; }

/* ── MOBILE ── */
@media (max-width: 768px) {
  .app { grid-template-columns: 1fr; }
  .sidebar { position: relative; height: auto; flex-direction: row; flex-wrap: wrap; gap: 1rem; padding: 1rem; }
  .logo-row { width: 100%; }
  .streak-card, .progress-block { flex: 1; min-width: 140px; }
  .filter-list { flex-direction: row; flex-wrap: wrap; }
  .section-label { display: none; }
  .cal-grid { grid-template-columns: repeat(2, 1fr); }
  .form-row { grid-template-columns: 1fr 1fr; }
  .form-row2 { grid-template-columns: 1fr; }
  .tabs { overflow-x: auto; padding-bottom: 0; }
}
</style>
</head>
<body>

<div class="app">

<!-- ══ SIDEBAR ══ -->
<aside class="sidebar">
  <div class="logo-row">
    <div class="logo">Focus<em>Fit</em></div>
    <button class="theme-btn" id="theme-btn" onclick="toggleTheme()" title="Toggle theme">🌙</button>
  </div>

  <!-- Streak -->
  <div class="streak-card">
    <div class="streak-icon">🔥</div>
    <div>
      <div class="streak-num" id="streak-num">0</div>
      <div class="streak-lbl">Day streak</div>
    </div>
  </div>

  <!-- Progress -->
  <div class="progress-block">
    <div class="section-label">Today's progress</div>
    <div class="prog-row">
      <div class="prog-label"><span>Fitness</span><span id="prog-fit-txt">0 / 0</span></div>
      <div class="prog-track"><div class="prog-fill prog-fit" id="prog-fit" style="width:0%"></div></div>
    </div>
    <div class="prog-row">
      <div class="prog-label"><span>Focus</span><span id="prog-foc-txt">0 / 0</span></div>
      <div class="prog-track"><div class="prog-fill prog-foc" id="prog-foc" style="width:0%"></div></div>
    </div>
  </div>

  <!-- Filters -->
  <div>
    <div class="section-label">Filter</div>
    <div class="filter-list" id="filter-list">
      <button class="fbtn active" onclick="applyFilter('all',this)"><span class="fdot" style="background:var(--text3)"></span>All</button>
      <button class="fbtn" onclick="applyFilter('fitness',this)"><span class="fdot" style="background:var(--fit)"></span>Fitness</button>
      <button class="fbtn" onclick="applyFilter('focus',this)"><span class="fdot" style="background:var(--foc)"></span>Focus</button>
      <button class="fbtn" onclick="applyFilter('pending',this)"><span class="fdot" style="background:var(--warn)"></span>Pending</button>
      <button class="fbtn" onclick="applyFilter('done',this)"><span class="fdot" style="background:var(--success)"></span>Completed</button>
    </div>
  </div>
</aside>

<!-- ══ MAIN ══ -->
<div class="main">
  <div class="tabs">
    <button class="tab active" onclick="showTab('tasks',this)">📋 Tasks</button>
    <button class="tab" onclick="showTab('calendar',this)">📅 Weekly Calendar</button>
    <button class="tab" onclick="showTab('pomodoro',this)">⏱ Pomodoro</button>
  </div>

  <!-- Tasks Panel -->
  <div class="panel active" id="panel-tasks">
    <div class="add-card">
      <div class="type-toggle">
        <button class="tbtn af" id="tbtn-fit" onclick="setType('fitness')">🏃 Fitness</button>
        <button class="tbtn" id="tbtn-foc" onclick="setType('focus')">🎯 Focus Work</button>
      </div>
      <div class="form-row">
        <input type="text" id="f-name" placeholder="Task name..." />
        <input type="time" id="f-time" />
        <select id="f-dur">
          <option value="15">15 min</option>
          <option value="30" selected>30 min</option>
          <option value="45">45 min</option>
          <option value="60">1 hr</option>
          <option value="90">1.5 hr</option>
          <option value="120">2 hr</option>
        </select>
        <select id="f-pri">
          <option value="high">High</option>
          <option value="mid" selected>Medium</option>
          <option value="low">Low</option>
        </select>
      </div>
      <div class="form-row2">
        <select id="f-day">
          <option value="Mon">Monday</option>
          <option value="Tue">Tuesday</option>
          <option value="Wed">Wednesday</option>
          <option value="Thu">Thursday</option>
          <option value="Fri">Friday</option>
          <option value="Sat">Saturday</option>
          <option value="Sun">Sunday</option>
        </select>
        <input type="text" id="f-notes" placeholder="Notes (optional)..." />
      </div>
      <button class="add-btn" id="add-btn" onclick="addTask()">+ Add Task</button>
    </div>

    <div class="task-list" id="task-list">
      <div class="empty-msg">Connecting to server...</div>
    </div>
  </div>

  <!-- Calendar Panel -->
  <div class="panel" id="panel-calendar">
    <div class="cal-grid" id="cal-grid"></div>
  </div>

  <!-- Pomodoro Panel -->
  <div class="panel" id="panel-pomodoro">
    <div class="pomo-wrap">
      <div class="pomo-ring-wrap">
        <svg class="pomo-svg" width="200" height="200" viewBox="0 0 200 200">
          <circle class="pomo-bg" cx="100" cy="100" r="88"/>
          <circle class="pomo-arc" id="pomo-arc" cx="100" cy="100" r="88"
            stroke="#b8f058" stroke-dasharray="552.9" stroke-dashoffset="0"/>
        </svg>
        <div class="pomo-time">
          <div class="mins" id="pomo-display">25:00</div>
          <div class="phase" id="pomo-phase">Focus</div>
        </div>
      </div>

      <div class="pomo-controls">
        <button class="pomo-btn primary" id="pomo-start" onclick="pomoToggle()">▶ Start</button>
        <button class="pomo-btn" onclick="pomoReset()">↺ Reset</button>
      </div>

      <div class="pomo-session-count">Sessions completed today: <span id="pomo-sessions">0</span></div>

      <div class="pomo-settings">
        <div class="pomo-set">
          <label>Focus (min)</label>
          <input type="number" id="set-focus" value="25" min="1" max="60" onchange="pomoReset()"/>
        </div>
        <div class="pomo-set">
          <label>Short break</label>
          <input type="number" id="set-short" value="5" min="1" max="30" onchange="pomoReset()"/>
        </div>
        <div class="pomo-set">
          <label>Long break</label>
          <input type="number" id="set-long" value="15" min="1" max="60" onchange="pomoReset()"/>
        </div>
      </div>
    </div>
  </div>
</div>
</div>

<div id="toast"></div>

<script>
const API = 'http://127.0.0.1:5000';
let tasks = [];
let currentType = 'fitness';
let currentFilter = 'all';
let dragSrcId = null;

const DAYS = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];
const DAY_FULL = { Mon:'Monday',Tue:'Tuesday',Wed:'Wednesday',Thu:'Thursday',Fri:'Friday',Sat:'Saturday',Sun:'Sunday' };

// ── Theme ──────────────────────────────────────────
function toggleTheme() {
  const html = document.documentElement;
  const isDark = html.getAttribute('data-theme') === 'dark';
  html.setAttribute('data-theme', isDark ? 'light' : 'dark');
  document.getElementById('theme-btn').textContent = isDark ? '🌙' : '☀️';
  localStorage.setItem('theme', isDark ? 'light' : 'dark');
}
(function initTheme() {
  const saved = localStorage.getItem('theme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);
  document.getElementById('theme-btn').textContent = saved === 'dark' ? '☀️' : '🌙';
})();

// ── Tabs ───────────────────────────────────────────
function showTab(name, el) {
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('panel-' + name).classList.add('active');
  if (name === 'calendar') renderCalendar();
}

// ── Type Toggle ────────────────────────────────────
function setType(t) {
  currentType = t;
  document.getElementById('tbtn-fit').className = 'tbtn' + (t === 'fitness' ? ' af' : '');
  document.getElementById('tbtn-foc').className = 'tbtn' + (t === 'focus' ? ' ac' : '');
  document.getElementById('add-btn').className = 'add-btn' + (t === 'focus' ? ' fm' : '');
}

// ── Filter ─────────────────────────────────────────
function applyFilter(f, el) {
  currentFilter = f;
  document.querySelectorAll('.fbtn').forEach(b => b.classList.remove('active'));
  el.classList.add('active');
  renderTasks();
}

// ── Toast ──────────────────────────────────────────
function toast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2200);
}

// ── API ────────────────────────────────────────────
async function fetchAll() {
  try {
    const [tr, mr] = await Promise.all([
      fetch(API + '/tasks'), fetch(API + '/meta')
    ]);
    tasks = await tr.json();
    const meta = await mr.json();
    document.getElementById('streak-num').textContent = meta.streak || 0;
    renderAll();
  } catch {
    document.getElementById('task-list').innerHTML =
      '<div class="empty-msg">⚠️ Cannot connect to Flask server.<br>Run: cd "fitness period" then python app.py</div>';
  }
}

async function addTask() {
  const name = document.getElementById('f-name').value.trim();
  if (!name) { document.getElementById('f-name').focus(); return; }
  const body = {
    name, type: currentType,
    time: document.getElementById('f-time').value,
    dur: parseInt(document.getElementById('f-dur').value),
    pri: document.getElementById('f-pri').value,
    notes: document.getElementById('f-notes').value.trim(),
    day: document.getElementById('f-day').value
  };
  try {
    const res = await fetch(API + '/tasks', {
      method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(body)
    });
    const task = await res.json();
    tasks.push(task);
    document.getElementById('f-name').value = '';
    document.getElementById('f-notes').value = '';
    renderAll();
    toast('Task added ✓');
  } catch { toast('Error: server not reachable'); }
}

async function toggleDone(id) {
  const task = tasks.find(t => t.id === id);
  if (!task) return;
  const newDone = !task.done;
  try {
    await fetch(API + '/tasks/' + id, {
      method: 'PATCH', headers: {'Content-Type':'application/json'},
      body: JSON.stringify({ done: newDone })
    });
    task.done = newDone;
    if (newDone) {
      const mr = await fetch(API + '/meta');
      const meta = await mr.json();
      document.getElementById('streak-num').textContent = meta.streak || 0;
    }
    renderAll();
    toast(newDone ? '🎉 Task completed!' : 'Marked as pending');
  } catch { toast('Error updating task'); }
}

async function deleteTask(id) {
  try {
    await fetch(API + '/tasks/' + id, { method: 'DELETE' });
    tasks = tasks.filter(t => t.id !== id);
    renderAll();
    toast('Task removed');
  } catch { toast('Error deleting'); }
}

// ── Drag & Drop ────────────────────────────────────
function setupDrag(el, id) {
  el.draggable = true;
  el.addEventListener('dragstart', () => { dragSrcId = id; el.classList.add('dragging'); });
  el.addEventListener('dragend', () => el.classList.remove('dragging'));
  el.addEventListener('dragover', e => { e.preventDefault(); el.classList.add('drag-over'); });
  el.addEventListener('dragleave', () => el.classList.remove('drag-over'));
  el.addEventListener('drop', async e => {
    e.preventDefault();
    el.classList.remove('drag-over');
    if (dragSrcId === id) return;
    const srcIdx = tasks.findIndex(t => t.id === dragSrcId);
    const dstIdx = tasks.findIndex(t => t.id === id);
    const [moved] = tasks.splice(srcIdx, 1);
    tasks.splice(dstIdx, 0, moved);
    renderTasks();
    try {
      await fetch(API + '/tasks/reorder', {
        method: 'POST', headers: {'Content-Type':'application/json'},
        body: JSON.stringify({ ids: tasks.map(t => t.id) })
      });
    } catch {}
  });
}

// ── Render ─────────────────────────────────────────
function renderAll() { renderStats(); renderTasks(); renderCalendar(); }

function renderStats() {
  const fitTasks = tasks.filter(t => t.type === 'fitness');
  const focTasks = tasks.filter(t => t.type === 'focus');
  const fitDone = fitTasks.filter(t => t.done).length;
  const focDone = focTasks.filter(t => t.done).length;
  const fitPct = fitTasks.length ? Math.round((fitDone / fitTasks.length) * 100) : 0;
  const focPct = focTasks.length ? Math.round((focDone / focTasks.length) * 100) : 0;
  document.getElementById('prog-fit').style.width = fitPct + '%';
  document.getElementById('prog-foc').style.width = focPct + '%';
  document.getElementById('prog-fit-txt').textContent = fitDone + ' / ' + fitTasks.length;
  document.getElementById('prog-foc-txt').textContent = focDone + ' / ' + focTasks.length;
}

function renderTasks() {
  const list = document.getElementById('task-list');
  let filtered = [...tasks];
  if (currentFilter === 'fitness') filtered = tasks.filter(t => t.type === 'fitness');
  else if (currentFilter === 'focus') filtered = tasks.filter(t => t.type === 'focus');
  else if (currentFilter === 'pending') filtered = tasks.filter(t => !t.done);
  else if (currentFilter === 'done') filtered = tasks.filter(t => t.done);

  if (!filtered.length) {
    list.innerHTML = '<div class="empty-msg">No tasks here. Add one above!</div>';
    return;
  }

  const priClass = { high:'tg-high', mid:'tg-mid', low:'tg-low' };
  const priLabel = { high:'High', mid:'Medium', low:'Low' };

  list.innerHTML = '';
  filtered.forEach(t => {
    const div = document.createElement('div');
    div.className = 'task-item' + (t.done ? ' done' : '');
    div.dataset.id = t.id;
    div.innerHTML = `
      <div class="drag-handle" title="Drag to reorder">⠿</div>
      <div class="task-icon ${t.type === 'fitness' ? 'ti-fit' : 'ti-foc'}">${t.type === 'fitness' ? '🏃' : '🎯'}</div>
      <div class="task-body">
        <div class="task-name ${t.done ? 'struck' : ''}">${t.name}</div>
        ${t.notes ? `<div class="task-notes">${t.notes}</div>` : ''}
        <div class="task-tags">
          <span class="tag ${t.type === 'fitness' ? 'tg-fit' : 'tg-foc'}">${t.type === 'fitness' ? 'Fitness' : 'Focus'}</span>
          <span class="tag tg-time">${t.dur}m${t.time ? ' · ' + t.time : ''}</span>
          <span class="tag ${priClass[t.pri]}">${priLabel[t.pri]}</span>
          ${t.day ? `<span class="tag tg-day">${t.day}</span>` : ''}
        </div>
      </div>
      <div class="task-actions">
        <button class="act ${t.done ? '' : 'done-act'}" onclick="toggleDone(${t.id})">${t.done ? 'Undo' : '✓ Done'}</button>
        <button class="act del-act" onclick="deleteTask(${t.id})">Delete</button>
      </div>`;
    setupDrag(div, t.id);
    list.appendChild(div);
  });
}

function renderCalendar() {
  const grid = document.getElementById('cal-grid');
  if (!grid) return;
  const todayDay = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'][new Date().getDay()];
  grid.innerHTML = DAYS.map(day => {
    const dayTasks = tasks.filter(t => t.day === day);
    const chips = dayTasks.map(t =>
      `<div class="cal-task-chip ${t.type==='fitness'?'chip-fit':'chip-foc'} ${t.done?'chip-done':''}" title="${t.name}">${t.name}</div>`
    ).join('');
    return `<div class="cal-day ${day===todayDay?'today':''}">
      <div class="cal-day-name">${day}</div>
      ${chips || '<div style="font-size:11px;color:var(--text3);margin-top:4px;">—</div>'}
    </div>`;
  }).join('');
}

// ── Pomodoro ───────────────────────────────────────
let pomoTimer = null;
let pomoRunning = false;
let pomoPhase = 'focus'; // focus | short | long
let pomoSecondsLeft = 25 * 60;
let pomoSessions = 0;
const circumference = 2 * Math.PI * 88;

function pomoGetDuration() {
  if (pomoPhase === 'focus') return parseInt(document.getElementById('set-focus').value) * 60;
  if (pomoPhase === 'short') return parseInt(document.getElementById('set-short').value) * 60;
  return parseInt(document.getElementById('set-long').value) * 60;
}

function pomoUpdateUI() {
  const m = Math.floor(pomoSecondsLeft / 60).toString().padStart(2,'0');
  const s = (pomoSecondsLeft % 60).toString().padStart(2,'0');
  document.getElementById('pomo-display').textContent = m + ':' + s;
  const total = pomoGetDuration();
  const progress = (total - pomoSecondsLeft) / total;
  const offset = circumference * (1 - progress);
  const arc = document.getElementById('pomo-arc');
  arc.style.strokeDashoffset = offset;
  const colors = { focus: '#b8f058', short: '#5eb8ff', long: '#ffb347' };
  arc.style.stroke = colors[pomoPhase];
  const labels = { focus: 'Focus', short: 'Short break', long: 'Long break' };
  document.getElementById('pomo-phase').textContent = labels[pomoPhase];
}

function pomoToggle() {
  if (pomoRunning) {
    clearInterval(pomoTimer);
    pomoRunning = false;
    document.getElementById('pomo-start').textContent = '▶ Resume';
  } else {
    pomoRunning = true;
    document.getElementById('pomo-start').textContent = '⏸ Pause';
    pomoTimer = setInterval(() => {
      pomoSecondsLeft--;
      pomoUpdateUI();
      if (pomoSecondsLeft <= 0) {
        clearInterval(pomoTimer);
        pomoRunning = false;
        if (pomoPhase === 'focus') {
          pomoSessions++;
          document.getElementById('pomo-sessions').textContent = pomoSessions;
          toast('🎉 Focus session done! Take a break.');
          pomoPhase = pomoSessions % 4 === 0 ? 'long' : 'short';
        } else {
          toast('⏱ Break over! Time to focus.');
          pomoPhase = 'focus';
        }
        pomoSecondsLeft = pomoGetDuration();
        document.getElementById('pomo-start').textContent = '▶ Start';
        pomoUpdateUI();
      }
    }, 1000);
  }
}

function pomoReset() {
  clearInterval(pomoTimer);
  pomoRunning = false;
  pomoPhase = 'focus';
  pomoSecondsLeft = parseInt(document.getElementById('set-focus').value) * 60;
  document.getElementById('pomo-start').textContent = '▶ Start';
  pomoUpdateUI();
}

// Set today's day as default in form
const todayIdx = new Date().getDay();
const dayOrder = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
document.getElementById('f-day').value = dayOrder[todayIdx];

pomoSecondsLeft = 25 * 60;
pomoUpdateUI();
fetchAll();
</script>
</body>
</html>
