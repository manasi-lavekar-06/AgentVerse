/**
 * FLOWCAL Knowledge Hub – Diagram renderer
 * Reads the semantic `.dg-items` list emitted by the Publishing Agent for
 * `render_hint: "diagram"` sections and renders it as a top-down hub-and-
 * spoke diagram: one hub node (the section heading) connected by straight
 * lines to a row of point nodes below — for relationships, comparisons, and
 * structural breakdowns. Re-initializes on Material's instant-navigation
 * page swaps.
 */
(function () {
  'use strict';

  var PALETTE = [
    { accent: '#2563eb', bg: '#dbeafe' },
    { accent: '#d97706', bg: '#fef3c7' },
    { accent: '#059669', bg: '#d1fae5' },
    { accent: '#db2777', bg: '#fce7f3' },
    { accent: '#7c3aed', bg: '#ede9fe' },
    { accent: '#0891b2', bg: '#cffafe' }
  ];

  function parseDiagram(container) {
    var listEl = container.querySelector('.dg-items');
    if (!listEl) return null;
    var rootEl = container.querySelector('.dg-root');
    var items = [];
    listEl.querySelectorAll(':scope > li.dg-item').forEach(function (li) {
      var text = li.textContent.trim();
      if (text) items.push(text);
    });
    if (!items.length) return null;
    return { listEl: listEl, root: rootEl ? rootEl.textContent.trim() : 'Overview', items: items };
  }

  function buildDiagram(container, data) {
    var wrap = document.createElement('div');
    wrap.className = 'dg-rendered';

    var hub = document.createElement('div');
    hub.className = 'dg-hub';
    hub.textContent = data.root;
    wrap.appendChild(hub);

    var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('class', 'dg-links');
    wrap.appendChild(svg);

    var spokes = document.createElement('div');
    spokes.className = 'dg-spokes';

    data.items.forEach(function (text, i) {
      var colors = PALETTE[i % PALETTE.length];
      var node = document.createElement('div');
      node.className = 'dg-node';
      node.style.animationDelay = (i * 80) + 'ms';
      node.style.borderColor = colors.accent;
      node.style.background = colors.bg;
      node.textContent = text;
      spokes.appendChild(node);
    });

    wrap.appendChild(spokes);
    container.appendChild(wrap);

    function drawLinks() {
      var hubRect = hub.getBoundingClientRect();
      var wrapRect = wrap.getBoundingClientRect();
      svg.setAttribute('width', wrapRect.width);
      svg.setAttribute('height', wrapRect.height);
      svg.setAttribute('viewBox', '0 0 ' + wrapRect.width + ' ' + wrapRect.height);
      while (svg.firstChild) svg.removeChild(svg.firstChild);

      var x1 = hubRect.left - wrapRect.left + hubRect.width / 2;
      var y1 = hubRect.bottom - wrapRect.top;
      spokes.querySelectorAll('.dg-node').forEach(function (node) {
        var r = node.getBoundingClientRect();
        var x2 = r.left - wrapRect.left + r.width / 2;
        var y2 = r.top - wrapRect.top;
        var path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        var my = (y1 + y2) / 2;
        path.setAttribute('d', 'M ' + x1 + ' ' + y1 + ' C ' + x1 + ' ' + my + ', ' + x2 + ' ' + my + ', ' + x2 + ' ' + y2);
        path.setAttribute('class', 'dg-link');
        svg.appendChild(path);
      });
    }

    drawLinks();
    if (typeof ResizeObserver !== 'undefined') {
      var scheduled = false;
      new ResizeObserver(function () {
        if (scheduled) return;
        scheduled = true;
        requestAnimationFrame(function () { scheduled = false; drawLinks(); });
      }).observe(wrap);
    }
  }

  function initDiagram(container) {
    if (container.dataset.dgBound) return;
    var data = parseDiagram(container);
    if (!data) return;
    container.dataset.dgBound = 'true';
    data.listEl.classList.add('dg-items-hidden');
    buildDiagram(container, data);
  }

  function initAll() {
    document.querySelectorAll('.dg-diagram').forEach(initDiagram);
  }

  if (typeof document$ !== 'undefined') {
    document$.subscribe(function () { initAll(); });
  } else {
    document.readyState === 'loading'
      ? document.addEventListener('DOMContentLoaded', initAll)
      : initAll();
  }
}());
