# DESIGN-TOKENS: the reference site reference (measured 2026-10-16, getComputedStyle, 1440 viewport)

Reference: the reference site/en (home), /en/v/private-health-insurance (product), /en/expat-guide/opportunity-card (article), home at 390 wide.
Screenshots in design-ref/: ref-home.jpg, ref-product.jpg (stitched from 4 viewport shots, sticky header repeats), ref-article.jpg, ref-home-mobile.jpg.
Legend: MEASURED = real the reference site value. BRAND = target substitution.

## 1. Typography (MEASURED)
| Role | Family | Size / line-height | Weight | Letter-spacing | Color |
|---|---|---|---|---|---|
| body | Figtree | 16 / 24 | 400 | normal | #667093 (home) / #33406f (product, cards) |
| h1 home hero | Figtree | 40 / 50 | 850 | normal | #00104b |
| h1 product/article | Figtree | 50 / 62.5 | 850 | normal | #00104b (white on dark article hero) |
| h2 | Figtree | 40 / 50 | 850 | normal | #00104b |
| h3 (card titles) | Figtree | 24 / 30 | 700 | normal | #00104b |
| article sub-heading | Figtree | 32 / 40 | 850 | normal | #00104b |
| hero subtitle | Figtree | 24 / 36 | 400 | normal | #667093 |
| card paragraph | Figtree | 16 / 24 | 400 | normal | #33406f |
| article body | Figtree | 20 / 32 | 400 | normal | #33406f (column 640px) |
| small / caption | Figtree | 13 / 20-23 | 400 | normal | #667093 |
| nav link | Figtree | 14 / 21 | 500 | normal | #667093 |
| button primary | Figtree | 16 | 700 | normal | #fff |
| button small (header) | Figtree | 14 | 700 | normal | #0070f0 / #fff |
| FAQ question | Figtree | 20 | 400 | normal | #33406f |
| footer heads / links | Figtree | 16 | 700 / 400 | normal | #00104b / #667093 |
Mobile (390): h1 28/35, h2 26, container padding 20.
Headings are very heavy (850), no tracking changes. An italic serif (Merriweather-like) appears only in video banners and review quotes.

## 2. Colors (MEASURED, hex)
| Role | the reference site |
|---|---|
| page bg | #ffffff |
| alt section bg | #fafafb (home bands), #f8f8f8 (product hero), #f2f3f6 (form wrapper) |
| card bg | #ffffff |
| primary text / headings | #00104b |
| body text | #33406f (strong), #667093 (muted) |
| primary accent (buttons) | #0070f0 |
| link / blue text | #0065d8 |
| primary button | bg #0070f0, text #ffffff |
| secondary button | transparent, border 0.8px #0070f0, text #0070f0 |
| border | #e5e7ed |
| icon tile bg | #f2f8ff |
| tint panels | #cce4ff (key figure, article bands) |
| highlight / alert | #d10c55 text on pale pink |
| dark card | #00104b |
| footer | white page bg, heads #00104b, links #667093 |
| promo top bar | green, not measured exactly (screenshot only) |

## 3. Shape (MEASURED)
| Item | Value |
|---|---|
| card radius | 16px audience/tariff cards; 12px key-figure cards; 8px small tiles/media |
| button radius | 6px (main), 4px (header small) |
| input radius | 6px |
| CTA banner radius | 10px |
| icon tile | 64x64, radius 8, bg #f2f8ff |
| avatars | 50% |
| card border | 0.8px #e5e7ed, no shadow (home audience cards) |
| shadows (3) | s1 0 2px 4px rgba(0,16,75,.2) (31 uses, key cards); s2 0 1px 2.5px + 0 2px 5px rgba(0,16,75,.15) (header button); s3 0 4px 12px rgba(0,16,75,.15) (product audience tiles) |
Shadows are navy-tinted, not black.

## 4. Layout (MEASURED)
| Item | Value |
|---|---|
| container | max-width 1160 with 20px side padding (inner 1120) |
| narrow widths | 780 section intros, 640 article column, 580/840/880 misc |
| mobile side padding | 20px |
| section rhythm | plain sections: margin 140px top and bottom. Alt-bg sections: padding 80-86 (home) or 140 (product), margin 0 |
| examples | tariffBoxes 86/86 #fafafb; keyfigures 80/80 #fafafb; advantages 140/140 #fafafb; product hero 192 top / 140 bottom #f8f8f8 |
| mobile rhythm | margin 48, alt padding 32-48 |
| card grids | audience 3 cols, 357px cards, ~25px gap, row 2 = two ~548px cards (flex-wrap); top-up 3 cols; product audience tiles 4 cols; key figures 3-col bento 353px wide (one navy card spans 2 rows, 714px) |
| header | promo bar 40px, utility bar ~37px, main nav ~61px (logo, 4 links left; phone + "Get a consultation" right); sticky; product page adds 65px tab nav |
| home hero | text col ~605px left, photo + "Not sure" card right, 539px tall |

## 5. Buttons (MEASURED)
| | primary | secondary | header small |
|---|---|---|---|
| bg | #0070f0 | transparent | #fff or #0070f0 |
| text | #fff | #0070f0 | #0070f0 / #fff |
| border | none | 0.8px #0070f0 | none |
| padding | 12px 24px | 12px 24px | 6px 0 |
| radius | 6px | 6px | 4px |
| font | 16 / 700 | 16 / 700 | 14 / 700 |
| height | 48px | ~50px | 36px |
Label ends with arrow glyph.

## 6. Fonts
- the reference site serves /assets/fonts/figtree.woff2 (variable 300-900, the only registered @font-face). Figtree is an open-source (OFL) Google Font, so it can be used directly.
- Italic serif accent in video banners is probably Merriweather (not registered in @font-face; unverified). Optional.

| the reference site | target mapping |
|---|---|
| Figtree variable, headings 850 | Figtree from Google Fonts (identical), load wght 300..900 |
| Avenir, Arial fallback | system-ui, sans-serif |
| target currently Inter | replace with Figtree (or Figtree headings + Inter body) |

## 7. READY CSS block (names for the target project)
```css
:root {
  /* ---- BRAND: exact the reference site palette (Marco, 2026-10-16: "use the reference site blue"; supersedes teal/navy substitution) ---- */
  --blue:#0070F0; --blue-dk:#0065D8; --blue-tint:#F2F8FF; --blue-pill:#E5F1FF; --blue-light:#CCE4FF;
  --navy:#00104B;
  --pink:#E80D5F; --pink-dk:#D10C55; --pink-tint:#FEF2F7;
  --pastel-pink:#FBDADB; --pastel-mint:#D5F1E6; --pastel-blue:#E1EEFF; --green:#1E9E6A;
  --band:#FAFAFB; --band-form:#F2F3F6; --surface:#FFFFFF;
  /* legacy aliases kept: --teal=blue, --teal-dk=blue-dk, --teal-tint=blue-tint, --coral=pink, --cream=band, --primary=blue */

  /* ---- MEASURED from the reference site (neutrals) ---- */
  --text:       #33406F;
  --text-muted: #667093;
  --text-faint: #999FB7;
  --border:     #E5E7ED;

  /* type: MEASURED */
  --font-sans: 'Figtree', system-ui, -apple-system, sans-serif;
  --fs-body: 16px;    --lh-body: 24px;
  --fs-h1: 50px;      --lh-h1: 62.5px;   /* home hero variant 40/50 */
  --fs-h2: 40px;      --lh-h2: 50px;
  --fs-h3: 24px;      --lh-h3: 30px;
  --fs-lead: 24px;    --lh-lead: 36px;
  --fs-article: 20px; --lh-article: 32px;
  --fs-small: 13px;   --lh-small: 20px;
  --fs-nav: 14px;
  --fw-heading: 850; --fw-h3: 700; --fw-body: 400; --fw-nav: 500; --fw-btn: 700;

  /* shape: MEASURED */
  --radius-card: 16px;
  --radius-card-sm: 12px;
  --radius-tile: 8px;
  --radius-btn: 6px;
  --radius-input: 6px;
  --radius-banner: 10px;
  --border-w: 0.8px;

  /* shadows: MEASURED shapes, brand-navy tint */
  --sh-card:   0 2px 4px rgba(15,42,68,.2);
  --sh-raised: 0 4px 12px rgba(15,42,68,.15);
  --sh-btn:    0 1px 2.5px rgba(15,42,68,.15), 0 2px 5px rgba(15,42,68,.15);

  /* layout: MEASURED */
  --container: 1160px;      /* includes 20px padding each side */
  --gutter: 20px;
  --narrow: 780px;
  --article: 640px;
  --section-y: 140px;       /* plain-section margin */
  --section-pad-alt: 80px;  /* alt-band padding (home 80-86, product 140) */
  --section-y-mobile: 48px;
  --grid-gap: 24px;         /* measured ~25px */
  --header-h: 98px;         /* utility 37 + nav 61 */
  --btn-h: 48px;
  --btn-pad: 12px 24px;
}
```

## 8. Page component inventory (the reference site)
### Homepage (margin/padding measured)
1. Promo bar (green, 40px, dismissible), utility bar, sticky white main nav.
2. JAEG alert accordion: pale pink pill, 12px radius, inside hero.
3. Hero split ~55/45: left h1 40/50, 24px subtitle, tab pills, 3 check bullets, primary CTA; right photo plus "Not sure" bordered card with secondary button. margin 130 top / 40 bottom, white.
4. Trust tab carousel (Awards/Customers/Experts/Regulation), text left, award badges right, dot pagination. margin 40/40, white.
5. Audience cards 3-up plus row of 2 (Expats card and "Not sure?" photo card); 64px icon tile, h3 24, tag pills, 16px radius, 0.8px border. padding 86/86, bg #fafafb.
6. Top-up cards 3-up in the same band.
7. Review carousel, 3-up Trustpilot-style cards. margin 140/140, white.
8. Referral banner: pale-blue panel radius 16, text left, photo right, round price bubble. margin 140.
9. Key-figures bento 3 cols (white, tall navy, blue, pale blue, white), radius 12, centered eyebrow pill + h2. padding 80/80, #fafafb.
10. Security chips row (3 small bordered chips), centered. margin 140.
11. App-preview carousel: pastel panels (pink, mint) with phone mockup, checklist, button. padding 80/80, #fafafb.
12. Text grid 2x2 (h3 + paragraph) beside image, 780 wide. margin 140.
13. Overview boxes 3-up (guide, video, ebook): outlined cards, product image, small button. margin 140.
14. Consultation form: grey (#f2f3f6) wrapper radius 16 with advisor cutout, inner white card with radio tiles. margin 140.
15. FAQ accordion, 8 rows, 20px question, plus icon, hairline dividers. margin 140.
16. CTA band: solid #0070f0, radius 10, padding 36/48, white button right. margin 140.
17. Footnote, trust chips, 4-column footer (Full Insurance, Company, Expat Guide, Legal) with bold heads, social icons row.

### Product page
1. Centered hero on #f8f8f8, padding 192 top / 140 bottom: h1 50/62, 24px paragraphs, primary + secondary buttons.
2. Sticky on-page tab nav (Advantages, Requirements, Costs, ...), white, 65px, active = pale-blue pill.
3. Intro + 4 audience tiles (icon + label, shadow s3) on #fafafb, padding 140/0.
4. Numbered facts list (4 items, 780 col). margin 140.
5. Video banner: photo left, blue panel right, serif italic title. margin 140.
6. Long-form text sections (h2, 640-780 col, h3 subsections, hairline dividers), repeated. margin 140/140 (some 40 top / 100 gap).
7. Blue CTA banners (radius 10) between sections.
8. Cost example text blocks (640 col).
9. Private vs public comparison rows (2 columns, blue uppercase labels).
10. Advisor strip: avatar, "Do you have any questions?", big phone number; bordered, sits below tab nav.
11. Advantages 3-up numbered columns (blue italic numerals), padding 140/140, #fafafb.
12. Consultation form, magazine text grid (#fafafb, 140/140), mockup tabs, ebook block, 7-step breakdown, Trustpilot slider, final form, footer.

### Article page
Full-bleed dark navy photo hero (white 50px h1, 20px intro, read time), 640px column, "Reviewed by experts" badge, TOC list with arrow rows, pale summary box, pale-blue (#cce4ff) bands, FAQ accordion, beige References box, author block with round avatar, related-articles 3-up carousel, footer.

### Mobile (390)
Hamburger nav, hero image moves above h1, hero card becomes full-width, audience cards become single-column horizontal rows with chevron, h1 28/35, margins 48.

## 9. Not measured or caveats
- Cookie dialog (German, shadow DOM) appeared on product page; dismissed via script. Home/article had none.
- Promo bar green and the beige References box colors estimated from screenshots only.
- Header/footer computed backgrounds report transparent (white comes from the page); sticky behavior inferred from screenshots.
- Product page 24.5k px full-page capture failed; stitched from 4 viewport captures at 1440x6200.
- Screenshot widths: home 1425 and mobile 375 (scrollbar).
