# site

[hiddentoken.com](https://hiddentoken.com): the Hidden Token Gaming website, built with
[Hugo](https://gohugo.io) and hosted on Cloudflare Pages.

This repo holds everything HTG publishes: the home, games and join pages, the rules
(`content/policy/`), the publisher rules, required notices, privacy policy and terms
(`content/legal/`), and the brand kit (`brand/`). The staff handbook, with the plan, runbooks and
questions for counsel, is private. Playbooks are members-only and live in Discord, not on the site.

## Working on it

Needs Hugo 0.162+.

```bash
hugo server                                   # http://localhost:1313
hugo --gc --minify --panicOnWarning           # what CI builds
npx markdownlint-cli2                         # what the lint workflow runs
```

The brand kit's SVGs and PNGs are generated: change `brand/tools/build.py`, never the files. See
[`brand/README.md`](brand/README.md).

## How it fits together

- **The rules and legal pages** are written to read on GitHub too, so they link to each other with
  relative `.md` paths. `layouts/_markup/render-link.html` resolves those to site pages, and a link
  that doesn't resolve fails the build.
- **The footer** is the "Site footer" block of `content/legal/notices.md`, so the publisher
  notices have one source. The build fails if the block or the Star Citizen notice is missing.
- **Brand colours and mark files** are mounted from `brand/` (`hugo.toml`), so a brand change is
  one PR here.
- **Link previews:** every page has Open Graph and Twitter-card tags (`layouts/baseof.html`). The
  card image is `brand/social/og-image-1200x630.png`, generated like the other brand files, and the
  build fails if it's missing. A page's `description` front matter feeds the preview, falling back
  to the site's.
- **No third-party anything:** no scripts, fonts, analytics or game logos. `static/_headers` sets a
  strict CSP.

## CI and deploys

`site.yml` builds with a checksum-pinned Hugo, checks every internal link and anchor with lychee,
and deploys with Wrangler: `main` to production, same-repo PRs to a preview whose URL is in the job
summary. It needs the `CLOUDFLARE_PAGES_TOKEN` secret (Pages edit only) and the
`CLOUDFLARE_ACCOUNT_ID` variable. The Pages project, domain and DNS are OpenTofu in
[`deploy`](https://github.com/hidden-token-gaming/deploy) (`tofu/cloudflare/`). `lint.yml` runs
markdownlint. Dependabot keeps the workflow actions current.
