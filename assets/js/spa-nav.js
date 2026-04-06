(function () {
  'use strict';

  var primaryNav = document.getElementById('primary-navigation');
  var navToggle = document.getElementById('nav-toggle');
  var navSectionIds = ['home', 'pricing', 'our-story', 'blog', 'support'];
  var ticking = false;

  function prefersReducedMotion() {
    return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  /** Same-page #section links: smooth scroll even if CSS scroll-behavior fails to load (e.g. asset 404). */
  function initInPageHashSmoothScroll() {
    if (prefersReducedMotion()) return;

    function scrollToId(id) {
      var el = document.getElementById(id);
      if (!el) return false;
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      return true;
    }

    document.addEventListener(
      'click',
      function (e) {
        if (e.defaultPrevented || e.button !== 0) return;
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
        var a = e.target.closest('a[href^="#"]');
        if (!a) return;
        var href = a.getAttribute('href');
        if (!href || href === '#' || href.length < 2) return;
        var id = href.slice(1);
        if (!id) return;
        if (!document.getElementById(id)) return;
        e.preventDefault();
        if (history.replaceState) {
          history.replaceState(null, '', href);
        } else {
          window.location.hash = href;
        }
        scrollToId(id);
        window.requestAnimationFrame(function () {
          if (primaryNav) updateScrollSpy();
        });
      },
      false
    );
  }

  function getHeaderOffset() {
    var root = document.documentElement;
    var v = getComputedStyle(root).getPropertyValue('--header-offset').trim();
    var n = parseInt(v, 10);
    return isNaN(n) ? 96 : n;
  }

  function closeMobileNav() {
    if (!primaryNav || !navToggle) return;
    primaryNav.classList.remove('is-open');
    navToggle.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('nav-open');
  }

  function openMobileNav() {
    if (!primaryNav || !navToggle) return;
    primaryNav.classList.add('is-open');
    navToggle.setAttribute('aria-expanded', 'true');
    document.body.classList.add('nav-open');
  }

  function toggleMobileNav() {
    if (!primaryNav || !navToggle) return;
    if (primaryNav.classList.contains('is-open')) closeMobileNav();
    else openMobileNav();
  }

  if (navToggle && primaryNav) {
    navToggle.addEventListener('click', function () {
      toggleMobileNav();
    });

    primaryNav.querySelectorAll('a[href^="#"]').forEach(function (link) {
      link.addEventListener('click', function () {
        closeMobileNav();
      });
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeMobileNav();
    });

    document.addEventListener('click', function (e) {
      if (!primaryNav.classList.contains('is-open')) return;
      var t = e.target;
      if (t === navToggle || navToggle.contains(t)) return;
      if (primaryNav.contains(t)) return;
      closeMobileNav();
    });
  }

  function setActiveNav(id) {
    if (!primaryNav) return;
    primaryNav.querySelectorAll('a[data-nav-target]').forEach(function (a) {
      var match = a.getAttribute('data-nav-target') === id;
      a.classList.toggle('is-active', match);
      if (match) a.setAttribute('aria-current', 'location');
      else a.removeAttribute('aria-current');
    });
  }

  function getDocumentOffsetTop(el) {
    var rect = el.getBoundingClientRect();
    return rect.top + (window.scrollY || document.documentElement.scrollTop);
  }

  function updateScrollSpy() {
    var headerOffset = getHeaderOffset();
    var current = 'home';
    var bestId = 'home';
    var bestDistance = Infinity;

    for (var i = 0; i < navSectionIds.length; i++) {
      var id = navSectionIds[i];
      var el = document.getElementById(id);
      if (!el) continue;

      var rect = el.getBoundingClientRect();
      var distance = Math.abs(rect.top - headerOffset - 12);

      if (distance < bestDistance) {
        bestDistance = distance;
        bestId = id;
      }
    }

    current = bestId;
    setActiveNav(current);
    ticking = false;
  }

  function onScroll() {
    if (!ticking) {
      ticking = true;
      window.requestAnimationFrame(updateScrollSpy);
    }
  }

  function initScrollSpy() {
    updateScrollSpy();
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', function () {
      updateScrollSpy();
    });
    window.addEventListener('hashchange', function () {
      window.requestAnimationFrame(updateScrollSpy);
    });
  }

  function initSpaNav() {
    initScrollSpy();
    initInPageHashSmoothScroll();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSpaNav);
  } else {
    initSpaNav();
  }
})();
