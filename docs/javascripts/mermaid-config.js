/* Render source-controlled FLOWCAL diagrams with a single theme per color mode. */
(function () {
  'use strict';

  function initialiseMermaid() {
    import('https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs')
      .then(function (module) {
        var mermaid = module.default;
        var dark = document.body.getAttribute('data-md-color-scheme') === 'slate';
        mermaid.initialize({
          startOnLoad: false,
          securityLevel: 'strict',
          theme: 'base',
          themeVariables: dark ? {
            background: '#111a22', primaryColor: '#193c44', primaryTextColor: '#edf6f5',
            primaryBorderColor: '#4cc2b4', lineColor: '#91aaa8', secondaryColor: '#3a2416'
          } : {
            background: '#ffffff', primaryColor: '#e5f3f0', primaryTextColor: '#17333b',
            primaryBorderColor: '#16796f', lineColor: '#557775', secondaryColor: '#fff0e5'
          },
          flowchart: { curve: 'basis', htmlLabels: true, useMaxWidth: true }
        });
        document.querySelectorAll('pre.fc-mermaid-source').forEach(function (source, index) {
          if (source.dataset.rendered === 'true') return;
          source.dataset.rendered = 'true';
          mermaid.render('flowcal-diagram-' + index, source.textContent)
            .then(function (result) {
              var diagram = document.createElement('div');
              diagram.className = 'fc-mermaid-diagram';
              diagram.innerHTML = result.svg;
              source.replaceWith(diagram);
              if (result.bindFunctions) result.bindFunctions(diagram);
            });
        });
      });
  }

  if (typeof document$ !== 'undefined') {
    document$.subscribe(initialiseMermaid);
  } else {
    document.addEventListener('DOMContentLoaded', initialiseMermaid);
  }
}());