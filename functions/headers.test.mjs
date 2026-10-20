// node --test functions/: the Function's copy of the site-wide headers must be static/_headers'
// "/*" block, word for word, or the join page would be served under another policy than the rest.
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { SECURITY_HEADERS, countText, peopleOnline } from "./join/index.js";

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

test("HTG's bots are left out of the count", () => {
  // 2026-10-20, the first answer: the three bots and John.
  const live = {
    presence_count: 4,
    members: [
      { username: "HAL 9000", status: "online" },
      { username: "HTG · Guard", status: "online" },
      { username: "HTG · Support", status: "online" },
      { username: "Jmac", status: "online" },
    ],
  };
  assert.equal(peopleOnline(live), 1);
  assert.equal(peopleOnline({ presence_count: 3, members: live.members.slice(0, 3) }), 0);
  assert.equal(peopleOnline({ presence_count: 150, members: [] }), 150); // past the list's cap
  assert.equal(peopleOnline({ presence_count: 2, members: live.members }), 0); // never below zero
  for (const bad of [{}, { presence_count: "4" }, { presence_count: -1 }, null]) {
    assert.equal(peopleOnline(bad), null);
  }
});
