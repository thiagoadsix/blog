# blog

Source for [thiagoadsix.com](https://thiagoadsix.com) — a Next.js site whose posts are
MDX files compiled by [Velite](https://velite.js.org/), plus the runnable code that
accompanies those posts.

## Layout

```
.
├── src/
│   ├── app/
│   │   ├── content/blog/   # the posts (MDX)
│   │   └── blog/           # post list and post detail routes
│   ├── components/
│   └── config/
└── examples/               # runnable code for posts
    ├── faceted-search-golang/
    ├── golang-air-docker/
    └── notification-service/
```

Each directory under `examples/` is a self-contained project with its own toolchain,
README and `.gitignore`. They were imported with `git subtree`, so their original
history is preserved here.

## Linking a post to its example

Add an `example` field to the post's frontmatter, set to the directory name under
`examples/`:

```yaml
---
slug: golang-air-docker
title: Golang Local Development with Live Reloading using Air and Docker Compose
date: 2024-08-12
example: golang-air-docker
---
```

The post header then renders a "Source code" link pointing at that directory on
GitHub. The field is optional — posts without accompanying code simply omit it.

## Development

```bash
nvm use        # version pinned in .nvmrc
npm install
npm run dev    # http://localhost:3000
```

`npm run build` runs Velite as part of the Next.js build, so `.velite/` is
regenerated from the MDX sources and is not committed.
