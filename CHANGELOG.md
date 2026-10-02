# Changelog

All notable changes to the site are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- PRs get `component:*` labels by path, from the org's reusable labeler and this repo's `.github/labeler.yml` (hidden-token-gaming/.github#3).
- The first version of hiddentoken.com: home, games and join pages, and the handbook's rules,
  playbooks and legal pages pulled in as a Hugo module, with their links resolved to site pages.
  The footer carries the publisher notices from the handbook's `legal/notices.md`, and the build
  fails if they are missing. Light and dark themes, no third-party requests, and a strict CSP.
  CI builds with a pinned Hugo, checks every internal link and anchor, and deploys to Cloudflare
  Pages (production from `main`, previews for PRs). Dependabot keeps the handbook current (#1).

### Changed

- Everyone reaches Discord through the join page, which carries the age limit and the rules: the header's Discord button is gone, Join is the header's call to action, and the home page's button and the footer link go to `/join/`. The Discord invite appears only on the join page.
- The playbooks are no longer on the site. They move to each game's Discord category for members, so the menu entry, the home page, join page and games page links, and the 404 page's link are gone or point to the Discord channels instead.
- The site uses the brand kit from the handbook (hidden-token-gaming/handbook#6). Colours come from the handbook's `brand/tokens.css`: dark by default with a green accent, light when the visitor's system asks for it. The header and favicon carry the HTG mark (one colour in light mode). The handbook module bump also publishes the draft privacy policy and terms of service, now listed on the Legal page, which no longer says they are being drafted. The questions for counsel stay off the site; the drafts link to them on GitHub.

### Fixed

- The deploy job no longer fails after a successful production deploy. Production has no branch alias, so the summary step's last test returned non-zero (#3).
