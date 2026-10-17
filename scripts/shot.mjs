// Screenshot helper for the design-clone component loop and later smoke tests.
// Usage: node scripts/shot.mjs <url> <out.jpg> [--width 1440] [--height 900] [--full] [--selector CSS] [--hover CSS] [--click CSS]
// Uses the locally installed Chrome/Edge via playwright-core (no browser download).
import { createRequire } from 'node:module';
import { join } from 'node:path';
// playwright-core is not a repo dependency: try local, then the global npm install.
const require = createRequire(import.meta.url);
let pw;
try { pw = require('playwright-core'); } catch {
  const g = join(process.env.APPDATA || '', 'npm', 'node_modules', 'playwright', 'node_modules', 'playwright-core');
  pw = require(g);
}
const { chromium } = pw;

const args = process.argv.slice(2);
const url = args[0];
const out = args[1];
if (!url || !out) {
  console.error('usage: node scripts/shot.mjs <url> <out.jpg> [--width N] [--height N] [--full] [--selector CSS] [--hover CSS] [--click CSS]');
  process.exit(1);
}
const opt = (name, def) => {
  const i = args.indexOf(`--${name}`);
  return i === -1 ? def : args[i + 1];
};
const flag = (name) => args.includes(`--${name}`);

const width = Number(opt('width', 1440));
const height = Number(opt('height', 900));

let browser;
for (const channel of ['chrome', 'msedge']) {
  try {
    browser = await chromium.launch({ channel, headless: true });
    break;
  } catch (e) {
    if (channel === 'msedge') throw e;
  }
}
const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: 1 });
await page.goto(url, { waitUntil: 'networkidle', timeout: 60_000 });
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(300);
if (flag('full')) {
  await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise((r) => setTimeout(r, 120)); } window.scrollTo(0, 0); });
  await page.waitForTimeout(800);
}
const hover = opt('hover');
if (hover) { await page.hover(hover); await page.waitForTimeout(300); }
const click = opt('click');
if (click) { await page.click(click); await page.waitForTimeout(400); }
const selector = opt('selector');
const shotOpts = { path: out, type: out.endsWith('.png') ? 'png' : 'jpeg', ...(out.endsWith('.png') ? {} : { quality: 85 }) };
if (selector) {
  await page.locator(selector).first().screenshot(shotOpts);
} else {
  await page.screenshot({ ...shotOpts, fullPage: flag('full') });
}
await browser.close();
console.log(`saved ${out}`);
