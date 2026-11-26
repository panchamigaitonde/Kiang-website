"""Shared pieces for every Kiang page: head, navigation, footer, helpers."""
import html, json

SITE = "https://kiang.in"
FORMSPREE = "https://formspree.io/f/xykvqnge"
EMAILS = ["panchami@kiang.in", "pradeep@kiang.in"]
PHONE_DISPLAY = "+91 94800 56287"
PHONE_LINK = "+919480056287"
WHATSAPP = "https://wa.me/919480056287"
INSTAGRAM = "https://www.instagram.com/kiangcollective/"
GOOGLE_REVIEWS = "https://share.google/rk4XKNHByz2eApeV1"

# Spiti price in US dollars. Set to a number (e.g. 1750) to show it on the site.
SPITI_USD = 1620
RAJASTHAN_USD = 6029

NAV = [("films.html", "Films"), ("expeditions.html", "Expeditions"),
       ("journal.html", "Journal"), ("about.html", "About")]

e = html.escape


def pic(name, alt, cls="", lazy=True, style=""):
    """<picture> with webp + jpg fallback for files in /images."""
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    c = f' class="{cls}"' if cls else ""
    s = f' style="{style}"' if style else ""
    return (f'<picture><source srcset="images/{name}.webp" type="image/webp">'
            f'<img src="images/{name}.jpg" alt="{e(alt)}"{c}{s}{load}></picture>')


def yt_thumb(vid, alt):
    return (f'<img src="https://img.youtube.com/vi/{vid}/maxresdefault.jpg" alt="{e(alt)}" loading="lazy" decoding="async" '
            f'onerror="this.onerror=null;this.src=\'https://img.youtube.com/vi/{vid}/hqdefault.jpg\'">')


ORG_LD = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Kiang Collective",
    "legalName": "Kiang Collective LLP",
    "url": SITE,
    "logo": SITE + "/images/kiang-logo.png",
    "description": "Kiang Collective works on wildlife films with broadcasters and production houses, and leads small wildlife expeditions.",
    "foundingDate": "2024",
    "founder": [{"@type": "Person", "name": "Panchami Gaitonde"}, {"@type": "Person", "name": "Pradeep Hegde"}],
    "address": {"@type": "PostalAddress", "addressLocality": "Bengaluru", "addressCountry": "IN"},
    "email": EMAILS[0],
    "telephone": PHONE_LINK,
    "sameAs": [INSTAGRAM],
}


def head(title, description, path, image="images/landing-hero-poster.jpg", image_alt="Kiang Collective", extra_ld=None):
    url = SITE + "/" + ("" if path == "index.html" else path)
    lds = [ORG_LD] + (extra_ld or [])
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-3YN0VKF84B"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('consent', 'default', {{ analytics_storage: 'denied', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied' }});
  gtag('js', new Date());
  gtag('config', 'G-3YN0VKF84B', {{ anonymize_ip: true }});
</script>
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0D0E0C">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Kiang Collective">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/{image}">
<meta property="og:image:alt" content="{e(image_alt)}">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(description)}">
<meta name="twitter:image" content="{SITE}/{image}">
<link rel="icon" type="image/x-icon" href="favicon.ico">
<link rel="icon" type="image/png" sizes="192x192" href="images/favicon-192.png">
<link rel="apple-touch-icon" href="images/favicon-512.png">
<link rel="preload" href="assets/fonts/barlow-condensed-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/barlow-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/site.css?v=6">
{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def nav(current, over_hero=True):
    cur = ' class="current" aria-current="page"'
    links = "".join('<a href="%s"%s>%s</a>' % (h, cur if h == current else "", t) for h, t in NAV)
    cc = ' current' if current == 'contact.html' else ''
    return f"""<nav class="nav{' over-hero' if over_hero else ''}" id="siteNav" aria-label="Main">
  <div class="nav-inner">
    <a href="index.html" class="nav-brand" aria-label="Kiang Collective, home"><img src="images/kiang-logo-white.png" alt="Kiang Collective" width="89" height="38"></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="navLinks">Menu</button>
    <div class="nav-links" id="navLinks">{links}<a href="contact.html" class="contact{cc}"{' aria-current="page"' if cc else ''}>Contact</a></div>
  </div>
</nav>
<main id="main">
"""


def footer():
    mails = "".join(f'<a href="mailto:{m}">{m}</a>' for m in EMAILS)
    return f"""</main>
<footer class="site-footer">
  <div class="footer-cta">
    <div>
      <div class="display">Get in touch</div>
      <div class="footer-actions">
        <a class="btn solid" href="contact.html#films">Film enquiries</a>
        <a class="btn" href="contact.html#expeditions">Expedition enquiries</a>
      </div>
    </div>
    <div class="footer-info">
      <img src="images/kiang-logo-white.png" alt="Kiang Collective" width="112" height="48">
      {mails}
      <a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a>
      <span>Bengaluru, India</span>
      <div class="footer-social">
        <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a>
        <a href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp</a>
        <a href="{GOOGLE_REVIEWS}" target="_blank" rel="noopener">Google reviews</a>
      </div>
    </div>
  </div>
  <div class="footer-base"><span>© 2026 Kiang Collective LLP</span><span>Films · Expeditions · Journal</span></div>
</footer>
<div class="cookie" id="cookieBanner" role="region" aria-label="Cookie notice">
  <div class="cookie-inner">
    <p>We use analytics cookies to see which pages and stories people read. Nothing else.</p>
    <div class="cookie-actions">
      <button class="btn" type="button" data-cookie="declined">Decline</button>
      <button class="btn solid" type="button" data-cookie="accepted">Accept</button>
    </div>
  </div>
</div>
<script src="assets/site.js?v=1"></script>
</body>
</html>
"""


def page_hero(title, sub, image, alt, eyebrow=""):
    eb = f'<div class="eyebrow">{eyebrow}</div>' if eyebrow else ""
    return f"""<section class="hero short">
  {pic(image, alt, "hero-media", lazy=False)}
  <div class="hero-shade"></div>
  <div class="hero-content">{eb}<h1>{title}</h1>{f'<p class="hero-sub">{sub}</p>' if sub else ''}</div>
</section>
"""
