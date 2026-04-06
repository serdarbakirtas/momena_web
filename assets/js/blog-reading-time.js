(function () {
  'use strict';

  var body = document.querySelector('[data-blog-article-body]');
  var out = document.querySelector('[data-reading-time-out]');
  if (!body || !out) return;

  var text = body.textContent || '';
  var words = text.trim().split(/\s+/).filter(function (w) {
    return w.length > 0;
  }).length;
  var mins = Math.max(1, Math.ceil(words / 200));
  out.textContent = mins + ' min read';
})();
