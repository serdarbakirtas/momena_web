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
  var lang = (document.documentElement && document.documentElement.lang) || 'en';
  if (lang === 'de') {
    out.textContent = mins + ' Min. Lesezeit';
  } else if (lang === 'tr') {
    out.textContent = mins + ' dk okuma';
  } else {
    out.textContent = mins + ' min read';
  }
})();
