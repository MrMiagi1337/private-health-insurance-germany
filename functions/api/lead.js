// Cloudflare Pages Function: POST /api/lead
// Proxies the lead form to the MHCB funnel endpoint so the browser never talks to MHCB directly.
// Env (Pages project settings): MHCB_LEAD_ENDPOINT (optional, defaults to production).
const ALLOWED = ['source', 'name', 'email', 'phone', 'status', 'consent', 'hp', 'ts', 'pageUrl', 'landingPage', 'referrer',
  'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'utmSource', 'utmMedium', 'utmCampaign', 'utmTerm', 'utmContent'];
const MAX_BODY = 10 * 1024;
const MAX_FIELD = 500;

const json = (status, body) =>
  new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json', 'cache-control': 'no-store' } });

export async function onRequest({ request, env }) {
  if (request.method !== 'POST') return json(405, { ok: false, error: 'Method not allowed' });
  let raw;
  try { raw = await request.text(); } catch { return json(400, { ok: false, error: 'Invalid body' }); }
  if (raw.length > MAX_BODY) return json(413, { ok: false, error: 'Payload too large' });
  let data;
  try { data = JSON.parse(raw); } catch { return json(400, { ok: false, error: 'Invalid JSON' }); }
  if (!data || typeof data !== 'object' || Array.isArray(data)) return json(400, { ok: false, error: 'Invalid JSON' });

  const clean = {};
  for (const k of ALLOWED) {
    const v = data[k];
    if (typeof v === 'string') clean[k] = v.trim().slice(0, MAX_FIELD);
    else if (typeof v === 'boolean' || typeof v === 'number') clean[k] = v;
  }
  if (!clean.name || clean.name.length < 2) return json(400, { ok: false, error: 'Invalid name' });
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(clean.email || '')) return json(400, { ok: false, error: 'Invalid email' });
  if (clean.consent !== true) return json(400, { ok: false, error: 'Consent required' });
  // Honeypot: pretend success, do not forward.
  if (clean.hp) return json(200, { ok: true });

  const endpoint = (env && env.MHCB_LEAD_ENDPOINT) || 'https://www.myhealthcarebroker.com/api/funnel-lead';
  const headers = { 'content-type': 'application/json' };
  const ip = request.headers.get('cf-connecting-ip') || request.headers.get('x-forwarded-for');
  if (ip) headers['x-forwarded-for'] = ip;
  try {
    const up = await fetch(endpoint, { method: 'POST', headers, body: JSON.stringify(clean), signal: AbortSignal.timeout(8000) });
    const text = await up.text();
    return new Response(text, {
      status: up.status,
      headers: { 'content-type': up.headers.get('content-type') || 'application/json', 'cache-control': 'no-store' },
    });
  } catch {
    return json(502, { ok: false, error: 'Upstream unavailable' });
  }
}
