#!/usr/bin/env bash
# Render the brand PNGs from the SVGs that build.py writes, with headless Chrome so filters, masks
# and gradients render the way browsers show them. Run from anywhere; needs google-chrome (or set
# CHROME) and ImageMagick's `magick` for the size check.
set -euo pipefail

BRAND="$(cd "$(dirname "$0")/.." && pwd)"
CHROME="${CHROME:-google-chrome}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# render <svg relative to brand/> <png relative to brand/> <width> <height> [css colour for currentColor]
render() {
  local src="$BRAND/$1" out="$BRAND/$2" w="$3" h="$4" colour="${5:-#000}"
  mkdir -p "$(dirname "$out")"
  # Inline the SVG so currentColor (the one-colour mark) picks up the requested colour.
  {
    printf '<!doctype html><html><head><style>html,body{margin:0;background:transparent}'
    printf 'svg{display:block;width:%spx;height:%spx;color:%s}</style></head><body>' "$w" "$h" "$colour"
    cat "$src"
    printf '</body></html>'
  } > "$TMP/page.html"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
    --default-background-color=00000000 --window-size="$w,$h" \
    --screenshot="$out" "file://$TMP/page.html" >/dev/null 2>&1
  local got
  got="$(magick identify -format '%wx%h' "$out")"
  if [[ "$got" != "${w}x${h}" ]]; then
    echo "render: $2 is $got, expected ${w}x${h}" >&2
    exit 1
  fi
  echo "rendered $2 (${w}x${h})"
}

for s in 1024 512 256 128; do
  render logo/htg-mark.svg "logo/png/htg-mark-$s.png" "$s" "$s"
done
for s in 64 32; do
  render logo/htg-mark-noglow.svg "logo/png/htg-mark-noglow-$s.png" "$s" "$s"
done
render logo/htg-mark-mono.svg logo/png/htg-mark-mono-black-512.png 512 512 '#0b1222'
render logo/htg-mark-mono.svg logo/png/htg-mark-mono-white-512.png 512 512 '#ffffff'

# Lockups at 2x their SVG size.
for name in htg-lockup htg-lockup-mono htg-lockup-stacked; do
  read -r w h < <(sed -n 's/.*<svg[^>]* width="\([0-9.]*\)" height="\([0-9.]*\)".*/\1 \2/p' "$BRAND/logo/$name.svg" | head -1)
  render "logo/$name.svg" "logo/png/$name@2x.png" "$(printf '%.0f' "$(echo "$w*2" | bc)")" "$(printf '%.0f' "$(echo "$h*2" | bc)")"
done

render discord/server-icon.svg discord/server-icon-512.png 512 512
render wardogs/server-banner.svg wardogs/server-banner-1024x256.png 1024 256
