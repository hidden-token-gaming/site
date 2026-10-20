// node --test functions/: the Function's copy of the site-wide headers must be static/_headers'
// "/*" block, word for word, or the join page would be served under another policy than the rest.
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { SECURITY_HEADERS, countText } from "./join/index.js";

function siteWide() {
  const lines = readFileSync(new URL("../static/_headers", import.meta.url), "utf8").split("\n");
  const out = {};
  let inBlock = false;
  for (const line of lines) {
    if (/^\S/.test(line)) {
      inBlock = line.trim() === "/*";
      continue;
    }
    const m = inBlock && line.match(/^\s+([A-Za-z-]+):\s*(.+)$/);
    if (m) out[m[1]] = m[2].trim();
  }
  return out;
}

test("the join Function sets static/_headers' site-wide headers", () => {
  const want = siteWide();
  assert.ok(Object.keys(want).length >= 5, "no /* block read from static/_headers");
  assert.deepEqual(SECURITY_HEADERS, want);
});

test("the count reads naturally", () => {
  assert.equal(countText(1), "<strong>1 member online</strong> in the Discord right now.");
  assert.equal(countText(0), "<strong>0 members online</strong> in the Discord right now.");
  assert.equal(countText(12), "<strong>12 members online</strong> in the Discord right now.");
});
