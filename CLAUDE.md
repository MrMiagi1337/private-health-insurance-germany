# PKV Germany — private-health-insurance-germany.com

Astro + Sanity site. Independent, plain-English PKV guidance for English-speaking expats in Germany.

## Brand kit (official — source: `Brand Kit PKV Germany.png` on Desktop)

**Positioning:** "Private Health Insurance Made Simple for Expats"
**Subline:** "Independent, plain-English PKV guidance for expats in Germany"
**Voice:** Independent, plain-English, research-based, trust-forward — not salesy.

### Logo
- Mark: teal bridge silhouette with a coral/orange heart above it (expats bridging to German PKV)
- Wordmark: "PKV" in large serif + "GERMANY" in letter-spaced sans below
- Use the full lockup (mark + wordmark) on primary surfaces

### Colors (approximate hex — replace with exact values if a definitive source file exists)
| Role | Hex | Use |
|---|---|---|
| Navy | `#0F2A44` | Headlines, "PKV" wordmark, primary text |
| Teal | `#4A9A8E` | Bridge mark, curves, "GERMANY" label, supporting graphics |
| Coral | `#E07A4F` | Heart, underline accents, checkmarks, CTA highlights |
| Cream | `#FAF6EF` | Primary background |
| Warm gray | `#B8B3A8` | Secondary text, dividers, UI neutrals |

### Typography
- Headlines: classical serif, high contrast, in Navy (e.g. Playfair Display, Cormorant, DM Serif)
- Body / subheads: humanist sans-serif (e.g. Inter, Source Sans, DM Sans)
- Small caps / labels: letter-spaced sans for meta text like "GERMANY"

### Visual style
- Soft teal "river" curve as recurring motif
- Berlin / German landmark photography for hero imagery
- Rounded cards with subtle shadow, generous cream whitespace
- Trust markers: shields and checkmarks in Coral

## Stack
- Astro (`astro.config.mjs`)
- Sanity CMS (studio at `./src/` — use Sanity MCP for schema/content ops)
- Tailwind / global CSS in `src/styles/global.css`
- Hosted via Netlify (`netlify.toml`) + Cloudflare Wrangler (`.wrangler/`)

## Separation from related projects
- **Not** MyHealthcareBroker (MHB) — different brand, different site
- **Not** living-in-germany.org — different site
- All three cover PKV/expat topics but are distinct properties with distinct brand kits. Do not mix assets.
