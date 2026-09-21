/**
 * FLOWCAL Knowledge Hub – Quiz Component
 * Reads .qz-q child elements, builds a multiple-choice quiz UI.
 *
 * HTML structure expected inside .quiz-deck:
 *   <div class="qz-q" data-correct="2" data-explanation="...">
 *     <p class="qz-question-text">Question text here?</p>
 *     <span class="qz-opt">Option A</span>
 *     <span class="qz-opt">Option B</span>
 *     <span class="qz-opt">Option C (correct)</span>
 *     <span class="qz-opt">Option D</span>
 *   </div>
 */
(function () {
  'use strict';

  var LETTERS = ['A', 'B', 'C', 'D', 'E'];

  function buildQuiz(deck) {
    var rawQs = deck.querySelectorAll('.qz-q');
    if (!rawQs.length) return;

    var questions = Array.from(rawQs).map(function (el) {
      return {
        text:        el.querySelector('.qz-question-text') ? el.querySelector('.qz-question-text').textContent.trim() : '',
        options:     Array.from(el.querySelectorAll('.qz-opt')).map(function (o) { return o.textContent.trim(); }),
        correct:     parseInt(el.dataset.correct, 10) || 0,
        explanation: el.dataset.explanation || '',
      };
    });

    var colorKey  = deck.dataset.color || 'blue';
    var total     = questions.length;
    var current   = 0;
    var score     = 0;
    var answered  = false;
    var results   = [];  // { selected, correct } per question

    // ── Build skeleton ──────────────────────────────────────────────────────
    deck.innerHTML =
      '<div class="qzd-wrapper">' +
        '<div class="qzd-header">' +
          '<div class="qzd-meta">' +
            '<span class="qzd-badge">Knowledge Check</span>' +
            '<span class="qzd-counter"><span class="qzd-cur">1</span> / ' + total + '</span>' +
          '</div>' +
          '<div class="qzd-score-inline">Score: <span class="qzd-score-val">0</span> / ' + total + '</div>' +
        '</div>' +
        '<div class="qzd-progress-bar"><div class="qzd-fill" style="width:0%"></div></div>' +

        '<div class="qzd-stage">' +
          '<div class="qzd-question-text"></div>' +
          '<div class="qzd-options"></div>' +
          '<div class="qzd-feedback" hidden>' +
            '<div class="qzd-fb-icon"></div>' +
            '<div class="qzd-fb-body">' +
              '<div class="qzd-fb-verdict"></div>' +
              '<div class="qzd-fb-explanation"></div>' +
            '</div>' +
          '</div>' +
        '</div>' +

        '<div class="qzd-nav">' +
          '<button class="qzd-btn qzd-next-btn" disabled>Next Question →</button>' +
        '</div>' +

        '<div class="qzd-results" hidden>' +
          '<div class="qzd-results-inner">' +
            '<div class="qzd-trophy">🎯</div>' +
            '<h3 class="qzd-results-title">Quiz Complete!</h3>' +
            '<div class="qzd-results-score"></div>' +
            '<div class="qzd-results-msg"></div>' +
            '<div class="qzd-results-breakdown"></div>' +
            '<button class="qzd-btn qzd-retry-btn">↺ Try Again</button>' +
          '</div>' +
        '</div>' +
      '</div>';

    // ── Element refs ─────────────────────────────────────────────────────────
    var qText    = deck.querySelector('.qzd-question-text');
    var optsEl   = deck.querySelector('.qzd-options');
    var fbEl     = deck.querySelector('.qzd-feedback');
    var fbIcon   = deck.querySelector('.qzd-fb-icon');
    var fbVerdict= deck.querySelector('.qzd-fb-verdict');
    var fbExpl   = deck.querySelector('.qzd-fb-explanation');
    var curEl    = deck.querySelector('.qzd-cur');
    var fillEl   = deck.querySelector('.qzd-fill');
    var scoreVal = deck.querySelector('.qzd-score-val');
    var nextBtn  = deck.querySelector('.qzd-next-btn');
    var resultsEl= deck.querySelector('.qzd-results');
    var stageEl  = deck.querySelector('.qzd-stage');
    var navEl    = deck.querySelector('.qzd-nav');
    var retryBtn = deck.querySelector('.qzd-retry-btn');
    var rScoreEl = deck.querySelector('.qzd-results-score');
    var rMsgEl   = deck.querySelector('.qzd-results-msg');
    var rBreakEl = deck.querySelector('.qzd-results-breakdown');

    function renderQuestion() {
      var q = questions[current];
      answered = false;
      fbEl.hidden = true;
      nextBtn.disabled = true;
      nextBtn.textContent = (current === total - 1) ? 'See Results →' : 'Next Question →';
      curEl.textContent = current + 1;
      fillEl.style.width = (current / total * 100).toFixed(1) + '%';
      qText.textContent = q.text;

      // Build options
      optsEl.innerHTML = '';
      q.options.forEach(function (opt, i) {
        var btn = document.createElement('button');
        btn.className = 'qzd-opt-btn';
        btn.setAttribute('data-idx', i);
        btn.innerHTML =
          '<span class="qzd-opt-letter">' + LETTERS[i] + '</span>' +
          '<span class="qzd-opt-text">' + escHtml(opt) + '</span>';
        btn.addEventListener('click', function () { selectAnswer(i); });
        optsEl.appendChild(btn);
      });
    }

    function selectAnswer(idx) {
      if (answered) return;
      answered = true;
      var q = questions[current];
      var correct = (idx === q.correct);
      if (correct) score++;
      results.push({ selected: idx, correct: q.correct });
      scoreVal.textContent = score;

      // Style option buttons
      var btns = optsEl.querySelectorAll('.qzd-opt-btn');
      btns.forEach(function (btn, i) {
        btn.disabled = true;
        if (i === q.correct) btn.classList.add('correct');
        if (i === idx && !correct) btn.classList.add('wrong');
      });

      // Show feedback
      fbIcon.textContent  = correct ? '✓' : '✗';
      fbIcon.className    = 'qzd-fb-icon ' + (correct ? 'fb-correct' : 'fb-wrong');
      fbVerdict.textContent = correct ? 'Correct!' : 'Not quite — the right answer is ' + LETTERS[q.correct] + '.';
      fbVerdict.className = 'qzd-fb-verdict ' + (correct ? 'fb-correct' : 'fb-wrong');
      fbExpl.textContent  = q.explanation;
      fbEl.hidden = false;

      nextBtn.disabled = false;
    }

    function showResults() {
      stageEl.hidden = true;
      navEl.hidden   = true;
      resultsEl.hidden = false;

      var pct = Math.round(score / total * 100);
      rScoreEl.innerHTML = '<span class="qzd-big-score">' + score + '</span><span class="qzd-big-denom"> / ' + total + '</span><span class="qzd-big-pct"> (' + pct + '%)</span>';

      var msg = pct === 100 ? 'Perfect score! Outstanding work.' :
                pct >= 80  ? 'Great job! You have a solid understanding.' :
                pct >= 60  ? 'Good effort! Review the feedback below to reinforce the gaps.' :
                             'Keep studying — the flashcards on the Core Features tab can help.';
      rMsgEl.textContent = msg;

      // Breakdown
      var html = '<div class="qzd-breakdown-list">';
      questions.forEach(function (q, i) {
        var r = results[i];
        var ok = r && r.selected === q.correct;
        html += '<div class="qzd-br-row ' + (ok ? 'br-ok' : 'br-fail') + '">' +
          '<span class="qzd-br-icon">' + (ok ? '✓' : '✗') + '</span>' +
          '<span class="qzd-br-q">' + escHtml(q.text) + '</span>' +
        '</div>';
      });
      html += '</div>';
      rBreakEl.innerHTML = html;
    }

    function reset() {
      current  = 0;
      score    = 0;
      answered = false;
      results  = [];
      scoreVal.textContent = 0;
      stageEl.hidden = false;
      navEl.hidden   = false;
      resultsEl.hidden = true;
      renderQuestion();
    }

    nextBtn.addEventListener('click', function () {
      if (current < total - 1) {
        current++;
        renderQuestion();
      } else {
        fillEl.style.width = '100%';
        showResults();
      }
    });

    retryBtn.addEventListener('click', reset);

    // Keyboard: Enter on focused option button
    deck.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && e.target.classList.contains('qzd-opt-btn')) {
        e.target.click();
      }
    });

    renderQuestion();
  }

  function escHtml(str) {
    return str.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }

  function initAll() {
    document.querySelectorAll('.quiz-deck').forEach(buildQuiz);
  }

  if (typeof document$ !== 'undefined') {
    document$.subscribe(function () { initAll(); });
  } else {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initAll);
    } else {
      initAll();
    }
  }
}());
