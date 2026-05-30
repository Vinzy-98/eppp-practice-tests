/* ================================================================
   EPPP Practice Test App — Single-page, localStorage-backed
   ================================================================ */

(function () {
  'use strict';

  // ── Storage helpers ──────────────────────────────────────
  const STORAGE_KEY = 'eppp_progress';
  const IN_PROGRESS_KEY = '__inProgress';
  const DASHBOARD_TAB_KEY = '__dashboardTab';

  function loadProgress() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {};
    } catch (e) { return {}; }
  }

  function saveProgress(data) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
  }

  function getTestAttempts(slug) {
    const p = loadProgress();
    return (p[slug] && p[slug].attempts) || [];
  }

  function saveAttempt(slug, attempt) {
    const p = loadProgress();
    if (!p[slug]) p[slug] = { attempts: [] };
    p[slug].attempts.push(attempt);
    saveProgress(p);
  }

  function getInProgress() {
    return getInProgressMap();
  }

  function saveInProgress(state) {
    const map = getInProgressMap();
    if (state && state.slug) {
      map[state.slug] = state;
      saveInProgressMap(map);
    }
  }

  function clearInProgress(slug) {
    if (!slug) return;
    const map = getInProgressMap();
    if (map[slug]) {
      delete map[slug];
      saveInProgressMap(map);
    }
  }

  function getInProgressMap() {
    const p = loadProgress();
    const raw = p[IN_PROGRESS_KEY];
    if (!raw) return {};

    // Backward compatibility for older single-state storage shape.
    if (raw.slug) {
      return { [raw.slug]: raw };
    }

    if (typeof raw !== 'object' || Array.isArray(raw)) return {};
    return raw;
  }

  function saveInProgressMap(map) {
    const p = loadProgress();
    p[IN_PROGRESS_KEY] = map;
    saveProgress(p);
  }

  function getSavedDashboardTab() {
    const p = loadProgress();
    return p[DASHBOARD_TAB_KEY] || 'tests';
  }

  function saveDashboardTab(tabName) {
    const p = loadProgress();
    p[DASHBOARD_TAB_KEY] = tabName;
    saveProgress(p);
  }

  // ── State ────────────────────────────────────────────────
  let manifest = [];
  const FALLBACK_MANIFEST = [
    { name: 'Ethics and Professional Issues', slug: 'ethics-and-professional-issues', category: 'Category Tests', questionCount: 89, file: 'data/ethics-and-professional-issues.json', jsFile: 'data/ethics-and-professional-issues.js' },
    { name: 'Industrial / Organizational Psychology', slug: 'industrial-organizational-psychology', category: 'Category Tests', questionCount: 1, file: 'data/industrial-organizational-psychology.json', jsFile: 'data/industrial-organizational-psychology.js' },
    { name: 'Learning Theory', slug: 'learning-theory', category: 'Category Tests', questionCount: 91, file: 'data/learning-theory.json', jsFile: 'data/learning-theory.js' },
    { name: 'Lifespan Development', slug: 'lifespan-development', category: 'Category Tests', questionCount: 1, file: 'data/lifespan-development.json', jsFile: 'data/lifespan-development.js' },
    { name: 'Physiological Psychology / Psychopharmacology', slug: 'physiological-psychology-psychopharmacology', category: 'Category Tests', questionCount: 101, file: 'data/physiological-psychology-psychopharmacology.json', jsFile: 'data/physiological-psychology-psychopharmacology.js' },
    { name: 'Psychological Assessment', slug: 'psychological-assessment', category: 'Category Tests', questionCount: 74, file: 'data/psychological-assessment.json', jsFile: 'data/psychological-assessment.js' },
    { name: 'Social Psychology', slug: 'social-psychology', category: 'Category Tests', questionCount: 67, file: 'data/social-psychology.json', jsFile: 'data/social-psychology.js' },
    { name: 'Statistics and Research Design', slug: 'statistics-and-research-design', category: 'Category Tests', questionCount: 65, file: 'data/statistics-and-research-design.json', jsFile: 'data/statistics-and-research-design.js' },
    { name: 'Test Construction', slug: 'test-construction', category: 'Category Tests', questionCount: 67, file: 'data/test-construction.json', jsFile: 'data/test-construction.js' },
    { name: '2025 Academic Review Test 1', slug: '2025-academic-review-test-1', category: 'Full Tests', questionCount: 225, file: 'data/2025-academic-review-test-1.json', jsFile: 'data/2025-academic-review-test-1.js' },
    { name: '2025 Academic Review Test 2', slug: '2025-academic-review-test-2', category: 'Full Tests', questionCount: 225, file: 'data/2025-academic-review-test-2.json', jsFile: 'data/2025-academic-review-test-2.js' },
    { name: '2025 Academic Review Test 3', slug: '2025-academic-review-test-3', category: 'Full Tests', questionCount: 225, file: 'data/2025-academic-review-test-3.json', jsFile: 'data/2025-academic-review-test-3.js' },
    { name: '2025 Academic Review Test 4', slug: '2025-academic-review-test-4', category: 'Full Tests', questionCount: 225, file: 'data/2025-academic-review-test-4.json', jsFile: 'data/2025-academic-review-test-4.js' },
    { name: 'Assessment Exam - EPPP', slug: 'assessment-exam---eppp', category: 'Full Tests', questionCount: 225, file: 'data/assessment-exam---eppp.json', jsFile: 'data/assessment-exam---eppp.js' },
    { name: 'EPPP Exam Simulation - Test 1', slug: 'eppp-exam-simulation---test-1', category: 'Full Tests', questionCount: 224, file: 'data/eppp-exam-simulation---test-1.json', jsFile: 'data/eppp-exam-simulation---test-1.js' },
    { name: 'EPPP Exam Simulation - Test 2', slug: 'eppp-exam-simulation---test-2', category: 'Full Tests', questionCount: 225, file: 'data/eppp-exam-simulation---test-2.json', jsFile: 'data/eppp-exam-simulation---test-2.js' },
    { name: 'Practice Exam 6', slug: 'practice-exam-6', category: 'Full Tests', questionCount: 225, file: 'data/practice-exam-6.json', jsFile: 'data/practice-exam-6.js' },
    { name: 'Practice Exam 7', slug: 'practice-exam-7', category: 'Full Tests', questionCount: 225, file: 'data/practice-exam-7.json', jsFile: 'data/practice-exam-7.js' },
    { name: 'Practice Exam 8', slug: 'practice-exam-8', category: 'Full Tests', questionCount: 225, file: 'data/practice-exam-8.json', jsFile: 'data/practice-exam-8.js' },
    { name: 'Practice Test 2 AR all domains', slug: 'practice-test-2-ar-all-domains', category: 'Full Tests', questionCount: 224, file: 'data/practice-test-2-ar-all-domains.json', jsFile: 'data/practice-test-2-ar-all-domains.js' },
    { name: 'Practice Test AR 1 all domains', slug: 'practice-test-ar-1-all-domains', category: 'Full Tests', questionCount: 224, file: 'data/practice-test-ar-1-all-domains.json', jsFile: 'data/practice-test-ar-1-all-domains.js' }
  ];
  const IS_FILE_PROTOCOL = window.location.protocol === 'file:';
  const DASHBOARD_PAGE_SIZE = 24;
  const dashboardDiscoveryState = {
    query: '',
    sort: 'name-asc',
    visible: {
      category: DASHBOARD_PAGE_SIZE,
      full: DASHBOARD_PAGE_SIZE
    }
  };
  let testMetaBySlug = {};
  let currentTest = null;       // { name, slug, category, questionCount, questions }
  let currentIndex = 0;         // current question index
  let userAnswers = {};          // { qIndex: 'A'|'B'|... }
  let markedQuestions = {};      // { qIndex: true }
  let timerInterval = null;
  let timerSeconds = 0;
  let lastResults = null;        // stored after submit for review

  // ── DOM refs ─────────────────────────────────────────────
  const $ = (sel) => document.querySelector(sel);
  const $$ = (sel) => document.querySelectorAll(sel);

  const dashboardView = $('#dashboard-view');
  const testView = $('#test-view');
  const startScreen = $('#test-start-screen');
  const activeScreen = $('#test-active-screen');
  const resultsScreen = $('#test-results-screen');
  const reviewScreen = $('#test-review-screen');

  // ── Init ─────────────────────────────────────────────────
  async function init() {
    try {
      // Use inline manifest if available (file:// protocol), otherwise fetch
      if (window.EPPP_MANIFEST) {
        manifest = window.EPPP_MANIFEST;
      } else if (IS_FILE_PROTOCOL) {
        manifest = FALLBACK_MANIFEST;
      } else {
        var resp = await fetch('tests-manifest.json');
        manifest = await resp.json();
      }

      if (!Array.isArray(manifest) || manifest.length === 0) {
        manifest = FALLBACK_MANIFEST;
      }

      buildTestMetaIndex();

      renderDashboard();
      bindEvents();
      bindUnloadAutoSave();
    } catch (e) {
      console.error('Failed to initialize app:', e);
      var app = document.getElementById('app');
      if (app) {
        app.innerHTML = '<div style="max-width:600px;margin:4rem auto;padding:2rem;text-align:center;font-family:sans-serif;">' +
          '<h2 style="color:#dc3545;">Failed to load tests</h2>' +
          '<p style="margin:1rem 0;color:#666;">The app could not load test data. This can happen if:</p>' +
          '<ul style="text-align:left;margin:1rem auto;max-width:400px;color:#444;">' +
          '<li>JavaScript files were blocked by your browser or antivirus</li>' +
          '<li>Files were not fully extracted from the zip</li>' +
          '<li>The <code>data/</code> folder is missing</li>' +
          '</ul>' +
          '<p style="margin-top:1.5rem;color:#666;">Try using a local server instead:<br><code>python -m http.server 8080</code></p>' +
          '<p style="margin-top:0.75rem;color:#666;">On Windows, use <code>start.bat</code> from this folder.</p>' +
          '</div>';
      }
    }
  }

  function buildTestMetaIndex() {
    testMetaBySlug = {};
    manifest.forEach(item => {
      if (item && item.slug) {
        testMetaBySlug[item.slug] = item;
      }
    });
  }

  function getTestMeta(slug) {
    return testMetaBySlug[slug] || null;
  }

  // ── Dashboard ────────────────────────────────────────────
  function renderDashboard() {
    renderDashboardTests();

    const testsSearchInput = $('#tests-search-input');
    if (testsSearchInput && testsSearchInput.value !== dashboardDiscoveryState.query) {
      testsSearchInput.value = dashboardDiscoveryState.query;
    }
    const testsSortSelect = $('#tests-sort-select');
    if (testsSortSelect && testsSortSelect.value !== dashboardDiscoveryState.sort) {
      testsSortSelect.value = dashboardDiscoveryState.sort;
    }

    updateStats();
    renderHistory();
    renderResumeSection();
    updateDashboardTabBadges();
    setActiveDashboardTab(getSavedDashboardTab());
    showView('dashboard');
  }

  function renderDashboardTests() {
    const categoryGrid = $('#category-tests-grid');
    const fullGrid = $('#full-tests-grid');
    if (!categoryGrid || !fullGrid) return;

    const progress = loadProgress();
    const query = dashboardDiscoveryState.query.trim().toLowerCase();

    const enriched = manifest.map(testMeta => {
      const attempts = (progress[testMeta.slug] && progress[testMeta.slug].attempts) || [];
      const best = attempts.length ? Math.max(...attempts.map(a => a.pct || 0)) : null;
      return {
        ...testMeta,
        attemptsCount: attempts.length,
        bestScore: best,
        lastAttemptDate: attempts.length ? attempts[attempts.length - 1].date : ''
      };
    });

    const filtered = query
      ? enriched.filter(testMeta => {
        const haystack = `${testMeta.name} ${testMeta.slug} ${testMeta.category}`.toLowerCase();
        return haystack.includes(query);
      })
      : enriched;

    const sorted = [...filtered].sort(getDashboardSortComparator(dashboardDiscoveryState.sort));
    const categoryTests = sorted.filter(testMeta => testMeta.category === 'Category Tests');
    const fullTests = sorted.filter(testMeta => testMeta.category !== 'Category Tests');

    renderTestSection('category', categoryTests, categoryGrid);
    renderTestSection('full', fullTests, fullGrid);

    const summary = $('#tests-results-summary');
    if (summary) {
      summary.textContent = `${filtered.length} of ${manifest.length} tests`;
    }
  }

  function getDashboardSortComparator(sortMode) {
    switch (sortMode) {
      case 'name-desc':
        return (a, b) => b.name.localeCompare(a.name);
      case 'best-desc':
        return (a, b) => (b.bestScore ?? -1) - (a.bestScore ?? -1) || a.name.localeCompare(b.name);
      case 'attempts-desc':
        return (a, b) => b.attemptsCount - a.attemptsCount || a.name.localeCompare(b.name);
      case 'questions-desc':
        return (a, b) => (b.questionCount || 0) - (a.questionCount || 0) || a.name.localeCompare(b.name);
      case 'name-asc':
      default:
        return (a, b) => a.name.localeCompare(b.name);
    }
  }

  function renderTestSection(kind, items, gridElement) {
    const visibleLimit = dashboardDiscoveryState.visible[kind] || DASHBOARD_PAGE_SIZE;
    const shown = items.slice(0, visibleLimit);
    gridElement.innerHTML = '';

    const fragment = document.createDocumentFragment();

    shown.forEach(testMeta => {
      const card = document.createElement('div');
      card.className = 'test-card';
      card.dataset.slug = testMeta.slug;
      card.dataset.file = testMeta.file;

      const badge = testMeta.bestScore !== null
        ? `<span class="test-card-badge badge-best">${Math.round(testMeta.bestScore)}%</span>`
        : '';

      card.innerHTML = `
        ${badge}
        <div class="test-card-name">${esc(testMeta.name)}</div>
        <div class="test-card-meta">
          <span>${testMeta.questionCount} questions</span>
          <span>${testMeta.attemptsCount} attempt${testMeta.attemptsCount !== 1 ? 's' : ''}</span>
        </div>
      `;
      fragment.appendChild(card);
    });

    if (!shown.length) {
      const empty = document.createElement('div');
      empty.className = 'tests-empty';
      empty.textContent = 'No tests match this filter.';
      fragment.appendChild(empty);
    }
    gridElement.appendChild(fragment);

    const countEl = kind === 'category' ? $('#category-tests-visible') : $('#full-tests-visible');
    if (countEl) {
      countEl.textContent = `${Math.min(visibleLimit, items.length)} / ${items.length} shown`;
    }

    const btn = kind === 'category' ? $('#btn-load-more-category') : $('#btn-load-more-full');
    if (btn) {
      const hasMore = items.length > visibleLimit;
      btn.style.display = hasMore ? '' : 'none';
      btn.disabled = !hasMore;
    }
  }

  function renderResumeSection() {
    const section = $('#resume-section');
    const list = $('#resume-list');
    if (!section || !list) return;

    const map = getInProgressMap();
    const states = Object.values(map).filter(s => s && s.slug);
    if (!states.length) {
      section.style.display = 'none';
      return;
    }

    states.sort((a, b) => new Date(b.savedAt || 0) - new Date(a.savedAt || 0));
    list.innerHTML = '';

    states.forEach(state => {
      const total = typeof state.total === 'number' ? state.total : 0;
      const answered = state.answers ? Object.keys(state.answers).length : 0;
      const qLabel = total > 0 ? `${state.currentIndex + 1}/${total}` : `${state.currentIndex + 1}`;

      const card = document.createElement('div');
      card.className = 'resume-card';
      card.innerHTML = `
        <h2>${esc(state.name || state.slug)}</h2>
        <p>Question ${qLabel} · ${answered} answered · ${formatTime(state.timerSeconds || 0)}</p>
        <div class="resume-actions">
          <button class="btn btn-primary btn-resume-test" data-slug="${esc(state.slug)}">Resume Test</button>
          <button class="btn btn-secondary btn-discard-resume" data-slug="${esc(state.slug)}">Discard Progress</button>
        </div>
      `;
      list.appendChild(card);
    });

    section.style.display = '';
  }

  function updateDashboardTabBadges() {
    const resumeCount = Object.values(getInProgressMap()).filter(s => s && s.slug).length;
    const resumeBadge = $('#tab-badge-resume');
    if (resumeBadge) {
      resumeBadge.textContent = String(resumeCount);
      resumeBadge.style.display = resumeCount > 0 ? '' : 'none';
    }

    const progress = loadProgress();
    let historyCount = 0;
    for (const slug in progress) {
      if (slug === IN_PROGRESS_KEY || slug === DASHBOARD_TAB_KEY) continue;
      const attempts = progress[slug] && progress[slug].attempts;
      if (Array.isArray(attempts)) historyCount += attempts.length;
    }
    const historyBadge = $('#tab-badge-history');
    if (historyBadge) {
      historyBadge.textContent = String(historyCount);
      historyBadge.style.display = historyCount > 0 ? '' : 'none';
    }
  }

  function setActiveDashboardTab(tabName) {
    const safeTab = ['tests', 'resume', 'history', 'stats'].includes(tabName) ? tabName : 'tests';

    $$('.dashboard-tab').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.tab === safeTab);
    });

    ['tests', 'resume', 'history', 'stats'].forEach(name => {
      const panel = document.getElementById(`dashboard-panel-${name}`);
      if (panel) panel.classList.toggle('active', name === safeTab);
    });

    saveDashboardTab(safeTab);
  }

  function updateStats() {
    const progress = loadProgress();
    let totalAttempts = 0;
    let totalQuestions = 0;
    let totalCorrect = 0;
    let totalSeconds = 0;
    const scores = [];
    const attempts = [];
    const byCategory = {};

    for (const slug in progress) {
      if (slug === IN_PROGRESS_KEY || slug === DASHBOARD_TAB_KEY) continue;
      const att = progress[slug].attempts || [];
      const meta = getTestMeta(slug);
      const category = (meta && meta.category) ? meta.category : 'Other';
      totalAttempts += att.length;
      att.forEach(a => {
        const total = typeof a.total === 'number' ? a.total : 0;
        const correct = typeof a.correct === 'number' ? a.correct : 0;
        const pct = typeof a.pct === 'number' ? a.pct : 0;
        const seconds = typeof a.seconds === 'number' ? a.seconds : 0;

        totalQuestions += total;
        totalCorrect += correct;
        totalSeconds += seconds;
        scores.push(pct);
        attempts.push({
          slug,
          testName: (meta && meta.name) ? meta.name : slug,
          category,
          pct,
          correct,
          total,
          seconds,
          date: a.date || ''
        });

        if (!byCategory[category]) {
          byCategory[category] = { attempts: 0, scoreSum: 0, correct: 0, total: 0 };
        }
        byCategory[category].attempts += 1;
        byCategory[category].scoreSum += pct;
        byCategory[category].correct += correct;
        byCategory[category].total += total;
      });
    }

    $('#stat-tests-taken').textContent = totalAttempts;
    $('#stat-questions-answered').textContent = totalQuestions;
    $('#stat-avg-score').textContent = scores.length ? Math.round(scores.reduce((a, b) => a + b, 0) / scores.length) + '%' : '—';
    $('#stat-best-score').textContent = scores.length ? Math.round(Math.max(...scores)) + '%' : '—';

    const weightedAccuracy = totalQuestions > 0 ? (totalCorrect / totalQuestions) * 100 : null;
    const avgTimePerQuestion = totalQuestions > 0 && totalSeconds > 0 ? totalSeconds / totalQuestions : null;
    const recent = [...attempts]
      .filter(a => a.date)
      .sort((a, b) => new Date(b.date) - new Date(a.date))
      .slice(0, 7);
    const recentAvg = recent.length ? recent.reduce((sum, a) => sum + a.pct, 0) / recent.length : null;

    $('#stat-total-correct').textContent = String(totalCorrect);
    $('#stat-weighted-accuracy').textContent = weightedAccuracy !== null ? `${Math.round(weightedAccuracy)}%` : '—';
    $('#stat-avg-time-question').textContent = avgTimePerQuestion !== null ? `${avgTimePerQuestion.toFixed(1)}s` : '—';
    $('#stat-last7-avg').textContent = recentAvg !== null ? `${Math.round(recentAvg)}%` : '—';

    renderScoreDistribution(attempts);
    renderCategoryPerformance(byCategory);
    renderTopicPerformance(attempts);
    renderRecentTrend(attempts);
  }

  function renderScoreDistribution(attempts) {
    const container = $('#stats-score-distribution');
    if (!container) return;
    if (!attempts.length) {
      container.innerHTML = '<div class="stats-empty">No attempts yet</div>';
      return;
    }

    const buckets = [
      { label: '0-49%', min: 0, max: 49, count: 0 },
      { label: '50-69%', min: 50, max: 69, count: 0 },
      { label: '70-84%', min: 70, max: 84, count: 0 },
      { label: '85-100%', min: 85, max: 100, count: 0 }
    ];

    attempts.forEach(a => {
      const score = Math.round(a.pct);
      const bucket = buckets.find(b => score >= b.min && score <= b.max);
      if (bucket) bucket.count += 1;
    });

    const colors = ['#ff7f7f', '#ffd166', '#5bc9be', '#5b97dd'];
    const segments = buckets.map((b, i) => ({
      label: b.label,
      value: b.count,
      color: colors[i],
      meta: `${b.count} attempt${b.count !== 1 ? 's' : ''}`
    }));

    container.innerHTML = renderDonutChart(segments, `${attempts.length}`, 'Attempts');
    wireDonutInteractivity(container);
  }

  function renderCategoryPerformance(byCategory) {
    const container = $('#stats-category-performance');
    if (!container) return;

    const entries = Object.entries(byCategory)
      .map(([name, data]) => ({
        name,
        attempts: data.attempts,
        avg: data.attempts ? data.scoreSum / data.attempts : 0
      }))
      .sort((a, b) => b.avg - a.avg);

    if (!entries.length) {
      container.innerHTML = '<div class="stats-empty">No category stats yet</div>';
      return;
    }

    const palette = ['#5b97dd', '#5bc9be', '#7f8aec', '#ffd166', '#f89ac1', '#a4b6cc'];
    const topEntries = entries.slice(0, 6);
    const segments = topEntries.map((entry, index) => ({
      label: esc(entry.name),
      value: entry.attempts,
      color: palette[index % palette.length],
      meta: `${Math.round(entry.avg)}% avg`
    }));

    container.innerHTML = renderDonutChart(segments, `${entries.length}`, 'Categories');
    wireDonutInteractivity(container);
  }

  function renderDonutChart(segments, centerText, centerLabel) {
    const visibleSegments = segments.filter(s => s.value > 0);
    if (!visibleSegments.length) {
      return '<div class="stats-empty">Not enough data</div>';
    }

    const total = visibleSegments.reduce((sum, s) => sum + s.value, 0);
    const radius = 44;
    const circumference = 2 * Math.PI * radius;
    let offset = 0;

    const arcs = visibleSegments.map((segment, index) => {
      const segLen = (segment.value / total) * circumference;
      const arc = `
        <circle
          class="stats-donut-segment${index === 0 ? ' active' : ''}"
          cx="60"
          cy="60"
          r="${radius}"
          fill="none"
          stroke="${segment.color}"
          stroke-width="14"
          stroke-dasharray="${segLen} ${circumference - segLen}"
          stroke-dashoffset="${-offset}"
          stroke-linecap="butt"
          data-label="${esc(segment.label)}"
          data-value="${segment.value}"
          data-meta="${esc(segment.meta)}"
          data-share="${Math.round((segment.value / total) * 100)}"
          tabindex="0"
        >
          <title>${segment.label}: ${segment.value} (${Math.round((segment.value / total) * 100)}%)</title>
        </circle>
      `;
      offset += segLen;
      return arc;
    }).join('');

    const legend = visibleSegments.map(segment => `
      <div class="stats-donut-legend-item">
        <span class="stats-donut-dot" style="background:${segment.color}"></span>
        <span class="stats-donut-label">${segment.label}</span>
        <span class="stats-donut-meta">${segment.meta}</span>
      </div>
    `).join('');

    const first = visibleSegments[0];
    return `
      <div class="stats-donut-layout">
        <div class="stats-donut-chart">
          <svg class="stats-donut-svg" viewBox="0 0 120 120" role="img" aria-label="Interactive donut chart">
            <circle class="stats-donut-track" cx="60" cy="60" r="${radius}" fill="none" stroke="#e2ebf5" stroke-width="14"></circle>
            <g transform="rotate(-90 60 60)">
              ${arcs}
            </g>
          </svg>
          <div class="stats-donut-center">
            <span class="stats-donut-center-main">${centerText}</span>
            <span class="stats-donut-center-sub">${centerLabel}</span>
          </div>
        </div>
        <div class="stats-donut-side">
          <div class="stats-donut-detail">
            <span class="stats-donut-detail-title">${first.label}</span>
            <span class="stats-donut-detail-meta">${first.meta} · ${Math.round((first.value / total) * 100)}%</span>
          </div>
          <div class="stats-donut-legend">${legend}</div>
        </div>
      </div>
    `;
  }

  function wireDonutInteractivity(container) {
    const segments = container.querySelectorAll('.stats-donut-segment');
    if (!segments.length) return;

    const detailTitle = container.querySelector('.stats-donut-detail-title');
    const detailMeta = container.querySelector('.stats-donut-detail-meta');

    function setActive(segment) {
      segments.forEach(s => s.classList.remove('active'));
      segment.classList.add('active');
      if (detailTitle) detailTitle.textContent = segment.dataset.label || '';
      if (detailMeta) {
        const meta = segment.dataset.meta || '';
        const share = segment.dataset.share || '0';
        detailMeta.textContent = `${meta} · ${share}%`;
      }
    }

    segments.forEach(segment => {
      segment.addEventListener('mouseenter', () => setActive(segment));
      segment.addEventListener('focus', () => setActive(segment));
    });
  }

  function renderTopicPerformance(attempts) {
    const container = $('#stats-topic-performance');
    if (!container) return;
    if (!attempts.length) {
      container.innerHTML = '<div class="stats-empty">No test-level stats yet</div>';
      return;
    }

    const byTest = {};
    attempts.forEach(a => {
      if (!byTest[a.slug]) {
        byTest[a.slug] = { name: a.testName, attempts: 0, scoreSum: 0 };
      }
      byTest[a.slug].attempts += 1;
      byTest[a.slug].scoreSum += a.pct;
    });

    const entries = Object.values(byTest)
      .map(t => ({
        name: t.name,
        attempts: t.attempts,
        avg: t.attempts ? t.scoreSum / t.attempts : 0
      }))
      .sort((a, b) => b.avg - a.avg);

    const strongest = entries.slice(0, 3);
    const weakest = [...entries].reverse().slice(0, 3);

    const renderList = (list) => list.length
      ? list.map(item => `
        <div class="stats-topic-item">
          <div class="stats-topic-row">
            <span class="stats-topic-name">${esc(item.name)}</span>
            <span class="stats-topic-score">${Math.round(item.avg)}%</span>
          </div>
          <div class="stats-topic-track"><div class="stats-topic-fill" style="width:${Math.max(4, item.avg)}%"></div></div>
          <div class="stats-topic-meta">${item.attempts} attempt${item.attempts !== 1 ? 's' : ''}</div>
        </div>
      `).join('')
      : '<div class="stats-empty">Not enough data</div>';

    container.innerHTML = `
      <div class="stats-topic-col">
        <h4>Strongest</h4>
        ${renderList(strongest)}
      </div>
      <div class="stats-topic-col">
        <h4>Needs Work</h4>
        ${renderList(weakest)}
      </div>
    `;
  }

  function renderRecentTrend(attempts) {
    const container = $('#stats-recent-trend');
    if (!container) return;

    const recent = [...attempts]
      .filter(a => a.date)
      .sort((a, b) => new Date(a.date) - new Date(b.date))
      .slice(-10);

    if (!recent.length) {
      container.innerHTML = '<div class="stats-empty">No trend data yet</div>';
      return;
    }

    const width = 340;
    const height = 150;
    const padX = 18;
    const padTop = 12;
    const padBottom = 26;
    const chartH = height - padTop - padBottom;
    const spanX = width - (padX * 2);
    const stepX = recent.length === 1 ? 0 : spanX / (recent.length - 1);

    const points = recent.map((entry, index) => {
      const score = Math.max(0, Math.min(100, entry.pct));
      const x = padX + (index * stepX);
      const y = padTop + ((100 - score) / 100) * chartH;
      return { x, y, score, date: entry.date };
    });

    const polylinePoints = points.map(p => `${p.x},${p.y}`).join(' ');
    const guideLines = [25, 50, 75].map(mark => {
      const y = padTop + ((100 - mark) / 100) * chartH;
      return `<line x1="${padX}" y1="${y}" x2="${width - padX}" y2="${y}" class="stats-line-grid"/>`;
    }).join('');

    const circles = points.map((p, i) => `
      <circle cx="${p.x}" cy="${p.y}" r="3.2" class="stats-line-point" title="Attempt ${i + 1}: ${Math.round(p.score)}%" />
    `).join('');

    const labels = points.map((p, i) => {
      let dateLabel = '—';
      if (p.date) {
        try {
          dateLabel = new Date(p.date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
        } catch (e) {}
      }
      return `
        <div class="stats-line-label">
          <span class="stats-line-label-date">${dateLabel}</span>
          <span class="stats-line-label-score">${Math.round(p.score)}%</span>
        </div>
      `;
    }).join('');

    container.innerHTML = `
      <div class="stats-line-wrap">
        <svg class="stats-line-chart" viewBox="0 0 ${width} ${height}" preserveAspectRatio="none" role="img" aria-label="Score trend chart">
          ${guideLines}
          <polyline points="${polylinePoints}" class="stats-line-path" />
          ${circles}
        </svg>
      </div>
      <div class="stats-line-labels">${labels}</div>
    `;
  }

  function renderHistory() {
    const progress = loadProgress();
    const allAttempts = [];

    for (const slug in progress) {
      const meta = getTestMeta(slug);
      (progress[slug].attempts || []).forEach((a, idx) => {
        allAttempts.push({ ...a, slug, name: meta ? meta.name : slug, attemptNum: idx + 1 });
      });
    }

    // Sort by date descending
    allAttempts.sort((a, b) => new Date(b.date) - new Date(a.date));

    const section = $('#history-section');
    const list = $('#history-list');

    if (allAttempts.length === 0) {
      section.style.display = 'none';
      return;
    }

    section.style.display = '';
    list.innerHTML = '';

    allAttempts.slice(0, 20).forEach(a => {
      const item = document.createElement('div');
      item.className = 'history-item';
      item.dataset.slug = a.slug;
      item.dataset.attemptIndex = a.attemptNum - 1;
      item.innerHTML = `
        <div>
          <div class="history-item-name">${esc(a.name)} <span style="color:#999;font-size:0.8rem">#${a.attemptNum}</span></div>
          <div class="history-item-detail">${formatDate(a.date)} · ${a.time} · ${a.correct}/${a.total}</div>
        </div>
        <div class="history-item-score">${Math.round(a.pct)}%</div>
      `;
      list.appendChild(item);
    });
  }

  // ── Events ───────────────────────────────────────────────
  function bindEvents() {
    // Test card click
    document.addEventListener('click', async (e) => {
      const card = e.target.closest('.test-card');
      if (card) {
        const slug = card.dataset.slug;
        const file = card.dataset.file;
        await loadTest(slug, file);
        return;
      }

      const histItem = e.target.closest('.history-item');
      if (histItem) {
        const slug = histItem.dataset.slug;
        const attemptIdx = parseInt(histItem.dataset.attemptIndex, 10);
        const meta = getTestMeta(slug);
        if (meta) {
          await loadTestForReview(meta, attemptIdx);
        }
        return;
      }

      const resumeBtn = e.target.closest('.btn-resume-test');
      if (resumeBtn) {
        await resumeSavedTest(resumeBtn.dataset.slug);
        return;
      }

      const discardBtn = e.target.closest('.btn-discard-resume');
      if (discardBtn) {
        clearInProgress(discardBtn.dataset.slug);
        renderDashboard();
        return;
      }

      const tabBtn = e.target.closest('.dashboard-tab');
      if (tabBtn && tabBtn.dataset.tab) {
        setActiveDashboardTab(tabBtn.dataset.tab);
        return;
      }

      const loadMoreBtn = e.target.closest('.btn-load-more-tests');
      if (loadMoreBtn && loadMoreBtn.dataset.kind) {
        const kind = loadMoreBtn.dataset.kind;
        if (dashboardDiscoveryState.visible[kind] !== undefined) {
          dashboardDiscoveryState.visible[kind] += DASHBOARD_PAGE_SIZE;
          renderDashboardTests();
        }
        return;
      }
    });

    const testsSearchInput = $('#tests-search-input');
    if (testsSearchInput) {
      testsSearchInput.addEventListener('input', () => {
        dashboardDiscoveryState.query = testsSearchInput.value || '';
        dashboardDiscoveryState.visible.category = DASHBOARD_PAGE_SIZE;
        dashboardDiscoveryState.visible.full = DASHBOARD_PAGE_SIZE;
        renderDashboardTests();
      });
    }

    const testsSortSelect = $('#tests-sort-select');
    if (testsSortSelect) {
      testsSortSelect.addEventListener('change', () => {
        dashboardDiscoveryState.sort = testsSortSelect.value || 'name-asc';
        dashboardDiscoveryState.visible.category = DASHBOARD_PAGE_SIZE;
        dashboardDiscoveryState.visible.full = DASHBOARD_PAGE_SIZE;
        renderDashboardTests();
      });
    }

    $('#btn-start-test').addEventListener('click', startTest);
    $('#btn-back-dashboard').addEventListener('click', () => renderDashboard());
    $('#btn-exit-test').addEventListener('click', () => confirmAction('Exit this test? Your progress will be lost.', () => {
      stopTimer();
      clearInProgress(currentTest && currentTest.slug);
      renderDashboard();
    }));
    $('#btn-pause-test').addEventListener('click', pauseCurrentTest);
    $('#btn-prev').addEventListener('click', () => navigateQuestion(-1));
    $('#btn-next').addEventListener('click', () => navigateQuestion(1));
    $('#btn-mark-review').addEventListener('click', toggleMarkReview);
    $('#btn-prev-bottom').addEventListener('click', () => navigateQuestion(-1));
    $('#btn-next-bottom').addEventListener('click', () => navigateQuestion(1));
    $('#btn-submit-test').addEventListener('click', () => {
      const answered = Object.keys(userAnswers).length;
      const total = currentTest.questions.length;
      const unanswered = total - answered;
      const msg = unanswered > 0
        ? `You have ${unanswered} unanswered question${unanswered > 1 ? 's' : ''}. Submit anyway?`
        : 'Submit your test?';
      confirmAction(msg, submitTest);
    });
    $('#btn-review').addEventListener('click', showReview);
    $('#btn-retake').addEventListener('click', retakeTest);
    $('#btn-results-dashboard').addEventListener('click', () => renderDashboard());
    $('#btn-review-back').addEventListener('click', () => showScreen('results'));
    $('#btn-review-top').addEventListener('click', scrollReviewToTop);
    const reviewTopFab = $('#btn-review-top-fab');
    if (reviewTopFab) {
      reviewTopFab.addEventListener('click', scrollReviewToTop);
    }
    $('#btn-review-dashboard').addEventListener('click', () => renderDashboard());
    $('#btn-review-retake').addEventListener('click', retakeTest);
    $('#btn-review-jump').addEventListener('click', jumpToReviewQuestion);
    $('#review-jump-select').addEventListener('change', jumpToReviewQuestion);
  }

  // ── Load Test ────────────────────────────────────────────
  async function loadTest(slug, file) {
    // Check if already loaded inline
    if (window.EPPP_TESTS && window.EPPP_TESTS[slug]) {
      currentTest = window.EPPP_TESTS[slug];
      showTestStartScreen();
      return;
    }

    // On file:// (common on Windows), fetch to local files may be blocked in Chrome.
    if (IS_FILE_PROTOCOL) {
      const meta = getTestMeta(slug);
      if (meta && meta.jsFile) {
        try {
          await loadScript(meta.jsFile);
          if (window.EPPP_TESTS && window.EPPP_TESTS[slug]) {
            currentTest = window.EPPP_TESTS[slug];
            showTestStartScreen();
            return;
          }
        } catch (e) {
          console.error('Failed to load local test script:', slug, e);
        }
      }
    }

    // Try fetch (works on http server)
    try {
      const resp = await fetch(file);
      currentTest = await resp.json();
      showTestStartScreen();
      return;
    } catch (e) {
      // Fallback: dynamic script loading for file:// protocol
      const meta = getTestMeta(slug);
      if (meta && meta.jsFile) {
        await loadScript(meta.jsFile);
        if (window.EPPP_TESTS && window.EPPP_TESTS[slug]) {
          currentTest = window.EPPP_TESTS[slug];
          showTestStartScreen();
          return;
        }
      }
      console.error('Failed to load test:', slug, e);
      confirmAction('Could not load this test file. On Windows, try running start.bat and opening http://localhost:8080.', function () {});
    }
  }

  function loadScript(src) {
    return new Promise((resolve, reject) => {
      const s = document.createElement('script');
      s.src = src;
      s.onload = resolve;
      s.onerror = reject;
      document.head.appendChild(s);
    });
  }

  async function loadTestForReview(meta, attemptIdx) {
    // Load test data
    if (window.EPPP_TESTS && window.EPPP_TESTS[meta.slug]) {
      currentTest = window.EPPP_TESTS[meta.slug];
    } else {
      if (IS_FILE_PROTOCOL && meta.jsFile) {
        try {
          await loadScript(meta.jsFile);
          currentTest = window.EPPP_TESTS && window.EPPP_TESTS[meta.slug];
        } catch (e) {
          console.error('Failed to load local review test script:', meta.slug, e);
        }
      }

      try {
        if (!currentTest) {
          const resp = await fetch(meta.file);
          currentTest = await resp.json();
        }
      } catch (e) {
        if (meta.jsFile) {
          await loadScript(meta.jsFile);
          currentTest = window.EPPP_TESTS && window.EPPP_TESTS[meta.slug];
        }
        if (!currentTest) return;
      }
    }
    const attempts = getTestAttempts(currentTest.slug);
    if (!attempts[attemptIdx]) return;
    lastResults = attempts[attemptIdx];
    userAnswers = lastResults.answers || {};
    markedQuestions = lastResults.markedQuestions || {};
    showView('test');
    showScreen('results');
    renderResults();
  }

  function showTestStartScreen() {
    showView('test');
    showScreen('start');

    $('#start-test-name').textContent = currentTest.name;
    $('#start-question-count').textContent = `${currentTest.questionCount} questions`;

    const attempts = getTestAttempts(currentTest.slug);
    if (attempts.length) {
      const best = Math.max(...attempts.map(a => a.pct));
      $('#start-past-attempts').textContent = `${attempts.length} previous attempt${attempts.length > 1 ? 's' : ''} · Best: ${Math.round(best)}%`;
    } else {
      $('#start-past-attempts').textContent = 'No previous attempts';
    }
  }

  // ── Start Test ───────────────────────────────────────────
  function startTest() {
    clearInProgress(currentTest && currentTest.slug);
    userAnswers = {};
    markedQuestions = {};
    currentIndex = 0;
    timerSeconds = 0;
    lastResults = null;

    showScreen('active');
    $('#test-title-bar').textContent = currentTest.name;

    buildQuestionNav();
    renderQuestion();
    updateAnsweredCount();
    startTimer();
    persistInProgressState(false);
  }

  function retakeTest() {
    showScreen('start');
    showTestStartScreen();
  }

  // ── Timer ────────────────────────────────────────────────
  function startTimer(resetSeconds) {
    stopTimer();
    if (resetSeconds !== false) timerSeconds = 0;
    updateTimerDisplay();
    timerInterval = setInterval(() => {
      timerSeconds++;
      updateTimerDisplay();
      // Periodic save keeps progress recoverable even if browser/app closes unexpectedly.
      persistInProgressState(false);
    }, 1000);
  }

  function stopTimer() {
    if (timerInterval) { clearInterval(timerInterval); timerInterval = null; }
  }

  function updateTimerDisplay() {
    const h = String(Math.floor(timerSeconds / 3600)).padStart(2, '0');
    const m = String(Math.floor((timerSeconds % 3600) / 60)).padStart(2, '0');
    const s = String(timerSeconds % 60).padStart(2, '0');
    $('#timer').textContent = `${h}:${m}:${s}`;
  }

  function formatTime(seconds) {
    const h = Math.floor(seconds / 3600);
    const m = Math.floor((seconds % 3600) / 60);
    const s = seconds % 60;
    if (h > 0) return `${h}h ${m}m ${s}s`;
    if (m > 0) return `${m}m ${s}s`;
    return `${s}s`;
  }

  // ── Question Nav ─────────────────────────────────────────
  function buildQuestionNav() {
    const strip = $('#question-nav-strip');
    strip.innerHTML = '';
    strip.classList.remove('expanded');
    currentTest.questions.forEach((_, i) => {
      const btn = document.createElement('button');
      btn.className = 'q-nav-btn';
      btn.textContent = i + 1;
      btn.addEventListener('click', () => { currentIndex = i; renderQuestion(); });
      strip.appendChild(btn);
    });

    // Toggle expand/collapse
    const summary = $('#question-nav-summary');
    summary.onclick = function () {
      const isExpanded = strip.classList.toggle('expanded');
      $('#nav-toggle-icon').classList.toggle('expanded', isExpanded);
    };
  }

  function updateNavStrip() {
    const btns = $$('.q-nav-btn');
    btns.forEach((btn, i) => {
      btn.classList.toggle('answered', userAnswers[i] !== undefined);
      btn.classList.toggle('marked', !!markedQuestions[i]);
      btn.classList.toggle('current', i === currentIndex);
    });

    // Update summary bar
    const total = currentTest.questions.length;
    const answered = Object.keys(userAnswers).length;
    var summaryText = $('#nav-summary-text');
    if (summaryText) summaryText.textContent = 'Q ' + (currentIndex + 1) + ' / ' + total;
    var answeredSummary = $('#nav-answered-summary');
    if (answeredSummary) answeredSummary.textContent = answered + ' answered';
    var progressFill = $('#nav-progress-fill');
    if (progressFill) progressFill.style.width = (answered / total * 100) + '%';
  }

  // ── Render Question ──────────────────────────────────────
  function renderQuestion() {
    const q = currentTest.questions[currentIndex];
    const total = currentTest.questions.length;

    $('#question-number').textContent = `Question ${currentIndex + 1} of ${total}`;
    $('#question-text').textContent = q.question;

    const optionsList = $('#options-list');
    optionsList.innerHTML = '';

    const letters = Object.keys(q.options).sort();
    letters.forEach(letter => {
      const btn = document.createElement('button');
      btn.className = 'option-btn' + (userAnswers[currentIndex] === letter ? ' selected' : '');
      btn.innerHTML = `
        <span class="option-letter">${letter}</span>
        <span class="option-text">${esc(q.options[letter])}</span>
      `;
      btn.addEventListener('click', () => selectOption(letter));
      optionsList.appendChild(btn);
    });

    const isFirst = currentIndex === 0;
    const isLast = currentIndex === total - 1;
    $('#btn-prev').disabled = isFirst;
    $('#btn-next').disabled = isLast;
    $('#btn-prev-bottom').disabled = isFirst;
    $('#btn-next-bottom').disabled = isLast;

    const markBtn = $('#btn-mark-review');
    const isMarked = !!markedQuestions[currentIndex];
    markBtn.textContent = isMarked ? '★ Marked for Review' : '☆ Mark for Review';
    markBtn.classList.toggle('active-mark', isMarked);
    markBtn.setAttribute('aria-pressed', isMarked ? 'true' : 'false');

    updateNavStrip();
    persistInProgressState(false);
  }

  function toggleMarkReview() {
    if (markedQuestions[currentIndex]) {
      delete markedQuestions[currentIndex];
    } else {
      markedQuestions[currentIndex] = true;
    }
    renderQuestion();
    persistInProgressState(false);
  }

  function selectOption(letter) {
    userAnswers[currentIndex] = letter;
    renderQuestion();
    updateAnsweredCount();
    persistInProgressState(false);
  }

  function navigateQuestion(dir) {
    const newIdx = currentIndex + dir;
    if (newIdx >= 0 && newIdx < currentTest.questions.length) {
      currentIndex = newIdx;
      renderQuestion();
      persistInProgressState(false);
    }
  }

  function updateAnsweredCount() {
    const answered = Object.keys(userAnswers).length;
    const total = currentTest.questions.length;
    $('#answered-count').textContent = `${answered} of ${total} answered`;
  }

  // ── Submit ───────────────────────────────────────────────
  function submitTest() {
    stopTimer();
    clearInProgress(currentTest && currentTest.slug);

    let correct = 0;
    const total = currentTest.questions.length;

    currentTest.questions.forEach((q, i) => {
      if (userAnswers[i] === q.correct) correct++;
    });

    const pct = (correct / total) * 100;
    const timeStr = formatTime(timerSeconds);

    lastResults = {
      date: new Date().toISOString(),
      correct,
      total,
      pct,
      time: timeStr,
      seconds: timerSeconds,
      answers: { ...userAnswers },
      markedQuestions: { ...markedQuestions }
    };

    saveAttempt(currentTest.slug, lastResults);
    showScreen('results');
    renderResults();
  }

  function renderResults() {
    const { correct, total, pct, time } = lastResults;

    $('#results-test-name').textContent = currentTest.name;
    $('#score-pct').textContent = `${Math.round(pct)}%`;
    $('#score-correct').textContent = correct;
    $('#score-total').textContent = total;
    $('#score-time').textContent = time;

    const circle = $('#score-circle');
    circle.classList.remove('score-high', 'score-mid', 'score-low');
    if (pct >= 70) circle.classList.add('score-high');
    else if (pct >= 50) circle.classList.add('score-mid');
    else circle.classList.add('score-low');
  }

  // ── Review ───────────────────────────────────────────────
  function showReview() {
    showScreen('review');

    $('#review-title').textContent = currentTest.name;
    $('#review-score-badge').textContent = `${lastResults.correct}/${lastResults.total} (${Math.round(lastResults.pct)}%)`;

    const list = $('#review-list');
    const jumpSelect = $('#review-jump-select');
    const questionMap = $('#review-question-map');
    list.innerHTML = '';
    jumpSelect.innerHTML = '';
    questionMap.innerHTML = '';

    currentTest.questions.forEach((q, i) => {
      const selected = lastResults.answers[i];
      const isMarked = !!(lastResults.markedQuestions && lastResults.markedQuestions[i]);
      const status = getReviewStatus(i, q.correct);

      const option = document.createElement('option');
      option.value = String(i);
      option.textContent = `Q${i + 1} - ${statusLabel(status)}${isMarked ? ' • Marked' : ''}`;
      jumpSelect.appendChild(option);

      const mapBtn = document.createElement('button');
      mapBtn.className = `review-map-btn ${status}${isMarked ? ' marked' : ''}`;
      mapBtn.textContent = i + 1;
      mapBtn.title = `Question ${i + 1}: ${statusLabel(status)}${isMarked ? ' (Marked for review)' : ''}`;
      mapBtn.addEventListener('click', () => scrollToReviewQuestion(i));
      questionMap.appendChild(mapBtn);

      const item = document.createElement('div');
      item.className = 'review-item ' + (status === 'correct' ? 'correct' : status === 'incorrect' ? 'incorrect' : 'unattempted');
      item.id = `review-q-${i}`;

      let optionsHtml = '';
      const letters = Object.keys(q.options).sort();
      letters.forEach(letter => {
        let cls = 'review-option';
        let tag = '';
        if (letter === q.correct && letter === selected) {
          cls += ' is-selected-correct';
          tag = '<span class="review-tag">✓ Your answer (Correct)</span>';
        } else if (letter === q.correct) {
          cls += ' is-correct';
          tag = '<span class="review-tag">✓ Correct answer</span>';
        } else if (letter === selected) {
          cls += ' is-selected-wrong';
          tag = '<span class="review-tag">✗ Your answer</span>';
        }
        optionsHtml += `<div class="${cls}"><span class="opt-letter">${letter}.</span> <span>${esc(q.options[letter])}</span>${tag}</div>`;
      });

      const selectedText = selected ? selected : 'Not attempted';
      const resultText = status === 'correct' ? 'Correct' : status === 'incorrect' ? 'Incorrect' : 'Unattempted';

      item.innerHTML = `
        <div class="review-q-num">Question ${i + 1} — ${status === 'correct' ? '✓ Correct' : status === 'incorrect' ? '✗ Incorrect' : '• Unattempted'}</div>
        <div class="review-q-text">${esc(q.question)}</div>
        <div class="review-answer-summary">
          <span><strong>Your answer:</strong> ${selectedText}</span>
          <span><strong>Result:</strong> ${resultText}</span>
          <span><strong>Correct answer:</strong> ${q.correct}</span>
        </div>
        ${optionsHtml}
        <div class="review-explanation"><strong>Explanation</strong>${esc(q.explanation)}</div>
      `;

      list.appendChild(item);
    });

    jumpSelect.value = '0';
  }

  function getReviewStatus(index, correctLetter) {
    const selected = lastResults.answers[index];
    if (selected === undefined || selected === null || selected === '') return 'unattempted';
    return selected === correctLetter ? 'correct' : 'incorrect';
  }

  function statusLabel(status) {
    if (status === 'correct') return 'Correct';
    if (status === 'incorrect') return 'Incorrect';
    return 'Unattempted';
  }

  function jumpToReviewQuestion() {
    const select = $('#review-jump-select');
    const idx = parseInt(select.value, 10);
    if (!Number.isNaN(idx)) {
      scrollToReviewQuestion(idx);
    }
  }

  function scrollToReviewQuestion(index) {
    const target = document.getElementById(`review-q-${index}`);
    if (!target) return;

    $$('.review-item.focused').forEach(node => node.classList.remove('focused'));
    target.classList.add('focused');
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });

    const select = $('#review-jump-select');
    if (select && select.value !== String(index)) {
      select.value = String(index);
    }
  }

  function scrollReviewToTop() {
    const topTarget = document.querySelector('.review-controls') || document.getElementById('test-review-screen');
    if (topTarget) {
      topTarget.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  function pauseCurrentTest() {
    if (!currentTest || !currentTest.questions || !currentTest.questions.length) return;
    persistInProgressState(true);
    stopTimer();
    renderDashboard();
  }

  async function resumeSavedTest(slug) {
    const map = getInProgressMap();
    const state = slug ? map[slug] : Object.values(map)[0];
    if (!state || !state.slug) return;

    const meta = getTestMeta(state.slug);
    if (!meta) {
      clearInProgress(state.slug);
      renderDashboard();
      return;
    }

    await loadTest(meta.slug, meta.file);
    if (!currentTest) return;

    userAnswers = state.answers || {};
    markedQuestions = state.markedQuestions || {};
    currentIndex = Math.min(Math.max(0, state.currentIndex || 0), currentTest.questions.length - 1);
    timerSeconds = typeof state.timerSeconds === 'number' ? state.timerSeconds : 0;
    lastResults = null;

    showView('test');
    showScreen('active');
    $('#test-title-bar').textContent = currentTest.name;

    buildQuestionNav();
    renderQuestion();
    updateAnsweredCount();
    startTimer(false);
  }

  function persistInProgressState(paused) {
    if (!currentTest || !currentTest.questions || !currentTest.questions.length) return;
    if (resultsScreen.style.display !== 'none' || reviewScreen.style.display !== 'none') return;
    if (activeScreen.style.display === 'none' && !paused) return;

    saveInProgress({
      slug: currentTest.slug,
      name: currentTest.name,
      total: currentTest.questions.length,
      currentIndex,
      answers: { ...userAnswers },
      markedQuestions: { ...markedQuestions },
      timerSeconds,
      paused: !!paused,
      savedAt: new Date().toISOString()
    });
  }

  function bindUnloadAutoSave() {
    const saveOnLeave = function () {
      persistInProgressState(false);
    };
    window.addEventListener('beforeunload', saveOnLeave);
    window.addEventListener('pagehide', saveOnLeave);
  }

  // ── View Management ──────────────────────────────────────
  function showView(name) {
    dashboardView.classList.toggle('active', name === 'dashboard');
    testView.classList.toggle('active', name === 'test');
  }

  function showScreen(name) {
    startScreen.style.display = name === 'start' ? '' : 'none';
    activeScreen.style.display = name === 'active' ? '' : 'none';
    resultsScreen.style.display = name === 'results' ? '' : 'none';
    reviewScreen.style.display = name === 'review' ? '' : 'none';
  }

  // ── Confirm Dialog ───────────────────────────────────────
  function confirmAction(message, onYes) {
    const overlay = $('#confirm-overlay');
    $('#confirm-message').textContent = message;
    overlay.style.display = '';

    const yesBtn = $('#confirm-yes');
    const noBtn = $('#confirm-no');

    function cleanup() {
      overlay.style.display = 'none';
      yesBtn.removeEventListener('click', handleYes);
      noBtn.removeEventListener('click', handleNo);
    }

    function handleYes() { cleanup(); onYes(); }
    function handleNo() { cleanup(); }

    yesBtn.addEventListener('click', handleYes);
    noBtn.addEventListener('click', handleNo);
  }

  // ── Helpers ──────────────────────────────────────────────
  function esc(str) {
    if (!str) return '';
    const d = document.createElement('div');
    d.textContent = str;
    return d.innerHTML;
  }

  function formatDate(iso) {
    try {
      const d = new Date(iso);
      return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
    } catch (e) { return ''; }
  }

  // ── Boot ─────────────────────────────────────────────────
  init();

})();
