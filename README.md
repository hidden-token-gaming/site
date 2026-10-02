# site

[hiddentoken.com](https://hiddentoken.com): the Hidden Token Gaming website, built with
[Hugo](https://gohugo.io) and hosted on Cloudflare Pages.

The rules, playbooks and legal pages come from the
[handbook](https://github.com/hidden-token-gaming/handbook) as a Hugo module, so they are edited
there, not here. This repo holds the home, games and join pages, the layouts and the styles.

## Working on it

Needs Hugo 0.162+ and Go (for the module).

```bash
hugo server                                   # http://localhost:1313
hugo --gc --minify --panicOnWarning           # what CI builds
hugo mod get -u github.com/hidden-token-gaming/handbook   # pull the latest handbook
```

To preview unpublished handbook changes, point the module at a local checkout:

```bash
HUGO_MODULE_REPLACEMENTS="github.com/hidden-token-gaming/handbook -> ../../handbook" hugo server
```

## How it fits together

- **Handbook pages** keep their handbook paths (`/policy/`, `/playbooks/`, `/legal/`), so their
  relative `.md` links resolve to site pages. Links to anything the site doesn't publish go to the
  handbook on GitHub (`layouts/_markup/render-link.html`). In this repo's own content, a link that
  doesn't resolve fails the build.
- **The footer** is the "Site footer" block of the handbook's `legal/notices.md`, so the
  publisher notices have one source. The build fails if the block or the Star Citizen notice is
  missing.
- **No third-party anything:** no scripts, fonts, analytics or game logos. `static/_headers` sets a
  strict CSP.

## CI and deploys

`site.yml` builds with a checksum-pinned Hugo, checks every internal link and anchor with lychee,
and deploys with Wrangler: `main` to production, same-repo PRs to a preview whose URL is in the job
summary. It needs the `CLOUDFLARE_PAGES_TOKEN` secret (Pages edit only) and the
`CLOUDFLARE_ACCOUNT_ID` variable. The Pages project, domain and DNS are OpenTofu in
[`deploy`](https://github.com/hidden-token-gaming/deploy) (`tofu/cloudflare/`). Dependabot proposes
handbook bumps daily.
