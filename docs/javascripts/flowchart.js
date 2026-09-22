/**
 * FLOWCAL Knowledge Hub – Flowchart renderer
 * Reads the semantic `.flow-steps` list emitted by the Publishing Agent for
 * `render_hint: "flowchart"` sections and renders it as a sequence of
 * connected rectangular nodes with arrows between them (click a node to
 * expand its full text). Re-initializes on Material's instant-navigation
 * page swaps.
 */
(function () {
  'use strict';

  var PALETTE = ['#2563eb', '#d97706', '#059669', '#db2777', '#7c3aed', '#0891b2'];

  function parseFlowchart(container) {
    var listEl = container.querySelector('.flow-steps');
    if (!listEl) return null;
    var rootEl = container.querySelector('.flow-root');
    var steps = [];
    listEl.querySelectorAll(':scope > li.flow-step').forEach(function (li) {
      var text = li.textContent.trim();
      if (text) steps.push(text);
    });
    if (!steps.length) return null;
    return { listEl: listEl, root: rootEl ? rootEl.textContent.trim() : '', steps: steps };
  }

  function buildChart(container, data) {
    var wrap = document.createElement('div');
    wrap.className = 'flow-rendered';
    wrap.setAttribute('role', 'list');

    if (data.root) {
      var title = document.createElement('div');
      title.className = 'flow-title';
      title.textContent = data.root;
      wrap.appendChild(title);
    }

    var track = document.createElement('div');
    track.className = 'flow-track';

    data.steps.forEach(function (text, i) {
      var color = PALETTE[i % PALETTE.length];
      var node = document.createElement('button');
      node.type = 'button';
      node.className = 'flow-node';
      node.style.animationDelay = (i * 90) + 'ms';
      node.style.borderColor = color;
      node.setAttribute('role', 'listitem');
      node.setAttribute('aria-expanded', 'false');

      var badge = document.createElement('span');
      badge.className = 'flow-index';
      badge.style.background = color;
      badge.textContent = String(i + 1);

      var label = document.createElement('span');
      label.className = 'flow-label';
      label.textContent = text;

      node.appendChild(badge);
      node.appendChild(label);
      node.addEventListener('click', function () {
        var expanded = node.classList.toggle('flow-expanded');
        node.setAttribute('aria-expanded', expanded ? 'true' : 'false');
      });

      track.appendChild(node);

      if (i < data.steps.length - 1) {
        var arrow = document.createElement('span');
        arrow.className = 'flow-arrow';
        arrow.style.animationDelay = (i * 90 + 45) + 'ms';
        arrow.setAttribute('aria-hidden', 'true');
        arrow.textContent = '\u2192';
        track.appendChild(arrow);
      }
    });

    wrap.appendChild(track);
    container.appendChild(wrap);
  }

  function initFlowchart(container) {
    if (container.dataset.flowBound) return;
    var data = parseFlowchart(container);
    if (!data) return;
    container.dataset.flowBound = 'true';
    data.listEl.classList.add('flow-steps-hidden');
    buildChart(container, data);
  }

  function initAll() {
    document.querySelectorAll('.flow-chart').forEach(initFlowchart);
  }

  if (typeof document$ !== 'undefined') {
    document$.subscribe(function () { initAll(); });
  } else {
    document.readyState === 'loading'
      ? document.addEventListener('DOMContentLoaded', initAll)
      : initAll();
  }
}());
