# FamilyaKit website

Static site for FamilyaKit’s landing page and privacy policy (GitHub Pages).

## Structure

- `index.html`: Landing page
- `privacy-policy/index.html`: Privacy Policy page (served at `/privacy-policy/`)
- `cookies-policy/index.html`: Cookie Policy page (served at `/cookies-policy/`)
- `assets/css/style.css`: Main styles
- `assets/images/`: Brand assets and app screenshots
- `assets/favicon/`: Favicon assets
- `CNAME`: Custom domain for GitHub Pages

## Local preview

From the repo root:

```bash
python3 -m http.server 8080
```

Then open `http://localhost:8080`.

Note: don’t open the HTML files via `file://` if you want clean folder URLs like `/privacy-policy/` to work—use the local server above (GitHub Pages behaves the same way).
