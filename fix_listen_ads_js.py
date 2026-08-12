from pathlib import Path
import re

p = Path("listen.html")
t = p.read_text(encoding="utf-8", errors="replace")
start = t.find("// Cookie consent + AdSense")
if start < 0:
    # already fixed?
    start = t.find("// Cookie banner only")
    if start >= 0:
        print("already cleaned")
    else:
        raise SystemExit("block not found")
end_marker = t.find("// ?q= search from URL", start)
if end_marker < 0:
    end_marker = t.find("?q= search from URL", start)
if end_marker < 0:
    raise SystemExit("end not found")

if t.startswith("// Cookie banner only", start) or "// Cookie banner only" in t[start : start + 80]:
    print("already has clean banner block")
else:
    replacement = """// Cookie banner only — Google ads DISABLED on listen.html (AdSense: no ads without publisher content)
function showAdRegions() { /* no-op */ }
function pushAdUnits() { /* no-op: player shell has no Google ads */ }
function loadAdSenseScript() { /* no-op */ }
(function cookieConsent() {
  const banner = document.getElementById('cookieBanner');
  const showBanner = () => { if (banner) banner.style.display = 'block'; };
  const hideBanner = () => { if (banner) banner.style.display = 'none'; };
  const accept = () => {
    localStorage.setItem('cookiesAccepted', 'true');
    hideBanner();
  };
  const decline = () => {
    localStorage.setItem('cookiesAccepted', 'false');
    hideBanner();
  };
  const consent = localStorage.getItem('cookiesAccepted');
  if (consent === 'true' || consent === 'false') {
    hideBanner();
  } else {
    showBanner();
  }
  const acc = document.getElementById('cookieAccept');
  const dec = document.getElementById('cookieDecline');
  if (acc) acc.onclick = accept;
  if (dec) dec.onclick = decline;
  document.querySelectorAll('.btn-enable-ads, #btn-ads-settings').forEach((btn) => {
    btn.addEventListener('click', () => {
      localStorage.removeItem('cookiesAccepted');
      showBanner();
    });
  });
})();

"""
    t = t[:start] + replacement + t[end_marker:]

t = re.sub(
    r"\s*<script[^>]+pagead2\.googlesyndication\.com[^>]*>\s*</script>\s*",
    "\n",
    t,
    flags=re.I,
)
t = re.sub(r"\s*<ins class=\"adsbygoogle\"[\s\S]*?</ins>\s*", "\n", t, flags=re.I)
# remove empty ad-region boxes content that only held ads
t = re.sub(
    r'<div class="ad-region[^"]*"[^>]*>\s*</div>',
    "",
    t,
    flags=re.I,
)

p.write_text(t, encoding="utf-8")
print("size", len(t))
print("adsbygoogle", t.count("adsbygoogle"))
print("pagead2", t.count("pagead2"))
print("createElement script ads", "data-lygo-adsense" in t)
print("ok")
