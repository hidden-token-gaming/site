# site — context for Claude Code

hiddentoken.com, built with Hugo and deployed to Cloudflare Pages. Read `README.md` first. This repo
is **public**: no secrets, private hostnames, IP addresses or personal data.

## Rules

- **This repo owns everything public:** the rules (`content/policy/`), the legal pages
  (`content/legal/`) and the brand kit (`brand/`). The handbook is private and staff-only: never
  link to it or copy its plan, runbooks or questions for counsel here. Playbooks are members-only:
  they live in Discord, not on the site.
- **Rules and legal pages are the owner's voice and stay verbatim.** Legal pages stay marked
  "pending legal review" until counsel signs off. Notices are copied from their source, dated.
- **Brand files are generated:** change `brand/tools/build.py` and re-run it, never hand-edit an
  SVG or PNG.
- **Publisher rules apply to the site** (`content/legal/publisher-rules.md`): no game logos or art
  without permission, nothing that implies endorsement, no Star Citizen or Sea of Thieves content
  near anything paid, and the footer notices verbatim and at equal size.
- **No third-party requests.** No external scripts, fonts, analytics or embeds; keep the CSP in
  `static/_headers` strict.
- Copy is the community owner's voice. Draft it, and John approves.

## Workflow

- Never commit on `main`: one issue → one branch → one PR, squash-merged.
- Conventional commits; messages get a why-paragraph, a change list, then `Closes #N`.
- `CHANGELOG.md` entry under `[Unreleased]` per issue.
- Before a PR: `hugo --gc --minify --panicOnWarning`, `npx markdownlint-cli2` and the lychee check
  from `site.yml` must pass, and look at the result at phone width and in dark mode.
- No AI attribution anywhere.
