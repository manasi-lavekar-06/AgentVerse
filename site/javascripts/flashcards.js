/**
 * FLOWCAL Knowledge Hub – Flashcard Deck Component
 * Reads .fc-card child elements, builds an interactive flip-card UI.
 */
(function () {
  'use strict';

  var PALETTE = {
    blue:   { start: '#1565C0', end: '#1E88E5', accent: '#E3F2FD', text: '#0D47A1' },
    teal:   { start: '#00695C', end: '#00897B', accent: '#E0F2F1', text: '#004D40' },
    purple: { start: '#6A1B9A', end: '#8E24AA', accent: '#F3E5F5', text: '#4A148C' },
    green:  { start: '#2E7D32', end: '#43A047', accent: '#E8F5E9', text: '#1B5E20' },
    orange: { start: '#BF360C', end: '#E64A19', accent: '#FBE9E7', text: '#870000' },
  };

  function buildDeck(deck) {
    var rawCards = deck.querySelectorAll('.fc-card');
    if (!rawCards.length) return;

    var cards = Array.from(rawCards).map(function (el) {
      return {
        term: el.dataset.term || 'Term',
        category: el.dataset.category || '',
        definition: el.textContent.trim(),
      };
    });

    var colorKey = deck.dataset.color || 'blue';
    var col = PALETTE[colorKey] || PALETTE.blue;
    var total = cards.length;
    var current = 0;
    var flipped = false;

    deck.innerHTML =
      '<div class="fcd-wrapper">' +
        '<div class="fcd-header">' +
          '<span class="fcd-label">Study Cards</span>' +
          '<span class="fcd-progress-text"><span class="fcd-cur">1</span>&thinsp;of&thinsp;' + total + '</span>' +
        '</div>' +
        '<div class="fcd-progress-bar"><div class="fcd-progress-fill"></div></div>' +
        '<div class="fcd-stage">' +
          '<div class="fcd-card" tabindex="0" role="button" aria-label="Flashcard — click to flip">' +
            '<div class="fcd-card-inner">' +
              '<div class="fcd-front" style="--cs:' + col.start + ';--ce:' + col.end + '">' +
                '<span class="fcd-badge fcd-badge-front"></span>' +
                '<div class="fcd-card-number"></div>' +
                '<div class="fcd-term"></div>' +
                '<div class="fcd-hint">tap to see definition ↓</div>' +
              '</div>' +
              '<div class="fcd-back" style="--ca:' + col.accent + ';--ct:' + col.text + '">' +
                '<span class="fcd-badge fcd-badge-back"></span>' +
                '<div class="fcd-definition"></div>' +
              '</div>' +
            '</div>' +
          '</div>' +
        '</div>' +
        '<div class="fcd-dots"></div>' +
        '<div class="fcd-nav">' +
          '<button class="fcd-btn fcd-prev" aria-label="Previous">&#8592; Prev</button>' +
          '<button class="fcd-btn fcd-flip-btn" aria-label="Flip">&#8635; Flip</button>' +
          '<button class="fcd-btn fcd-next" aria-label="Next">Next &#8594;</button>' +
        '</div>' +
        '<div class="fcd-shortcut-hint">&#9664; &#9654; arrow keys navigate &nbsp;|&nbsp; Space / Enter flips</div>' +
      '</div>';

    var cardEl   = deck.querySelector('.fcd-card');
    var termEl   = deck.querySelector('.fcd-term');
    var defEl    = deck.querySelector('.fcd-definition');
    var badgeF   = deck.querySelector('.fcd-badge-front');
    var badgeB   = deck.querySelector('.fcd-badge-back');
    var numEl    = deck.querySelector('.fcd-card-number');
    var curEl    = deck.querySelector('.fcd-cur');
    var fill     = deck.querySelector('.fcd-progress-fill');
    var dotsEl   = deck.querySelector('.fcd-dots');
    var prevBtn  = deck.querySelector('.fcd-prev');
    var nextBtn  = deck.querySelector('.fcd-next');
    var flipBtn  = deck.querySelector('.fcd-flip-btn');

    // Build dots
    dotsEl.innerHTML = cards.map(function (_, i) {
      return '<span class="fcd-dot' + (i === 0 ? ' active' : '') + '"></span>';
    }).join('');
    var dots = dotsEl.querySelectorAll('.fcd-dot');

    function render() {
      var c = cards[current];
      termEl.textContent = c.term;
      defEl.textContent  = c.definition;
      badgeF.textContent = c.category;
      badgeB.textContent = c.category;
      numEl.textContent  = (current + 1) + ' / ' + total;
      curEl.textContent  = current + 1;
      fill.style.width   = ((current + 1) / total * 100).toFixed(1) + '%';
      dots.forEach(function (d, i) { d.classList.toggle('active', i === current); });
      prevBtn.disabled = (current === 0);
      nextBtn.disabled = (current === total - 1);
      // announce for screen readers
      cardEl.setAttribute('aria-label', 'Card ' + (current + 1) + ' of ' + total + ': ' + c.term + '. Click to flip.');
    }

    function setFlip(f) {
      flipped = f;
      cardEl.classList.toggle('flipped', flipped);
      flipBtn.textContent = flipped ? '\u8635 Term' : '\u8635 Flip';
    }

    function goTo(idx) {
      var n = Math.max(0, Math.min(idx, total - 1));
      if (n === current) return;
      current = n;
      setFlip(false);
      render();
    }

    // Click to flip
    cardEl.addEventListener('click', function () { setFlip(!flipped); });

    // Keyboard on card
    cardEl.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); setFlip(!flipped); }
    });

    // Buttons
    flipBtn.addEventListener('click', function (e) { e.stopPropagation(); setFlip(!flipped); });
    prevBtn.addEventListener('click', function () { goTo(current - 1); });
    nextBtn.addEventListener('click', function () { goTo(current + 1); });

    // Global keyboard (arrow keys) while deck is focused
    deck.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { e.preventDefault(); goTo(current + 1); }
      if (e.key === 'ArrowLeft')  { e.preventDefault(); goTo(current - 1); }
    });

    // Touch / swipe
    var touchStartX = 0;
    var touchStartY = 0;
    cardEl.addEventListener('touchstart', function (e) {
      touchStartX = e.touches[0].clientX;
      touchStartY = e.touches[0].clientY;
    }, { passive: true });
    cardEl.addEventListener('touchend', function (e) {
      var dx = e.changedTouches[0].clientX - touchStartX;
      var dy = e.changedTouches[0].clientY - touchStartY;
      if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 45) {
        goTo(current + (dx < 0 ? 1 : -1));
      } else if (Math.abs(dx) < 10 && Math.abs(dy) < 10) {
        setFlip(!flipped);
      }
    });

    render();
  }

  function initAll() {
    document.querySelectorAll('.flashcard-deck').forEach(buildDeck);
  }

  // MkDocs Material uses a SPA-style navigation; hook into document$ observable
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
