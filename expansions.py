"""Extra editorial sections inserted before each page's FAQ."""

EXTRA = {}

EXTRA["how-to-use-the-player.html"] = """
<article class="card">
  <h2>A five-minute listening session</h2>
  <p>If you want a useful first session, do not start with shuffle. Pick one album from the catalog, queue the first three tracks, and turn crossfade off so you hear the transitions the artist chose. Set the sleep timer to 30 minutes if you are listening at night. Use the search box to find the album by name, then let the queue run.</p>
  <p>After three tracks, open the ledger tab and look at the hashes. The ledger is not required for listening, but it shows that the public catalog has a verifiable record. If a track fails, note the title and whether the other tracks on the same album play; that is the difference between a single missing file and a network problem.</p>
  <p>On a phone, add the player to the home screen before you start. The installed shell opens faster and avoids the browser chrome taking up the screen. If you are on a metered connection, keep the session short and avoid leaving radio running in the background for hours.</p>
</article>
"""

EXTRA["independent-music-listening.html"] = """
<article class="card">
  <h2>A simple test for any portal</h2>
  <p>When you find an independent portal, ask five questions before you invest time in it. Who owns the catalog? Can you listen without an account? Is the license stated in plain language? Can you share a link without re-uploading the file? Does it work on a phone without an app-store install?</p>
  <p>A portal that answers all five is a room worth returning to. A portal that answers none is probably a landing page for someone else&rsquo;s storefront. The answers do not need to be perfect; they need to be honest. &ldquo;We own this catalog, listening is free, do not resell the files, here is the player&rdquo; is a complete answer.</p>
  <p>This site answers those questions in the <a href="/about.html">about page</a>, the <a href="/terms.html">terms</a>, and the player itself. If you find a portal that hides the answers, treat the absence as an answer.</p>
</article>
"""

EXTRA["why-free-streams.html"] = """
<article class="card">
  <h2>How the catalog stays sustainable</h2>
  <p>Free listening still costs money. Hosting, storage, bandwidth, and the time to maintain the catalog are real expenses. This site covers them with optional support and, on the editorial pages, advertising. The player itself stays ad-free because an ad interrupting a track is a different product than an ad beside an article.</p>
  <p>The model is not &ldquo;free because nobody paid.&rdquo; It is &ldquo;free to hear, supported by people who want it to continue.&rdquo; That is a weaker guarantee than a subscription, and a more honest one. If support disappears, the catalog may shrink; the site does not pretend otherwise.</p>
  <p>If you want the work to continue, the useful actions are simple: share the player link, buy a download when one exists, or use the optional support link. Do not re-upload the files to &ldquo;help&rdquo; &mdash; that takes the work out of the artist&rsquo;s hands and adds nothing to the room.</p>
  <h2>A note on permanence</h2>
  <p>The public catalog is maintained, not guaranteed. Tracks can be withdrawn, files can move, and a stream that works today may be gone next year. The ledger records a snapshot so the public record survives a change, but a snapshot is not a promise of playback. Keep your own copy of anything you would be devastated to lose.</p>
</article>
"""

EXTRA["how-free-streaming-works.html"] = """
<article class="card">
  <h2>What good streaming looks like</h2>
  <p>A good stream starts in about a second, plays without stuttering, and keeps a consistent volume across tracks. If the start time is long, the network or the file is the likely cause. If the volume jumps, the files were mastered at different levels, which is a catalog issue rather than a player bug.</p>
  <p>Browser compatibility is usually boring: Chrome, Edge, Firefox, and Safari all decode MP3. The differences show up in background playback, media keys, and install behavior. If a feature is missing on one browser, the player still plays; the shell is a convenience, not a requirement.</p>
  <p>The best test is a short session on the connection you actually use. Start one track, skip to the middle, and let it run for two minutes. If it survives that, the rest is catalog preference rather than streaming mechanics.</p>
</article>
"""

EXTRA["lyrics-and-copyright.html"] = """
<article class="card">
  <h2>How to credit a lyric properly</h2>
  <p>A useful credit names the song, the recording artist, the songwriter if different, and the source you are quoting from. For a review, a format like &ldquo;&lsquo;line&rsquo; from &lsquo;Title&rsquo; by Excavationpro, from the asiancoastline.com lyric page&rdquo; is enough. The link matters: it lets a reader check the context instead of trusting a screenshot.</p>
  <p>Common mistakes are easy to avoid. Do not attribute a lyric to the wrong artist because a cover version is more famous. Do not present a paraphrase as an exact quote. Do not strip the songwriter credit when the composition and the recording have different owners. Do not use a lyric as a headline if the line is the whole hook and the article is commercial.</p>
  <p>If you are unsure, quote less and link more. A short, accurate quotation with a working link is better than a full reproduction with a vague credit.</p>
  <h2>What about public-domain lyrics?</h2>
  <p>Some older songs are in the public domain, but the recording of them may still be protected. A public-domain lyric does not automatically make a specific recording free to use. Check the composition and the recording separately; the <a href="/why-free-streams.html">streams vs masters guide</a> explains why those are different objects.</p>
  <p>For modern catalog music, assume the lyric is protected until you have a written reason to think otherwise. That assumption is boring, and it keeps you out of the most common copyright mistake.</p>
  <p>If you need a longer excerpt for a classroom or a private study group, keep it inside that setting and cite the source. Publishing the same excerpt on a public site is a different use with a different answer.</p>
</article>
"""

EXTRA["independent-artist-checklist.html"] = """
<article class="card">
  <h2>A 30-day release timeline</h2>
  <p><strong>Four weeks out:</strong> confirm the master, the splits, and the metadata. Order the ISRCs, finalize the cover, and upload the lossless files to your own backup. Write the release page and the one-paragraph description while the work is fresh.</p>
  <p><strong>Two weeks out:</strong> deliver to the distributor, check the preview, and fix any metadata mismatch before it goes live. Tell the three people most likely to care. Prepare three short posts: the story, the sound, and the link. Do not schedule ten posts; schedule three good ones.</p>
  <p><strong>Release week:</strong> verify the platform links, the own-site player, and the contact form. Post once on the day, once with a detail people missed, and once when a playlist or friend shares it. Answer every message that week; the release is a conversation, not a broadcast.</p>
  <p><strong>After:</strong> record what sold, what was played, and what was ignored. Pay collaborators on the agreed schedule. Keep the master and the metadata; the next release starts from the same folder.</p>
</article>
"""

EXTRA["guides.html"] = """
<article class="card">
  <h2>How to read these guides</h2>
  <p>Each guide is written to be useful on its own. If you only have two minutes, read the first section and the FAQ; the first section states the job, and the FAQ catches the common mistakes. If you are making a decision about rights, read the whole page and then the terms; the guide explains the reasoning, the terms are the actual permission.</p>
  <p>The guides are not a course and they are not a replacement for legal advice. They are a map of the questions that come up most often on this site: how to use the player, why the music is free, how streaming works, what you can do with lyrics, and how to release independent music without losing the plot.</p>
  <h2>What is not here</h2>
  <p>There is no guide to every distributor, no comparison table of every platform, and no promise that one release strategy works for everyone. Those pages age badly and usually exist to sell something. The guides here stick to the parts that stay true: rights, files, metadata, listening, and the difference between a stream and a master.</p>
  <p>If a question is missing, the <a href="/contact.html">contact page</a> is the route. A real question is a better guide idea than a keyword.</p>
  <h2>A note on links</h2>
  <p>The guides link to the player, the terms, and each other because those are the pages that answer the next question. They do not link to a distributor affiliate or a paid course. If a link is broken, the contact page is the fastest repair route.</p>
</article>
"""

EXTRA["about.html"] = """
<article class="card">
  <h2>How to verify the catalog</h2>
  <p>The player includes a ledger tab with the public catalog snapshot: hashes, titles, and metadata. The ledger is not a marketing claim; it is a reference you can compare against the files the player exposes. If a stream is missing, the ledger still shows what the catalog expected.</p>
  <p>The site also publishes a sitemap, a privacy policy, and terms. Those are the boring pages that make the rest trustworthy. If something is wrong, the contact address reaches a person, not a ticket queue.</p>
</article>
"""

EXTRA["privacy.html"] = """
<article class="card">
  <h2>Your controls</h2>
  <p>You can clear the cookie choice and local favorites through your browser&rsquo;s site-data settings. You can block third-party cookies; the player and guides still work. You can use the site without an account, and you can email a privacy request without creating one.</p>
  <p>If you use a content blocker, some ad requests may be blocked. That does not affect playback. If you want to support the site without advertising cookies, the optional support link is the direct route.</p>
</article>
"""

EXTRA["contact.html"] = """
<article class="card">
  <h2>Response times and scope</h2>
  <p>This is a small independent project, not a 24-hour support desk. Most messages get a reply within a few business days. Player bugs and broken streams are prioritized; permission requests may take longer because they need a real decision rather than a quick answer.</p>
  <p>If you are reporting a broken track, include the title and whether other tracks play. If you are reporting a guide error, include the URL and the sentence. A precise report is faster to fix than a screenshot with no context.</p>
</article>
"""
