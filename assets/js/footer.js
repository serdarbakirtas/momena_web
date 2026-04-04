(function () {
  document.querySelectorAll('a.footer-social-link[href="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      e.preventDefault();
    });
  });
})();
