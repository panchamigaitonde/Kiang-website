"""Builds the Kiang Collective site into ../site. Run: python3 build.py"""
import os
from common import *
from data import *
import trips

OUT = os.path.join(os.path.dirname(__file__), "..")


def write(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)



CREDIT_NAMES = [("national-geographic", "National Geographic"), ("terra-mater", "Terra Mater"), ("nhk", "NHK"),
                ("roundglass-sustain", "Roundglass Sustain"), ("discovery", "Discovery"), ("animal-planet", "Animal Planet")]


def credit_logos():
    """Show a logo from images/logos/<slug>.svg or .png when it exists; otherwise the name as text."""
    out = []
    for slug, name in CREDIT_NAMES:
        f = next((f"images/logos/{slug}.{x}" for x in ("svg", "png") if os.path.exists(os.path.join(OUT, f"images/logos/{slug}.{x}"))), None)
        out.append(f'<img class="credit-logo logo-{slug}" src="{f}" alt="{e(name)}">' if f else f"<span>{e(name)}</span>")
    return "".join(out)


def credits_html(credits, kiang=""):
    parts = [f"<b>{e(p)}</b> — {e(r)}" for p, r in credits]
    if kiang:
        parts.append(f"<b>Kiang Collective</b> — {e(kiang)}")
    return "<br>".join(parts)


def spiti_price():
    return f"US$ {SPITI_USD:,}" if SPITI_USD else "Price on request"


# ───────────────────────── HOME ─────────────────────────
def home():
    raptors, tamil = FEATURES[0], FEATURES[1]
    wild_india = UPCOMING[0]
    cards = f"""
      <a class="film-card" href="https://youtu.be/{raptors['yt']}" target="_blank" rel="noopener">
        <div class="thumb">{yt_thumb(raptors['yt'], raptors['title'])}<span class="play" aria-hidden="true"></span></div>
        <span class="meta">{raptors['by']} · {raptors['year']}</span>
        <h3>{raptors['title']}</h3>
        <div class="credit">{credits_html(raptors['credits'])}</div>
      </a>
      <a class="film-card" href="films.html">
        <div class="thumb text-only"><span>Terra Mater<br>2026</span></div>
        <span class="meta">{wild_india['by']} · {wild_india['year']} · Upcoming</span>
        <h3>{wild_india['title']}</h3>
        <div class="credit">{credits_html(wild_india['credits'], wild_india['kiang'])}</div>
      </a>
      <a class="film-card" href="https://youtu.be/{tamil['yt']}" target="_blank" rel="noopener">
        <div class="thumb">{yt_thumb(tamil['yt'], tamil['title'])}<span class="play" aria-hidden="true"></span></div>
        <span class="meta">{tamil['by']} · {tamil['year']}</span>
        <h3>{tamil['title']}</h3>
        <div class="credit">{credits_html(tamil['credits'])}</div>
      </a>"""
    s = STORIES[0]
    body = f"""
<header class="hero">
  <video class="hero-media" autoplay muted loop playsinline preload="auto" poster="images/landing-hero-poster.jpg" aria-label="Scenes from the field: waterfalls, a leopard, misty forests and Himalayan mountains">
    <source src="images/landing-hero.webm" type="video/webm">
    <source src="images/landing-hero.mp4" type="video/mp4">
  </video>
  <div class="hero-shade"></div>
  <div class="hero-content hero-center">
    <div class="eyebrow">India · Est. 2024</div>
    <h1 class="wordmark"><span class="wm-big">Kiang</span><span class="wm-small">Collective</span></h1>
    <span class="wm-rule" aria-hidden="true"></span>
    <p class="wm-tag">Wildlife films and expeditions</p>
  </div>
</header>

<div class="wrap">
  <section class="doors reveal" aria-label="Films and expeditions">
    <a class="door" href="films.html">
      <div class="door-img">{pic("landscape-peacock", "An Indian peacock in full display", style="object-position:58% 70%")}</div>
      <div class="door-body">
        <div class="eyebrow">For broadcasters and production houses</div>
        <div class="door-title">Kiang Films</div>
        <p>Camera, research, line production and field production for wildlife films and documentaries.</p>
        <span class="link">See the work →</span>
      </div>
    </a>
    <a class="door" href="expeditions.html">
      <div class="door-img">{pic("landscape-snow-leopard", "Snow leopard on a rocky slope in winter Spiti", style="object-position:60% 40%")}</div>
      <div class="door-body">
        <div class="eyebrow">For wildlife enthusiasts</div>
        <div class="door-title">Kiang Expeditions</div>
        <p>Wildlife expeditions led by Panchami and Pradeep.</p>
        <span class="link">See expeditions →</span>
      </div>
    </a>
  </section>

  <section class="credits-strip reveal" aria-label="Who our crew has worked with">
    <div class="eyebrow">Our crew has worked with</div>
    <div class="credits-names">
      {credit_logos()}
    </div>
  </section>

  <section class="section reveal">
    <div class="section-head">
      <div><span class="eyebrow">Recent work</span><h2>Films</h2></div>
      <a class="link" href="films.html">All films and credits →</a>
    </div>
    <div class="card-grid">{cards}
    </div>
  </section>
</div>

<section class="band reveal" aria-labelledby="exp-h">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow">Expeditions</span><h2 id="exp-h">Travel with us</h2></div>
      <a class="link" href="expeditions.html">All expeditions →</a>
    </div>
    {trip_row("expedition-spiti-2027.html", "landscape-snow-leopard", "Snow leopard in Spiti",
              "Spiti Valley · 4,150 m · 22–31 Jan 2027", "Ghost of the Himalayas",
              "In search of the snow leopard · 10 days · 6 guests", spiti_price(), "per person", None)}
  </div>
</section>

<div class="wrap">
  <section class="section reveal">
    <div class="split">
      <div>
        <span class="eyebrow">About</span>
        <h2 style="margin:14px 0 24px">Who we are</h2>
        <div class="prose"><p>Kiang Collective is Panchami Gaitonde and Pradeep Hegde. We first worked together in Ladakh, and started Kiang in 2024. Our first project was a snow leopard expedition there.</p></div>
        <p style="margin-top:28px"><a class="link" href="about.html">More about us →</a></p>
      </div>
      <div class="people">
        <figure class="person" style="margin:0">{pic("portrait-panchami", "Panchami Gaitonde")}<figcaption><div class="person-name">Panchami Gaitonde</div><div class="person-role">Co-founder · Camera, field producer, expedition leader</div></figcaption></figure>
        <figure class="person" style="margin:0">{pic("portrait-pradeep", "Pradeep Hegde")}<figcaption><div class="person-name">Pradeep Hegde</div><div class="person-role">Co-founder · Producer, cinematographer</div></figcaption></figure>
      </div>
    </div>
  </section>

  <section class="section reveal">
    <a class="journal-feature" href="{s['slug']}.html">
      {pic(s['image'], s['alt'])}
      <div>
        <span class="eyebrow">From the journal · {s['place']}</span>
        <div class="journal-title">{s['title']}</div>
        <p class="lead" style="margin:0 0 24px">Tiny green lights rose from under the coffee plants, reached the trees, and began to pulse together, for hours.</p>
        <span class="link">Read the story →</span>
      </div>
    </a>
  </section>
</div>
"""
    write("index.html", head("Kiang Collective — Wildlife Films and Expeditions",
                             "Kiang Collective is Panchami Gaitonde and Pradeep Hegde: camera, research and production for wildlife films, and small wildlife expeditions led by us.",
                             "index.html", image_alt="A leopard in dry golden grass")
          + nav("index.html") + body + footer())


def trip_row(href, img, alt, meta, title, sub, price, price_note, badge):
    b = f'<span class="badge closed">{badge}</span>' if badge else ""
    pn = f"<small>{price_note}</small>" if price_note and price != "Price on request" else ""
    return f"""<a class="trip-row" href="{href}">
      {pic(img, alt)}
      <div><span class="meta">{meta}</span><div class="trip-title">{title}</div><div class="muted">{sub}</div></div>
      <div class="trip-side">{b}<div class="price">{price}{pn}</div><span class="link">Details →</span></div>
    </a>"""


# ───────────────────────── FILMS ─────────────────────────
def films():
    up = "".join(f"""
      <div class="film-row">
        <div class="thumb text-only"><span>{e(f['by'])}<br>{f['year'] or '&nbsp;'}</span></div>
        <div>
          <span class="meta">{e(f['by'])}{' · ' + f['year'] if f['year'] else ''} · {e(f['status'])}</span>
          <h3>{e(f['title'])}</h3>
          <div class="credit">{credits_html(f['credits'], f['kiang'])}</div>
        </div>
      </div>""" for f in UPCOMING)

    def feat(f):
        by = (f['by'] + " · " if f['by'] else "") + f['year']
        note = f'<p class="note">{e(f["note"])}</p>' if f['note'] else ""
        inner = f"""
          <span class="meta">{e(by)}</span>
          <h3>{e(f['title'])}</h3>
          <div class="credit">{credits_html(f['credits'])}</div>{note}"""
        if f['yt']:
            return f"""
      <a class="film-row" href="https://youtu.be/{f['yt']}" target="_blank" rel="noopener">
        <div class="thumb">{yt_thumb(f['yt'], f['title'])}<span class="play" aria-hidden="true"></span></div>
        <div>{inner}</div>
      </a>"""
        return f"""
      <div class="film-row">
        <div class="thumb" style="background:#000">{pic(f['poster'], f['title'], style="object-fit:contain")}</div>
        <div>{inner}</div>
      </div>"""
    feats = "".join(feat(f) for f in FEATURES)
    shorts = "".join(f"""
      <a href="https://youtu.be/{f['yt']}" target="_blank" rel="noopener">
        <div class="thumb">{yt_thumb(f['yt'], f['title'])}<span class="play" aria-hidden="true"></span></div>
        <span class="meta">{e(f['by'])} · {f['year']}</span>
        <h3>{e(f['title'])}</h3>
        <div class="credit">{e(f['credit'])}</div>
      </a>""" for f in SHORTS)
    body = page_hero("Films", "Camera, research and production for wildlife films",
                     "landscape-peacock", "An Indian peacock in full display", "Kiang Films") + f"""
<div class="wrap">
  <section class="section reveal">
    <p class="lead">These are the films our crew has worked on, and the role each of us played. Kiang Collective was set up in 2024; credits for earlier films are in our own names.</p>
  </section>

  <section class="section reveal" aria-labelledby="up-h">
    <div class="section-head"><div><span class="eyebrow">Coming in 2026</span><h2 id="up-h">Upcoming</h2></div></div>
    <div class="film-list">{up}
    </div>
  </section>

  <section class="section reveal" aria-labelledby="ft-h">
    <div class="section-head"><div><span class="eyebrow">Broadcast and theatrical</span><h2 id="ft-h">Feature-length</h2></div></div>
    <div class="film-list">{feats}
    </div>
  </section>

  <section class="section reveal" aria-labelledby="sh-h">
    <div class="section-head"><div><span class="eyebrow">Roundglass Sustain and independent</span><h2 id="sh-h">Short films</h2></div></div>
    <div class="short-grid">{shorts}
    </div>
  </section>
</div>
"""
    items = [{"@type": "ListItem", "position": i + 1, "item": {"@type": "Movie", "name": f["title"]}}
             for i, f in enumerate(UPCOMING[:2] + FEATURES + SHORTS)]
    ld = {"@context": "https://schema.org", "@type": "ItemList", "name": "Films by the Kiang Collective crew", "itemListElement": items}
    write("films.html", head("Films — Wildlife Documentaries | Kiang Collective",
                             "Wildlife films our crew has worked on, with credits: Terra Mater, NHK, Roundglass Sustain, National Geographic, Discovery and more.",
                             "films.html", "images/landscape-peacock.jpg", "An Indian peacock in full display", [ld])
          + nav("films.html") + body + footer())


# ───────────────────────── EXPEDITIONS ─────────────────────────
def expeditions():
    body = page_hero("Expeditions", "Six guests per trip, led by Panchami and Pradeep",
                     "landscape-snow-leopard", "A snow leopard in winter Spiti", "Kiang Expeditions") + f"""
<div class="wrap">
  <section class="section reveal">
    <p class="lead">Six guests per trip, led by Panchami and Pradeep, with local naturalists who know these valleys.</p>
  </section>

  <section class="section reveal" aria-labelledby="dep-h">
    <div class="section-head"><div><span class="eyebrow">Departures</span><h2 id="dep-h">Expeditions</h2></div></div>
    <div>
      {trip_row("expedition-spiti-2027.html", "landscape-snow-leopard", "Snow leopard in Spiti",
                "Spiti Valley · 4,150 m · 22–31 Jan 2027", "Ghost of the Himalayas",
                "In search of the snow leopard · 10 days, 9 nights · 6 guests", spiti_price(), "per person", None)}
      {trip_row("expedition-rajasthan-2026.html", "rajasthan-bustard", "Great Indian Bustard in Rajasthan",
                "Rajasthan · Wetland, grassland, desert · 8–16 Dec 2026", "The Land of Bustards",
                "A winter birding tour across three habitats · 9 days, 8 nights", f"US$ {RAJASTHAN_USD:,}", "per person", "Closed")}
    </div>
  </section>

  <section class="section reveal" aria-labelledby="past-h">
    <div class="split">
      <div><span class="eyebrow">Past journeys</span><h2 id="past-h" style="margin-top:14px">Where we've been</h2></div>
      <div>
        <div class="terms">
          <div><div class="t">Ladakh</div><div class="d">Snow leopard expeditions, two winters. Kiang's first project, in 2024.</div></div>
        </div>
        <p style="margin-top:32px"><a class="link" href="{GOOGLE_REVIEWS}" target="_blank" rel="noopener">Read reviews from past guests on Google →</a></p>
      </div>
    </div>
  </section>
</div>
"""
    write("expeditions.html", head("Expeditions — Snow Leopard and Wildlife Trips | Kiang Collective",
                                   "Small wildlife expeditions, six guests per trip, led by Panchami Gaitonde and Pradeep Hegde. Snow leopards in Spiti, January 2027.",
                                   "expeditions.html", "images/landscape-snow-leopard.jpg", "A snow leopard in winter Spiti")
          + nav("expeditions.html") + body + footer())


# ───────────────────────── ABOUT ─────────────────────────
def about():
    body = page_hero("About Kiang", "", "landscape-enquire-banner",
                     "A snow-dusted high-altitude valley under a clear winter sky", "Kiang Collective LLP · Bengaluru") + f"""
<div class="wrap">
  <section class="section reveal">
    <div class="split">
      <div><span class="eyebrow">Our story</span></div>
      <div class="prose" style="max-width:720px">
        <p>Kiang Collective grew out of years we each spent filming, leading expeditions and living in the outdoors. We first worked together in Ladakh, and the Himalaya has stayed at the centre of our work ever since.</p>
        <p>We started Kiang in 2024. Our first project was a snow leopard expedition in Ladakh for a small group of wildlife enthusiasts. Since then we've filmed across India and abroad, and led journeys in the Himalaya.</p>
        <p>Our work has two sides. On films, we work with broadcasters and production houses: behind the camera, in research, and in line and field production. On expeditions, we take small groups into the same kinds of places, with time to watch, wait and learn from the people who live there.</p>
      </div>
    </div>
  </section>

  <section class="section reveal" aria-label="Founders">
    <article class="bio">
      {pic("portrait-panchami", "Panchami Gaitonde")}
      <div>
        <h2 class="person-name">Panchami Gaitonde</h2>
        <div class="person-role">Co-founder · Camera, field producer, expedition leader</div>
        <div class="prose">
          <p>Panchami spent years in India's trekking and outdoor-education world, leading journeys built on the idea that the best learning happens in mountains, forests and water.</p>
          <p>She has worked as a line producer, field producer and second camera on films for broadcasters including National Geographic and Terra Mater. At Kiang she leads story and research, and designs and leads the expeditions. She is now developing her own documentaries as a director.</p>
        </div>
      </div>
    </article>
    <article class="bio">
      {pic("portrait-pradeep", "Pradeep Hegde")}
      <div>
        <h2 class="person-name">Pradeep Hegde</h2>
        <div class="person-role">Co-founder · Producer, cinematographer</div>
        <div class="prose">
          <p>Pradeep has spent more than a decade filming wildlife in remote and difficult terrain. His work, built on long observational shoots, behaviour sequences and camera traps, has appeared with National Geographic, Discovery, Terra Mater, NHK and Roundglass Sustain.</p>
          <p>At Kiang he leads production and camera work.</p>
        </div>
      </div>
    </article>
  </section>

  <section class="section reveal" aria-labelledby="col-h">
    <div class="section-head"><div><span class="eyebrow">We work with</span><h2 id="col-h">Collaborators</h2></div></div>
    <div class="collab">
      <article>
        {pic("portrait-dheeraj", "Dheeraj Aithal")}
        <div class="person-name">Dheeraj Aithal</div>
        <div class="person-role">Cinematographer, drone pilot</div>
        <p>Dheeraj is a cinematographer and drone pilot with a background in natural history filmmaking. His work has taken him across remote landscapes in India, often in difficult field conditions. With Kiang, he leads aerial cinematography.</p>
      </article>
      <article>
        {pic("portrait-george", "George Thengummoottil")}
        <div class="person-name">George Thengummoottil</div>
        <div class="person-role">Editor</div>
        <p>George is a documentary editor and founder of Moundain Films, focused on natural history and wildlife storytelling. His recent work includes <em>The Dooars World</em>.</p>
      </article>
    </div>
  </section>
</div>
"""
    write("about.html", head("About — Panchami Gaitonde and Pradeep Hegde | Kiang Collective",
                             "Kiang Collective is Panchami Gaitonde and Pradeep Hegde, wildlife filmmakers and expedition leaders based in Bengaluru.",
                             "about.html", "images/landscape-enquire-banner.jpg", "A snow-dusted Himalayan valley")
          + nav("about.html") + body + footer())


# ───────────────────────── CONTACT ─────────────────────────
def contact():
    body = page_hero("Get in touch", "We reply within two working days", "landscape-ftl",
                     "A fan-throated lizard displaying on the Chalkewadi plateau", "Contact") + f"""
<div class="wrap">
  <section class="section reveal">
    <div class="split contact-split">
      <div>
        <div class="tabs" role="tablist" aria-label="Type of enquiry">
          <button class="tab" role="tab" id="tab-films" aria-controls="panel-films" aria-selected="true">Films</button>
          <button class="tab" role="tab" id="tab-exp" aria-controls="panel-expeditions" aria-selected="false" tabindex="-1">Expeditions</button>
        </div>

        <div id="panel-films" role="tabpanel" aria-labelledby="tab-films">
          <form action="{FORMSPREE}" method="POST" data-ajax>
            <input type="hidden" name="_subject" value="Film enquiry from kiang.in">
            <input type="hidden" name="enquiry" value="Film">
            <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
            <div class="form-grid">
              <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" required autocomplete="name"></div>
              <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" required autocomplete="email"></div>
              <div class="field"><label for="f-company">Company or broadcaster</label><input id="f-company" name="company" autocomplete="organization"></div>
              <div class="field"><label for="f-type">What do you need?</label>
                <select id="f-type" name="project_type">
                  <option>Camera crew</option><option>Research</option><option>Line or field production</option><option>Something else</option>
                </select></div>
              <div class="field"><label for="f-where">Locations</label><input id="f-where" name="locations" placeholder="Where you want to film"></div>
              <div class="field"><label for="f-when">Dates</label><input id="f-when" name="dates" placeholder="Approximate shoot dates"></div>
              <div class="field full"><label for="f-msg">About the project</label><textarea id="f-msg" name="message" required placeholder="The story, the species, the timeline."></textarea></div>
            </div>
            <p style="margin-top:32px"><button class="btn solid" type="submit">Send film enquiry</button></p>
            <p class="form-status" role="status" aria-live="polite"></p>
          </form>
        </div>

        <div id="panel-expeditions" role="tabpanel" aria-labelledby="tab-exp" hidden>
          <form action="{FORMSPREE}" method="POST" data-ajax>
            <input type="hidden" name="_subject" value="Expedition enquiry from kiang.in">
            <input type="hidden" name="enquiry" value="Expedition">
            <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
            <div class="form-grid">
              <div class="field"><label for="x-name">Your name</label><input id="x-name" name="name" required autocomplete="name"></div>
              <div class="field"><label for="x-email">Email</label><input id="x-email" name="email" type="email" required autocomplete="email"></div>
              <div class="field"><label for="x-phone">Phone or WhatsApp</label><input id="x-phone" name="phone" type="tel" autocomplete="tel"></div>
              <div class="field"><label for="x-trip">Which expedition?</label>
                <select id="x-trip" name="expedition">
                  <option>Ghost of the Himalayas — Spiti, Jan 2027</option><option>Future trips</option>
                </select></div>
              <div class="field"><label for="x-people">Number of people</label><input id="x-people" name="people" inputmode="numeric"></div>
              <div class="field"><label for="x-country">Travelling from</label><input id="x-country" name="country" placeholder="City and country"></div>
              <div class="field full"><label for="x-msg">Message</label><textarea id="x-msg" name="message" required placeholder="Anything we should know: experience at altitude, photography, dates."></textarea></div>
            </div>
            <p style="margin-top:32px"><button class="btn solid" type="submit">Send expedition enquiry</button></p>
            <p class="form-status" role="status" aria-live="polite"></p>
          </form>
        </div>
      </div>

      <aside class="contact-side" aria-label="Contact details">
        <div><div class="label">Email</div><div class="value"><a href="mailto:{EMAILS[0]}">{EMAILS[0]}</a><br><a href="mailto:{EMAILS[1]}">{EMAILS[1]}</a></div></div>
        <div><div class="label">Phone and WhatsApp</div><div class="value"><a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a></div></div>
        <div><div class="label">Based in</div><div class="value">Bengaluru, India</div></div>
        <div><div class="label">Elsewhere</div><div class="value"><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a><br><a href="{GOOGLE_REVIEWS}" target="_blank" rel="noopener">Google reviews</a></div></div>
      </aside>
    </div>
  </section>
</div>
"""
    ld = {"@context": "https://schema.org", "@type": "ContactPage", "name": "Contact Kiang Collective", "url": SITE + "/contact.html"}
    write("contact.html", head("Contact | Kiang Collective",
                               "Get in touch with Kiang Collective about a film in India or one of our wildlife expeditions. We reply within two working days.",
                               "contact.html", "images/landscape-ftl.jpg", "A fan-throated lizard on the Chalkewadi plateau", [ld])
          + nav("contact.html") + body + footer())
    # Old address keeps working
    write("enquire.html", """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Contact | Kiang Collective</title>
<meta http-equiv="refresh" content="0; url=contact.html"><link rel="canonical" href="https://kiang.in/contact.html"></head>
<body style="background:#0D0E0C;color:#ECEBE6;font-family:sans-serif"><p>This page has moved to <a style="color:#D2A86A" href="contact.html">contact.html</a>.</p></body></html>
""")


# ───────────────────────── JOURNAL ─────────────────────────
def journal():
    cards = "".join(f"""
      <a class="journal-card" href="{s['slug']}.html">
        <div class="img">{pic(s['card'], s['alt'])}</div>
        <span class="meta">{s['place']}</span>
        <h3>{s['title']}</h3>
        <p>{e(s['body'][0][:150].rsplit(' ', 1)[0])}…</p>
      </a>""" for s in STORIES)
    body = page_hero("Journal", "Field notes and small stories", "journal-hero-fireflies",
                     "Fireflies glowing through a forest canopy at dusk", "From the field") + f"""
<div class="wrap">
  <section class="section reveal"><div class="journal-grid">{cards}
  </div></section>
</div>
"""
    blog = {"@context": "https://schema.org", "@type": "Blog", "name": "Kiang Collective Journal", "url": SITE + "/journal.html",
            "blogPost": [{"@type": "BlogPosting", "headline": s["title"], "url": f"{SITE}/{s['slug']}.html",
                          "author": {"@type": "Person", "name": "Panchami Gaitonde"}} for s in STORIES]}
    write("journal.html", head("Journal — Field Notes | Kiang Collective",
                               "Field notes from the wild by Panchami Gaitonde: fireflies in Valparai, the Valley of Flowers, and the fan-throated lizards of Chalkewadi.",
                               "journal.html", "images/journal-hero-fireflies.jpg", "Fireflies in a forest at dusk", [blog])
          + nav("journal.html") + body + footer())

    for s in STORIES:
        paras = "".join(f"<p>{e(p)}</p>" for p in s["body"])
        href, label, line = s["related"]
        body = f"""
<div style="padding-top:140px">
  <div class="story">
    <a class="back" href="journal.html">← Journal</a>
    <div class="eyebrow" style="margin:32px 0 16px">{s['place']}</div>
    <h1 style="font-size:clamp(52px,7vw,104px)">{s['title']}</h1>
  </div>
  <figure class="story-figure reveal" style="margin:56px auto">{pic(s['image'], s['alt'], lazy=False)}</figure>
  <article class="story reveal">
    <div class="story-body">{paras}</div>
    <div class="byline">{s['byline']}</div>
    <a class="next-link" href="{href}"><span><span class="eyebrow">{label}</span><br><span class="muted">{line}</span></span><span class="link">Go →</span></a>
  </article>
</div>
<div style="height:120px"></div>
"""
        ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": s["title"],
              "image": f"{SITE}/images/{s['image']}.jpg", "author": {"@type": "Person", "name": "Panchami Gaitonde"},
              "publisher": {"@type": "Organization", "name": "Kiang Collective"}, "url": f"{SITE}/{s['slug']}.html"}
        write(f"{s['slug']}.html", head(f"{s['title']} — Journal | Kiang Collective",
                                        e(s["body"][0][:155].rsplit(' ', 1)[0]) + "…",
                                        f"{s['slug']}.html", f"images/{s['image']}.jpg", s["alt"], [ld])
              + nav("journal.html", over_hero=False) + body + footer())


def seo_files():
    pages = ["", "films.html", "expeditions.html", "expedition-spiti-2027.html", "expedition-rajasthan-2026.html",
             "journal.html"] + [s["slug"] + ".html" for s in STORIES] + ["about.html", "contact.html"]
    urls = "".join(f"  <url><loc>{SITE}/{p}</loc><lastmod>2026-11-21</lastmod></url>\n" for p in pages)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")


if __name__ == "__main__":
    home(); films(); expeditions(); about(); contact(); journal()
    trips.build(write, spiti_price)
    seo_files()
    print("built")
