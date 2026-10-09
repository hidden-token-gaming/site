# brand

Hidden Token Gaming's logo, colours and artwork: the mark, the lockups, the link-preview card, the
Discord server icon and the War Dogs server banner (#6).

![Hidden Token Gaming](logo/png/htg-lockup@2x.png)

## Where the name comes from

In the 1990s, John worked at a video arcade. When his friends came in, they said it was like he had a
"hidden token": he could play any machine he liked. That's the idea behind HTG: a place where you
always have a game to play.

The mark is two arcade tokens, with the second one hidden behind the first. There's always another
game.

## The one-liner

> Your hidden token to always having a game to play. Variety gaming for adults who play fair. 18+.

HTG's description wherever one line is shown: the Discord server description (invites and
Discovery), the site's meta and link-preview description, the GitHub org, listing sites, and the
Steam, RSI and Twitch pages. Use it word for word. It names no games, so it doesn't change when the
line-up does (John, 2026-10-03). Discord allows 120 characters; this is 96.

## The mark

- Two chrome tokens, struck like real coins: a raised rim, raised beads and a star stamped into the
  face. Light comes from the top left. The back token is darker and partly hidden.
- A glow surrounds the pair, running green, then a wide band of blue, then purple. It follows the
  chrome's angle, from top left to bottom right. The glow sits only outside the two tokens, never
  between them.
- The one-colour version swaps the shading for cut-outs and a thin gap between the tokens. Use it on
  light backgrounds, in a single colour, or at 24 px and below.

| File | Use |
|---|---|
| [`logo/htg-mark.svg`](logo/htg-mark.svg) | The main mark, full colour with glow, on dark backgrounds |
| [`logo/htg-mark-noglow.svg`](logo/htg-mark-noglow.svg) | Full colour without the glow, for 64 px and below |
| [`logo/htg-mark-mono.svg`](logo/htg-mark-mono.svg) | One colour (`currentColor`), for light backgrounds and small sizes |
| [`logo/htg-mark-auto.svg`](logo/htg-mark-auto.svg) | Follows the viewer's colour scheme: full colour without the glow in dark mode, one colour in ink (`#0b1222`, the light theme's text) in light mode. For a logo or favicon that has to be one file in both schemes, such as the hub's on app.hiddentoken.com |
| [`logo/htg-lockup.svg`](logo/htg-lockup.svg) | Mark plus wordmark, side by side, on dark backgrounds |
| [`logo/htg-lockup-stacked.svg`](logo/htg-lockup-stacked.svg) | Mark above the wordmark, on dark backgrounds |
| [`logo/htg-lockup-mono.svg`](logo/htg-lockup-mono.svg) | Side-by-side lockup in ink, for light backgrounds |
| [`logo/png/`](logo/png/) | PNG renders: the mark at 1024 to 128 px, without glow at 64 and 32 px, one colour at 512 px in black and white, and each lockup at 2× |
| [`social/og-image-1200x630.png`](social/og-image-1200x630.png) | The link-preview card (`og:image`): the main lockup on the dark ground, 1200×630. The site serves it on every page |
| [`discord/server-icon-512.png`](discord/server-icon-512.png) | The Discord server icon |
| [`wardogs/server-banner-1024x256.png`](wardogs/server-banner-1024x256.png) | The War Dogs server-browser banner (`ServerImageURL`) |

### Using it

- Put full-colour versions on the dark ground (`#070b17`) or something close to it. Chrome and the
  glow disappear on light backgrounds; use the one-colour version there.
- Where one file has to serve both colour schemes, use `htg-mark-auto.svg`. An internal
  `<style>` switches it on `prefers-color-scheme`, which browsers apply when the file is an image
  or a favicon. It follows the viewer's setting, not the page's background, so use it only on pages
  that follow the setting too.
- Leave clear space around the mark of at least a quarter of its width.
- Don't recolour, stretch, rotate or outline the tokens, and don't add effects.
- **Never combine the mark with game logos, game art or look-alikes.** HTG's identity is its own;
  the [publisher rules](../content/legal/publisher-rules.md) say what each publisher allows.

## Variations

The one-colour mark with another emblem struck into the front token, in place of the star. Staff,
events, services and each game share the family look and can still be told apart at a glance. They
are for channel and category art, bot avatars, event posts and the site. Discord role icons need a
level 2 server boost, which the server doesn't have yet.

| Variation | Emblem | For | Colour |
|---|---|---|---|
| [`staff`](logo/variations/htg-mark-staff.svg) | Shield | Staff: HMFIC, Admin, Moderators | `#f1c40f` |
| [`host`](logo/variations/htg-mark-host.svg) | Arcade prize ticket | Event hosts and events | `#8a63f5` |
| [`supporter`](logo/variations/htg-mark-supporter.svg) | Heart | Supporters, when they launch | none yet |
| [`seeding`](logo/variations/htg-mark-seeding.svg) | Seedling | Seeding the War Dogs server | `#3ee07a` |
| [`bot`](logo/variations/htg-mark-bot.svg) | Bot | The HTG bot: avatar and bot posts | `#3d8bff` |
| [`muster`](logo/variations/htg-mark-muster.svg) | Rally flag | Muster, the crew-up service (later) | `#3d8bff` |
| [`sot`](logo/variations/htg-mark-sot.svg) | Anchor | Sea of Thieves | `#1abc9c` |
| [`sc`](logo/variations/htg-mark-sc.svg) | Ringed planet | Star Citizen | `#3498db` |
| [`wd`](logo/variations/htg-mark-wd.svg) | Dog tag | War Dogs | `#95a5a6` |
| [`cs`](logo/variations/htg-mark-cs.svg) | Crosshair | Counter-Strike 2 | `#f39c12` |
| [`pubg`](logo/variations/htg-mark-pubg.svg) | Parachute | PUBG: BATTLEGROUNDS | `#e74c3c` |

- Every emblem is HTG's own symbol. None is, or imitates, a game's logo or art, which the
  publisher rules forbid. Add a game's variation the same way: an HTG symbol for how the community
  plays it, never the game's mark.
- **Colours:** staff and the games use their Discord role colours (Moderator, Game Lead), so the
  art and Discord agree. Events use the brand purple, which means "events" in the kit. Every colour
  is at least 3:1 on the dark ground and on Discord's dark theme. Supporters get a colour when they
  launch. On light backgrounds, use ink.
- **Files:** each SVG takes its colour from `currentColor`. `logo/variations/png/` has each one at
  512 px in white and in ink, and at 256 px in its colour. `logo/variations/variations.json` lists
  them for tools.
- Like the main mark, they read as a plain token at 24 px and below.

## Wordmark

"HIDDEN TOKEN" is set in [Archivo](https://github.com/Omnibus-Type/Archivo) at weight 800 and its
widest width (125), in chrome. "GAMING" sits below in Archivo 600, tracked out at 0.55em, with a thin
green-blue-purple line beside it, centred on the capitals. The stacked lockup puts a line on each
side of "GAMING". The one-colour lockup uses a solid slate line.

Archivo is under the SIL Open Font License ([`fonts/OFL.txt`](fonts/OFL.txt)). The lockups and
banner have their text converted to outlines, so they don't need the font installed.

## Colours

Dark is the designed default. Light mode follows the visitor's system setting. The values are in
[`tokens.json`](tokens.json) and, as CSS custom properties, in [`tokens.css`](tokens.css).

| Token | Dark | Light |
|---|---|---|
| Ground | `#070b17` | `#f2f5f9` |
| Surface | `#0f1526` | `#ffffff` |
| Line | `#1f2a44` | `#d5dce6` |
| Text | `#e8eef6` (16.8:1) | `#0b1222` |
| Muted text | `#93a3bb` (7.7:1) | `#4f5d74` (6.1:1) |

| Accent | Value | Job | As text in light mode |
|---|---|---|---|
| Green (lead) | `#3ee07a` (11.4:1 on the dark ground) | Logo glow, calls to action, links, "online" | `#0a7a3a` (5.0:1) |
| Blue | `#3d8bff` (5.9:1) | "New", secondary links | `#1554d1` (6.0:1) |
| Purple | `#8a63f5` (4.9:1) | Events | `#6a3fd8` (5.8:1) |

Contrast is against that mode's ground. Every text pairing passes WCAG AA (4.5:1). Text on a green
button is the ground colour (11.4:1).

Chrome (logo and wordmark) runs `#ffffff` → `#dfe6ee` → `#7d8ca6` → `#c9d3de` → `#f4f7fb`.

## Discord

The server icon is ready to upload. A server banner and invite splash need server boost levels the
server doesn't have yet, so they aren't part of this kit.

## War Dogs banner

The server browser shows a 1024×256 image from `ServerImageURL`. War Dogs only accepts images hosted
on catbox.moe, imgbb.com or postimg.cc; any other host fails every config edit with a 422.
[`wardogs/server-banner-1024x256.png`](wardogs/server-banner-1024x256.png) is live on the HTG server
since 2026-10-02, hosted on imgbb. To change it, rebuild the banner, upload the new file and set the
new URL in the server config.

## Rebuilding

Every SVG is generated by [`tools/build.py`](tools/build.py) from the design's geometry, and every
PNG is rendered from those SVGs by [`tools/render.sh`](tools/render.sh) in headless Chrome. Change
the script, not the SVGs.

```sh
python3 -m venv .venv && .venv/bin/pip install fonttools uharfbuzz
.venv/bin/python brand/tools/build.py
brand/tools/render.sh   # needs google-chrome and ImageMagick
```
