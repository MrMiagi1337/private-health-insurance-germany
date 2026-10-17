// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import os from 'node:os';
import path from 'node:path';

export default defineConfig({
  site: 'https://private-health-insurance-germany.com',
  // Canonical URL form is WITHOUT a trailing slash (e.g. /guide/who-qualifies).
  // `format: 'file'` emits /guide/who-qualifies.html instead of
  // /guide/who-qualifies/index.html, so every internal <a href> in the codebase
  // (all slash-less) points straight at the canonical URL with no 3xx redirect.
  // `trailingSlash: 'never'` makes the canonical link, sitemap, and dev server
  // agree on the no-slash form. Netlify 301s any stray /…/ request to no-slash.
  trailingSlash: 'never',
  build: {
    format: 'file',
  },
  integrations: [
    sitemap({
      // Exclude any pages you don't want indexed
      filter: (page) => !page.includes('/404'),
    }),
  ],
  // Generate static HTML for every page — best for SEO + Netlify
  output: 'static',
  // Vite's dependency cache lives outside the repo. On this Windows machine,
  // On Marco's Windows PC Vite's dependency pre-bundling fails on a FRESH cache
  // dir with "UNKNOWN: unknown error, open ...deps_temp_*/chunk-*.js" (a Windows
  // file-lock / rename race inside the optimizer; no antivirus involved, AV is
  // off). This static site has no client deps that need pre-bundling, so the
  // optimizer is disabled entirely. cacheDir stays configurable so several dev
  // servers can run side by side; on Linux/Netlify the OS temp dir is used.
  vite: {
    optimizeDeps: {
      noDiscovery: true,
      include: [],
      // sourcemap:false removes the .map outputs whose post-processing step
      // (writeFileSync on a freshly written chunk) is the line that fails.
      esbuildOptions: { sourcemap: false },
    },
    cacheDir:
      process.env.VITE_CACHE_DIR ||
      (process.platform === 'win32'
        ? 'C:/tmp/phig-vite-cache'
        : path.join(os.tmpdir(), 'phig-vite-cache')),
  },
});
