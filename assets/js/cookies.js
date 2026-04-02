(function () {
  var STORAGE_KEY = 'familyakit_cookie_consent';

  function getConsent() {
    try {
      return localStorage.getItem(STORAGE_KEY);
    } catch (e) {
      return null;
    }
  }

  function setConsent(value) {
    try {
      localStorage.setItem(STORAGE_KEY, value);
    } catch (e) {}
  }

  function showBanner() {
    var banner = document.getElementById('cookie-banner');
    if (banner) banner.classList.add('show');
  }

  function hideBanner() {
    var banner = document.getElementById('cookie-banner');
    if (banner) banner.classList.remove('show');
  }

  function init() {
    var consent = getConsent();
    if (!consent) {
      showBanner();
    }

    var acceptBtn = document.querySelector('.cookie-btn-accept');
    var rejectBtn = document.querySelector('.cookie-btn-reject');

    if (acceptBtn) {
      acceptBtn.addEventListener('click', function () {
        setConsent('accepted');
        hideBanner();
      });
    }

    if (rejectBtn) {
      rejectBtn.addEventListener('click', function () {
        setConsent('rejected');
        hideBanner();
      });
    }

    var prefsLink = document.getElementById('cookie-prefs');
    if (prefsLink) {
      prefsLink.addEventListener('click', function (e) {
        e.preventDefault();
        setConsent('');
        showBanner();
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
