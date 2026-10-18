"""Targeted fixes for listen.html: remove the two ad regions, disable ad loading,
replace the stale giant JSON-LD, and add a static editorial section. Does not touch
the player JavaScript, catalog data, audio element, or control IDs."""
from __future__ import annotations

import json
import re
from pathlib import Path

P = Path(__file__).resolve().parent / "listen.html"
s = P.read_text(encoding="utf-8", errors="replace")


def cut_div(text: str, marker: str) -> str:
    start = text.index(marker)
    depth = 0
    for m in re.finditer(r"<div\b|</div>", text[start:]):
        depth += 1 if m.group() == "<div" else -1
        if depth == 0:
            end = start + m.end()
            return text[:start] + text[end:]
    raise RuntimeError("unbalanced div for " + marker)


before = len(s)
s = cut_div(s, '<div class="ad-region" id="ad-top"')
s = cut_div(s, '<div class="ad-region" id="ad-mid"')
print("removed ad regions:", before - len(s), "chars")

# Disable the consent-triggered AdSense loader; keep the cookie banner itself.
needle = "function loadAdSenseScript() {\n  showAdRegions();"
if needle not in s:
    raise SystemExit("loadAdSenseScript signature not found")
s = s.replace(needle, "function loadAdSenseScript() {\n  return; // player is intentionally ad-free\n  showAdRegions();", 1)

# Replace stale title/description/keywords.
s = s.replace(
    "<title>Excavationpro Listen Free — 11162 Songs · Sovereign Music Portal · Lattice Ledger</title>",
    "<title>Listen Free — Excavationpro Music Portal | asiancoastline.com</title>", 1)
s = re.sub(
    r'<meta name="description" content="[^"]*">',
    '<meta name="description" content="Stream the Excavationpro catalog free in your browser. Search the player, build a queue, and read the guides. No account; masters stay offline.">',
    s, count=1)
s = re.sub(r'<meta name="keywords" content="[^"]*">\s*', "", s, count=1)

# Compact, canonical schema.
schema = {
    "@context": "https://schema.org",
    "@graph": [
        {"@type": "WebSite", "@id": "https://asiancoastline.com/#website",
         "url": "https://asiancoastline.com/", "name": "asiancoastline.com",
         "publisher": {"@id": "https://asiancoastline.com/#organization"}},
        {"@type": "Organization", "@id": "https://asiancoastline.com/#organization",
         "name": "Excavationpro / Asian Coastline", "url": "https://asiancoastline.com/",
         "founder": {"@type": "Person", "name": "Justin Helmer"},
         "sameAs": ["https://excavationpro.ca/",
                    "https://huggingface.co/DeepSeekOracle",
                    "https://github.com/DeepSeekOracle"]},
        {"@type": "WebPage", "@id": "https://asiancoastline.com/listen.html#webpage",
         "url": "https://asiancoastline.com/listen.html",
         "name": "Listen Free — Excavationpro Music Portal",
         "description": "Free browser player for the Excavationpro catalog.",
         "isPartOf": {"@id": "https://asiancoastline.com/#website"}},
        {"@type": "MusicPlaylist", "@id": "https://asiancoastline.com/listen.html#playlist",
         "name": "Excavationpro public catalog",
         "url": "https://asiancoastline.com/listen.html",
         "isPartOf": {"@id": "https://asiancoastline.com/listen.html#webpage"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://asiancoastline.com/"},
            {"@type": "ListItem", "position": 2, "name": "Listen free",
             "item": "https://asiancoastline.com/listen.html"},
        ]},
    ],
}
ld_start = s.index('<script type="application/ld+json">')
ld_end = s.index("</script>", ld_start) + len("</script>")
s = s[:ld_start] + '<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + "</script>" + s[ld_end:]

notes = """
<section class="wrap player-notes" id="about-player">
  <style>
    .player-notes { max-width: 820px; margin: 2.2rem auto 8rem; padding: 0 1.15rem; color: #d8d8e8; line-height: 1.7; }
    .player-notes h2 { color: #fff; font-size: 1.22rem; margin: 1.6rem 0 .45rem; }
    .player-notes p, .player-notes li { color: #b9b9cc; }
    .player-notes a { color: #7ec8ff; }
    .player-notes .family { display: flex; flex-wrap: wrap; gap: .45rem 1rem; font-size: .86rem; }
  </style>
  <h2>How this player works</h2>
  <p>The player loads a public catalog of compressed streams and plays them through the browser&rsquo;s audio element. Search filters by title, ISRC, or a hash fragment; the chips switch between the music catalog, Eternal Haven audio, favorites, and the queue. Radio keeps playing after the current track, shuffle changes the order, and the sleep timer stops playback after 15&ndash;90 minutes.</p>
  <p>Nothing is uploaded. Favorites and queue are stored in your browser, not an account. The installed version caches the page shell, but the audio still streams from the public files. The player is intentionally ad-free: the catalog is the product, and an ad interrupting a track would be a different experience.</p>
  <h2>Catalog, masters, and the ledger</h2>
  <p>The public streams are listening copies. The archival WAV/AIF masters stay offline in the artist&rsquo;s vault. The ledger tab records a public snapshot of the catalog &mdash; titles, hashes, and metadata &mdash; so the record can be checked even when a file moves. A snapshot is not a promise of permanent playback; it is a reference.</p>
  <p>New work is added deliberately. This is a curated catalog, not an infinite upload feed. If a track is missing, the ledger shows what the catalog expected, and the <a href="/contact.html">contact page</a> is the repair route.</p>
  <h2>Keyboard and mobile</h2>
  <p>On desktop: Space play/pause, N/P next/previous, S shuffle, R radio, F favorite, / search. On mobile, the dock and controls stack; add the player to the home screen for a standalone window. Background playback depends on the browser, so keep the tab active if the audio stops when the screen locks.</p>
  <h2>Privacy and data</h2>
  <p>The hosting provider and audio host see standard request data such as IP address, user agent, and the file requested. The player does not build a listening profile. Cookies and advertising on the editorial pages are covered by the <a href="/privacy.html">privacy policy</a> and the cookie banner; the player itself does not load the ad script.</p>
  <h2>More from the workshop</h2>
  <p>Read <a href="/how-to-use-the-player.html">how to use the player</a>, <a href="/why-free-streams.html">why free streams exist</a>, or <a href="/guides.html">all six guides</a>. The wider tool map is at <a href="https://bpmfinder.ca/tools.html">bpmfinder.ca/tools.html</a>.</p>
  <p class="family">
    <a href="https://excavationpro.ca/">Excavationpro</a>
    <a href="https://bpmfinder.ca/">BPMfinder</a>
    <a href="https://justinhelmer.ca/">Justin Helmer</a>
    <a href="https://deepseekoracle.com/">DeepSeek Oracle</a>
    <a href="https://eternalhaven.ca/">Eternal Haven</a>
    <a href="https://chatagent.ca/">Chatagent</a>
  </p>
</section>
"""

boot = s.index('<script id="boot"')
s = s[:boot] + notes + s[boot:]
P.write_text(s, encoding="utf-8")
print("patched listen.html:", len(s), "chars")
