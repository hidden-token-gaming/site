#!/usr/bin/env python3
"""Build the Hidden Token Gaming brand SVGs from the locked design.

The mark, the lockup, the Discord icon and the War Dogs banner are all generated here, so a change
to the design (or a new variation) is a change to this file, not a hand edit of an SVG. Text is
shaped with HarfBuzz (kerning included) and converted to outlines, so no SVG depends on a font.

    python3 -m venv .venv && .venv/bin/pip install fonttools uharfbuzz
    .venv/bin/python brand/tools/build.py      # writes the SVGs
    brand/tools/render.sh                      # renders the PNGs with headless Chrome

All mark geometry is in a 0-100 box. Light comes from the top left.
"""
import math
import pathlib

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

BRAND = pathlib.Path(__file__).resolve().parent.parent
FONT = BRAND / "fonts" / "Archivo[wdth,wght].ttf"

# Palette. tokens.json and tokens.css carry the same values.
GROUND = "#070b17"
INK = "#0b1222"
MUTED = "#93a3bb"
GREEN = "#3ee07a"
BLUE = "#3d8bff"
PURPLE = "#8a63f5"

CHROME = [(0, "#ffffff"), (0.38, "#dfe6ee"), (0.5, "#7d8ca6"), (0.62, "#c9d3de"), (1, "#f4f7fb")]
# The glow runs at the chrome's angle, with a wide blue band.
GLOW = [(0, GREEN), (0.12, GREEN), (0.25, BLUE), (0.75, BLUE), (0.88, PURPLE), (1, PURPLE)]
RULE = [(0, GREEN), (0.3, BLUE), (0.7, BLUE), (1, PURPLE)]

# Two tokens at 0.78 scale: the back one up and right, mostly hidden by the front one.
SCALE = 0.78
BACK = (59, 41)
FRONT = (41, 59)
R = 48 * SCALE  # token radius in the mark box


def f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def circle(cx, cy, r):
    return f"M{f(cx - r)} {f(cy)}a{f(r)} {f(r)} 0 1 0 {f(2 * r)} 0a{f(r)} {f(r)} 0 1 0 {f(-2 * r)} 0Z"


def poly(points):
    return "M" + " L".join(f"{f(x)} {f(y)}" for x, y in points) + "Z"


def star(cx, cy, outer, inner):
    return [
        (cx + (outer if i % 2 == 0 else inner) * math.cos(math.radians(-90 + 36 * i)),
         cy + (outer if i % 2 == 0 else inner) * math.sin(math.radians(-90 + 36 * i)))
        for i in range(10)
    ]


def stops(spec):
    return "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in spec)


def lin(gid, x1, y1, x2, y2, spec, user=True):
    units = ' gradientUnits="userSpaceOnUse"' if user else ""
    return f'<linearGradient id="{gid}"{units} x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}">{stops(spec)}</linearGradient>'


# ---------------------------------------------------------------- the full-colour mark

def mark_defs():
    rim_wall = ('<linearGradient id="htg-rim-wall" gradientUnits="userSpaceOnUse" x1="14" y1="14" x2="86" y2="86">'
                '<stop offset="0" stop-color="#0d1320" stop-opacity="0.75"/>'
                '<stop offset="0.45" stop-color="#0d1320" stop-opacity="0"/>'
                '<stop offset="0.55" stop-color="#ffffff" stop-opacity="0"/>'
                '<stop offset="1" stop-color="#ffffff" stop-opacity="0.85"/></linearGradient>')
    return "\n".join([
        lin("htg-coin-rim", 14, 2, 86, 98, [(0, "#ffffff"), (0.35, "#dfe6ee"), (0.5, "#7d8ca6"), (0.65, "#c9d3de"), (1, "#f4f7fb")]),
        lin("htg-coin-field", 14, 8, 86, 92, [(0, "#e3e9f0"), (0.42, "#bfc9d6"), (0.55, "#8d9ab0"), (0.7, "#b3bfce"), (1, "#d9e0e9")]),
        lin("htg-coin-rim-dark", 14, 2, 86, 98, [(0, "#c9d3de"), (0.35, "#8d9ab0"), (0.5, "#3c475c"), (0.65, "#6f7f99"), (1, "#a9b6c8")]),
        lin("htg-coin-field-dark", 14, 8, 86, 92, [(0, "#8e9aae"), (0.45, "#5d6a80"), (0.55, "#3a4558"), (1, "#7a879c")]),
        rim_wall,
        # 37 degrees from vertical, the same as the chrome, across the two tokens' silhouette.
        lin("htg-glow", 26.5, 18.6, 73.5, 81.4, GLOW),
        '<filter id="htg-glow-blur" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="4.5"/></filter>',
        '<filter id="htg-soft-shadow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="1.8"/></filter>',
        # The glow only shows outside the two tokens, never between them.
        f'<mask id="htg-glow-mask" maskUnits="userSpaceOnUse" x="-30" y="-30" width="160" height="160">'
        f'<rect x="-30" y="-30" width="160" height="160" fill="#fff"/>'
        f'<circle cx="{BACK[0]}" cy="{BACK[1]}" r="{f(R - 0.3)}" fill="#000"/>'
        f'<circle cx="{FRONT[0]}" cy="{FRONT[1]}" r="{f(R - 0.3)}" fill="#000"/></mask>',
        f'<clipPath id="htg-back-clip"><circle cx="{BACK[0]}" cy="{BACK[1]}" r="{f(R)}"/></clipPath>',
    ])


def coin(dark, with_star):
    """One struck token in its own 0-100 box: raised rim, field, raised beads, bevelled star."""
    rim = "url(#htg-coin-rim-dark)" if dark else "url(#htg-coin-rim)"
    field = "url(#htg-coin-field-dark)" if dark else "url(#htg-coin-field)"
    bead = "#9aa6b8" if dark else "#eef2f7"
    beads = [(50 + 37 * math.cos(2 * math.pi * j / 32), 50 + 37 * math.sin(2 * math.pi * j / 32)) for j in range(32)]
    out = [
        f'<path d="{circle(50, 50, 48)}" fill="{rim}"/>',
        f'<path d="{circle(50, 50, 42)}" fill="{field}"/>',
        '<circle cx="50" cy="50" r="42" fill="none" stroke="url(#htg-rim-wall)" stroke-width="1.8"/>',
        '<circle cx="50" cy="50" r="47.6" fill="none" stroke="#0d1320" stroke-opacity="0.35" stroke-width="0.8"/>',
        f'<path d="{" ".join(circle(x + 0.35, y + 0.4, 1.45) for x, y in beads)}" fill="#0d1320" opacity="0.4"/>',
        f'<path d="{" ".join(circle(x - 0.3, y - 0.3, 1.45) for x, y in beads)}" fill="#fff" opacity="0.7"/>',
        f'<path d="{" ".join(circle(x, y, 1.3) for x, y in beads)}" fill="{bead}"/>',
    ]
    if with_star:
        # Struck from the same metal as the field: relief comes only from bevel facets lit from the
        # top left. No drop shadow or outside highlight, which made the star look like it floated.
        cx, cy = 50, 51
        outer = star(cx, cy, 17, 7.2)
        plateau = [(cx + (x - cx) * 0.62, cy + (y - cy) * 0.62) for x, y in outer]
        out += [
            f'<path d="{poly(outer)}" fill="#0d1320" opacity="0.28" transform="translate(0.5 0.6)"/>',
            f'<path d="{poly(outer)}" fill="{field}"/>',
            f'<path d="{poly(plateau)}" fill="#fff" opacity="0.12"/>',
        ]
        light = (-0.6, -0.8)
        for i in range(10):
            a, b = outer[i], outer[(i + 1) % 10]
            c, d = plateau[(i + 1) % 10], plateau[i]
            nx, ny = b[1] - a[1], -(b[0] - a[0])
            ln = math.hypot(nx, ny)
            nx, ny = nx / ln, ny / ln
            mx, my = (a[0] + b[0]) / 2 - cx, (a[1] + b[1]) / 2 - cy
            if nx * mx + ny * my < 0:
                nx, ny = -nx, -ny
            dot = nx * light[0] + ny * light[1]
            colour, opacity = ("#fff", 0.25 + 0.6 * dot) if dot >= 0 else ("#0d1320", 0.18 + 0.5 * -dot)
            out.append(f'<path d="{poly([a, b, c, d])}" fill="{colour}" opacity="{opacity:.2f}"/>')
    return "\n".join(out)


def place(centre, inner, extra=""):
    tx, ty = centre[0] - 50 * SCALE, centre[1] - 50 * SCALE
    return f'<g{extra}><g transform="translate({f(tx)} {f(ty)}) scale({SCALE})">\n{inner}\n</g></g>'


def mark_full(glow=True):
    parts = []
    if glow:
        parts.append(
            '<g mask="url(#htg-glow-mask)"><g filter="url(#htg-glow-blur)" opacity="0.95">'
            f'<circle cx="{BACK[0]}" cy="{BACK[1]}" r="{f(R + 1.5)}" fill="url(#htg-glow)"/>'
            f'<circle cx="{FRONT[0]}" cy="{FRONT[1]}" r="{f(R + 1.5)}" fill="url(#htg-glow)"/></g></g>')
    parts.append(place(BACK, coin(dark=True, with_star=False)))
    # The front token sits directly on the back one; a soft contact shadow separates them.
    parts.append(f'<g clip-path="url(#htg-back-clip)"><circle cx="{FRONT[0] + 1.2}" cy="{FRONT[1] - 1.2}" '
                 f'r="{f(R + 1.2)}" fill="#05080f" opacity="0.75" filter="url(#htg-soft-shadow)"/></g>')
    parts.append(place(FRONT, coin(dark=False, with_star=True)))
    return "\n".join(parts)


# ---------------------------------------------------------------- the one-colour mark

def mark_flat_defs():
    return (f'<mask id="htg-flat-gap" maskUnits="userSpaceOnUse" x="0" y="0" width="100" height="100">'
            f'<rect width="100" height="100" fill="#fff"/><circle cx="{FRONT[0]}" cy="{FRONT[1]}" r="{f(R + 4)}" fill="#000"/></mask>')


def flat_coin(with_star):
    beads = " ".join(circle(50 + 34 * math.cos(2 * math.pi * k / 30), 50 + 34 * math.sin(2 * math.pi * k / 30), 1.7) for k in range(30))
    face = f"{circle(50, 50, 39)} {beads}" + (f" {poly(star(50, 51, 14, 5.8))}" if with_star else "")
    return (f'<path d="{circle(50, 50, 48)} {circle(50, 50, 42)}" fill-rule="evenodd"/>\n'
            f'<path d="{face}" fill-rule="evenodd"/>')


def mark_flat():
    """One colour, inherited from the element's fill. Cut-outs instead of shading, a gap instead of a shadow."""
    return (place(BACK, flat_coin(False), ' mask="url(#htg-flat-gap)"') + "\n" + place(FRONT, flat_coin(True)))


# ---------------------------------------------------------------- one-colour variations
#
# Each variation strikes a different emblem into the front token, in place of the star, so the
# family shares the locked geometry. Emblems are drawn into a mask in the token's own 0-100 box:
# black cuts the face away, white fills it back in for inner detail. They sit inside the beads
# (radius 34) with the same weight as the star, centred where the star is (50, 51).
#
# Every emblem is HTG's own symbol. None is, or imitates, a game's logo or art (publisher rules).

STROKE = 'fill="none" stroke="#000" stroke-linecap="round" stroke-linejoin="round"'


def _emblem_star():
    return f'<path d="{poly(star(50, 51, 14, 5.8))}"/>'


def _emblem_shield():
    return '<path d="M50 36.5 L62.5 41 V51.5 C62.5 59 57.5 63.5 50 66.5 C42.5 63.5 37.5 59 37.5 51.5 V41 Z"/>'


def _emblem_heart():
    return ('<path d="M50 64.5 C41 58.5 36 53 36 47 C36 42 39.5 38.5 43.5 38.5 C46.5 38.5 48.7 40.3 50 43 '
            'C51.3 40.3 53.5 38.5 56.5 38.5 C60.5 38.5 64 42 64 47 C64 53 59 58.5 50 64.5 Z"/>')


def _emblem_ticket():
    # An arcade prize ticket, tilted: notched ends and a perforation.
    return ('<g transform="rotate(-14 50 51)">'
            '<rect x="35" y="43" width="30" height="16" rx="1.5"/>'
            '<circle cx="35" cy="51" r="3" fill="#fff"/><circle cx="65" cy="51" r="3" fill="#fff"/>'
            '<path d="M57 44.8 V57.2" stroke="#fff" stroke-width="1.4" stroke-dasharray="1.6 1.6"/></g>')


def _emblem_seedling():
    return (f'<path d="M50 65 V50" {STROKE} stroke-width="3"/>'
            '<path d="M50 52 C44 52 39 48 38.5 41.5 C45 41.5 49.5 45.5 50 52 Z"/>'
            '<path d="M50 48.5 C50.8 41.5 56 37 62.5 37 C62.3 43.8 57 48.5 50 48.5 Z"/>')


def _emblem_bot():
    return (f'<path d="M50 42 V37.5" {STROKE} stroke-width="2.4"/><circle cx="50" cy="36" r="2.2"/>'
            '<rect x="38" y="42" width="24" height="19" rx="5"/>'
            '<circle cx="45" cy="50.5" r="2.6" fill="#fff"/><circle cx="55" cy="50.5" r="2.6" fill="#fff"/>'
            '<path d="M45.5 56.5 H54.5" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/>')


def _emblem_flag():
    # A rally flag: where the crew musters.
    return (f'<path d="M41 66 V37" {STROKE} stroke-width="3"/>'
            '<path d="M42.5 38 H62 L57 44.5 L62 51 H42.5 Z"/>')


def _emblem_anchor():
    return (f'<circle cx="50" cy="38.5" r="3.2" {STROKE} stroke-width="3"/>'
            f'<path d="M50 41.7 V64.5 M42.5 47 H57.5 M37.5 55.5 C38.5 61.5 43.5 64.5 50 64.5 '
            f'C56.5 64.5 61.5 61.5 62.5 55.5" {STROKE} stroke-width="3.2"/>'
            '<path d="M35.5 57.5 L37.5 52.5 L40.5 56.5 Z M64.5 57.5 L62.5 52.5 L59.5 56.5 Z"/>')


def _emblem_planet():
    # A ringed planet; the ring passes in front of the planet's lower half.
    ring = 'ellipse cx="50" cy="51" rx="16" ry="5" transform="rotate(-18 50 51)"'
    return (f'<{ring} {STROKE} stroke-width="2.4"/>'
            '<circle cx="50" cy="51" r="8.5"/>'
            '<clipPath id="htg-front-ring"><rect x="30" y="51" width="40" height="20" transform="rotate(-18 50 51)"/></clipPath>'
            f'<g clip-path="url(#htg-front-ring)"><{ring} fill="none" stroke="#fff" stroke-width="5"/>'
            f'<{ring} {STROKE} stroke-width="2.4"/></g>')


def _emblem_dogtag():
    return ('<g transform="rotate(12 50 51)">'
            '<rect x="41.5" y="37" width="17" height="27" rx="6"/>'
            '<circle cx="50" cy="41.5" r="1.8" fill="#fff"/>'
            '<path d="M45.5 49.5 H54.5 M45.5 53.5 H54.5 M45.5 57.5 H51.5" stroke="#fff" stroke-width="1.5" stroke-linecap="round"/></g>')


def _emblem_crosshair():
    return (f'<circle cx="50" cy="51" r="10" {STROKE} stroke-width="3.2"/>'
            f'<path d="M50 36.5 V44.5 M50 57.5 V65.5 M35.5 51 H43.5 M56.5 51 H64.5" {STROKE} stroke-width="3.2"/>'
            '<circle cx="50" cy="51" r="2.2"/>')


def _emblem_parachute():
    return ('<path d="M36 48 C36 40 42.5 35.5 50 35.5 C57.5 35.5 64 40 64 48 '
            'C61.7 46 59 46 56.7 48 C54.4 46 51.7 46 50 48 C48.3 46 45.6 46 43.3 48 C41 46 38.3 46 36 48 Z"/>'
            f'<path d="M37 48.5 L47.5 59.5 M50 48.5 V59.5 M63 48.5 L52.5 59.5" {STROKE} stroke-width="1.5"/>'
            '<rect x="46.5" y="59" width="7" height="6.5" rx="1.2"/>')


# name → (emblem, what it marks, suggested colour or None for ink only)
VARIATIONS = {
    "star": (_emblem_star, "The HTG mark itself (for reference)", GREEN),
    "staff": (_emblem_shield, "Staff: HMFIC, Admin, Moderators", "#f1c40f"),
    "host": (_emblem_ticket, "Event hosts, and events (an arcade prize ticket)", "#9b59b6"),
    "supporter": (_emblem_heart, "Supporters (when they launch)", PURPLE),
    "seeding": (_emblem_seedling, "Seeding the War Dogs server", GREEN),
    "bot": (_emblem_bot, "The HTG bot's avatar and bot posts", BLUE),
    "muster": (_emblem_flag, "Muster, the crew-up service (later)", BLUE),
    "sot": (_emblem_anchor, "Sea of Thieves", "#1abc9c"),
    "sc": (_emblem_planet, "Star Citizen", "#3498db"),
    "wd": (_emblem_dogtag, "War Dogs", "#95a5a6"),
    "cs": (_emblem_crosshair, "Counter-Strike 2", "#f39c12"),
    "pubg": (_emblem_parachute, "PUBG: BATTLEGROUNDS", "#e74c3c"),
}


def flat_coin_emblem(mask_id):
    beads = " ".join(circle(50 + 34 * math.cos(2 * math.pi * k / 30), 50 + 34 * math.sin(2 * math.pi * k / 30), 1.7) for k in range(30))
    return (f'<path d="{circle(50, 50, 48)} {circle(50, 50, 42)}" fill-rule="evenodd"/>\n'
            f'<path d="{circle(50, 50, 39)} {beads}" fill-rule="evenodd" mask="url(#{mask_id})"/>')


def variation(name):
    """The one-colour mark with this variation's emblem. Returns (body, defs)."""
    emblem = VARIATIONS[name][0]()
    mask_id = f"htg-emblem-{name}"
    defs = (mark_flat_defs() + "\n"
            f'<mask id="{mask_id}" maskUnits="userSpaceOnUse" x="0" y="0" width="100" height="100">'
            f'<rect width="100" height="100" fill="#fff"/><g fill="#000">{emblem}</g></mask>')
    body = place(BACK, flat_coin(False), ' mask="url(#htg-flat-gap)"') + "\n" + place(FRONT, flat_coin_emblem(mask_id))
    return body, defs


# ---------------------------------------------------------------- text as outlines

_fonts = {}


def _font(wdth, wght):
    key = (wdth, wght)
    if key not in _fonts:
        blob = hb.Blob.from_file_path(str(FONT))
        hbfont = hb.Font(hb.Face(blob))
        hbfont.set_variations({"wdth": wdth, "wght": wght})
        static = instantiateVariableFont(TTFont(FONT), {"wdth": wdth, "wght": wght})
        _fonts[key] = (hbfont, static)
    return _fonts[key]


def text(s, size, wdth, wght, x, baseline, letter_spacing_em=0.0, fill="#000", extra=""):
    """Shape and outline s. Returns (svg path element, visible width, CSS box width)."""
    hbfont, static = _font(wdth, wght)
    upem = static["head"].unitsPerEm
    buf = hb.Buffer()
    buf.add_str(s)
    buf.guess_segment_properties()
    hb.shape(hbfont, buf, {"kern": True, "liga": False})
    order = static.getGlyphOrder()
    glyphs = static.getGlyphSet()
    k = size / upem
    ls = letter_spacing_em * size
    pen = SVGPathPen(glyphs)
    pen_x = x
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        glyphs[order[info.codepoint]].draw(TransformPen(pen, (k, 0, 0, -k, pen_x + pos.x_offset * k, baseline - pos.y_offset * k)))
        pen_x += pos.x_advance * k + ls
    box = pen_x - x
    return f'<path d="{pen.getCommands()}" fill="{fill}"{extra}/>', box - ls, box


def baseline_in_box(top, line_height, size):
    """Where CSS puts the baseline of Archivo text in a line box (ascent 878, descent 210)."""
    content = (0.878 + 0.210) * size
    return top + (line_height - content) / 2 + 0.878 * size


CAP = 0.686  # Archivo cap height / em


def rule(x0, x1, baseline, size, gid):
    """The 2 px green-blue-purple line, centred on the capitals of the text beside it."""
    y = baseline - CAP * size / 2 - 1
    return f'<rect x="{f(x0)}" y="{f(y)}" width="{f(x1 - x0)}" height="2" rx="1" fill="url(#{gid})"/>', lin(gid, x0, 0, x1, 0, RULE)


def wordmark(x, top, size, chrome=True, ink=INK, muted=MUTED, rule_on=True, gid="htg-wm",
             stacked=False, g_size=16, g_track=0.55, g_gap=16, rule_solid=None):
    """HIDDEN TOKEN over GAMING with the rule. Side-by-side lockups put one rule after GAMING;
    the stacked lockup centres GAMING between two. Returns (svg, defs, width, height)."""
    wm_base = baseline_in_box(top, size * 1.2, size)
    fill = f"url(#{gid}-chrome)" if chrome else ink
    wm, wm_w, _ = text("HIDDEN TOKEN", size, 125, 800, x, wm_base, 0.01, fill)
    defs = [lin(f"{gid}-chrome", 0, top, 0, top + size * 1.2, CHROME)] if chrome else []
    g_top = top + size * 1.2 + 8
    g_base = baseline_in_box(g_top, g_size, g_size)
    g_visible = text("GAMING", g_size, 100, 600, 0, 0, g_track)[1]
    gx = x + (wm_w - g_visible) / 2 if stacked else x
    gm, _, gm_box = text("GAMING", g_size, 100, 600, gx, g_base, g_track, muted)
    parts = [wm, gm]
    if rule_on and stacked:
        y = g_base - CAP * g_size / 2 - 1
        l0, l1, r0, r1 = x, gx - g_gap, gx + g_visible + g_gap, x + wm_w
        parts.append(f'<rect x="{f(l0)}" y="{f(y)}" width="{f(l1 - l0)}" height="2" rx="1" fill="url(#{gid}-rule-l)"/>')
        parts.append(f'<rect x="{f(r0)}" y="{f(y)}" width="{f(r1 - r0)}" height="2" rx="1" fill="url(#{gid}-rule-r)"/>')
        defs.append(lin(f"{gid}-rule-l", l0, 0, l1, 0, [(0, GREEN), (0.2, GREEN), (0.75, BLUE)]))
        defs.append(lin(f"{gid}-rule-r", r0, 0, r1, 0, [(0.25, BLUE), (0.8, PURPLE), (1, PURPLE)]))
    elif rule_on:
        r, rdef = rule(x + gm_box + g_gap, x + wm_w, g_base, g_size, f"{gid}-rule")
        if rule_solid:
            r = r.replace(f'url(#{gid}-rule)', rule_solid)
        else:
            defs.append(rdef)
        parts.append(r)
    return "\n".join(parts), "\n".join(defs), wm_w, size * 1.2 + 8 + g_size


# ---------------------------------------------------------------- files

def svg(path, w, h, body, defs="", view=None, extra=""):
    vb = view or f"0 0 {f(w)} {f(h)}"
    doc = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{f(w)}" height="{f(h)}" viewBox="{vb}"{extra}>\n'
           f'<defs>\n{defs}\n</defs>\n{body}\n</svg>\n')
    out = BRAND / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc)
    print(f"wrote {path} ({len(doc) // 1024} KiB)")


def main():
    title = "<title>Hidden Token Gaming</title>"
    # The mark: with glow (room around it for the glow), without, and one colour.
    svg("logo/htg-mark.svg", 128, 128, title + mark_full(True), mark_defs(), view="-14 -14 128 128")
    svg("logo/htg-mark-noglow.svg", 100, 100, title + mark_full(False), mark_defs())
    svg("logo/htg-mark-mono.svg", 100, 100, title + f'<g fill="currentColor">{mark_flat()}</g>', mark_flat_defs())
    # One-colour variations: the same mark with another emblem on the front token.
    for name, (_, what, _) in VARIATIONS.items():
        if name == "star":
            continue
        body, defs = variation(name)
        svg(f"logo/variations/htg-mark-{name}.svg", 100, 100,
            f"<title>Hidden Token Gaming: {what}</title>" + f'<g fill="currentColor">{body}</g>', defs)

    # Main lockup on dark: mark 120 px, wordmark 52 px, rule beside GAMING. 20 px room for the glow.
    pad, mark_px, gap, size = 20, 120, 28, 52
    probe = wordmark(0, 0, size)
    text_w, text_h = probe[2], probe[3]
    w, h = pad + mark_px + gap + text_w + pad, pad * 2 + mark_px
    tx, ty = pad + mark_px + gap, pad + (mark_px - text_h) / 2
    body, tdefs, _, _ = wordmark(tx, ty, size)
    mark = f'<g transform="translate({pad} {pad}) scale({mark_px / 100})">{mark_full(True)}</g>'
    svg("logo/htg-lockup.svg", w, h, title + mark + "\n" + body, mark_defs() + "\n" + tdefs)
    # One-colour lockup for light backgrounds: no chrome, no glow, a solid slate rule.
    body, tdefs, _, _ = wordmark(tx, ty, size, chrome=False, muted="#4f5d74", gid="htg-mono", rule_solid="#4f5d74")
    mark = f'<g transform="translate({pad} {pad}) scale({mark_px / 100})" fill="{INK}">{mark_flat()}</g>'
    svg("logo/htg-lockup-mono.svg", w, h, title + mark + "\n" + body, mark_flat_defs() + "\n" + tdefs)

    # Stacked lockup: mark centred over the wordmark, GAMING between two rules.
    pad, mark_px, size = 24, 240, 44
    probe = wordmark(0, 0, size, stacked=True, g_size=18, g_track=0.5, g_gap=18)
    text_w, text_h = probe[2], probe[3]
    w = max(text_w, mark_px) + 2 * pad
    h = pad + mark_px + 32 + text_h + pad
    body, tdefs, _, _ = wordmark((w - text_w) / 2, pad + mark_px + 32, size, gid="htg-stack",
                                 stacked=True, g_size=18, g_track=0.5, g_gap=18)
    mark = f'<g transform="translate({f((w - mark_px) / 2)} {pad}) scale({mark_px / 100})">{mark_full(True)}</g>'
    svg("logo/htg-lockup-stacked.svg", w, h, title + mark + "\n" + body, mark_defs() + "\n" + tdefs)

    # Discord server icon: ground square, mark with glow, inside the circle Discord crops to.
    icon_mark = 380
    off = (512 - icon_mark) / 2
    body = (f'<rect width="512" height="512" fill="{GROUND}"/>'
            f'<g transform="translate({f(off)} {f(off)}) scale({icon_mark / 100})">{mark_full(True)}</g>')
    svg("discord/server-icon.svg", 512, 512, title + body, mark_defs())

    # War Dogs server-browser banner, 1024 x 256 (ServerImageURL). Sizes measured, not guessed:
    # the 50 px wordmark is ~508 px wide and stops ~35 px short of the angled block.
    parts = [f'<rect width="1024" height="256" fill="{GROUND}"/>',
             f'<g transform="translate(40 58) scale(1.4)">{mark_full(True)}</g>']
    body, tdefs, _, _ = wordmark(204, 86, 50, gid="htg-banner")
    parts.append(body)
    parts.append(f'<path d="M780 0 H1024 V256 H724Z" fill="{GREEN}"/>')
    wd_base = baseline_in_box(98.2, 38.4, 32)
    probe = text("WAR DOGS", 32, 125, 800, 0, 0)
    wd, _, _ = text("WAR DOGS", 32, 125, 800, 994 - probe[1], wd_base, fill=GROUND)
    cs_base = 142.6 + (0.878 + 0.210) * 14 - 0.210 * 14
    probe = text("COMMUNITY SERVER", 14, 100, 700, 0, 0, 0.378)
    cs, _, _ = text("COMMUNITY SERVER", 14, 100, 700, 994 - probe[1], cs_base, 0.378, fill=GROUND)
    parts += [wd, cs]
    svg("wardogs/server-banner.svg", 1024, 256, title + "\n".join(parts), mark_defs() + "\n" + tdefs)


if __name__ == "__main__":
    main()
