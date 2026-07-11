# Publish checklist — "Feeding Tracking, Built for 3 AM — and Free" (2026-07-29)

## Already done (2026-07-11)

- Post pages created: `blog/feeding-tracking-built-for-3-am.html`, `de/blog/...`, `tr/blog/...`
- Hero image: `assets/images/blog/blog-10.jpg`
- Cards + JSON-LD added to: `blog/index.html`, `de/blog/index.html`, `tr/blog/index.html`, `index.html`, `de/index.html`, `tr/index.html`

⚠️ The post is now LINKED from the blog listings and homepages. If the site is deployed before publish day, visitors will see the post (search engines won't index it thanks to noindex). Don't push to production until you're ready for it to be visible.

## Remaining steps on publish day

### 1. Flip robots meta in all three post files

In `blog/feeding-tracking-built-for-3-am.html`, `de/blog/feeding-tracking-built-for-3-am.html`, `tr/blog/feeding-tracking-built-for-3-am.html`, replace the `<!-- DRAFT: ... -->` comment + `noindex, nofollow` meta with:

```html
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
```

### 2. Add to `sitemap.xml` (with the other blog post entries)

```xml
  <!-- Blog yazıları — Feeding Tracking, Built for 3 AM -->
  <url>
    <loc>https://momena.app/blog/feeding-tracking-built-for-3-am.html</loc>
    <lastmod>2026-07-29</lastmod>
    <changefreq>never</changefreq>
    <priority>0.8</priority>
    <xhtml:link rel="alternate" hreflang="en" href="https://momena.app/blog/feeding-tracking-built-for-3-am.html"/>
    <xhtml:link rel="alternate" hreflang="tr" href="https://momena.app/tr/blog/feeding-tracking-built-for-3-am.html"/>
    <xhtml:link rel="alternate" hreflang="de" href="https://momena.app/de/blog/feeding-tracking-built-for-3-am.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://momena.app/blog/feeding-tracking-built-for-3-am.html"/>
  </url>
  <url>
    <loc>https://momena.app/tr/blog/feeding-tracking-built-for-3-am.html</loc>
    <lastmod>2026-07-29</lastmod>
    <changefreq>never</changefreq>
    <priority>0.7</priority>
    <xhtml:link rel="alternate" hreflang="en" href="https://momena.app/blog/feeding-tracking-built-for-3-am.html"/>
    <xhtml:link rel="alternate" hreflang="tr" href="https://momena.app/tr/blog/feeding-tracking-built-for-3-am.html"/>
    <xhtml:link rel="alternate" hreflang="de" href="https://momena.app/de/blog/feeding-tracking-built-for-3-am.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://momena.app/blog/feeding-tracking-built-for-3-am.html"/>
  </url>
  <url>
    <loc>https://momena.app/de/blog/feeding-tracking-built-for-3-am.html</loc>
    <lastmod>2026-07-29</lastmod>
    <changefreq>never</changefreq>
    <priority>0.7</priority>
    <xhtml:link rel="alternate" hreflang="en" href="https://momena.app/blog/feeding-tracking-built-for-3-am.html"/>
    <xhtml:link rel="alternate" hreflang="tr" href="https://momena.app/tr/blog/feeding-tracking-built-for-3-am.html"/>
    <xhtml:link rel="alternate" hreflang="de" href="https://momena.app/de/blog/feeding-tracking-built-for-3-am.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://momena.app/blog/feeding-tracking-built-for-3-am.html"/>
  </url>
```

### 3. Delete this checklist file

## Notes

- World Breastfeeding Week is Aug 1–7. The post opens with "It's World Breastfeeding Week" but the planned date is Jul 29 — either move publish to Aug 1 or soften the opening line.
- `blog-10.jpg` is 640×427 — low for a 1200px-wide hero and og:image. Swap in a higher-res version before publish if available.
