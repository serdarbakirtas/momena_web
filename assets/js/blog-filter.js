/* Blog index category filter (vanilla JS) */
(function () {
  function slugifyCategory(label) {
    return String(label || '')
      .trim()
      .toLowerCase()
      .replace(/&/g, 'and')
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '');
  }

  function initBlogFilter() {
    var filterRoot = document.querySelector('[data-blog-filter]');
    var cards = Array.prototype.slice.call(document.querySelectorAll('[data-blog-card]'));
    if (!filterRoot || cards.length === 0) return;

    var buttons = Array.prototype.slice.call(filterRoot.querySelectorAll('[data-blog-filter-btn]'));
    if (buttons.length === 0) return;

    function applyFilter(value) {
      buttons.forEach(function (btn) {
        btn.setAttribute('aria-pressed', String(btn.getAttribute('data-blog-filter-btn') === value));
      });

      cards.forEach(function (card) {
        var cat = card.getAttribute('data-blog-category') || '';
        var match = value === 'all' || cat === value;
        card.classList.toggle('is-hidden', !match);
      });
    }

    filterRoot.addEventListener(
      'click',
      function (e) {
        var btn = e.target && e.target.closest ? e.target.closest('[data-blog-filter-btn]') : null;
        if (!btn) return;
        e.preventDefault();
        var value = btn.getAttribute('data-blog-filter-btn') || 'all';
        applyFilter(value);
        if (history && history.replaceState) {
          var url = new URL(window.location.href);
          if (value === 'all') url.searchParams.delete('category');
          else url.searchParams.set('category', value);
          history.replaceState(null, '', url.toString());
        }
      },
      false
    );

    // Optional: allow deep link like ?category=engineering
    var initial = 'all';
    try {
      var params = new URL(window.location.href).searchParams;
      var fromQuery = params.get('category');
      if (fromQuery) initial = slugifyCategory(fromQuery);
    } catch (err) {}

    // If initial doesn't match any known button, fall back to all
    var has = buttons.some(function (b) {
      return b.getAttribute('data-blog-filter-btn') === initial;
    });
    applyFilter(has ? initial : 'all');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initBlogFilter);
  } else {
    initBlogFilter();
  }
})();

