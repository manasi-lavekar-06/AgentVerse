/**
 * FLOWCAL Knowledge Hub – Slideshow renderer
 * Reads the semantic `.sl-slides` list emitted by the Publishing Agent for
 * `render_hint: "slideshow"` sections and renders it as a small carousel:
 * one point shown at a time, with prev/next controls, dot navigation, and a
 * light auto-advance that pauses on hover/focus. Re-initializes on
 * Material's instant-navigation page swaps.
 */
(function () {
  'use strict';

  var AUTO_ADVANCE_MS = 4500;

  function parseSlideshow(container) {
    var listEl = container.querySelector('.sl-slides');
    if (!listEl) return null;
    var rootEl = container.querySelector('.sl-root');
    var slides = [];
    listEl.querySelectorAll(':scope > li.sl-slide').forEach(function (li) {
      var text = li.textContent.trim();
      if (text) slides.push(text);
    });
    if (!slides.length) return null;
    return { listEl: listEl, root: rootEl ? rootEl.textContent.trim() : '', slides: slides };
  }

  function buildCarousel(container, data) {
    var wrap = document.createElement('div');
    wrap.className = 'sl-rendered';

    if (data.root) {
      var title = document.createElement('div');
      title.className = 'sl-title';
      title.textContent = data.root;
      wrap.appendChild(title);
    }

    var viewport = document.createElement('div');
    viewport.className = 'sl-viewport';
    var textEl = document.createElement('p');
    textEl.className = 'sl-text';
    viewport.appendChild(textEl);

    var prevBtn = document.createElement('button');
    prevBtn.type = 'button';
    prevBtn.className = 'sl-nav sl-prev';
    prevBtn.setAttribute('aria-label', 'Previous');
    prevBtn.textContent = '\u2039';

    var nextBtn = document.createElement('button');
    nextBtn.type = 'button';
    nextBtn.className = 'sl-nav sl-next';
    nextBtn.setAttribute('aria-label', 'Next');
    nextBtn.textContent = '\u203a';

    var dots = document.createElement('div');
    dots.className = 'sl-dots';
    var dotEls = data.slides.map(function (_, i) {
      var dot = document.createElement('button');
      dot.type = 'button';
      dot.className = 'sl-dot';
      dot.setAttribute('aria-label', 'Slide ' + (i + 1));
      dot.addEventListener('click', function () { goTo(i); });
      dots.appendChild(dot);
      return dot;
    });

    var current = 0;
    var timer = null;

    function render() {
      textEl.style.animation = 'none';
      // Force reflow so the fade-in animation replays every slide change.
      void textEl.offsetWidth;
      textEl.style.animation = '';
      textEl.textContent = data.slides[current];
      dotEls.forEach(function (dot, i) { dot.classList.toggle('sl-dot-active', i === current); });
    }

    function goTo(i) {
      current = (i + data.slides.length) % data.slides.length;
      render();
      restartTimer();
    }

    function restartTimer() {
      if (timer) clearInterval(timer);
      timer = setInterval(function () { goTo(current + 1); }, AUTO_ADVANCE_MS);
    }

    prevBtn.addEventListener('click', function () { goTo(current - 1); });
    nextBtn.addEventListener('click', function () { goTo(current + 1); });
    wrap.addEventListener('mouseenter', function () { if (timer) clearInterval(timer); });
    wrap.addEventListener('mouseleave', restartTimer);

    viewport.insertBefore(prevBtn, textEl);
    viewport.appendChild(nextBtn);
    wrap.appendChild(viewport);
    wrap.appendChild(dots);
    container.appendChild(wrap);

    render();
    if (data.slides.length > 1) restartTimer();
  }

  function initSlideshow(container) {
    if (container.dataset.slBound) return;
    var data = parseSlideshow(container);
    if (!data) return;
    container.dataset.slBound = 'true';
    data.listEl.classList.add('sl-slides-hidden');
    buildCarousel(container, data);
  }

  function initAll() {
    document.querySelectorAll('.sl-slideshow').forEach(initSlideshow);
  }

  if (typeof document$ !== 'undefined') {
    document$.subscribe(function () { initAll(); });
  } else {
    document.readyState === 'loading'
      ? document.addEventListener('DOMContentLoaded', initAll)
      : initAll();
  }
}());
