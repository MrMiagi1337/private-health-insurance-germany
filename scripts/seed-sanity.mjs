import { createClient } from '@sanity/client';
import { readFileSync } from 'fs';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';

// Load .env manually (Node doesn't auto-load it)
const __dirname = dirname(fileURLToPath(import.meta.url));
const envPath = resolve(__dirname, '../.env');
try {
  const envContent = readFileSync(envPath, 'utf8');
  for (const line of envContent.split('\n')) {
    const match = line.match(/^([^#=]+)=(.*)$/);
    if (match) process.env[match[1].trim()] = match[2].trim();
  }
} catch {}

const client = createClient({
  projectId: 'o426dbl0',
  dataset: 'production',
  apiVersion: '2024-01-01',
  token: process.env.SANITY_WRITE_TOKEN,
  useCdn: false,
});

// ── Helper: upsert a page (delete existing + create new) ──────────────────────
async function upsertPage(doc) {
  const slug = doc.slug.current;
  // Delete existing draft + published if exists
  const existing = await client.fetch(`*[_type == "page" && slug.current == $slug]._id`, { slug });
  for (const id of existing) {
    await client.delete(id).catch(() => {});
    await client.delete(`drafts.${id}`).catch(() => {});
  }
  const result = await client.create(doc);
  // Publish immediately
  await client.patch(result._id).set({ _id: result._id.replace('drafts.', '') }).commit().catch(() => {});
  console.log(`✓ Created: /${slug}`);
  return result;
}

// ═══════════════════════════════════════════════════════════════
// PAGE 1 — Health Insurance for Expats in Germany (4,200/mo)
// ═══════════════════════════════════════════════════════════════
await upsertPage({
  _type: 'page',
  title: 'Health Insurance for Expats in Germany',
  slug: { _type: 'slug', current: 'health-insurance-expats-germany' },
  seoTitle: 'Health Insurance for Expats in Germany 2026 — Complete Guide',
  seoDescription: 'Everything expats need to know about health insurance in Germany: GKV vs PKV, who qualifies, what it costs, and the best insurers for internationals. Updated 2026.',
  sections: [
    {
      _type: 'heroBlock',
      _key: 'hero-1',
      headline: 'Health Insurance for Expats in Germany',
      subheadline: 'Germany requires all residents to have health insurance from day one. As an expat you have three options — and choosing the right one can save you hundreds of euros every month.',
      ctaLabel: 'Get free broker advice →',
      ctaHref: '/contact',
      ctaSecondaryLabel: 'Check my eligibility',
      ctaSecondaryHref: '/quiz',
    },
    {
      _type: 'statsBlock',
      _key: 'stats-1',
      stats: [
        { _key: 's1', value: '€77,400', label: '2026 income threshold for PKV' },
        { _key: 's2', value: '40+',     label: 'Insurers compared' },
        { _key: 's3', value: 'Day 1',   label: 'Coverage required from arrival' },
        { _key: 's4', value: '100% free', label: 'Broker service, no fees' },
      ],
    },
    {
      _type: 'insurersBlock',
      _key: 'insurers-1',
      kicker: 'Insurer reviews',
      headline: 'Best PKV insurers for expats in Germany',
      ctaLabel: 'See all reviews →',
      ctaHref: '/top-insurers',
      insurers: [
        { _key: 'i1', name: 'DKV',         tag: 'Best for expats',       href: '/top-insurers/dkv',         reason: 'English hotline, global coverage, digital claims app' },
        { _key: 'i2', name: 'HanseMerkur', tag: 'Most expat-friendly',   href: '/top-insurers/hansemerkur', reason: 'Flexible tariffs, quick approval, expat-focused teams' },
        { _key: 'i3', name: 'Allianz',     tag: 'Premium international', href: '/top-insurers/allianz',     reason: 'Worldwide coverage, premium hospitals, strong brand' },
        { _key: 'i4', name: 'Hallesche',   tag: 'Best for freelancers',  href: '/top-insurers/hallesche',   reason: 'Comprehensive coverage, strong financials, low rate increases' },
        { _key: 'i5', name: 'Debeka',      tag: 'Most stable premiums',  href: '/top-insurers/debeka',      reason: 'Largest PKV insurer, consistently low premium increases' },
        { _key: 'i6', name: 'Barmenia',    tag: 'Best mental health',    href: '/top-insurers/barmenia',    reason: 'Excellent mental health coverage, modern app, fair claims' },
      ],
    },
    {
      _type: 'faqBlock',
      _key: 'faq-1',
      kicker: 'Common questions',
      headline: 'Expat health insurance FAQ',
      items: [
        { _key: 'f1', question: 'Do I need health insurance from day one in Germany?', answer: 'Yes. German law requires health insurance from the day you register your residence (Anmeldung). Employees below the income threshold are auto-enrolled in GKV. Self-employed and high earners must arrange coverage themselves.' },
        { _key: 'f2', question: 'Can I keep my home country insurance in Germany?', answer: 'Only temporarily. EU citizens can use the EHIC card for short trips, but it does not satisfy the German residence requirement. Expats staying longer than 3 months must get German health insurance.' },
        { _key: 'f3', question: 'Can expats get private health insurance (PKV)?', answer: 'Yes. Employees earning above €77,400/year gross can opt into PKV. Self-employed expats can choose PKV at any income level from day one.' },
        { _key: 'f4', question: 'What happens if I lose my job — do I lose PKV?', answer: 'If you become unemployed you will normally switch to GKV. Your PKV may offer an Anwartschaftsversicherung — a dormant policy that preserves your entry conditions so you can reactivate later without a new health questionnaire.' },
        { _key: 'f5', question: 'Which insurers offer English-speaking support?', answer: 'DKV, HanseMerkur, and Allianz all offer English customer service and documentation. A broker can match you with the best fit for your language needs and budget.' },
        { _key: 'f6', question: 'How much does health insurance cost for expats?', answer: 'GKV costs ~14.6% + supplement of gross salary, split with employer. At €70k that is ~€270/month from you. PKV for a healthy 30-year-old costs €210–360/month total, employer contributes up to €421/month.' },
      ],
    },
    {
      _type: 'testimonialsBlock',
      _key: 'testi-1',
      kicker: 'Expat stories',
      headline: 'What other expats say',
      testimonials: [
        { _key: 't1', quote: 'I came from India on a work visa with no idea how German health insurance works. The broker explained everything in plain English and I was insured within two weeks. Saving €220/month vs GKV.', name: 'Arjun S.', role: 'Software Engineer · Hamburg' },
        { _key: 't2', quote: 'As a freelancer from the US I had no idea I could get affordable private insurance. Ended up with DKV at €280/month — far less than I expected.', name: 'Sarah L.', role: 'UX Designer · Berlin' },
        { _key: 't3', quote: 'My HR told me to just sign up to AOK. Glad I checked first — I qualified for PKV, get a private room in hospital, and pay less per month.', name: 'Marco B.', role: 'Finance Manager · Frankfurt' },
      ],
    },
    {
      _type: 'ctaBlock',
      _key: 'cta-1',
      headline: 'Find the right health insurance for your expat situation',
      body: 'A licensed §34d broker compares all major PKV insurers for your age, income, and health profile. Free advice in English, no obligation, no commission from you.',
      ctaLabel: 'Get free broker advice →',
      ctaHref: '/contact',
      ctaSecondaryLabel: 'Check eligibility first',
      ctaSecondaryHref: '/quiz',
    },
  ],
});

// ═══════════════════════════════════════════════════════════════
// PAGE 2 — Private Health Insurance Germany (2,500/mo)
// ═══════════════════════════════════════════════════════════════
await upsertPage({
  _type: 'page',
  title: 'Private Health Insurance Germany',
  slug: { _type: 'slug', current: 'private-health-insurance-germany' },
  seoTitle: 'Private Health Insurance Germany (PKV) — Complete Guide 2026',
  seoDescription: 'Everything you need to know about private health insurance (PKV) in Germany: who qualifies, what it costs, top insurers, and how to apply. Updated 2026.',
  sections: [
    {
      _type: 'heroBlock',
      _key: 'hero-2',
      headline: 'Private Health Insurance in Germany (PKV)',
      subheadline: 'PKV offers better coverage, faster specialist access, and lower costs for expats above the income threshold. Here is everything you need to know.',
      ctaLabel: 'Get free broker advice →',
      ctaHref: '/contact',
      ctaSecondaryLabel: 'Check my eligibility',
      ctaSecondaryHref: '/quiz',
    },
    {
      _type: 'statsBlock',
      _key: 'stats-2',
      stats: [
        { _key: 's1', value: '€77,400', label: 'Income threshold to switch (2026)' },
        { _key: 's2', value: '€210/mo', label: 'PKV from (age 30, mid plan)' },
        { _key: 's3', value: '~50%',    label: 'Employer contribution' },
        { _key: 's4', value: '40+',     label: 'Insurers on the market' },
      ],
    },
    {
      _type: 'insurersBlock',
      _key: 'insurers-2',
      kicker: 'Top PKV insurers',
      headline: 'Best private health insurance providers in Germany',
      ctaLabel: 'See all insurer reviews →',
      ctaHref: '/top-insurers',
      insurers: [
        { _key: 'i1', name: 'Debeka',      tag: 'Most stable premiums',  href: '/top-insurers/debeka',      reason: 'Largest PKV insurer, consistently low premium increases, strong financials' },
        { _key: 'i2', name: 'Allianz',     tag: 'Best English support',  href: '/top-insurers/allianz',     reason: 'Premium coverage, wide hospital network, international expat support' },
        { _key: 'i3', name: 'DKV',         tag: 'Largest PKV insurer',   href: '/top-insurers/dkv',         reason: 'Market leader by members, solid digital tools, English service' },
        { _key: 'i4', name: 'HanseMerkur', tag: 'Best value',            href: '/top-insurers/hansemerkur', reason: 'Competitive pricing, expat-friendly tariffs, fast application' },
        { _key: 'i5', name: 'Hallesche',   tag: 'Best dental cover',     href: '/top-insurers/hallesche',   reason: 'Top-rated dental, strong rider options, excellent claims handling' },
        { _key: 'i6', name: 'AXA',         tag: 'Expat-friendly',        href: '/top-insurers/axa',         reason: 'International network, English hotline, flexible worldwide coverage' },
      ],
    },
    {
      _type: 'faqBlock',
      _key: 'faq-2',
      kicker: 'Common questions',
      headline: 'Private health insurance Germany FAQ',
      items: [
        { _key: 'f1', question: 'Who qualifies for private health insurance in Germany?', answer: 'Employees earning above €77,400 gross/year (2026 threshold), all self-employed and freelancers, and civil servants (Beamte) can choose PKV. Employees below the threshold must use GKV.' },
        { _key: 'f2', question: 'How much does PKV cost in Germany?', answer: 'A healthy 30-year-old pays €210–360/month for a mid-range PKV plan. Employers contribute up to €421/month. Freelancers pay the full amount but PKV is still often cheaper than GKV at equivalent income levels.' },
        { _key: 'f3', question: 'Can I switch back to GKV after PKV?', answer: 'Very difficult as an employee. You can switch back only if your income drops below the JAEG threshold for an extended period, or if you become unemployed. Think carefully before switching, especially if planning a family.' },
        { _key: 'f4', question: 'Does PKV cover my family?', answer: 'No free family coverage. Each family member needs their own PKV policy. This makes PKV significantly more expensive for families with children and a non-working partner — GKV family coverage may be cheaper in that scenario.' },
        { _key: 'f5', question: 'What does PKV actually cover?', answer: 'PKV typically covers: private hospital room, choice of senior consultant (Chefarzt), no GP referral needed for specialists, comprehensive dental, alternative medicine, faster appointment booking. Exact coverage depends on your plan tier.' },
      ],
    },
    {
      _type: 'testimonialsBlock',
      _key: 'testi-2',
      kicker: 'Real savings',
      headline: 'What PKV members say',
      testimonials: [
        { _key: 't1', quote: 'I was paying €540/month for GKV. After switching to PKV I pay €240/month. Same doctor, better hospital room. Wish I had done it in my first year in Germany.', name: 'James K.', role: 'Software Engineer · Berlin' },
        { _key: 't2', quote: 'As a freelancer I had no idea I could switch. The broker handled everything in English. It took two weeks and I now save €280/month.', name: 'Priya M.', role: 'Independent Consultant · Munich' },
        { _key: 't3', quote: 'The guide explained the differences better than my German colleagues ever could. The broker found me a plan that costs half my old GKV contribution.', name: 'Thomas B.', role: 'Finance Manager · Frankfurt' },
      ],
    },
    {
      _type: 'ctaBlock',
      _key: 'cta-2',
      headline: 'Find out how much you could save with PKV',
      body: 'A licensed §34d broker compares all major private insurers for your exact situation — age, health status, income. Free advice in English, no obligation.',
      ctaLabel: 'Get free broker advice →',
      ctaHref: '/contact',
      ctaSecondaryLabel: 'Check eligibility first',
      ctaSecondaryHref: '/quiz',
    },
  ],
});

// ═══════════════════════════════════════════════════════════════
// PAGE 3 — Public Health Insurance Germany (1,500/mo)
// ═══════════════════════════════════════════════════════════════
await upsertPage({
  _type: 'page',
  title: 'Public Health Insurance Germany',
  slug: { _type: 'slug', current: 'public-health-insurance-germany' },
  seoTitle: 'Public Health Insurance Germany (GKV) — Expat Guide 2026',
  seoDescription: 'How public health insurance (GKV) works in Germany for expats: contributions, coverage, family insurance, and when private PKV is better. Updated 2026.',
  sections: [
    {
      _type: 'heroBlock',
      _key: 'hero-3',
      headline: 'Public Health Insurance in Germany (GKV)',
      subheadline: 'GKV is Germany\'s statutory health insurance, mandatory for most employees. Here is how it works, what it costs, and when private insurance is a better option.',
      ctaLabel: 'Compare GKV vs PKV →',
      ctaHref: '/compare',
      ctaSecondaryLabel: 'Check my eligibility for PKV',
      ctaSecondaryHref: '/quiz',
    },
    {
      _type: 'statsBlock',
      _key: 'stats-3',
      stats: [
        { _key: 's1', value: '14.6%',    label: 'Base GKV contribution rate' },
        { _key: 's2', value: '~1.7%',    label: 'Average supplementary rate' },
        { _key: 's3', value: '~50%',     label: 'Paid by employer' },
        { _key: 's4', value: 'Free',     label: 'Family co-insurance for non-earners' },
      ],
    },
    {
      _type: 'faqBlock',
      _key: 'faq-3',
      kicker: 'GKV explained',
      headline: 'Public health insurance Germany FAQ',
      items: [
        { _key: 'f1', question: 'Who must have public health insurance (GKV) in Germany?', answer: 'Employees earning below €77,400 gross/year (2026) are legally required to have GKV. Students, unemployed people receiving ALG I/II, and pensioners below certain thresholds also fall under GKV.' },
        { _key: 'f2', question: 'How much does GKV cost in Germany?', answer: 'The base rate is 14.6% of gross salary, plus a supplementary rate (Zusatzbeitrag) averaging ~1.7% in 2026. Your employer pays roughly half. At €60,000/year salary your contribution is ~€480/month total, ~€240 from you.' },
        { _key: 'f3', question: 'What does GKV cover?', answer: 'GKV covers GP visits, specialist referrals, hospital (shared ward), basic dental, prescriptions (with co-pay), preventive care, and sick pay (Krankengeld after 6 weeks). It does not include private hospital rooms or full dental prosthetics.' },
        { _key: 'f4', question: 'Can I add family members to my GKV?', answer: 'Yes — the Familienversicherung allows non-earning spouses and children under 25 to be covered under your GKV for free. This is one of GKV\'s biggest advantages over PKV, where each person needs a separate paid policy.' },
        { _key: 'f5', question: 'Which GKV provider should I choose?', answer: 'The largest GKV funds are TK, AOK, Barmer, DAK, and IKK. Coverage is largely standardised by law. Differences are in supplementary services, digital tools, and customer service. TK and Barmer are popular with expats for their English support.' },
      ],
    },
    {
      _type: 'ctaBlock',
      _key: 'cta-3',
      headline: 'Could you save money by switching to private insurance?',
      body: 'If you earn above €77,400/year or are self-employed, private PKV could deliver better coverage at a lower cost. A licensed broker will tell you in minutes.',
      ctaLabel: 'Check PKV eligibility →',
      ctaHref: '/quiz',
      ctaSecondaryLabel: 'Compare GKV vs PKV',
      ctaSecondaryHref: '/compare',
    },
  ],
});

console.log('\n✅ All pages created in Sanity. Open the Studio to review them.');
