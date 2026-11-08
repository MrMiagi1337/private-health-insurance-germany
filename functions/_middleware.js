// Cloudflare Pages middleware: maintenance mode while the redesign is built.
// Every request gets a 503 with Retry-After, so Google keeps the URLs instead of dropping them.
// robots.txt and favicons stay reachable (a 503 on robots.txt stops all crawling).
// To go live again: delete this file and push.
const PASS = ['/robots.txt', '/favicon.ico', '/favicon.svg'];

const PAGE = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Private Health Insurance Germany: back soon</title>
<link rel="icon" href="/favicon.svg">
<style>
  body { margin: 0; min-height: 100vh; display: grid; place-items: center; background: #FCF8EF; color: #10201E;
         font-family: system-ui, -apple-system, "Segoe UI", sans-serif; padding: 16px; box-sizing: border-box; }
  main { max-width: 520px; }
  h1 { color: #0A4D4A; font-size: clamp(1.6rem, 5vw, 2.2rem); line-height: 1.15; margin: 0 0 16px; }
  p { font-size: 1.05rem; line-height: 1.6; margin: 0; }
  .bar { width: 48px; height: 4px; background: #F5B700; margin-bottom: 24px; border-radius: 2px; }
</style>
</head>
<body>
<main>
  <div class="bar"></div>
  <h1>Private Health Insurance Germany is getting a new look</h1>
  <p>We are rebuilding this site and will be back shortly with updated guides on private health insurance for expats in Germany.</p>
</main>
</body>
</html>`;

export async function onRequest({ request, next }) {
  const { pathname } = new URL(request.url);
  if (PASS.includes(pathname)) return next();
  return new Response(PAGE, {
    status: 503,
    headers: { 'content-type': 'text/html; charset=utf-8', 'retry-after': '86400', 'cache-control': 'no-store' },
  });
}
