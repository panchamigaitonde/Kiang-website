/* Kiang Collective — site behaviour */
(function () {
  // Navigation: transparent over a hero, solid after scrolling; mobile menu
  var nav = document.getElementById('siteNav');
  var hero = document.querySelector('.hero');
  var toggle = document.querySelector('.nav-toggle');
  if (nav && hero) {
    var update = function () {
      if (nav.classList.contains('open')) return;
      if (window.scrollY < hero.offsetHeight - 90) nav.classList.add('over-hero');
      else nav.classList.remove('over-hero');
    };
    update();
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
  }
  if (nav && toggle) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.textContent = open ? 'Close' : 'Menu';
      if (open) nav.classList.remove('over-hero');
      else window.dispatchEvent(new Event('scroll'));
    });
  }

  // Fade sections in as they scroll into view
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && els.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -6% 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('in'); });
  }

  // Cookie consent for Google Analytics
  var banner = document.getElementById('cookieBanner');
  var store = {
    get: function () { try { return localStorage.getItem('kiang_cookie_consent'); } catch (e) { return null; } },
    set: function (v) { try { localStorage.setItem('kiang_cookie_consent', v); } catch (e) {} }
  };
  var consent = store.get();
  if (consent === 'accepted' && window.gtag) {
    gtag('consent', 'update', { analytics_storage: 'granted' });
  } else if (!consent && banner) {
    setTimeout(function () { banner.classList.add('visible'); }, 1400);
  }
  document.querySelectorAll('[data-cookie]').forEach(function (b) {
    b.addEventListener('click', function () {
      var v = b.getAttribute('data-cookie');
      store.set(v);
      if (v === 'accepted' && window.gtag) gtag('consent', 'update', { analytics_storage: 'granted' });
      if (banner) banner.classList.remove('visible');
    });
  });

  // Contact page: tabs between film and expedition enquiries
  var tabs = document.querySelectorAll('.tab');
  if (tabs.length) {
    var show = function (id) {
      tabs.forEach(function (t) {
        var on = t.getAttribute('aria-controls') === id;
        t.setAttribute('aria-selected', on ? 'true' : 'false');
        t.tabIndex = on ? 0 : -1;
        document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
      });
    };
    tabs.forEach(function (t) {
      t.addEventListener('click', function () { show(t.getAttribute('aria-controls')); });
    });
    if (location.hash === '#expeditions') show('panel-expeditions');
  }

  // Forms: send to Formspree without leaving the page
  document.querySelectorAll('form[data-ajax]').forEach(function (form) {
    var status = form.querySelector('.form-status');
    var btn = form.querySelector('button[type="submit"]');
    var label = btn ? btn.textContent : '';
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      status.className = 'form-status';
      btn.disabled = true; btn.textContent = 'Sending…';
      var fail = function (msg) {
        status.textContent = msg || 'Something went wrong. Please try again, or email us directly.';
        status.className = 'form-status show error';
        btn.disabled = false; btn.textContent = label;
      };
      fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
        .then(function (r) {
          if (r.ok) {
            form.reset();
            status.textContent = 'Thank you. Your message has reached us, and we will reply within two working days.';
            status.className = 'form-status show';
            btn.textContent = 'Sent';
          } else {
            r.json().then(function (d) {
              fail(d && d.errors ? d.errors.map(function (x) { return x.message; }).join(', ') : null);
            }).catch(function () { fail(); });
          }
        })
        .catch(function () { fail('Could not send. Please check your connection, or email us directly.'); });
    });
  });
})();
