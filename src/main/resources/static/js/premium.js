/**
 * 🌱 KRUSHI SEVA KENDRA — PREMIUM INTERACTIONS v2.0
 * Count-up, scroll reveal, navbar blur, WhatsApp, ripple, smooth scroll
 */

(function () {
  'use strict';

  /* ── Navbar Scroll Blur ──────────────────────────────────────── */
  var navbar = document.querySelector('.navbar-krushi');
  if (navbar) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 30) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    }, { passive: true });
  }

  /* ── Scroll-to-Top Button ────────────────────────────────────── */
  var scrollBtn = document.getElementById('scrollTopBtn');
  if (scrollBtn) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 350) {
        scrollBtn.classList.add('show');
      } else {
        scrollBtn.classList.remove('show');
      }
    }, { passive: true });
    scrollBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ── Count-Up Animation ──────────────────────────────────────── */
  function animateCountUp(el) {
    var target = parseFloat(el.getAttribute('data-count') || el.textContent.replace(/[^0-9.]/g, ''));
    var prefix = el.getAttribute('data-prefix') || '';
    var suffix = el.getAttribute('data-suffix') || '';
    var duration = 1800;
    var startTime = null;
    var isFloat = target % 1 !== 0;

    function step(timestamp) {
      if (!startTime) startTime = timestamp;
      var progress = Math.min((timestamp - startTime) / duration, 1);
      var ease = 1 - Math.pow(1 - progress, 3);
      var value = target * ease;
      el.textContent = prefix + (isFloat ? value.toFixed(1) : Math.floor(value).toLocaleString('en-IN')) + suffix;
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  /* ── Scroll Reveal ───────────────────────────────────────────── */
  function initScrollReveal() {
    var elements = document.querySelectorAll('.reveal');
    if (!elements.length) return;

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          // Count-up trigger
          var countEls = entry.target.querySelectorAll('[data-count]');
          countEls.forEach(animateCountUp);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    elements.forEach(function (el) { observer.observe(el); });
  }

  /* ── KPI Count-up (page load) ────────────────────────────────── */
  function initKPICountUp() {
    var kpiVals = document.querySelectorAll('.kpi-value[data-count], .hero-stat-number[data-count]');
    if (!kpiVals.length) return;

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCountUp(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.3 });

    kpiVals.forEach(function (el) { observer.observe(el); });
  }

  /* ── Ripple Effect on Buttons ────────────────────────────────── */
  function initRipple() {
    document.querySelectorAll('.btn-krushi, .btn-harvest, .btn-krushi-outline').forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        var rect = btn.getBoundingClientRect();
        var span = document.createElement('span');
        var size = Math.max(rect.width, rect.height);
        span.style.cssText = 'position:absolute;border-radius:50%;background:rgba(255,255,255,0.3);width:' + size + 'px;height:' + size + 'px;top:' + (e.clientY - rect.top - size / 2) + 'px;left:' + (e.clientX - rect.left - size / 2) + 'px;transform:scale(0);animation:ripple-anim 0.6s linear;pointer-events:none;';
        btn.style.position = 'relative';
        btn.style.overflow = 'hidden';
        btn.appendChild(span);
        setTimeout(function () { span.remove(); }, 700);
      });
    });
  }

  /* ── Wishlist Toggle ─────────────────────────────────────────── */
  function initWishlist() {
    document.querySelectorAll('.product-wishlist-btn').forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        btn.classList.toggle('active');
        var icon = btn.querySelector('i');
        if (icon) {
          if (btn.classList.contains('active')) {
            icon.classList.remove('bi-heart');
            icon.classList.add('bi-heart-fill');
          } else {
            icon.classList.remove('bi-heart-fill');
            icon.classList.add('bi-heart');
          }
        }
      });
    });
  }

  /* ── Dark Mode Toggle ────────────────────────────────────────── */
  function initDarkMode() {
    var btn = document.getElementById('themeToggleBtn');
    if (!btn) return;
    var savedTheme = localStorage.getItem('krushi-theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateToggleIcon(btn, savedTheme);

    btn.addEventListener('click', function () {
      var current = document.documentElement.getAttribute('data-theme');
      var next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('krushi-theme', next);
      updateToggleIcon(btn, next);
    });
  }

  function updateToggleIcon(btn, theme) {
    var icon = btn.querySelector('i');
    if (!icon) return;
    if (theme === 'dark') {
      icon.className = 'bi bi-sun-fill';
      btn.title = 'Switch to Light Mode';
    } else {
      icon.className = 'bi bi-moon-stars-fill';
      btn.title = 'Switch to Dark Mode';
    }
  }

  /* ── Hero Video Fallback ─────────────────────────────────────── */
  function initHeroVideo() {
    var vid = document.querySelector('.hero-farm-video');
    var imgBg = document.getElementById('heroFarmImgBg');
    if (!vid) return;

    vid.addEventListener('canplay', function () {
      if (imgBg) imgBg.style.display = 'none';
    });
    vid.addEventListener('error', function () {
      vid.style.display = 'none';
      if (imgBg) imgBg.style.display = 'block';
    });
    setTimeout(function () {
      if (vid.readyState < 3 && vid.paused) {
        vid.style.display = 'none';
        if (imgBg) imgBg.style.display = 'block';
      }
    }, 3000);
  }

  /* ── Newsletter Form ─────────────────────────────────────────── */
  function initNewsletter() {
    var form = document.getElementById('newsletterForm');
    if (!form) return;
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var inp = form.querySelector('input');
      if (inp && inp.value.trim()) {
        inp.value = '';
        var btn = form.querySelector('button');
        if (btn) {
          var orig = btn.innerHTML;
          btn.innerHTML = '<i class="bi bi-check-lg"></i> ✓';
          btn.style.background = '#16a34a';
          setTimeout(function () { btn.innerHTML = orig; btn.style.background = ''; }, 2500);
        }
      }
    });
  }

  /* ── Live Search ─────────────────────────────────────────────── */
  function initLiveSearch() {
    var input = document.getElementById('globalSearchInput');
    var results = document.getElementById('searchDropdownResults');
    if (!input || !results) return;

    var debounceTimer;
    input.addEventListener('input', function () {
      clearTimeout(debounceTimer);
      var query = input.value.trim();
      if (query.length < 2) { results.style.display = 'none'; return; }
      debounceTimer = setTimeout(function () {
        fetch('/api/products/search?keyword=' + encodeURIComponent(query))
          .then(function (r) { return r.json(); })
          .then(function (data) {
            if (!data || !data.length) { results.style.display = 'none'; return; }
            var html = data.slice(0, 8).map(function (p) {
              return '<a href="/products/' + p.id + '" class="d-flex align-items-center gap-2 px-3 py-2 text-decoration-none text-dark border-bottom" style="font-size:0.85rem;">' +
                '<i class="bi bi-box-seam text-success"></i>' +
                '<span>' + p.name + '</span>' +
                '<span class="ms-auto text-success fw-bold">₹' + p.price + '</span>' +
                '</a>';
            }).join('');
            results.innerHTML = html;
            results.style.display = 'block';
          }).catch(function () { results.style.display = 'none'; });
      }, 320);
    });

    document.addEventListener('click', function (e) {
      if (!input.contains(e.target) && !results.contains(e.target)) {
        results.style.display = 'none';
      }
    });
  }

  /* ── Tooltip Bootstrap Init ──────────────────────────────────── */
  function initTooltips() {
    if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
      document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(function (el) {
        new bootstrap.Tooltip(el, { trigger: 'hover' });
      });
    }
  }

  /* ── Smooth Dropdown Animation ───────────────────────────────── */
  function initDropdownAnimations() {
    document.querySelectorAll('.dropdown').forEach(function (dd) {
      var menu = dd.querySelector('.dropdown-menu');
      if (!menu) return;
      menu.style.animation = '';
      dd.addEventListener('show.bs.dropdown', function () {
        menu.style.animation = 'slideDown 0.2s ease both';
      });
    });
  }

  /* ── Page Load Animation for Cards ──────────────────────────── */
  function initCardAnimations() {
    var cards = document.querySelectorAll('.product-card, .kpi-card, .category-pill-card, .dash-card');
    cards.forEach(function (card, i) {
      if (!card.closest('.reveal')) {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.45s ease, transform 0.45s ease';
        card.style.transitionDelay = Math.min(i * 0.06, 0.5) + 's';
        setTimeout(function () {
          card.style.opacity = '1';
          card.style.transform = 'translateY(0)';
        }, 80);
      }
    });
  }

  /* ── Init All ────────────────────────────────────────────────── */
  document.addEventListener('DOMContentLoaded', function () {
    initScrollReveal();
    initKPICountUp();
    initRipple();
    initWishlist();
    initDarkMode();
    initHeroVideo();
    initNewsletter();
    initLiveSearch();
    initTooltips();
    initDropdownAnimations();
    initCardAnimations();
  });

})();
