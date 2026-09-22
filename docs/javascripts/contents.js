/**
 * FLOWCAL Knowledge Hub - Contents Page Interactivity
 * Enhances the Contents tile grid with smooth navigation and active state tracking
 */

document.addEventListener('DOMContentLoaded', function() {
  // Get all content tiles and make them clickable
  const contentsTiles = document.querySelectorAll('.contents-tile');
  
  contentsTiles.forEach((tile, index) => {
    // Get the href from the tile
    let href = tile.getAttribute('href');
    
    if (!href) {
      console.warn(`Tile ${index} has no href`);
      return;
    }
    
    // Fix the href path - MkDocs resolves relative links as /contents/... when we're on /contents/
    // We need to strip the /contents/ prefix if it exists
    if (href.startsWith('/contents/')) {
      // e.g., /contents/core-features/meters/ → /core-features/meters/
      href = href.replace('/contents/', '/');
      tile.setAttribute('href', href);
      console.log(`Fixed tile href: ${tile.getAttribute('href')}`);
    }
    
    // Add click animation and let MkDocs handle navigation
    tile.addEventListener('click', function(e) {
      // Add click animation
      this.style.transform = 'scale(0.95)';
      setTimeout(() => {
        this.style.transform = '';
      }, 150);
      // Let the default link behavior work (MkDocs instant navigation)
    });
    
    // Handle keyboard navigation (Enter/Space)
    tile.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        e.stopPropagation();
        // Trigger click to follow the link with animation
        this.click();
      }
    });
    
    // Highlight current page tile
    const currentPath = window.location.pathname;
    const tileHref = href.replace(/\.md$/, '').replace(/\/$/, '');
    const normalizedPath = currentPath.replace(/\.html$/, '').replace(/\/$/, '');
    
    if (normalizedPath.includes(tileHref)) {
      tile.style.borderColor = 'var(--fc-cyan)';
      tile.style.opacity = '0.95';
      tile.setAttribute('aria-current', 'page');
    }
  });
  
  // Add smooth scroll behavior to page
  document.documentElement.style.scrollBehavior = 'smooth';
  
  console.log(`Contents page: ${contentsTiles.length} tiles initialized with corrected hrefs`);
});
