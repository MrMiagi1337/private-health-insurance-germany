# Private Health Insurance Germany — private-health-insurance-germany.com

Astro + Sanity site. Honest, English-language advice for expats in Germany on whether private health insurance makes sense for them. The whole service is free; the insurer pays the broker.

## 1. Ranking first (applies to every change)

The site exists to rank and to turn visitors into consultations. Every headline, text, slug, section and design choice is checked against search **before** it is shown to Marco. Design never wins against ranking in the title, H1, slug or headings.

**Before writing or designing a page**
- Fix one primary keyword and 2–5 secondary keywords. If unsure, check real search volume (SE Ranking / GSC) instead of guessing.
- Use the words people actually search for. Write "private health insurance" and "public health insurance", never "private cover" / "public cover" or other made-up synonyms. "PKV" is allowed at most once, as "(PKV)".

**On every page**
- `<title>`: primary keyword first, max ~60 characters. Meta description: keyword + benefit + "free", max ~155 characters.
- Exactly one H1, containing the primary keyword. A kicker line inside the H1 is allowed. Emotional hooks go in the lede, not instead of the keyword.
- The keyword appears in the first 100 words, in the slug, and in at least one H2. Use keyword variants in other H2s and image alt texts where they fit naturally.
- Keep headings in order (H1 → H2 → H3). Text must be real HTML text, never baked into images.
- Content that should rank must be server-rendered, not only revealed by JS. The eligibility check results are fine as JS, but the facts they state must also appear in page text or the FAQ.
- Internal links to the money pages and guides use descriptive keyword anchors, never "click here".
- Schema: InsuranceAgency/Organization site-wide, FAQPage where there is a FAQ, BreadcrumbList on subpages.
- Performance: hero image eager-loaded, WebP with width/height, everything below it lazy. No layout shift from fonts or images.

**When presenting a proposal to Marco**, add one line on its SEO effect (e.g. "H1 now contains 'private health insurance', title unchanged").

## 2. Copy rules
- The **whole service** is free (consultation, comparison, application, paperwork), not just "the consultation". The button may stay "Free consultation".
- Never "Quiz". Say "Eligibility Check".
- No invented testimonials, ratings, customer counts or savings claims. Never name competitor brokers.
- Money and legal facts (JAEG €77,400, contribution ceiling €5,812.50/month for 2026, rates) need a source check before going live.
- Banned words: delve, seamless(ly), unlock, effortless, supercharge, empower, journey, hassle-free, "in today's fast-paced".

## 3. Design (v3 redesign, Oct 2026: supersedes the old brand kit, DESIGN-TOKENS.md and DESIGN.md)
Reference mockup: `../phig-redesign/design-ref/directions/v3/index.html`.
- Colours: teal `#0A4D4A`, dark teal `#073937`, sand `#F0E2C8`, light sand `#F8F0E1`, cream `#FCF8EF`, mustard `#F5B700` (accent words, buttons, logo mark), ink `#10201E`. No orange or coral.
- Fonts: Schibsted Grotesk (headings), Figtree (body and labels).
- Highlight words by colour only. **No italic serif accent words.**
- Never use the photo `flux-woman-videocall` or a look-alike (woman in a green sweater at a laptop). It has been deleted.
- Ask Marco before taking photos from MHCB or generating new images.

## Stack
- Astro (`astro.config.mjs`), Sanity CMS (use Sanity MCP for schema and content operations), global CSS in `src/styles/global.css`.
- Hosting: Cloudflare Pages, so deploy = git push. Never push without Marco's go.

## Separation from related projects
Not MyHealthcareBroker (MHB) and not living-in-germany.org. These are separate brands; don't mix assets.
