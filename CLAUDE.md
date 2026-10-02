# site — context for Claude Code

hiddentoken.com, built with Hugo and deployed to Cloudflare Pages. Read `README.md` first. This repo
is **public**: no secrets, private hostnames, IP addresses or personal data.

## Rules

- **Rules and legal text live in the handbook**, not here. Fix them there and bump the module
  (`hugo mod get -u github.com/hidden-token-gaming/handbook`). Playbooks are members-only: they live
  in Discord, not on the site.
- **Publisher rules apply to the site** (handbook `legal/publisher-rules.md`): no game logos or art
  without permission, nothing that implies endorsement, no Star Citizen or Sea of Thieves content
  near anything paid, and the footer notices verbatim and at equal size.
- **No third-party requests.** No external scripts, fonts, analytics or embeds; keep the CSP in
  `static/_headers` strict.
- Copy is the community owner's voice. Draft it, and John approves.

## Workflow

- Never commit on `main`: one issue → one branch → one PR, squash-merged.
- Conventional commits; messages get a why-paragraph, a change list, then `Closes #N`.
- `CHANGELOG.md` entry under `[Unreleased]` per issue.
- Before a PR: `hugo --gc --minify --panicOnWarning` and the lychee check from `site.yml` must pass,
  and look at the result at phone width and in dark mode.
- No AI attribution anywhere.
