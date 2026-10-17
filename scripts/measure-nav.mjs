import { chromium } from 'playwright-core';
let browser; for (const channel of ['chrome','msedge']) { try { browser = await chromium.launch({ channel }); break; } catch {} }
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
await page.goto(process.argv[2], { waitUntil: 'load', timeout: 60000 }); await page.waitForTimeout(1500);
const r = await page.evaluate(() => {
  const P = ['fontFamily','fontSize','fontWeight','lineHeight','color','backgroundColor','borderRadius','border','borderBottom','borderRight','boxShadow','padding','margin','gap','height','width','position','top','textTransform','display','alignItems','justifyContent','letterSpacing'];
  const cs = el => { const s = getComputedStyle(el); const o = {}; for (const p of P) { const v = s[p]; if (v && v !== 'none' && v !== 'normal' && v !== 'auto' && v !== '0px' && v !== 'rgba(0, 0, 0, 0)' && v !== 'static') o[p] = v; } return o; };
  const box = el => { const b = el.getBoundingClientRect(); return [Math.round(b.x), Math.round(b.y), Math.round(b.width), Math.round(b.height)]; };
  const t = el => (el.innerText || '').trim().replace(/\s+/g,' ').slice(0,50);
  // everything in the top 140px of the page
  const out = [];
  for (const el of document.querySelectorAll('body *')) {
    const b = el.getBoundingClientRect(); if (b.height === 0 || b.width === 0 || b.top > 135 || b.top < -1) continue;
    if (!['NAV','HEADER','DIV','UL','LI','A','BUTTON','SPAN','IMG','SVG','P'].includes(el.tagName)) continue;
    const kids = el.children.length; const txt = t(el);
    if (el.tagName === 'DIV' && (b.width < 100 || b.height < 20)) continue;
    out.push({ tag: el.tagName.toLowerCase(), cls: (typeof el.className==='string'?el.className:'').slice(0,50), text: txt, box: box(el), kids, css: cs(el), svg: el.tagName==='SVG' ? [el.getAttribute('viewBox'), getComputedStyle(el).fill, getComputedStyle(el).stroke, el.getAttribute('width')] : undefined, src: el.tagName==='IMG' ? (el.currentSrc||'').slice(-70) : undefined });
    if (out.length > 90) break;
  }
  const h = document.querySelector('header, .header, [class*=header]');
  return { sticky: h ? [h.className, getComputedStyle(h).position, getComputedStyle(h).top, getComputedStyle(h).zIndex, getComputedStyle(h).boxShadow, getComputedStyle(h).borderBottom] : null, items: out };
});
console.log(JSON.stringify(r, null, 0).replace(/\},\{/g, '},\n{'));
await browser.close();
