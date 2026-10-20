# DESIGN.md: design foundation (phase 1, 2026-10-19)

Supersedes `DESIGN-TOKENS.md` (third-party reference measurements, kept for history only).
All tokens live in `src/styles/global.css` (`:root`). Do not hard-code values in components.

## Direction
Calm, editorial, trustworthy. Navy ink on cool white, one coral accent for markers, one burnt-orange for the single main action. Flat: borders instead of shadows, no gradients, no frosted glass.
Main action everywhere: "Free consultation" -> `/free-consultation`.

## Colour
| Token | Value | Use |
|---|---|---|
| `--navy` | #00104B | text, headings, dark panels |
| `--brand-coral` | #FF6B4A | logo, small square markers, hover rules (never text on white) |
| `--accent` / `--accent-dk` | #C2410C / #9F3509 | CTA button (white text, 5.2:1), links, mono labels |
| `--text` / `--text-muted` | #38426A / #5A6483 | body / secondary (ink greys derived from navy) |
| `--band`, `--surface` | #F6F8FC, #FFFFFF | alternating section backgrounds |
| `--border`, `--border-strong` | #DDE3EF, #C3CCDE | hairlines, card borders |
No cream/beige, no pastel card colours. Legacy names (`--blue*`, `--red*`, `--pink*`) alias these.

## Type (Google Fonts)
- Archivo 700/800, `font-stretch: 112%` (`--font-display`): h1-h3, logo, big numbers.
- Hanken Grotesk 400-700 (`--font-sans`): body, UI.
- IBM Plex Mono 400/500 (`--font-mono`): eyebrows, table heads, meta line, captions only.
Banned: Inter, Roboto, Poppins, Montserrat, Lato, Space Grotesk, Fraunces, Geist, Plus Jakarta Sans.

## Shape
Buttons 8px (`--radius-btn`), cards/inputs/media 4px, chips 2px. No coloured side borders on cards, no three-icon feature cards.

## Components (`src/components/`)
Navbar, Footer, `layouts/ArticleLayout` (breadcrumbs, TL;DR, meta line, sticky TOC from H2s, inline CTA after every 2nd H2, FAQ + FAQPage JSON-LD, sources, advisors, related, Article JSON-LD), `layouts/GuideLayout` (wrapper for existing guides), TldrBox, ConsultationCTA, GermanTerm, Advisor, LinkedInTrust, Testimonials (reads `data/recommendations.json`, renders nothing while empty), `forms/ConsultationForm` (5 steps).

## Content rules
No invented testimonials, stars or numbers. Advisor photos are grey placeholders until cleared. Placeholder text is marked `[...]`.
Lead path: `POST /api/lead` -> MHCB funnel-lead (see `functions/api/lead.js`).
