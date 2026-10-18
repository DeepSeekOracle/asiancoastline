"""Content bodies for asiancoastline.com. Imported by build_articles.py."""

PUB = "ca-pub-0646320966060599"
AD = """<div class="ad-slot" aria-label="Advertisement">
  <div class="ad-label">Advertisement</div>
  <ins class="adsbygoogle" style="display:block" data-ad-client="{pub}" data-ad-format="auto" data-full-width-responsive="true"></ins>
  <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
</div>""".format(pub=PUB)

RELATED = {
    "how-to-use-the-player.html": [
        ("/how-free-streaming-works.html", "How browser streaming works"),
        ("/why-free-streams.html", "Why free streams exist"),
        ("/independent-music-listening.html", "Independent listening"),
    ],
    "independent-music-listening.html": [
        ("/why-free-streams.html", "Why free streams exist"),
        ("/how-free-streaming-works.html", "How browser streaming works"),
        ("/independent-artist-checklist.html", "Independent artist checklist"),
    ],
    "why-free-streams.html": [
        ("/how-free-streaming-works.html", "How browser streaming works"),
        ("/independent-music-listening.html", "Independent listening"),
        ("/lyrics-and-copyright.html", "Lyrics and copyright"),
    ],
    "how-free-streaming-works.html": [
        ("/how-to-use-the-player.html", "How to use the player"),
        ("/why-free-streams.html", "Why free streams exist"),
        ("/lyrics-and-copyright.html", "Lyrics and copyright"),
    ],
    "lyrics-and-copyright.html": [
        ("/why-free-streams.html", "Why free streams exist"),
        ("/independent-artist-checklist.html", "Independent artist checklist"),
        ("/how-to-use-the-player.html", "How to use the player"),
    ],
    "independent-artist-checklist.html": [
        ("/why-free-streams.html", "Why free streams exist"),
        ("/independent-music-listening.html", "Independent listening"),
        ("/lyrics-and-copyright.html", "Lyrics and copyright"),
    ],
}


def related(slug):
    items = RELATED.get(slug, [])
    if not items:
        return ""
    links = "".join(f'<li><a href="{href}">{label}</a></li>' for href, label in items)
    return f'<div class="related"><h2>Related guides</h2><ul>{links}</ul></div>'


AUTHOR = """<div class="author-box">
  <strong>Justin Helmer</strong> publishes asiancoastline.com and records as
  <a href="https://excavationpro.ca/">Excavationpro</a>. The catalog is his own; the player is a
  free public listening room, not a distributor storefront. <a href="/about.html">About the site</a>.
</div>"""


PAGES = {}

# ---------------------------------------------------------------- player guide
PAGES["how-to-use-the-player.html"] = dict(
    title="How to Use the Free Listen Player | asiancoastline.com",
    desc="A practical guide to the free Excavationpro browser player: search, filters, keyboard shortcuts, shuffle, radio, favorites, crossfade, sleep, and PWA install.",
    path="/how-to-use-the-player.html",
    active="guides",
    h1="How to use the free listen player",
    lead="The player at /listen.html is a full browser listening room: search the catalog, filter by album or Haven books, build a queue, shuffle, run radio, crossfade, and install it as an app. Here is the short version.",
    minutes="7 min read",
    updated="2026-10-20",
    tags=["player", "how-to", "listening"],
    body=f"""
<article class="card">
  <h2>Open the player and find a track</h2>
  <p>Go to <a href="/listen.html">/listen.html</a>. The player loads the public catalog and shows the full track list. Use the search box for a title, an ISRC, or a hash fragment. The sort menu orders by title, size, or ISRC presence; the filter menu narrows to playable tracks or tracks with an ISRC.</p>
  <p>The chips under the toolbar are the fast path: <strong>Music</strong> for the main catalog, <strong>Haven books</strong> for the Eternal Haven audio, <strong>Favorites</strong> for what you have hearted, and <strong>Queue</strong> for what you have lined up. The library is large; searching is faster than scrolling.</p>
  <h2>Play, pause, and move through the catalog</h2>
  <p>Click a row to play it. The dock at the bottom holds play/pause, previous/next, shuffle, radio, repeat, volume, crossfade, and the sleep timer. On desktop, the keyboard is quicker: <strong>Space</strong> play/pause, <strong>N</strong>/<strong>P</strong> next/previous, <strong>S</strong> shuffle, <strong>R</strong> radio, <strong>F</strong> favorite, and <strong>/</strong> search.</p>
  <p>Radio keeps playing after the current track. Shuffle changes the order. Repeat one holds a single track. Crossfade blends the end of one track into the next; the sleep timer stops playback after 15&ndash;90 minutes, which is useful for a listening session at night.</p>
</article>
{AD}
<article class="card">
  <h2>Favorites, queue, and sharing</h2>
  <p>The heart button saves a track to your local favorites. Favorites are stored in your browser, not on an account. The queue lets you line up a few tracks without losing your place. The share button copies a link to the current track or opens the share sheet on mobile.</p>
  <p>If you clear your browser storage, favorites and queue are lost. That is the trade-off for not requiring an account. If you want a permanent list, keep a note or a playlist file outside the browser.</p>
  <h2>Install it as an app</h2>
  <p>On Chrome or Edge, use the install button in the toolbar or the browser menu&rsquo;s <strong>Install</strong> / <strong>Add to Home Screen</strong> option. On iOS Safari, use Share &rarr; Add to Home Screen. The installed version opens the same player in a standalone window and keeps the basic shell cached, so it feels less like a website and more like a small app.</p>
  <h2>Mobile and data use</h2>
  <p>The player is responsive; the track list, dock, and controls stack on a phone. Streaming uses data like any browser audio: a long session can consume hundreds of megabytes. On a metered connection, lower the volume, use shorter sessions, or download the tracks you own elsewhere rather than streaming for hours.</p>
  <h2>Troubleshooting</h2>
  <ul>
    <li><strong>A track will not start.</strong> Try another track first; if only one fails, the stream file may be missing from the public catalog. The ledger shows what is expected.</li>
    <li><strong>Playback stops when the screen locks.</strong> Mobile browsers may suspend background audio. Keep the tab active or use the installed app where the browser allows it.</li>
    <li><strong>The list is empty after a filter.</strong> Clear the search and set the filter back to All. The Haven filter only shows audio tagged as Haven books.</li>
    <li><strong>No sound.</strong> Check the volume slider in the dock, the system volume, and whether another tab is holding the audio session.</li>
  </ul>
  <p>The player does not require an account and does not upload your listening history. The <a href="/privacy.html">privacy policy</a> covers the hosting, streaming, and advertising layers.</p>
</article>
<article class="card faq">
  <h2>FAQ</h2>
  <h3>Do I need an account to listen?</h3>
  <p>No. The player opens without a signup. Favorites and queue are stored locally in your browser.</p>
  <h3>Can I download the tracks?</h3>
  <p>The player streams the public catalog. It is a listening room, not a download store. The <a href="/terms.html">terms</a> explain the listening license.</p>
  <h3>Why does the catalog show Haven books?</h3>
  <p>The same public player carries the Eternal Haven audio alongside the music. Use the Haven chip to isolate it, or All to see everything.</p>
  <h3>Does the player work offline?</h3>
  <p>The installed app caches the shell, but the audio streams from the public catalog. Full offline listening would require downloading files you own.</p>
</article>
{related("how-to-use-the-player.html")}
{AUTHOR}
""",
    faqs=[
        ("Do I need an account to listen?", "No. Favorites and queue are stored locally in the browser."),
        ("Can I download the tracks?", "The player streams the public catalog; it is a listening room, not a download store."),
        ("Why does the catalog show Haven books?", "The player carries the Eternal Haven audio alongside the music; the Haven chip isolates it."),
        ("Does the player work offline?", "The installed app caches the shell, but audio streams from the public catalog."),
    ],
)

# ---------------------------------------------------------------- independent listening
PAGES["independent-music-listening.html"] = dict(
    title="Independent Music Listening in a Platform World | asiancoastline.com",
    desc="How independent listening differs from platform feeds: curation, ownership, privacy, direct support, and a practical way to use both worlds without losing the album.",
    path="/independent-music-listening.html",
    active="guides",
    h1="Independent music listening in a platform world",
    lead="Streaming platforms are convenient and incomplete. An independent portal is a different deal: a catalog someone actually curates, a player that does not require an account, and a direct line between the listener and the work.",
    minutes="7 min read",
    updated="2026-10-20",
    tags=["independent", "listening", "platforms"],
    body=f"""
<article class="card">
  <h2>Platforms are great &mdash; and incomplete</h2>
  <p>A platform is a catalog, a recommendation engine, and a payment rail at once. That is useful when you want to hear something new with one tap. It is less useful when you want to understand a catalog, follow a small artist, or listen without an account and a recommendation feed shaping every next track.</p>
  <p>The recommendation engine is not neutral. It is optimized for engagement, which often means more tracks, shorter attention, and a bias toward what already works. An independent portal can be smaller and still be more useful: a curated body of work, a player that stays out of the way, and a clear statement of what the listener is allowed to do.</p>
  <h2>What independent listening means here</h2>
  <p>On asiancoastline.com, independent listening means three concrete things. The catalog is the artist&rsquo;s own, not a label&rsquo;s licensed subset. The player is a browser page, not an account-gated app. The rights are stated: you can listen, you can share a link, and you cannot re-upload the files or sell them.</p>
  <p>That is a narrower promise than a platform&rsquo;s, and a more honest one. You are not paying with a subscription or a profile; you are listening to a public stream that the artist chose to expose.</p>
</article>
{AD}
<article class="card">
  <h2>What you gain</h2>
  <ul>
    <li><strong>Curation.</strong> A catalog with a point of view, not an infinite feed.</li>
    <li><strong>Privacy.</strong> No account, no listening profile, no social graph required.</li>
    <li><strong>Directness.</strong> The player and the artist site are the same project; a broken link has a human owner.</li>
    <li><strong>Context.</strong> The guides and the ledger explain what you are hearing and where it came from.</li>
    <li><strong>Portability.</strong> A browser and a URL are enough; there is no app-store gate.</li>
  </ul>
  <h2>What you give up</h2>
  <p>You give up the platform&rsquo;s recommendation engine, its offline library, and its one-tap payment relationship. You also give up the illusion that every track ever made is in one place. An independent portal is a room, not the whole city. If you want discovery at scale, use a platform; if you want a relationship with a catalog, use the room.</p>
  <h2>How to use both worlds</h2>
  <p>Use the platform for discovery and the independent portal for attention. When a platform recommends something you actually want to sit with, look for the artist&rsquo;s own site and listen there. Buy the download if it exists, share the artist&rsquo;s link instead of a re-upload, and treat the platform as a map rather than the destination.</p>
  <p>If you are an artist, the same logic applies in reverse: use the platform for reach, but keep a direct room you control. The <a href="/independent-artist-checklist.html">independent artist checklist</a> covers the practical version of that.</p>
</article>
<article class="card faq">
  <h2>FAQ</h2>
  <h3>Is independent listening anti-platform?</h3>
  <p>No. It is a correction to the idea that the platform is the only room. Use both, but know which one owns the relationship.</p>
  <h3>Do I need to pay to listen here?</h3>
  <p>No. The public player is free. Optional support links help with hosting; they are not a subscription.</p>
  <h3>Why does the site keep masters offline?</h3>
  <p>Streams are listening copies. Masters are the archival files. Keeping them offline protects the catalog while the public stream stays open.</p>
  <h3>Can I share a track?</h3>
  <p>Yes. Share the player link. Do not re-upload the audio file as your own or sell it.</p>
</article>
{related("independent-music-listening.html")}
{AUTHOR}
""",
    faqs=[
        ("Is independent listening anti-platform?", "No. It is a correction to the idea that the platform is the only room."),
        ("Do I need to pay to listen here?", "No. The public player is free; optional support is not a subscription."),
        ("Why does the site keep masters offline?", "Streams are listening copies; masters are archival files kept offline."),
        ("Can I share a track?", "Yes, share the player link. Do not re-upload or sell the audio."),
    ],
)

# ---------------------------------------------------------------- why free streams
PAGES["why-free-streams.html"] = dict(
    title="Why Free Streams Exist — Streams vs Masters | asiancoastline.com",
    desc="What free streams are, what they are not, and why the Excavationpro catalog keeps masters offline while the public player stays open.",
    path="/why-free-streams.html",
    active="guides",
    h1="Why free streams exist (and what they are not)",
    lead="Streams are listening copies. Masters stay in the vault. That distinction is the whole model: open listening, closed ownership, and a clear line between the two.",
    minutes="7 min read",
    updated="2026-10-20",
    tags=["rights", "streams", "masters"],
    body=f"""
<article class="card">
  <h2>Streams vs masters</h2>
  <p>A public stream is usually a compressed file optimized for browsers and bandwidth. A master is the archival production file, often WAV or AIF, used for distribution and long-term storage. They are not the same object and they do not carry the same rights. The stream is a listening copy; the master is the source.</p>
  <p>Keeping masters offline protects the catalog while still letting people listen freely online. It also keeps the site honest about what it is: a public listening room, not a file locker. If the masters were exposed, the site would become a download site with a player attached, and the rights model would collapse.</p>
  <h2>What free streams are for</h2>
  <ul>
    <li>Fans discovering original music without a paywall.</li>
    <li>Radio-style continuous play in a browser.</li>
    <li>A sovereign path that does not depend on one distributor&rsquo;s UI.</li>
    <li>A public reference for the catalog: titles, hashes, ISRCs, and the ledger.</li>
  </ul>
  <h2>What free streams are not</h2>
  <ul>
    <li>Not a license to re-upload the audio to another platform as your own.</li>
    <li>Not permission to sell the files or include them in a paid product.</li>
    <li>Not a transfer of ownership, exclusivity, or sync rights.</li>
    <li>Not a promise that every track will stay online forever.</li>
  </ul>
</article>
{AD}
<article class="card">
  <h2>Why give the streams away?</h2>
  <p>Because the first encounter should be a listen, not a negotiation. A preview behind a storefront is a sales pitch; a full stream is a relationship. The catalog is large and independent, and the artist would rather have a smaller circle of people who heard the whole piece than a dashboard full of thirty-second previews that bounced.</p>
  <p>There is also a practical reason. Most independent catalogs never earn back the anxiety of distribution. Keeping a direct listening room means the work is still reachable if a platform changes its terms, delists a track, or disappears. The platform is a map; the room is the place.</p>
  <h2>What support means</h2>
  <p>Optional support through PayPal helps cover hosting, storage, and time. It is a gift, not a subscription. It does not buy exclusivity, a custom track, or a say in the catalog. The music stays free to hear either way.</p>
  <h2>The limits</h2>
  <p>Free listening is not the same as free licensing. If you want to use a track in a video, a game, a podcast, or a commercial project, ask first. Sync and commercial use are separate permissions. The <a href="/lyrics-and-copyright.html">lyrics and copyright guide</a> covers the related rules for words.</p>
</article>
<article class="card faq">
  <h2>FAQ</h2>
  <h3>Can I download the streams?</h3>
  <p>The player is a listening room, not a download store. The terms describe the listening license.</p>
  <h3>Can I use a track in my video?</h3>
  <p>Ask first. Sync and commercial use are separate permissions from free listening.</p>
  <h3>Why are some tracks missing?</h3>
  <p>The public catalog changes as work is added or withdrawn. The ledger records the public snapshot; it is not a guarantee of permanent availability.</p>
  <h3>Does free mean public domain?</h3>
  <p>No. Free listening is a permission to listen, not a transfer of ownership or a waiver of copyright.</p>
</article>
{related("why-free-streams.html")}
{AUTHOR}
""",
    faqs=[
        ("Can I download the streams?", "The player is a listening room, not a download store."),
        ("Can I use a track in my video?", "Ask first. Sync and commercial use are separate permissions."),
        ("Why are some tracks missing?", "The public catalog changes; the ledger records a snapshot, not permanent availability."),
        ("Does free mean public domain?", "No. Free listening is a permission to listen, not a waiver of copyright."),
    ],
)

# ---------------------------------------------------------------- how streaming works
PAGES["how-free-streaming-works.html"] = dict(
    title="How Browser Music Streaming Works | asiancoastline.com",
    desc="What happens when you press play in a browser player: audio files, bitrate, buffering, caching, data use, and why this player does not need an account.",
    path="/how-free-streaming-works.html",
    active="guides",
    h1="How browser music streaming works",
    lead="A browser player is a small negotiation between a file, a codec, a network, and a speaker. Understanding the pieces explains why a track starts in a second, why it sometimes stalls, and why no account is required.",
    minutes="6 min read",
    updated="2026-10-20",
    tags=["streaming", "browser", "technical"],
    body=f"""
<article class="card">
  <h2>The file and the codec</h2>
  <p>The public catalog is stored as compressed audio files, usually MP3 for browser compatibility. Compression removes detail the ear is less likely to notice, which is why a stream is smaller than a master. The browser receives the file, decodes it, and sends the result to the audio output.</p>
  <p>The player does not need a special app because every modern browser can decode MP3. That is the entire reason this portal can be a URL instead of an install. The trade-off is that a compressed stream is not the archival master; it is a listening copy.</p>
  <h2>Buffering and the network</h2>
  <p>When you press play, the browser requests the file and buffers a small amount before it starts. If the network is slow, the buffer empties and playback stalls. If the network is fast, the browser may read ahead so a brief hiccup does not stop the track. The progress bar is not only a position; it is also a picture of how much has been fetched.</p>
  <p>Streaming uses data for the whole session, not just the first few seconds. A long listening session can consume hundreds of megabytes. On a metered connection, shorter sessions or lower volume (which does not reduce data, but reduces the temptation to leave it running) are the practical controls.</p>
</article>
{AD}
<article class="card">
  <h2>Why there is no account</h2>
  <p>A platform account exists to personalize, to bill, and to remember. This player does none of those things. Favorites and queue are stored in your browser&rsquo;s local storage; the catalog is public; there is no profile to sync. That is why the player can open without a signup and why clearing your browser storage also clears your favorites.</p>
  <h2>Caching and the installed app</h2>
  <p>The installed version uses a service worker to cache the shell &mdash; the page, styles, and basic scripts. It does not cache the entire catalog. Audio still streams from the public files. The install improves the launch experience and keeps the interface available on a weak connection; it is not an offline music library.</p>
  <h2>What the ledger adds</h2>
  <p>The ledger records a public snapshot: titles, hashes, and catalog metadata. It is a reference, not a playback mechanism. If a stream file moves, the ledger still tells you what the catalog expected. That is useful for verification and for understanding why a link broke, but it does not replace the file.</p>
  <h2>Privacy at the network layer</h2>
  <p>The hosting provider and the audio host see standard request data: IP address, user agent, and the file requested. The player does not require an identity, and the site does not build a listening profile. The <a href="/privacy.html">privacy policy</a> explains the advertising and consent layer separately.</p>
</article>
<article class="card faq">
  <h2>FAQ</h2>
  <h3>Why does a track buffer?</h3>
  <p>The browser has not fetched enough audio to start, or the network is slower than the playback rate. Try again or choose a smaller file.</p>
  <h3>Does the player download the whole song?</h3>
  <p>The browser fetches the audio it needs for playback; it may read ahead. It is still a stream, not a saved download.</p>
  <h3>Can I listen offline?</h3>
  <p>The installed shell may open offline, but the audio streams from the public files. Full offline listening requires files you own.</p>
  <h3>Is the stream the master?</h3>
  <p>No. The stream is a compressed listening copy. Masters stay offline.</p>
</article>
{related("how-free-streaming-works.html")}
{AUTHOR}
""",
    faqs=[
        ("Why does a track buffer?", "The browser has not fetched enough audio, or the network is slower than playback."),
        ("Does the player download the whole song?", "It fetches audio for playback and may read ahead; it is still a stream."),
        ("Can I listen offline?", "The installed shell may open offline, but audio streams from the public files."),
        ("Is the stream the master?", "No. The stream is a compressed listening copy; masters stay offline."),
    ],
)

# ---------------------------------------------------------------- lyrics/copyright
PAGES["lyrics-and-copyright.html"] = dict(
    title="Lyrics and Copyright: What You Can Share | asiancoastline.com",
    desc="How lyrics copyright works for listeners: personal use, quoting with attribution, no re-upload, sync and AI training, and how to request permission.",
    path="/lyrics-and-copyright.html",
    active="guides",
    h1="Lyrics and copyright: what you can share",
    lead="Lyrics are a written work inside a song. Listening free does not make the words free to republish, sell, or feed to a commercial model. Here is the practical line.",
    minutes="6 min read",
    updated="2026-10-20",
    tags=["lyrics", "copyright", "rights"],
    body=f"""
<article class="card">
  <h2>Lyrics are their own copyright</h2>
  <p>A song usually contains at least two copyrights: the composition (words and melody) and the sound recording. The lyrics page on this site is a reference for listeners, not a public-domain text dump. The words are protected even when the stream is free to hear.</p>
  <p>That means you can listen, quote a short line in a review with attribution, and link to the page. You cannot copy the full lyric into another site, print it on merchandise, or include it in a commercial product without permission.</p>
  <h2>What is usually fine</h2>
  <ul>
    <li>Quoting a line or two in a review, essay, or classroom discussion, with attribution.</li>
    <li>Linking to the lyric page instead of copying it.</li>
    <li>Singing along, performing privately, or using the words in a personal notebook.</li>
    <li>Discussing the meaning, structure, or imagery without reproducing the whole text.</li>
  </ul>
  <h2>What needs permission</h2>
  <ul>
    <li>Republishing a full lyric on another website or app.</li>
    <li>Printing lyrics on merchandise, posters, or packaging for sale.</li>
    <li>Using lyrics in a video, podcast, game, or ad (sync and commercial use).</li>
    <li>Feeding the lyrics into a commercial model or dataset for resale.</li>
  </ul>
</article>
{AD}
<article class="card">
  <h2>Sync, samples, and AI</h2>
  <p>A sync license is the permission to pair music or lyrics with moving images. It is separate from listening and separate from mechanical reproduction. If you want to use a track in a video, ask before you publish, even if the video is free.</p>
  <p>AI training is its own permission question. A public stream is not a license to train a commercial model on the catalog and sell a derivative. If you are researching or building a personal tool, say so and ask; the answer may still be no, but the request is the honest starting point.</p>
  <h2>How to request permission</h2>
  <p>Email <a href="mailto:excavationstation@gmail.com?subject=Asian%20Coastline%20permission">excavationstation@gmail.com</a> with the track title, the intended use, the platform, and whether money is involved. A clear request gets a clear answer faster than a vague one. If the use is commercial, include a timeline.</p>
  <p>If you are unsure whether your use is personal or commercial, describe it plainly. The <a href="/terms.html">terms</a> and the <a href="/why-free-streams.html">streams vs masters guide</a> explain the listening license; this page is about the words.</p>
</article>
<article class="card faq">
  <h2>FAQ</h2>
  <h3>Can I quote a lyric in a review?</h3>
  <p>A short quotation with attribution is usually fine. Reproducing the full lyric is not.</p>
  <h3>Can I put lyrics on a T-shirt?</h3>
  <p>Not without permission. Merchandise is a commercial use of the composition.</p>
  <h3>Can I use a song in my YouTube video?</h3>
  <p>Ask first. That is a sync use, not the same as listening free on the site.</p>
  <h3>Can I train an AI on the lyrics?</h3>
  <p>A public stream is not a training license. Ask before using the catalog in a commercial model.</p>
</article>
{related("lyrics-and-copyright.html")}
{AUTHOR}
""",
    faqs=[
        ("Can I quote a lyric in a review?", "A short quotation with attribution is usually fine; reproducing the full lyric is not."),
        ("Can I put lyrics on a T-shirt?", "Not without permission; merchandise is a commercial use."),
        ("Can I use a song in my YouTube video?", "Ask first; that is a sync use, not the same as free listening."),
        ("Can I train an AI on the lyrics?", "A public stream is not a training license; ask first."),
    ],
)

# ---------------------------------------------------------------- artist checklist
PAGES["independent-artist-checklist.html"] = dict(
    title="Independent Artist Release Checklist | asiancoastline.com",
    desc="A practical checklist for independent releases: rights, masters, metadata, ISRC, cover art, distribution, your own player, promotion, and royalties.",
    path="/independent-artist-checklist.html",
    active="guides",
    h1="Independent artist release checklist",
    lead="A release is not one upload. It is a chain of small decisions: who owns the master, what the metadata says, where the files live, and how a listener can find you without a platform in the middle.",
    minutes="8 min read",
    updated="2026-10-20",
    tags=["artists", "release", "checklist"],
    body=f"""
<article class="card">
  <h2>1. Rights and masters</h2>
  <p>Before you distribute anything, know who owns the master and the composition. If you recorded with a collaborator, get the split in writing. If you used a sample, clear it or replace it. A release with an uncleared sample is a liability that follows the catalog, not a small detail you can fix after launch.</p>
  <p>Keep the archival masters in a place you control, in a lossless format, with a backup. The public stream is a compressed copy; the master is the asset. The <a href="/why-free-streams.html">streams vs masters guide</a> explains the difference.</p>
  <h2>2. Metadata</h2>
  <ul>
    <li>Artist name, track title, album, release date, and genre &mdash; consistent everywhere.</li>
    <li>ISRC for each recording; a separate code for each distinct version.</li>
    <li>Composer and publisher credits, splits, and contact information.</li>
    <li>Explicit-content flags where required, and correct language tags.</li>
  </ul>
  <p>Bad metadata is the most common reason a release is hard to find, hard to pay, or hard to correct later. Write it down once in a master spreadsheet and copy it; do not retype it into every platform.</p>
</article>
{AD}
<article class="card">
  <h2>3. Artwork and files</h2>
  <p>Use a square cover at the distributor&rsquo;s required resolution, with no unlicensed images or fonts. Keep a clean version without text for reuse. Deliver the audio in the format the distributor asks for, and keep the lossless master separate from the streaming copy.</p>
  <h2>4. Distribution and your own room</h2>
  <p>A distributor gets you into platforms; it does not give you a home. Put the release on your own site too: a player, a page with credits, and a way to contact you. That page is the one you control if a platform changes terms or delists the track.</p>
  <p>This site is an example of the own-room model: a free browser player, a public catalog, and a clear listening license. You do not need a 10,000-track catalog to do it; you need one page that works.</p>
  <h2>5. Promotion without spam</h2>
  <p>Pick the three places your actual listeners are and tell them once, clearly. A direct message to a friend who likes the genre is worth more than a mass post. Share the player link, not a re-upload. If you pitch a playlist or a blog, include the one-sentence reason it fits.</p>
  <h2>6. Money and records</h2>
  <p>Track royalties, splits, and expenses in one place from the first release. Register with a performance rights organization if you perform or broadcast; keep receipts; pay collaborators on the agreed schedule. A small catalog with clean books is easier to grow than a large one with a mystery spreadsheet.</p>
</article>
<article class="card faq">
  <h2>FAQ</h2>
  <h3>Do I need a distributor?</h3>
  <p>If you want platform reach, usually yes. You still need your own page and a direct way for listeners to find you.</p>
  <h3>What is an ISRC?</h3>
  <p>A unique code for a recording. It helps platforms and royalty systems identify the track. Each distinct recording needs its own.</p>
  <h3>Can I release without a label?</h3>
  <p>Yes. The checklist is the label work: rights, metadata, files, distribution, promotion, and books.</p>
  <h3>Where should the master live?</h3>
  <p>In a lossless format, on storage you control, with a backup. The public stream is a compressed copy, not the archive.</p>
</article>
{related("independent-artist-checklist.html")}
{AUTHOR}
""",
    faqs=[
        ("Do I need a distributor?", "For platform reach usually yes; you still need your own page and direct listener path."),
        ("What is an ISRC?", "A unique code for a recording, used by platforms and royalty systems."),
        ("Can I release without a label?", "Yes. The checklist is the label work."),
        ("Where should the master live?", "In a lossless format on storage you control, with a backup."),
    ],
)


# ---------------------------------------------------------------- guides index
PAGES["guides.html"] = dict(
    title="Music Portal Guides: Player, Rights, Streaming | asiancoastline.com",
    desc="Original guides for the free Excavationpro player: how to use it, independent listening, streams vs masters, browser streaming, lyrics, and releasing music.",
    path="/guides.html",
    active="guides",
    h1="Music portal guides",
    lead="Six practical guides for listening, rights, and releasing independent music. Start with the player, then choose the question you actually have.",
    minutes="4 min read",
    updated="2026-10-20",
    tags=["guides", "listening", "rights"],
    body="""
<article class="card">
  <h2>Start with the job in front of you</h2>
  <p>Most visitors arrive with one of four questions: how do I use the player, why is the music free, how does browser streaming work, or what am I allowed to do with the lyrics? The guides are organized around those jobs instead of around keywords.</p>
  <p>If you are new, read <a href="/how-to-use-the-player.html">How to use the free listen player</a> first. It covers search, filters, keyboard shortcuts, favorites, radio, crossfade, sleep, and install. If you are an artist, start with the <a href="/independent-artist-checklist.html">release checklist</a> and the <a href="/why-free-streams.html">streams vs masters guide</a>.</p>
</article>
<article class="card">
  <h2>All guides</h2>
  <div class="grid2">
    <a class="tile" href="/how-to-use-the-player.html"><strong>How to use the player</strong><span>Search, filters, shortcuts, favorites, queue, radio, crossfade, sleep, and PWA install.</span></a>
    <a class="tile" href="/independent-music-listening.html"><strong>Independent listening</strong><span>What a curated portal gives you that a platform feed does not.</span></a>
    <a class="tile" href="/why-free-streams.html"><strong>Why free streams exist</strong><span>Streams vs masters, what free means, and what it does not permit.</span></a>
    <a class="tile" href="/how-free-streaming-works.html"><strong>How browser streaming works</strong><span>Files, codecs, buffering, data use, caching, and privacy.</span></a>
    <a class="tile" href="/lyrics-and-copyright.html"><strong>Lyrics and copyright</strong><span>Quoting, republishing, sync, merchandise, and AI training.</span></a>
    <a class="tile" href="/independent-artist-checklist.html"><strong>Independent artist checklist</strong><span>Rights, metadata, ISRC, artwork, distribution, promotion, and books.</span></a>
  </div>
</article>
<article class="card">
  <h2>How these guides are made</h2>
  <p>Each guide is written to answer a real listening or release question, not to fill a page. Where a claim can be checked against the player or the catalog, it is. Where a rule is a copyright convention rather than a technical fact, the guide says so and points to the terms or the contact page.</p>
  <p>The free player is at <a href="/listen.html">/listen.html</a>; the public catalog ledger is inside it. If a guide raises a question that is not answered, the <a href="/contact.html">contact page</a> is the fastest route.</p>
</article>
""",
)

# ---------------------------------------------------------------- about
PAGES["about.html"] = dict(
    title="About asiancoastline.com — Free Excavationpro Player",
    desc="Who publishes asiancoastline.com, why the free player exists, how the catalog is maintained, the editorial standard, and how advertising works.",
    path="/about.html",
    active="about",
    h1="About asiancoastline.com",
    lead="A free public listening room for the Excavationpro catalog, published by Justin Helmer. No account, no storefront, and a clear line between streams and masters.",
    minutes="3 min read",
    updated="2026-10-20",
    tags=["about", "publisher"],
    body="""
<article class="card">
  <h2>What this site is</h2>
  <p>asiancoastline.com is the public listen domain for Justin Helmer / Excavationpro. The player carries the music catalog and the Eternal Haven audio in a browser, without an account. The catalog is the artist&rsquo;s own, not a licensed subset, and the site states the listening terms plainly.</p>
  <p>It is part of the same workshop as <a href="https://excavationpro.ca/">excavationpro.ca</a> (music and essays), <a href="https://bpmfinder.ca/">bpmfinder.ca</a> (tempo tools), <a href="https://deepseekoracle.com/">deepseekoracle.com</a> (AI and creator guides), <a href="https://eternalhaven.ca/">eternalhaven.ca</a> (books and games), <a href="https://chatagent.ca/">chatagent.ca</a> (AI agent guides), and <a href="https://justinhelmer.ca/">justinhelmer.ca</a> (artist portal).</p>
  <h2>Why it exists</h2>
  <p>The first encounter with music should be a listen, not a negotiation. A platform feed is useful for discovery, but it is not the only room. This site keeps a direct listening room that survives platform changes, delistings, and recommendation algorithms. The player is intentionally simple: search, play, queue, radio, and a ledger, with no account wall.</p>
  <h2>How the catalog is maintained</h2>
  <p>Public streams are compressed listening copies. Masters stay offline in the vault. The ledger records a public snapshot of the catalog &mdash; titles, hashes, and metadata &mdash; so the public record can be checked even when a file moves. New work is added to the catalog deliberately; the site is curated, not an infinite upload feed.</p>
  <h2>Editorial standard</h2>
  <ul>
    <li>Original writing, not scraped or auto-spun text.</li>
    <li>One real job per guide; no doorway pages or keyword stuffing.</li>
    <li>Visible byline and update date on every guide.</li>
    <li>Advertising is labelled and kept off the player, policy, and error pages.</li>
    <li>Corrections are made in place and the update date changes.</li>
  </ul>
  <h2>Advertising and contact</h2>
  <p>This site may show Google AdSense advertising on editorial pages to support hosting and time. The player stays ad-free. The <a href="/privacy.html">privacy policy</a> explains cookies and consent. Contact: <a href="mailto:excavationstation@gmail.com">excavationstation@gmail.com</a> with &ldquo;Asian Coastline&rdquo; in the subject.</p>
</article>
{AUTHOR}
""",
)

# ---------------------------------------------------------------- privacy
PAGES["privacy.html"] = dict(
    title="Privacy Policy — asiancoastline.com",
    desc="How asiancoastline.com handles streaming, logs, cookies, Google AdSense, consent, third parties, and privacy requests.",
    path="/privacy.html",
    active="privacy",
    h1="Privacy Policy — asiancoastline.com",
    lead="This policy explains what happens when you stream a track, read a guide, or see an ad. The short version: no account is required, and the player does not build a listening profile.",
    minutes="4 min read",
    updated="2026-10-20",
    tags=["privacy"],
    body="""
<article class="card">
  <h2>Streaming and logs</h2>
  <p>The player requests public audio files from a hosting provider. Like most websites, that provider may process standard technical logs such as IP address, user agent, requested URL, and timestamps for security and reliability. The player does not require an identity and does not create an account-level listening history.</p>
  <p>Favorites, queue, and the cookie choice are stored locally in your browser. Clearing site data removes them. They are not synced to a server.</p>
  <h2>Cookies and advertising</h2>
  <p>We may use cookies or similar storage for essential site function, such as remembering your cookie choice. When Google AdSense is active on editorial pages, Google and its partners may use cookies or device information to serve and measure ads, including ads based on visits to this site or other sites.</p>
  <p>The AdSense publisher ID for this site is <code>ca-pub-0646320966060599</code>. You can review Google&rsquo;s advertising controls at <a href="https://policies.google.com/technologies/ads">policies.google.com/technologies/ads</a> and manage personalized ads at <a href="https://adssettings.google.com/">adssettings.google.com</a>. Blocking advertising cookies may affect personalization but does not lock the player or the guides.</p>
  <h2>Consent</h2>
  <p>The site shows a cookie banner with Accept and Decline. Your choice is stored locally. If you decline, the banner will not keep asking on every page. You can change the choice by clearing the site&rsquo;s local storage in your browser settings.</p>
  <h2>Third parties</h2>
  <ul>
    <li><strong>GitHub Pages</strong> &mdash; hosts the static site and may keep standard access logs.</li>
    <li><strong>Hugging Face</strong> &mdash; hosts the public stream files; its own terms and logs apply.</li>
    <li><strong>Google AdSense</strong> &mdash; serves advertising on editorial pages when active.</li>
    <li><strong>PayPal</strong> &mdash; handles optional support payments under its own policy.</li>
  </ul>
  <h2>Retention and children</h2>
  <p>We do not maintain reader accounts or an uploaded-audio database. Email correspondence is kept only as long as needed to answer the request. This is a general music site; we do not knowingly collect personal information from children, and no account is required.</p>
  <h2>Changes and contact</h2>
  <p>If this policy changes, the update date at the top of the page will change. For privacy questions, email <a href="mailto:excavationstation@gmail.com">excavationstation@gmail.com</a> with &ldquo;Asian Coastline privacy&rdquo; in the subject. See also the <a href="/terms.html">terms of use</a>.</p>
</article>
""",
)

# ---------------------------------------------------------------- terms
PAGES["terms.html"] = dict(
    title="Terms of Use — asiancoastline.com",
    desc="The terms for listening on asiancoastline.com: the listening license, acceptable use, intellectual property, warranty and liability limits.",
    path="/terms.html",
    active="terms",
    h1="Terms of use — asiancoastline.com",
    lead="These terms cover the free player and the guides. By using the site, you agree to them. The short version: listen freely, do not re-upload or sell the files.",
    minutes="3 min read",
    updated="2026-10-20",
    tags=["terms", "license"],
    body="""
<article class="card">
  <h2>License to listen</h2>
  <p>You may stream the public catalog for personal listening, share links to the player, and quote short passages from the guides with attribution. You may not re-upload the audio files, sell them, include them in a paid product, or present them as your own. The stream is a listening copy, not a transfer of ownership.</p>
  <h2>Acceptable use</h2>
  <ul>
    <li>Do not use the site to break the law or infringe someone else&rsquo;s rights.</li>
    <li>Do not attempt to disrupt the site, scrape it at abusive volume, or bypass security controls.</li>
    <li>Do not use the catalog in a commercial video, game, or ad without permission.</li>
    <li>Do not feed the lyrics or audio into a commercial model for resale.</li>
  </ul>
  <h2>Intellectual property</h2>
  <p>The music, lyrics, guides, and site design are owned by Justin Helmer / Excavationpro unless otherwise stated. The player and catalog may not be rebranded or resold. Short quotations from the guides are allowed with a link back to the page.</p>
  <h2>No warranty</h2>
  <p>The site and player are provided as-is, without warranties of any kind, including fitness for a particular purpose and non-infringement. Streams may be unavailable, a track may be withdrawn, or a browser may fail to play a file. You are responsible for verifying anything you rely on.</p>
  <h2>Limitation of liability</h2>
  <p>To the maximum extent permitted by law, Justin Helmer / Excavationpro is not liable for indirect, incidental, special, or consequential damages arising from use of the site or player, including lost work, lost revenue, or damage to a device.</p>
  <h2>Changes and contact</h2>
  <p>These terms may be updated; the date at the top of the page will change when they are. Questions: <a href="mailto:excavationstation@gmail.com">excavationstation@gmail.com</a> with &ldquo;Asian Coastline terms&rdquo; in the subject. See also the <a href="/privacy.html">privacy policy</a>.</p>
</article>
""",
)

# ---------------------------------------------------------------- contact
PAGES["contact.html"] = dict(
    title="Contact asiancoastline.com — Publisher & Support",
    desc="Contact asiancoastline.com about the player, a broken stream, a guide correction, privacy requests, or optional support.",
    path="/contact.html",
    active="contact",
    h1="Contact asiancoastline.com",
    lead="Questions about the player, a broken stream, a guide correction, a privacy request, or a permission question &mdash; email is the reliable route.",
    minutes="2 min read",
    updated="2026-10-20",
    tags=["contact"],
    body="""
<article class="card">
  <h2>Email</h2>
  <p><a href="mailto:excavationstation@gmail.com?subject=Asian%20Coastline">excavationstation@gmail.com</a></p>
  <p>Please put <strong>&ldquo;Asian Coastline&rdquo;</strong> in the subject and allow a few business days for a reply. This is a small independent project, not a support desk.</p>
  <h2>What to include</h2>
  <ul>
    <li>For a player issue: the browser, the track title, and what you saw (an error, silence, a stall).</li>
    <li>For a broken stream: the track title or the URL, and whether other tracks play.</li>
    <li>For a guide correction: the page URL and the sentence you think is wrong.</li>
    <li>For a privacy request: the email you used and what you want changed or removed.</li>
    <li>For a permission request: the track, the intended use, the platform, and whether money is involved.</li>
  </ul>
  <p>Do not send passwords, API keys, or private audio you do not want a stranger to hear.</p>
  <h2>Publisher and support</h2>
  <p>Justin Helmer &middot; Canada. The site is part of the Excavationpro / LYGO workshop. Optional support through <a href="https://www.paypal.com/paypalme/ExcavationPro">PayPal.me/ExcavationPro</a> helps with hosting and time; it does not buy a custom track or a guarantee of support.</p>
  <h2>Policy pages</h2>
  <p><a href="/privacy.html">Privacy policy</a> &middot; <a href="/terms.html">Terms of use</a> &middot; <a href="/about.html">About the site</a></p>
</article>
""",
)
