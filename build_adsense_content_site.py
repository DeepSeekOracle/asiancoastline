#!/usr/bin/env python3
"""
asiancoastline.com AdSense fix:
  Violation: Google-served ads on screens without publisher-content

Actions:
  1) REMOVE ad units + ad push from listen.html (player shell = low-value for ads)
  2) REPLACE giant 404 player clone with a simple content 404 (no ads)
  3) Expand content pages: index, guides, about, contact, privacy, terms
  4) Keep ads ONLY on high-value content pages
  5) Preserve listen.html player boot/playlist system
"""
from __future__ import annotations

import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PUB = "ca-pub-0646320966060599"
YEAR = str(date.today().year)

CSS = """
:root {
  --bg: #0f1218; --card: #171c26; --ink: #e8eaef; --muted: #9aa3b2;
  --line: #2a3344; --accent: #3d9cf0; --accent2: #7dd3a0; --link: #7ec8ff;
}
* { box-sizing: border-box; }
body { margin: 0; font-family: system-ui, -apple-system, Segoe UI, sans-serif;
  color: var(--ink); background: var(--bg); line-height: 1.65; font-size: 17px; }
a { color: var(--link); }
.wrap { max-width: 820px; margin: 0 auto; padding: 0 1.15rem; }
header.site { background: rgba(23,28,38,.96); border-bottom: 1px solid var(--line);
  padding: .85rem 0; position: sticky; top: 0; z-index: 40; backdrop-filter: blur(8px); }
.nav { display: flex; flex-wrap: wrap; gap: .7rem 1rem; align-items: center; justify-content: space-between; }
.brand { font-weight: 800; color: #fff; text-decoration: none; letter-spacing: .02em; }
.navlinks { display: flex; flex-wrap: wrap; gap: .5rem .85rem; font-size: .88rem; }
.navlinks a { text-decoration: none; color: var(--muted); }
.navlinks a:hover, .navlinks a[aria-current="page"] { color: var(--accent2); }
.hero { padding: 2rem 0 1rem; }
.hero h1 { font-size: clamp(1.55rem, 3.8vw, 2.15rem); line-height: 1.25; margin: 0 0 .7rem; color: #fff; }
.lead { color: var(--muted); font-size: 1.05rem; margin: 0 0 1.05rem; }
.cta-row { display: flex; flex-wrap: wrap; gap: .55rem; }
.btn { display: inline-block; padding: .68rem 1.05rem; border-radius: 9px; text-decoration: none !important;
  font-weight: 700; font-size: .9rem; border: 1px solid var(--line); background: var(--card); color: #fff; }
.btn.primary { background: linear-gradient(135deg, #1f6feb, #238636); border-color: transparent; }
.notice { margin: 1.05rem 0 0; padding: .85rem 1rem; background: #13201a; border: 1px solid #234d38;
  border-radius: 10px; font-size: .9rem; color: #cfe9d8; }
.card { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 1.3rem 1.2rem; margin: 1.05rem 0; }
.card h2 { margin: 0 0 .45rem; font-size: 1.22rem; color: #fff; }
.card h3 { margin: 1rem 0 .3rem; font-size: 1.02rem; color: #dfe7f3; }
.meta { font-size: .8rem; color: var(--muted); margin-bottom: .55rem; }
.ad-slot { margin: 1.05rem 0; min-height: 90px; padding: 8px; background: #121722;
  border: 1px dashed var(--line); border-radius: 8px; text-align: center; }
.ad-label { font-size: 10px; text-transform: uppercase; letter-spacing: .08em; color: #778; margin-bottom: 6px; }
.grid2 { display: grid; gap: .85rem; }
@media (min-width: 700px) { .grid2 { grid-template-columns: 1fr 1fr; } }
.tile { display: block; padding: 1rem; background: #121722; border: 1px solid var(--line);
  border-radius: 10px; text-decoration: none; color: inherit; }
.tile strong { display: block; color: #fff; margin-bottom: .25rem; }
.tile span { color: var(--muted); font-size: .9rem; }
footer.site { border-top: 1px solid var(--line); padding: 1.35rem 0 2.4rem; margin-top: 1.4rem;
  font-size: .86rem; color: var(--muted); }
footer.site nav { display: flex; flex-wrap: wrap; gap: .45rem 1rem; margin-bottom: .55rem; }
ul, ol { padding-left: 1.2rem; }
"""


def head(title: str, desc: str, path: str, with_ads: bool = True) -> str:
    can = f"https://asiancoastline.com{path}"
    ads = ""
    if with_ads:
        ads = f"""<meta name="google-adsense-account" content="{PUB}">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={PUB}" crossorigin="anonymous"></script>
"""
    else:
        # ownership meta only — no ad script on player screens
        ads = f'<meta name="google-adsense-account" content="{PUB}">\n'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Justin Helmer / Excavationpro">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="{can}">
{ads}<meta property="og:type" content="website">
<meta property="og:url" content="{can}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:site_name" content="asiancoastline.com">
<meta name="twitter:card" content="summary">
<meta name="twitter:site" content="@Excavationpro">
<meta name="theme-color" content="#0f1218">
<style>{CSS}</style>
</head>
"""


def nav(active: str = "") -> str:
    links = [
        ("/", "Home"),
        ("/listen.html", "Listen free"),
        ("/guides.html", "Guides"),
        ("/about.html", "About"),
        ("/contact.html", "Contact"),
        ("/privacy.html", "Privacy"),
    ]
    items = []
    for href, label in links:
        cur = ' aria-current="page"' if active == href else ""
        items.append(f'<a href="{href}"{cur}>{label}</a>')
    return f"""<header class="site"><div class="wrap nav">
<a class="brand" href="/">asiancoastline.com</a>
<nav class="navlinks" aria-label="Primary">{" ".join(items)}</nav>
</div></header>
"""


def footer() -> str:
    return f"""<footer class="site"><div class="wrap">
<nav aria-label="Footer">
  <a href="/">Home</a>
  <a href="/listen.html">Listen free</a>
  <a href="/guides.html">Guides</a>
  <a href="/independent-music-listening.html">Independent listening</a>
  <a href="/why-free-streams.html">Why free streams</a>
  <a href="/about.html">About</a>
  <a href="/contact.html">Contact</a>
  <a href="/privacy.html">Privacy</a>
  <a href="/terms.html">Terms</a>
</nav>
<p>© {YEAR} Justin Helmer / Excavationpro · asiancoastline.com — free original music listen portal.
Contact: <a href="mailto:excavationstation@gmail.com">excavationstation@gmail.com</a></p>
</div></footer>
"""


def ad_slot() -> str:
    return f"""  <div class="ad-slot" aria-label="Advertisement">
    <div class="ad-label">Advertisement</div>
    <ins class="adsbygoogle" style="display:block" data-ad-client="{PUB}" data-ad-format="auto" data-full-width-responsive="true"></ins>
    <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
  </div>
"""


def page(title: str, desc: str, path: str, active: str, body: str, with_ads: bool = True) -> str:
    return (
        head(title, desc, path, with_ads=with_ads)
        + "<body>\n"
        + nav(active)
        + '<div class="wrap">\n'
        + body
        + "\n</div>\n"
        + footer()
        + "\n</body>\n</html>\n"
    )


def write(name: str, content: str) -> None:
    (ROOT / name).write_text(content, encoding="utf-8")
    print("wrote", name, len(content))


def strip_ads_from_listen() -> None:
    """Remove Google ad units from listen.html while preserving player."""
    p = ROOT / "listen.html"
    t = p.read_text(encoding="utf-8", errors="replace")
    orig = len(t)

    # Remove full AdSense loader script tags in head
    t = re.sub(
        r'\s*<script[^>]+pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js[^>]*>\s*</script>\s*',
        "\n",
        t,
        flags=re.I,
    )
    # Remove ad-box blocks with ins.adsbygoogle
    t = re.sub(
        r'\s*<div class="ad-box">[\s\S]*?</div>\s*',
        "\n",
        t,
        flags=re.I,
    )
    # Remove generic adsbygoogle ins blocks
    t = re.sub(
        r'\s*<ins class="adsbygoogle"[\s\S]*?</ins>\s*',
        "\n",
        t,
        flags=re.I,
    )
    # Neutralize pushAdUnits / ADSENSE_SRC loaders (keep page JS intact)
    t = re.sub(
        r"const ADSENSE_SRC\s*=\s*['\"][^'\"]+['\"];?",
        "const ADSENSE_SRC = '';",
        t,
    )
    # Replace function bodies that push ads with no-ops if present
    t = re.sub(
        r"function\s+pushAdUnits\s*\([^)]*\)\s*\{[\s\S]*?\n\s*\}",
        "function pushAdUnits(){ /* ads disabled on player shell — AdSense content policy */ }",
        t,
        count=1,
    )
    t = re.sub(
        r"function\s+loadAdSense\s*\([^)]*\)\s*\{[\s\S]*?\n\s*\}",
        "function loadAdSense(){ /* ads disabled on player shell */ }",
        t,
        count=1,
    )
    # Soft-disable remaining push calls on this page
    t = t.replace(
        "(window.adsbygoogle = window.adsbygoogle || []).push({});",
        "/* adsbygoogle push disabled on listen.html */",
    )
    t = t.replace(
        "(adsbygoogle = window.adsbygoogle || []).push({});",
        "/* adsbygoogle push disabled on listen.html */",
    )

    # Ensure privacy/contact/home links in page somewhere
    if 'href="/privacy.html"' not in t and "privacy.html" not in t:
        t = t.replace(
            "</body>",
            """
<footer style="font-family:system-ui,sans-serif;font-size:13px;padding:1rem;border-top:1px solid #333;margin-top:1rem;background:#0b0e14;color:#9aa3b2">
  <div style="max-width:960px;margin:0 auto">
    <a href="/" style="color:#7ec8ff">Home (guides)</a> ·
    <a href="/guides.html" style="color:#7ec8ff">Guides</a> ·
    <a href="/about.html" style="color:#7ec8ff">About</a> ·
    <a href="/contact.html" style="color:#7ec8ff">Contact</a> ·
    <a href="/privacy.html" style="color:#7ec8ff">Privacy</a> ·
    <a href="/terms.html" style="color:#7ec8ff">Terms</a>
    <p style="margin:.45rem 0 0">Player shell: no Google ads on this screen (publisher content lives on Home/Guides).</p>
  </div>
</footer>
</body>""",
            1,
        )

    # Note near ads.txt mention
    t = re.sub(
        r"AdSense publisher:.*?</p>",
        '<p class="muted">Ads are not shown on the player screen. See <a href="/">home guides</a> and <a href="ads.txt">ads.txt</a>.</p>',
        t,
        count=1,
        flags=re.I | re.S,
    )

    p.write_text(t, encoding="utf-8")
    print(f"listen.html ads stripped ({orig} → {len(t)} bytes)")


def write_content_pages() -> None:
    index_body = f"""
  <section class="hero">
    <h1>Free browser music portal for original Excavationpro streams</h1>
    <p class="lead">
      asiancoastline.com is the public listen domain for <strong>Justin Helmer / Excavationpro</strong> original music.
      This homepage is real publisher content: how free independent listening works, why masters stay offline, and how to use the portal.
      The full player stays at a separate URL so the system remains intact — without putting ads on a pure player chrome screen.
    </p>
    <div class="cta-row">
      <a class="btn primary" href="/listen.html">Open free listen player →</a>
      <a class="btn" href="/guides.html">Read guides</a>
      <a class="btn" href="/about.html">About the publisher</a>
    </div>
    <p class="notice">
      <strong>Full player preserved:</strong> search, shuffle, radio, catalog, and live links live at
      <a href="/listen.html">/listen.html</a>. Google ads are intentionally limited to content pages (this site’s articles),
      not empty or navigation-only screens.
    </p>
  </section>

{ad_slot()}

  <main>
    <article class="card">
      <h2>What this portal is</h2>
      <p class="meta">Independent free listening · Original work only · Updated 2026</p>
      <p>
        Major apps are useful, but a free browser portal keeps a direct path to original music. Streams here are derived
        for web listening from masters owned by the artist. You can explore without creating an account. Commercial rights
        stay with Justin Helmer / Excavationpro unless a separate license is granted.
      </p>
      <p>
        The player page is intentionally powerful: large catalog, radio modes, and live room links. Ad networks require
        publisher content around advertising — so this homepage and guide articles carry the educational writing, while
        the player focuses on listening.
      </p>
    </article>

    <article class="card">
      <h2>How free independent listening works</h2>
      <ol>
        <li>Open the free player at <a href="/listen.html">/listen.html</a>.</li>
        <li>Search or browse the catalog of original streams.</li>
        <li>Use radio / shuffle modes for continuous play.</li>
        <li>Optionally visit live rooms (Kick, Rumble, Twitch) linked from the player.</li>
        <li>Optional support links help hosting — never required to listen.</li>
      </ol>
      <p>
        For tempo prep while you build a set, use the free
        <a href="https://bpmfinder.ca/app.html">BPM tool on bpmfinder.ca</a>.
      </p>
    </article>

    <article class="card">
      <h2>Why keep masters offline?</h2>
      <p>
        Public streams are listening copies (typically compressed). Keep archival WAV/AIF masters in your own vault.
        That separation protects releases while still giving fans a free way to press play. Free listen is not a license
        to re-upload tracks as your own or to claim authorship.
      </p>
      <p>Read more: <a href="/why-free-streams.html">Why free streams exist</a> · <a href="/independent-music-listening.html">Independent music listening</a></p>
    </article>

    <article class="card">
      <h2>Guides</h2>
      <div class="grid2">
        <a class="tile" href="/independent-music-listening.html"><strong>Independent music listening</strong><span>How free portals fit next to Spotify and radio.</span></a>
        <a class="tile" href="/why-free-streams.html"><strong>Why free streams</strong><span>Streams vs masters, rights, and respect.</span></a>
        <a class="tile" href="/how-to-use-the-player.html"><strong>How to use the player</strong><span>Search, radio, favorites, and live rooms.</span></a>
        <a class="tile" href="/about.html"><strong>About / publisher</strong><span>Who runs asiancoastline.com and how to contact us.</span></a>
      </div>
    </article>

    <article class="card" id="faq">
      <h2>FAQ</h2>
      <h3>Is listening free?</h3>
      <p>Yes. No account is required for the public player.</p>
      <h3>Can I re-upload tracks as my own?</h3>
      <p>No. Free listening is not a license to republish or claim authorship.</p>
      <h3>Where is the full player?</h3>
      <p><a href="/listen.html">https://asiancoastline.com/listen.html</a></p>
      <h3>Why don’t I see ads on the player?</h3>
      <p>By design. AdSense policy forbids ads on low-content or navigation-only screens. Publisher content and any ads live on Home and Guides.</p>
      <h3>Privacy?</h3>
      <p>See <a href="/privacy.html">Privacy policy</a>.</p>
    </article>

    <article class="card">
      <h2>Related free projects</h2>
      <ul>
        <li><a href="https://bpmfinder.ca/">bpmfinder.ca</a> — BPM guides &amp; tool</li>
        <li><a href="https://eternalhaven.ca/">eternalhaven.ca</a> — books &amp; systems home</li>
        <li><a href="https://www.paypal.com/paypalme/ExcavationPro">PayPal support</a> (optional)</li>
      </ul>
    </article>
  </main>
"""
    write(
        "index.html",
        page(
            "Excavationpro Free Music Portal — Listen Online | asiancoastline.com",
            "Free browser music portal for original Excavationpro streams. Guides on independent listening plus a full free player.",
            "/",
            "/",
            index_body,
            with_ads=True,
        ),
    )

    guides = f"""
  <section class="hero">
    <h1>Music portal guides</h1>
    <p class="lead">Original articles about free independent listening, streams vs masters, and how to use the player.</p>
    <div class="cta-row"><a class="btn primary" href="/listen.html">Open player</a></div>
  </section>
{ad_slot()}
  <main>
    <article class="card">
      <div class="grid2">
        <a class="tile" href="/independent-music-listening.html"><strong>Independent music listening</strong><span>Direct artist portals beside big platforms.</span></a>
        <a class="tile" href="/why-free-streams.html"><strong>Why free streams</strong><span>Listening copies, rights, and respect.</span></a>
        <a class="tile" href="/how-to-use-the-player.html"><strong>How to use the player</strong><span>Search, radio, live rooms.</span></a>
        <a class="tile" href="/about.html"><strong>About</strong><span>Publisher and mission.</span></a>
      </div>
    </article>
  </main>
"""
    write(
        "guides.html",
        page(
            "Guides — Free Independent Music Listening | asiancoastline.com",
            "Guides for the Excavationpro free music portal: independent listening, free streams, and player help.",
            "/guides.html",
            "/guides.html",
            guides,
        ),
    )

    ind = f"""
  <section class="hero">
    <h1>Independent music listening in a platform world</h1>
    <p class="lead">Why a free artist-owned listen portal still matters next to Spotify, YouTube, and radio.</p>
    <div class="cta-row"><a class="btn primary" href="/listen.html">Listen free</a></div>
  </section>
{ad_slot()}
  <main>
    <article class="card">
      <h2>Platforms are great — and incomplete</h2>
      <p>
        Streaming apps make discovery easy. They also insert middle layers: algorithms, account walls, and policies that
        can change overnight. An independent browser portal gives listeners a second door: press play without installing
        an app, and without pretending the artist handed away every path to their own work.
      </p>
      <h2>What “free listen” means here</h2>
      <p>
        Free listen means you can hear web streams of original Excavationpro / Justin Helmer music in a browser.
        It does not mean public domain. It does not mean you may re-upload tracks, mint them as your own NFT drops,
        or strip credits. Free access and free ownership are different ideas.
      </p>
      <h2>How to use both worlds</h2>
      <ol>
        <li>Use major platforms for everyday playlists and social sharing.</li>
        <li>Use <a href="/listen.html">asiancoastline.com/listen.html</a> for a direct free portal.</li>
        <li>Support when you can — optional PayPal tips help hosting.</li>
        <li>Respect the work: stream, don’t steal.</li>
      </ol>
      <p>Next: <a href="/why-free-streams.html">Why free streams exist</a></p>
    </article>
  </main>
"""
    write(
        "independent-music-listening.html",
        page(
            "Independent Music Listening — Free Artist Portals Explained | asiancoastline.com",
            "Why independent free music portals matter alongside Spotify and radio, and how to listen respectfully.",
            "/independent-music-listening.html",
            "",
            ind,
        ),
    )

    why = f"""
  <section class="hero">
    <h1>Why free streams exist (and what they are not)</h1>
    <p class="lead">Streams are listening copies. Masters stay in the vault. Here is the respectful model.</p>
  </section>
{ad_slot()}
  <main>
    <article class="card">
      <h2>Streams vs masters</h2>
      <p>
        A public stream is usually a compressed file optimized for browsers and bandwidth. A master is the archival
        production file (often WAV/AIF) used for distribution and long-term storage. Keeping masters offline protects
        the catalog while still letting people listen freely online.
      </p>
      <h2>What free streams are for</h2>
      <ul>
        <li>Fans discovering original music without a paywall</li>
        <li>Radio-style continuous play in a browser</li>
        <li>A sovereign path that does not depend on one distributor UI</li>
      </ul>
      <h2>What free streams are not</h2>
      <ul>
        <li>Not a license to re-upload to other platforms as your own</li>
        <li>Not permission to sell the files</li>
        <li>Not permission to strip artist credits</li>
      </ul>
      <p>
        If you want commercial licensing, contact the publisher via
        <a href="/contact.html">Contact</a>.
      </p>
      <p><a href="/listen.html"><strong>Open the free player →</strong></a></p>
    </article>
  </main>
"""
    write(
        "why-free-streams.html",
        page(
            "Why Free Streams Exist — Streams vs Masters | asiancoastline.com",
            "Explain free music streams vs masters, rights, and respectful listening on the Excavationpro portal.",
            "/why-free-streams.html",
            "",
            why,
        ),
    )

    how = f"""
  <section class="hero">
    <h1>How to use the free listen player</h1>
    <p class="lead">Search, radio, shuffle, favorites, and live rooms — without breaking the catalog.</p>
    <div class="cta-row"><a class="btn primary" href="/listen.html">Open player</a></div>
  </section>
{ad_slot()}
  <main>
    <article class="card">
      <h2>Basic steps</h2>
      <ol>
        <li>Go to <a href="/listen.html">listen.html</a>.</li>
        <li>Use search to find a title, or browse the list.</li>
        <li>Press play. Use next/previous as needed.</li>
        <li>Try shuffle or radio mode for continuous listening.</li>
        <li>Open live portal links if you want Kick / Rumble / Twitch rooms.</li>
      </ol>
      <h2>Tips</h2>
      <ul>
        <li>On mobile, use headphones and keep the tab open for background play (browser dependent).</li>
        <li>If a track fails, try another — streams are hosted for free listening and can be re-checked.</li>
        <li>Return to <a href="/">Home</a> for guides and publisher info.</li>
      </ul>
      <h2>Keyboard (desktop)</h2>
      <p>Where enabled, space toggles play/pause; N/P move tracks; S shuffles. Check the player dock for the current shortcuts.</p>
    </article>
  </main>
"""
    write(
        "how-to-use-the-player.html",
        page(
            "How to Use the Free Music Player | asiancoastline.com",
            "How to search, play, shuffle, and use radio mode on the Excavationpro free listen portal.",
            "/how-to-use-the-player.html",
            "",
            how,
        ),
    )

    about = f"""
  <section class="hero">
    <h1>About asiancoastline.com</h1>
    <p class="lead">Publisher content for the free Excavationpro music listen portal.</p>
  </section>
  <main>
    <article class="card">
      <h2>Mission</h2>
      <p>
        asiancoastline.com hosts free listening for original music by Justin Helmer / Excavationpro, plus clear educational
        pages about independent listening. The player is a product surface; this domain is also a publisher site with
        real articles, policies, and contact information.
      </p>
      <h2>Publisher</h2>
      <p><strong>Justin Helmer</strong> · Canada · Email: <a href="mailto:excavationstation@gmail.com">excavationstation@gmail.com</a></p>
      <h2>Advertising policy on this domain</h2>
      <p>
        Google ads, when approved, are intended for content pages (home, guides, about). The listen player screen is kept
        free of Google-served ads to comply with policies against ads on low-content or navigation-only screens.
      </p>
      <h2>Related</h2>
      <ul>
        <li><a href="https://bpmfinder.ca/">bpmfinder.ca</a></li>
        <li><a href="https://eternalhaven.ca/">eternalhaven.ca</a></li>
        <li><a href="https://www.paypal.com/paypalme/ExcavationPro">PayPal support</a></li>
      </ul>
    </article>
  </main>
"""
    write(
        "about.html",
        page(
            "About asiancoastline.com — Excavationpro Free Music Portal",
            "About asiancoastline.com: free Excavationpro music portal, publisher Justin Helmer, and contact details.",
            "/about.html",
            "/about.html",
            about,
        ),
    )

    contact = f"""
  <section class="hero">
    <h1>Contact</h1>
    <p class="lead">Questions about free listening, rights, privacy, or this website.</p>
  </section>
  <main>
    <article class="card">
      <h2>Email</h2>
      <p><a href="mailto:excavationstation@gmail.com">excavationstation@gmail.com</a></p>
      <p>Include “asiancoastline” in the subject. Allow a few business days for reply.</p>
      <h2>Publisher</h2>
      <p>Justin Helmer / Excavationpro · Canada</p>
      <h2>Support hosting (optional)</h2>
      <p><a href="https://www.paypal.com/paypalme/ExcavationPro">PayPal.me/ExcavationPro</a></p>
      <h2>Policies</h2>
      <p><a href="/privacy.html">Privacy</a> · <a href="/terms.html">Terms</a></p>
    </article>
  </main>
"""
    write(
        "contact.html",
        page(
            "Contact — asiancoastline.com",
            "Contact Justin Helmer about the free Excavationpro music portal on asiancoastline.com.",
            "/contact.html",
            "/contact.html",
            contact,
        ),
    )

    privacy = f"""
  <section class="hero">
    <h1>Privacy Policy</h1>
    <p class="meta">Last updated: 2026-08-09 · Justin Helmer / Excavationpro</p>
  </section>
  <main>
    <article class="card">
      <h2>Summary</h2>
      <p>asiancoastline.com provides free listening to original music streams and educational pages about independent music. We aim to be transparent about cookies and advertising.</p>
      <h2>Streaming and logs</h2>
      <p>When you play streams, your browser requests audio files from hosting providers (including public stream hosts such as Hugging Face datasets and site CDN/hosting). Hosts may process standard technical logs (IP, user agent, URLs) for security and delivery.</p>
      <h2>Cookies and advertising</h2>
      <p>We may use cookies for essential site function and, when approved, Google AdSense on <strong>content pages</strong> (publisher ID <code>{PUB}</code>). We intentionally avoid Google-served ads on pure player chrome screens to respect AdSense content policies.</p>
      <p>Google: <a href="https://policies.google.com/technologies/ads">Advertising</a> · <a href="https://policies.google.com/privacy">Privacy</a> · <a href="https://adssettings.google.com/">Ad Settings</a></p>
      <h2>Contact</h2>
      <p><a href="mailto:excavationstation@gmail.com">excavationstation@gmail.com</a> · <a href="/contact.html">Contact page</a></p>
    </article>
  </main>
"""
    write(
        "privacy.html",
        page(
            "Privacy Policy — asiancoastline.com",
            "Privacy policy for asiancoastline.com free music portal: streams, cookies, AdSense, and contact.",
            "/privacy.html",
            "/privacy.html",
            privacy,
        ),
    )

    terms = f"""
  <section class="hero">
    <h1>Terms of use</h1>
    <p class="meta">Last updated: 2026-08-09</p>
  </section>
  <main>
    <article class="card">
      <h2>Acceptance</h2>
      <p>By using asiancoastline.com you agree to these terms.</p>
      <h2>License to listen</h2>
      <p>You may stream available free listens for personal, non-commercial enjoyment. You may not re-upload, resell, or claim authorship of the music.</p>
      <h2>No warranty</h2>
      <p>The site and streams are provided “as is.” Availability may change.</p>
      <h2>Contact</h2>
      <p><a href="mailto:excavationstation@gmail.com">excavationstation@gmail.com</a></p>
    </article>
  </main>
"""
    write(
        "terms.html",
        page(
            "Terms of Use — asiancoastline.com",
            "Terms of use for free listening on asiancoastline.com / Excavationpro music portal.",
            "/terms.html",
            "",
            terms,
        ),
    )

    # Clean 404 with content, NO ads (error screens)
    not_found = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Page not found — asiancoastline.com</title>
<meta name="robots" content="noindex">
<meta name="google-adsense-account" content="{PUB}">
<style>{CSS}</style>
</head>
<body>
{nav("")}
<div class="wrap">
  <section class="hero">
    <h1>Page not found</h1>
    <p class="lead">That URL is missing or moved. Try one of these working pages:</p>
    <div class="cta-row">
      <a class="btn primary" href="/">Home</a>
      <a class="btn" href="/listen.html">Listen free</a>
      <a class="btn" href="/guides.html">Guides</a>
      <a class="btn" href="/contact.html">Contact</a>
    </div>
  </section>
  <article class="card">
    <h2>Popular destinations</h2>
    <ul>
      <li><a href="/listen.html">Free music player</a></li>
      <li><a href="/independent-music-listening.html">Independent listening guide</a></li>
      <li><a href="/privacy.html">Privacy policy</a></li>
    </ul>
    <p>No ads on error pages. Publisher content lives on Home and Guides.</p>
  </article>
</div>
{footer()}
</body>
</html>
"""
    write("404.html", not_found)

    # ads/robots/sitemap
    (ROOT / "ads.txt").write_text(
        "google.com, pub-0646320966060599, DIRECT, f08c47fec0942fa0\n",
        encoding="utf-8",
    )
    (ROOT / "robots.txt").write_text(
        """User-agent: *
Allow: /

Sitemap: https://asiancoastline.com/sitemap.xml
""",
        encoding="utf-8",
    )
    urls = [
        ("https://asiancoastline.com/", "1.0"),
        ("https://asiancoastline.com/listen.html", "0.95"),
        ("https://asiancoastline.com/guides.html", "0.9"),
        ("https://asiancoastline.com/independent-music-listening.html", "0.9"),
        ("https://asiancoastline.com/why-free-streams.html", "0.85"),
        ("https://asiancoastline.com/how-to-use-the-player.html", "0.85"),
        ("https://asiancoastline.com/about.html", "0.75"),
        ("https://asiancoastline.com/contact.html", "0.75"),
        ("https://asiancoastline.com/privacy.html", "0.5"),
        ("https://asiancoastline.com/terms.html", "0.5"),
    ]
    sm = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for loc, pri in urls:
        sm.append(
            f"  <url><loc>{loc}</loc><changefreq>weekly</changefreq><priority>{pri}</priority></url>"
        )
    sm.append("</urlset>\n")
    (ROOT / "sitemap.xml").write_text("\n".join(sm), encoding="utf-8")
    print("sitemap + robots + ads.txt ok")


def main() -> None:
    write_content_pages()
    strip_ads_from_listen()
    print("DONE — content up; ads removed from player/404")


if __name__ == "__main__":
    main()
