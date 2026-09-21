/**
 * FLOWCAL Knowledge Hub – Visual Story Slideshow
 * Auto-advances slides, animates a progress bar, supports prev/next/pause.
 */
(function () {
  'use strict';

  var SLIDE_DURATION = 5500; // ms per slide

  function initStory(container) {
    var slides   = Array.from(container.querySelectorAll('.vs-slide'));
    var dotsWrap = container.querySelector('.vs-dots');
    var prevBtn  = container.querySelector('.vs-prev-btn');
    var nextBtn  = container.querySelector('.vs-next-btn');
    var playBtn  = container.querySelector('.vs-play-btn');
    var fillEl   = container.querySelector('.vs-progress-fill');

    if (!slides.length) return;

    var current  = 0;
    var playing  = true;
    var timer    = null;
    var fillAnim = null;

    /* build dots */
    dotsWrap.innerHTML = slides.map(function (_, i) {
      return '<button class="vs-dot' + (i === 0 ? ' active' : '') + '" aria-label="Slide ' + (i + 1) + '"></button>';
    }).join('');
    var dots = dotsWrap.querySelectorAll('.vs-dot');

    dots.forEach(function (dot, i) {
      dot.addEventListener('click', function () { goTo(i); });
    });

    /* show a slide */
    function goTo(idx) {
      slides[current].classList.remove('active');
      dots[current].classList.remove('active');

      current = (idx + slides.length) % slides.length;

      slides[current].classList.add('active');
      dots[current].classList.add('active');

      resetProgress();
      if (playing) startTimer();
    }

    /* progress bar */
    function resetProgress() {
      clearInterval(fillAnim);
      fillEl.style.transition = 'none';
      fillEl.style.width = '0%';
      /* force reflow */
      void fillEl.offsetWidth;
    }

    function startProgress() {
      fillEl.style.transition = 'width ' + SLIDE_DURATION + 'ms linear';
      fillEl.style.width = '100%';
    }

    /* auto-advance timer */
    function startTimer() {
      clearTimeout(timer);
      startProgress();
      timer = setTimeout(function () {
        if (playing) goTo(current + 1);
      }, SLIDE_DURATION);
    }

    function stopTimer() {
      clearTimeout(timer);
      resetProgress();
    }

    /* controls */
    prevBtn.addEventListener('click', function () {
      stopTimer();
      playing = false;
      playBtn.textContent = '▶';
      slides[current].classList.remove('active');
      dots[current].classList.remove('active');
      current = (current - 1 + slides.length) % slides.length;
      slides[current].classList.add('active');
      dots[current].classList.add('active');
    });

    nextBtn.addEventListener('click', function () {
      stopTimer();
      playing = false;
      playBtn.textContent = '▶';
      slides[current].classList.remove('active');
      dots[current].classList.remove('active');
      current = (current + 1) % slides.length;
      slides[current].classList.add('active');
      dots[current].classList.add('active');
    });

    playBtn.addEventListener('click', function () {
      playing = !playing;
      playBtn.textContent = playing ? '⏸' : '▶';
      if (playing) startTimer();
      else stopTimer();
    });

    /* keyboard */
    container.setAttribute('tabindex', '0');
    container.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') nextBtn.click();
      if (e.key === 'ArrowLeft')  prevBtn.click();
      if (e.key === ' ') { e.preventDefault(); playBtn.click(); }
    });

    /* start */
    slides[0].classList.add('active');
    startTimer();
  }

  function initAll() {
    document.querySelectorAll('.vs-container').forEach(initStory);
  }

  if (typeof document$ !== 'undefined') {
    document$.subscribe(function () { initAll(); });
  } else {
    document.readyState === 'loading'
      ? document.addEventListener('DOMContentLoaded', initAll)
      : initAll();
  }
}());
