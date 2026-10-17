// One-off: strip PKV/GKV acronyms from the two CMS explainer pages. Run once, delete.
import 'dotenv/config';
import { createClient } from '@sanity/client';

const client = createClient({
  projectId: process.env.PUBLIC_SANITY_PROJECT_ID || 'o426dbl0',
  dataset: process.env.PUBLIC_SANITY_DATASET || 'production',
  apiVersion: '2024-01-01',
  token: process.env.SANITY_WRITE_TOKEN,
  useCdn: false,
});

const privatePage = {
  seoTitle: 'Private Health Insurance in Germany — Complete Guide 2026',
  seoDescription: 'Everything you need to know about private health insurance in Germany: who qualifies, what it costs, top insurers, and how to apply. Updated 2026.',
  'sections[_key=="hero-2"].headline': 'Private Health Insurance in Germany',
  'sections[_key=="hero-2"].subheadline': 'Private health insurance offers better coverage, faster specialist access, and lower costs for expats above the income threshold. Here is everything you need to know.',
  'sections[_key=="stats-2"].stats[_key=="s2"].label': 'Private health insurance from (age 30, mid plan)',
  'sections[_key=="insurers-2"].kicker': 'Top private health insurers',
  'sections[_key=="insurers-2"].insurers[_key=="i1"].reason': 'Largest private health insurer, consistently low premium increases, strong financials',
  'sections[_key=="insurers-2"].insurers[_key=="i3"].tag': 'Largest private health insurer',
  'sections[_key=="faq-2"].items[_key=="f1"].answer': 'Employees earning above €77,400 gross/year (2026 threshold), all self-employed and freelancers, and civil servants (Beamte) can choose private health insurance. Employees below the threshold must use public health insurance.',
  'sections[_key=="faq-2"].items[_key=="f2"].question': 'How much does private health insurance cost in Germany?',
  'sections[_key=="faq-2"].items[_key=="f2"].answer': 'A healthy 30-year-old pays €210–360/month for a mid-range private health insurance plan. Employers contribute up to €421/month. Freelancers pay the full amount but private health insurance is still often cheaper than public health insurance at equivalent income levels.',
  'sections[_key=="faq-2"].items[_key=="f3"].question': 'Can I switch back to public health insurance afterwards?',
  'sections[_key=="faq-2"].items[_key=="f4"].question': 'Does private health insurance cover my family?',
  'sections[_key=="faq-2"].items[_key=="f4"].answer': 'No free family coverage. Each family member needs their own private health insurance policy. This makes private health insurance significantly more expensive for families with children and a non-working partner — public health insurance family coverage may be cheaper in that scenario.',
  'sections[_key=="faq-2"].items[_key=="f5"].question': 'What does private health insurance actually cover?',
  'sections[_key=="faq-2"].items[_key=="f5"].answer': 'Private health insurance typically covers: private hospital room, choice of senior consultant (Chefarzt), no GP referral needed for specialists, comprehensive dental, alternative medicine, faster appointment booking. Exact coverage depends on your plan tier.',
  'sections[_key=="testi-2"].headline': 'What private health insurance members say',
  'sections[_key=="testi-2"].testimonials[_key=="t1"].quote': 'I was paying €540/month for public health insurance. After switching to private health insurance I pay €240/month. Same doctor, better hospital room. Wish I had done it in my first year in Germany.',
  'sections[_key=="testi-2"].testimonials[_key=="t3"].quote': 'The guide explained the differences better than my German colleagues ever could. The broker found me a plan that costs half my old public health insurance contribution.',
  'sections[_key=="cta-2"].headline': 'Find out how much you could save with private health insurance',
};

const publicPage = {
  seoTitle: 'Public Health Insurance in Germany — Expat Guide 2026',
  seoDescription: 'How public health insurance works in Germany for expats: contributions, coverage, family insurance, and when private health insurance is better. Updated 2026.',
  'sections[_key=="hero-3"].headline': 'Public Health Insurance in Germany',
  'sections[_key=="hero-3"].subheadline': "Public health insurance is Germany's statutory health insurance, mandatory for most employees. Here is how it works, what it costs, and when private insurance is a better option.",
  'sections[_key=="hero-3"].ctaLabel': 'Compare public vs private health insurance →',
  'sections[_key=="hero-3"].ctaSecondaryLabel': 'Check my eligibility for private health insurance',
  'sections[_key=="stats-3"].stats[_key=="s1"].label': 'Base public health insurance contribution rate',
  'sections[_key=="faq-3"].kicker': 'Public health insurance explained',
  'sections[_key=="faq-3"].items[_key=="f1"].question': 'Who must have public health insurance in Germany?',
  'sections[_key=="faq-3"].items[_key=="f1"].answer': 'Employees earning below €77,400 gross/year (2026) are legally required to have public health insurance. Students, unemployed people receiving ALG I/II, and pensioners below certain thresholds also fall under public health insurance.',
  'sections[_key=="faq-3"].items[_key=="f2"].question': 'How much does public health insurance cost in Germany?',
  'sections[_key=="faq-3"].items[_key=="f3"].question': 'What does public health insurance cover?',
  'sections[_key=="faq-3"].items[_key=="f3"].answer': 'Public health insurance covers GP visits, specialist referrals, hospital (shared ward), basic dental, prescriptions (with co-pay), preventive care, and sick pay (Krankengeld after 6 weeks). It does not include private hospital rooms or full dental prosthetics.',
  'sections[_key=="faq-3"].items[_key=="f4"].question': 'Can I add family members to my public health insurance?',
  'sections[_key=="faq-3"].items[_key=="f4"].answer': 'Yes — the Familienversicherung allows non-earning spouses and children under 25 to be covered under your public health insurance for free. This is one of its biggest advantages over private health insurance, where each person needs a separate paid policy.',
  'sections[_key=="faq-3"].items[_key=="f5"].question': 'Which public health insurance provider should I choose?',
  'sections[_key=="faq-3"].items[_key=="f5"].answer': 'The largest public health insurance funds are TK, AOK, Barmer, DAK, and IKK. Coverage is largely standardised by law. Differences are in supplementary services, digital tools, and customer service. TK and Barmer are popular with expats for their English support.',
  'sections[_key=="cta-3"].body': 'If you earn above €77,400/year or are self-employed, private health insurance could deliver better coverage at a lower cost. A licensed broker will tell you in minutes.',
  'sections[_key=="cta-3"].ctaLabel': 'Check private health insurance eligibility →',
  'sections[_key=="cta-3"].ctaSecondaryLabel': 'Compare public vs private health insurance',
};

if (!process.env.SANITY_WRITE_TOKEN) { console.error('No SANITY_WRITE_TOKEN'); process.exit(1); }

await client.patch('XUsBft605m1IpWTwmkHHD1').set(privatePage).commit();
console.log('patched private-health-insurance-germany');
await client.patch('DYfNUm2vFEdNMWuSKk3fAJ').set(publicPage).commit();
console.log('patched public-health-insurance-germany');
