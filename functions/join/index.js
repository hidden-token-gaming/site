// The join page with how many members are on the Discord right now (site#33).
//
// The page is static; this Function adds one number to it on each request, server-side: the
// online count (presence_count) from Discord's server widget, which answers with no token while
// the widget is on (Server Settings → Widget). The browser gets plain HTML and makes no
// third-party request, so the site's CSP stays as it is. The widget also lists online members'
// names; they are read only to leave HTG's own bots out of the count, and nothing is stored or
// logged.
//
// Without a count (the widget off, Discord slow or down, an answer that isn't a count), or with
// nobody on, the page is served as built: the element stays hidden. "0 online" would only put a
// newcomer off, and the page never shows a number it can't stand behind. Either way the answer says what it found in
// x-online-now (the count, or "unknown"), so the Function can be seen at work.
//
// _headers isn't applied to a Function's response (Cloudflare Pages, "Headers"), so the site-wide
// headers are set here too. functions/headers.test.mjs fails CI if this copy and static/_headers'
// "/*" block differ.

const WIDGET = "https://discord.com/api/guilds/519496143298756611/widget.json";

// HTG's bots, by the names the widget shows them under (their nicknames in the server: deploy
// discord/mapping.md, R1). They are always online, so presence_count, which counts them, would
// say four with one person on. A rename here goes with a rename there.
export const BOTS = ["HAL 9000", "HTG · Guard", "HTG · Support"];

// peopleOnline is the widget's online count without HTG's bots; null when the answer has no count.
// The widget lists at most 100 members, so past 100 a bot may be missing from the list and counted:
// three too many at most, at a size where it doesn't matter.
export function peopleOnline(widget) {
  const n = widget?.presence_count;
  if (!Number.isInteger(n) || n < 0) return null;
  const members = Array.isArray(widget.members) ? widget.members : [];
  const bots = members.filter((m) => BOTS.includes(m?.username)).length;
  return Math.max(0, n - bots);
}

export const SECURITY_HEADERS = {
  "Content-Security-Policy":
    "default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'",
  "Referrer-Policy": "strict-origin-when-cross-origin",
  "X-Content-Type-Options": "nosniff",
  "Permissions-Policy": "camera=(), microphone=(), geolocation=(), interest-cohort=()",
  "Strict-Transport-Security": "max-age=31536000",
};

// countText is what the page says for n online.
export function countText(n) {
  return `<strong>${n} ${n === 1 ? "member" : "members"} online</strong> in the Discord right now.`;
}

// onlineCount reads the widget, at most once a minute per Cloudflare location: the people online,
// null without a count.
async function onlineCount() {
  try {
    const res = await fetch(WIDGET, {
      cf: { cacheTtl: 60, cacheEverything: true },
      signal: AbortSignal.timeout(2000),
    });
    if (!res.ok) return null;
    return peopleOnline(await res.json());
  } catch {
    return null;
  }
}

export async function onRequestGet(context) {
  const page = await context.next();
  const headers = new Headers(page.headers);
  for (const [name, value] of Object.entries(SECURITY_HEADERS)) headers.set(name, value);
  const served = new Response(page.body, { status: page.status, statusText: page.statusText, headers });
  if (!page.ok || !(page.headers.get("content-type") || "").includes("text/html")) return served;
  const n = await onlineCount();
  served.headers.set("x-online-now", n === null ? "unknown" : String(n));
  if (n === null || n === 0) return served;
  return new HTMLRewriter()
    .on("[data-online-now]", {
      element(el) {
        el.removeAttribute("hidden");
        el.setInnerContent(countText(n), { html: true });
      },
    })
    .transform(served);
}
