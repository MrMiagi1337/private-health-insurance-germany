// node scripts/measure.mjs <url> <out.json> [--width 1440] [--height 900]
// Dumps computed styles for header, each top-level section of <main>/<body>
// and representative children (headings, paragraphs, links, buttons, images).
import { chromium } from 'playwright-core';
import fs from 'node:fs';
const [url, out] = process.argv.slice(2);
const arg = (k, d) => { const i = process.argv.indexOf(k); return i > -1 ? process.argv[i + 1] : d; };
const width = +arg('--width', 1440), height = +arg('--height', 900);
let browser;
for (const channel of ['chrome', 'msedge']) { try { browser = await chromium.launch({ channel }); break; } catch {} }
const page = await browser.newPage({ viewport: { width, height } });
await page.goto(url, { waitUntil: 'load', timeout: 60000 });
await page.waitForTimeout(1500);
// scroll through to trigger lazy content
await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 700) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); } window.scrollTo(0, 0); });
await page.waitForTimeout(800);
const data = await page.evaluate(() => {
  const P = ['fontFamily','fontSize','fontWeight','lineHeight','letterSpacing','color','backgroundColor','backgroundImage','borderRadius','border','borderTop','borderBottom','boxShadow','padding','margin','gap','display','gridTemplateColumns','flexDirection','alignItems','justifyContent','maxWidth','width','height','textTransform','objectFit','opacity'];
  const cs = (el) => { const s = getComputedStyle(el); const o = {}; for (const p of P) { const v = s[p]; if (v && v !== 'none' && v !== 'normal' && v !== 'auto' && v !== '0px' && v !== 'rgba(0, 0, 0, 0)' && v !== 'static') o[p] = v; } return o; };
  const box = (el) => { const r = el.getBoundingClientRect(); return { x: Math.round(r.x), y: Math.round(r.y + window.scrollY), w: Math.round(r.width), h: Math.round(r.height) }; };
  const txt = (el) => (el.innerText || el.getAttribute('alt') || '').trim().replace(/\s+/g, ' ').slice(0, 90);
  const sel = 'h1,h2,h3,h4,p,a,button,img,picture,svg,ul,li,input,label,[class*=card],[class*=Card],[class*=badge],[class*=pill],[class*=tag],[class*=chip]';
  const describe = (root, depth = 0, max = 60) => {
    const items = [];
    for (const el of root.querySelectorAll(sel)) {
      if (items.length >= max) break;
      const b = box(el); if (b.w === 0 || b.h === 0) continue;
      const e = { tag: el.tagName.toLowerCase(), cls: (el.className && typeof el.className === 'string') ? el.className.slice(0, 80) : '', text: txt(el), box: b, css: cs(el) };
      if (el.tagName === 'IMG') { e.src = (el.currentSrc || el.src || '').slice(0, 160); e.natural = [el.naturalWidth, el.naturalHeight]; }
      if (el.tagName === 'SVG') { e.svgSize = [el.getAttribute('width'), el.getAttribute('height'), el.getAttribute('viewBox')]; e.fill = getComputedStyle(el).fill; e.stroke = getComputedStyle(el).stroke; }
      items.push(e);
    }
    return items;
  };
  const header = document.querySelector('header') || document.querySelector('nav')?.closest('div');
  const footer = document.querySelector('footer');
  const main = document.querySelector('main') || document.body;
  const sections = [];
  const tops = Array.from(main.children).filter(el => box(el).h > 40);
  for (const s of tops) {
    const b = box(s);
    sections.push({ tag: s.tagName.toLowerCase(), id: s.id, cls: (typeof s.className === 'string' ? s.className : '').slice(0, 120), box: b, css: cs(s), firstText: txt(s).slice(0, 120), children: describe(s, 0, 70) });
  }
  const fonts = Array.from(document.fonts).map(f => `${f.family} ${f.weight} ${f.style} ${f.status}`);
  const root = cs(document.documentElement); const body = cs(document.body);
  const cssVars = {}; for (const sh of document.styleSheets) { try { for (const r of sh.cssRules) { if (r.selectorText === ':root' || r.selectorText === 'html') { for (const p of r.style) if (p.startsWith('--')) cssVars[p] = r.style.getPropertyValue(p).trim(); } } } catch {} }
  return { url: location.href, viewport: [innerWidth, innerHeight], docHeight: document.body.scrollHeight, fonts: [...new Set(fonts)], root, body, cssVars, header: header ? { box: box(header), css: cs(header), children: describe(header, 0, 60) } : null, sections, footer: footer ? { box: box(footer), css: cs(footer), children: describe(footer, 0, 80) } : null };
});
fs.writeFileSync(out, JSON.stringify(data, null, 1));
console.log('saved', out, 'sections', data.sections.length, 'height', data.docHeight, 'fonts', data.fonts.slice(0, 6));
await browser.close();
