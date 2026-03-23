// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://living-in-germany.org',
  integrations: [
    sitemap({
      // Exclude any pages you don't want indexed
      filter: (page) => !page.includes('/404'),
    }),
  ],
  // Generate static HTML for every page — best for SEO + Netlify
  output: 'static',
});
