import os, json

base_dir = r"C:/Users/marco/Desktop/private-health-insurance-germany/src/pages/top-insurers"

insurers = [
    {"slug":"dkv","name":"DKV","tagline":"One of Germany's oldest and most trusted PKV insurers, strong in outpatient care and preventive health.","founded":"1927","hq":"Cologne","type":"Stock insurer (Ergo Group)","english":"&#9733;&#9733;&#9733;&#9734;&#9734;","pricing":"&#9733;&#9733;&#9733;&#9733;&#9734;","coverage":"&#9733;&#9733;&#9733;&#9733;&#9734;","service":"&#9733;&#9733;&#9733;&#9733;&#9734;","pros":["Nearly 100 years of PKV experience","Excellent outpatient and preventive care coverage","Strong digital tools and mobile app","Wide network of partner hospitals and specialists","Good value in the mid-price segment"],"cons":["English support less comprehensive than Allianz","Some tariffs require GP referral to see specialists","Premium increases moderate but not the lowest","Part of ERGO/Munich Re, less independence than mutual insurers"],"tariffs":[{"name":"KomfortSelect","level":"Premium","desc":"Single room, choice of specialist, comprehensive outpatient and dental"},{"name":"MedicalBalance","level":"Mid-range","desc":"Strong outpatient focus, two-bed hospital room, deductible options"},{"name":"AktivStart","level":"Entry","desc":"Lower premium entry tariff with higher co-payment structure"}],"bestFor":"Employed professionals who use healthcare regularly, families, people focused on preventive and outpatient care.","verdict":"DKV sits comfortably in the upper-mid tier of German PKV. Its century of history and solid financial backing through Munich Re make it a dependable choice. Coverage is strong across the board, especially for outpatient care and preventive health. It is not the cheapest option, but it offers genuine value and peace of mind."},
    {"slug":"hansemerkur","name":"HanseMerkur","tagline":"Hamburg-based mutual insurer with competitive pricing and a loyal customer base among young professionals.","founded":"1875","hq":"Hamburg","type":"Mutual insurer","english":"&#9733;&#9733;&#9733;&#9734;&#9734;","pricing":"&#9733;&#9733;&#9733;&#9733;&#9733;","coverage":"&#9733;&#9733;&#9733;&#9733;&#9734;","service":"&#9733;&#9733;&#9733;&#9733;&#9734;","pros":["Consistently among the most competitive premium pricing","Mutual structure aligned with policyholder interests","Good digital infrastructure and fast claims processing","Strong in travel insurance and supplementary health products","Stable premium history compared to stock insurers"],"cons":["Limited English-language support","Less well-known internationally than Allianz or DKV","Some tariffs have stricter underwriting criteria","Smaller hospital network in some regions"],"tariffs":[{"name":"HM Premium","level":"Premium","desc":"Single room, Chefarzt treatment, 100% outpatient, top dental"},{"name":"HM Komfort","level":"Mid-range","desc":"Two-bed room, deductible options, comprehensive outpatient"},{"name":"HM Smart","level":"Entry","desc":"Budget-friendly with deductible, ideal for healthy young applicants"}],"bestFor":"Young professionals and recent graduates, cost-conscious applicants who still want solid coverage, freelancers with tight budgets.","verdict":"HanseMerkur is a standout on price. For applicants entering PKV young and healthy, it offers premium quality at a genuinely competitive rate. The mutual structure means no shareholder pressure to cut corners on service. The main limitation for expats is the limited English support. For those comfortable managing German-language correspondence, HanseMerkur is one of the best-value PKV providers in the market."},
    {"slug":"hallesche","name":"Hallesche","tagline":"Specialist PKV insurer with some of the best dental coverage in Germany and historically low premium increases.","founded":"1933","hq":"Stuttgart","type":"Mutual insurer","english":"&#9733;&#9733;&#9733;&#9734;&#9734;","pricing":"&#9733;&#9733;&#9733;&#9733;&#9734;","coverage":"&#9733;&#9733;&#9733;&#9733;&#9733;","service":"&#9733;&#9733;&#9733;&#9733;&#9734;","pros":["Market-leading dental coverage across most tariffs","Historically very low premium increases","Mutual structure with no shareholder pressure","Strong customer satisfaction scores","Good outpatient mental health coverage"],"cons":["Limited English customer service","Smaller brand, less known outside Germany","Digital tools lag behind Allianz and DKV","Some tariffs are region-centric in hospital networks"],"tariffs":[{"name":"NK Plus","level":"Premium","desc":"Full single room, Chefarzt, 100% dental, comprehensive mental health coverage"},{"name":"NK Select","level":"Mid-range","desc":"Two-bed room, 80% dental, strong outpatient, deductible options"},{"name":"NK Start","level":"Entry","desc":"Higher deductible entry tariff, good dental even at entry level"}],"bestFor":"Anyone who values strong dental coverage, long-term cost stability, and is comfortable managing in German.","verdict":"Hallesche is the insurer dentists recommend. Its dental coverage is genuinely best-in-class with no fine print exclusions. Combined with one of the best premium-stability records in the market, Hallesche is a favourite among brokers who think long-term. If dental costs are a concern and you plan to stay in Germany for many years, Hallesche deserves a spot on your shortlist."},
    {"slug":"signal-iduna","name":"Signal Iduna","tagline":"A large mutual insurer offering reliable mid-range PKV with strong service and straightforward tariffs.","founded":"1907","hq":"Dortmund / Hamburg","type":"Mutual insurer","english":"&#9733;&#9733;&#9733;&#9734;&#9734;","pricing":"&#9733;&#9733;&#9733;&#9733;&#9734;","coverage":"&#9733;&#9733;&#9733;&#9733;&#9734;","service":"&#9733;&#9733;&#9733;&#9733;&#9734;","pros":["Solid mid-market pricing with transparent tariff structure","Mutual insurer, customer-focused by design","Good hospital and outpatient coverage","Strong regional presence and broker network","Reliable premium history"],"cons":["English support is limited","Less innovative digitally than newer insurers","Not the lowest premium option in most age brackets","Some tariffs require referral to see specialists"],"tariffs":[{"name":"SI excellent","level":"Premium","desc":"Single room, free choice of hospital and specialist, full dental"},{"name":"SI comfort","level":"Mid-range","desc":"Two-bed room, 80% dental, good outpatient coverage"},{"name":"SI basic","level":"Entry","desc":"Entry tariff with deductible, recommended for healthy young applicants"}],"bestFor":"Employees and freelancers looking for solid, predictable PKV without frills. Good for long-term planning.","verdict":"Signal Iduna does not try to be the cheapest or the flashiest PKV insurer. It aims for reliability, and by that measure it succeeds. Its tariff structure is clear, its premium history is steady, and its claims processing is well-regarded. For expats comfortable dealing with German-language correspondence, Signal Iduna is a dependable option at a fair price point."},
    {"slug":"axa","name":"AXA","tagline":"Global insurance brand with strong English support and flexible modular tariffs popular with international professionals.","founded":"1838","hq":"Paris (Germany: Cologne)","type":"Stock insurer","english":"&#9733;&#9733;&#9733;&#9733;&#9734;","pricing":"&#9733;&#9733;&#9733;&#9734;&#9734;","coverage":"&#9733;&#9733;&#9733;&#9733;&#9734;","service":"&#9733;&#9733;&#9733;&#9733;&#9734;","pros":["Strong English-language support for expats","Modular tariff design, customize your coverage","Global brand, easy to deal with from abroad","Good mental health and psychotherapy coverage","Fast digital claims processing"],"cons":["Stock insurer, premium increases can be driven by profitability","More expensive than mid-tier German mutual insurers","Modular structure can get complex to compare","Not always available through all independent brokers"],"tariffs":[{"name":"Premium365","level":"Premium","desc":"Single room, unlimited specialist access, premium dental, global cover"},{"name":"MedFlex","level":"Mid-range","desc":"Flexible module-based coverage, good outpatient, optional dental add-on"},{"name":"StartMed","level":"Entry","desc":"Deductible-based entry tariff suitable for healthy young professionals"}],"bestFor":"International professionals, frequent travellers, expats who want English-speaking customer service and modular flexibility.","verdict":"AXA occupies a similar niche to Allianz among expat-friendly PKV providers. Its English support is strong, its global reach is genuine, and its modular design lets you build a policy that fits your lifestyle. AXA premiums sit in the upper range, and as a stock insurer, profitability can influence pricing. Worth considering if you want Allianz-level service at a slightly lower price."},
    {"slug":"barmenia","name":"Barmenia","tagline":"Wuppertal-based mutual insurer with strong mental health coverage and growing popularity among younger applicants.","founded":"1902","hq":"Wuppertal","type":"Mutual insurer","english":"&#9733;&#9733;&#9733;&#9734;&#9734;","pricing":"&#9733;&#9733;&#9733;&#9733;&#9734;","coverage":"&#9733;&#9733;&#9733;&#9733;&#9734;","service":"&#9733;&#9733;&#9733;&#9733;&#9734;","pros":["Strong psychotherapy and mental health benefits","Mutual structure with stable premium history","Growing digital capabilities and app quality","Good dental coverage across mid-range tariffs","Competitive pricing for under-40 applicants"],"cons":["Limited English customer service","Less well-known than market leaders","Some tariffs have limited hospital choice in rural areas","Premium increases have slightly accelerated in recent years"],"tariffs":[{"name":"Barmenia Mehr","level":"Premium","desc":"Single room, full specialist access, premium dental, strong mental health coverage"},{"name":"Barmenia Balance","level":"Mid-range","desc":"Two-bed room, 80% dental, comprehensive outpatient, deductible options"},{"name":"Barmenia Start","level":"Entry","desc":"Entry-level with higher co-pay, best for young healthy applicants"}],"bestFor":"Younger professionals who value mental health coverage, cost-conscious applicants, those planning long-term stays in Germany.","verdict":"Barmenia has built a strong reputation for mental health benefits at a time when demand for psychotherapy is rising. For expats managing the stress of relocation, that coverage matters. Among mutual insurers in the mid-range, Barmenia offers good value and improving digital tools. A solid choice for under-40 applicants in good health."},
    {"slug":"gothaer","name":"Gothaer","tagline":"One of Germany's oldest mutual insurers with reliable coverage and a strong track record in premium stability.","founded":"1820","hq":"Cologne","type":"Mutual insurer","english":"&#9733;&#9733;&#9733;&#9734;&#9734;","pricing":"&#9733;&#9733;&#9733;&#9733;&#9734;","coverage":"&#9733;&#9733;&#9733;&#9733;&#9734;","service":"&#9733;&#9733;&#9733;&#9734;&#9734;","pros":["Over 200 years of history, exceptional financial stability","Competitive mid-range pricing","Good hospital and specialist access","Mutual structure focused on member interests","Strong in supplementary dental and vision coverage"],"cons":["Digital tools and app behind more modern competitors","Limited English language support","Less proactive in product innovation","Claims processing can be slower than digital-first insurers"],"tariffs":[{"name":"MED Top","level":"Premium","desc":"Single room, free hospital choice, comprehensive outpatient and dental"},{"name":"MED Comfort","level":"Mid-range","desc":"Two-bed room, deductible options, solid outpatient and dental"},{"name":"MED Start","level":"Entry","desc":"Budget entry with deductible, suitable for healthy young applicants"}],"bestFor":"Applicants who prioritise financial stability and a long track record over digital features. Good for older applicants comparing premium stability.","verdict":"Gothaer's 200-year history is a genuine selling point when considering PKV. A provider that has survived two world wars and multiple healthcare reforms demonstrates real resilience. Coverage is solid and pricing competitive. The weakness is digital experience, which matters less for those who prefer dealing through a broker or by phone."},
    {"slug":"continentale","name":"Continentale","tagline":"Dortmund-based mutual insurer with some of the most flexible tariff structures in the German PKV market.","founded":"1874","hq":"Dortmund","type":"Mutual insurer","english":"&#9733;&#9733;&#9733;&#9734;&#9734;","pricing":"&#9733;&#9733;&#9733;&#9733;&#9734;","coverage":"&#9733;&#9733;&#9733;&#9733;&#9734;","service":"&#9733;&#9733;&#9733;&#9733;&#9734;","pros":["Highly flexible and modular tariff design","Mutual structure with long-term premium stability focus","Strong network in North Rhine-Westphalia region","Good value across all age segments","Solid dental and rehabilitation benefits"],"cons":["Limited English-language service","Less well-known outside Germany","Digital tools lag behind Allianz and DKV","Some tariff options complex to compare without a broker"],"tariffs":[{"name":"Continentale Premium","level":"Premium","desc":"Single room, free hospital and specialist choice, top dental and rehabilitation"},{"name":"Continentale Select","level":"Mid-range","desc":"Flexible modules, two-bed room, strong outpatient, deductible options"},{"name":"Continentale Best","level":"Entry","desc":"Entry tariff with higher deductible, cost-effective for young healthy applicants"}],"bestFor":"Applicants who want to customize their policy carefully. Good for NRW-based professionals and families.","verdict":"Continentale is the broker's favourite for clients who want to fine-tune their coverage. Its modular design means you pay for what you actually need rather than a pre-packaged bundle. Without a broker, comparing Continentale tariffs is genuinely difficult. With broker guidance, it can offer excellent value for the right applicant profile."},
]

def make_astro(ins):
    pros_js = json.dumps(ins["pros"])
    cons_js = json.dumps(ins["cons"])
    tariffs_js = json.dumps(ins["tariffs"])
    slug = ins["slug"]
    name = ins["name"]

    return f"""---
import Layout from '../../layouts/Layout.astro';

const insurer = {{
  name: {json.dumps(name)},
  tagline: {json.dumps(ins["tagline"])},
  founded: {json.dumps(ins["founded"])},
  hq: {json.dumps(ins["hq"])},
  type: {json.dumps(ins["type"])},
  englishSupport: {json.dumps(ins["english"])},
  pricing: {json.dumps(ins["pricing"])},
  coverage: {json.dumps(ins["coverage"])},
  service: {json.dumps(ins["service"])},
  pros: {pros_js},
  cons: {cons_js},
  tariffs: {tariffs_js},
  bestFor: {json.dumps(ins["bestFor"])},
  verdict: {json.dumps(ins["verdict"])},
}};

const schema = {{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "Article",
      "headline": "{name} PKV Review 2026 - Private Health Insurance Germany",
      "author": {{ "@type": "Person", "name": "Marco Maurelli", "url": "https://private-health-insurance-germany.com/about" }},
      "dateModified": "2026-04-01"
    }},
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://private-health-insurance-germany.com/" }},
        {{ "@type": "ListItem", "position": 2, "name": "Top Insurers", "item": "https://private-health-insurance-germany.com/top-insurers" }},
        {{ "@type": "ListItem", "position": 3, "name": "{name}", "item": "https://private-health-insurance-germany.com/top-insurers/{slug}" }}
      ]
    }}
  ]
}};
---

<Layout
  title="{name} PKV Review 2026 - Private Health Insurance Germany"
  description="Independent review of {name} private health insurance in Germany. Pros, cons, tariffs, English support, and who {name} PKV is best for in 2026."
>
  <script type="application/ld+json" is:inline set:html={{JSON.stringify(schema)}} />
  <main>
    <div class="review-wrap container">
      <nav class="breadcrumb" aria-label="Breadcrumb">
        <ol>
          <li><a href="/">Home</a></li>
          <li aria-hidden="true">&#8250;</li>
          <li><a href="/top-insurers">Top Insurers</a></li>
          <li aria-hidden="true">&#8250;</li>
          <li aria-current="page">{{insurer.name}}</li>
        </ol>
      </nav>

      <header class="review-header">
        <span class="page-tag">Insurer Review</span>
        <h1>{{insurer.name}} Private Health Insurance Review</h1>
        <p class="review-tagline">{{insurer.tagline}}</p>
        <div class="meta-row">
          <span class="meta-item">By Marco Maurelli</span>
          <span class="meta-item">Updated April 2026</span>
          <span class="meta-item">5 min read</span>
        </div>
      </header>

      <div class="review-grid">
        <div class="review-main">
          <div class="scores-card">
            <div class="score-item"><span class="score-label">English support</span><span class="score-stars" set:html={{insurer.englishSupport}}></span></div>
            <div class="score-item"><span class="score-label">Pricing</span><span class="score-stars" set:html={{insurer.pricing}}></span></div>
            <div class="score-item"><span class="score-label">Coverage</span><span class="score-stars" set:html={{insurer.coverage}}></span></div>
            <div class="score-item"><span class="score-label">Service</span><span class="score-stars" set:html={{insurer.service}}></span></div>
          </div>

          <div class="review-body">
            <h2>Overview</h2>
            <p>Founded in {{insurer.founded}} and headquartered in {{insurer.hq}}, {{insurer.name}} is a well-established name in the German PKV market. As a {{insurer.type}}, it brings distinct advantages in terms of how it balances policyholder interests with long-term financial sustainability.</p>

            <h2>Pros</h2>
            <ul>{{insurer.pros.map(pro => <li>{{pro}}</li>)}}</ul>

            <h2>Cons</h2>
            <ul>{{insurer.cons.map(con => <li>{{con}}</li>)}}</ul>

            <h2>Key Tariffs</h2>
            <table>
              <thead><tr><th>Tariff</th><th>Level</th><th>What it covers</th></tr></thead>
              <tbody>{{insurer.tariffs.map(t => (<tr><td><strong>{{t.name}}</strong></td><td>{{t.level}}</td><td>{{t.desc}}</td></tr>))}}</tbody>
            </table>

            <h2>Best For</h2>
            <p>{{insurer.bestFor}}</p>

            <h2>Verdict</h2>
            <p>{{insurer.verdict}}</p>

            <div class="cta-inline">
              <p>Want a personalised {{insurer.name}} quote alongside other top insurers?</p>
              <a href="/contact" class="btn-primary">Get free broker comparison &#8594;</a>
            </div>
          </div>
        </div>

        <aside class="review-sidebar">
          <div class="sidebar-card">
            <div class="sc-top"></div>
            <div class="sc-body">
              <p class="sc-eyebrow">Quick facts</p>
              <dl class="quick-facts">
                <dt>Founded</dt><dd>{{insurer.founded}}</dd>
                <dt>HQ</dt><dd>{{insurer.hq}}</dd>
                <dt>Type</dt><dd>{{insurer.type}}</dd>
              </dl>
              <a href="/contact" class="sc-btn">Get a quote &#8594;</a>
            </div>
          </div>
          <div class="sidebar-nav-card">
            <p class="sidebar-label">Other reviews</p>
            <ul>
              <li><a href="/top-insurers/debeka">Debeka</a></li>
              <li><a href="/top-insurers/allianz">Allianz</a></li>
              <li><a href="/top-insurers/dkv">DKV</a></li>
              <li><a href="/top-insurers/hallesche">Hallesche</a></li>
              <li><a href="/top-insurers">All 10 insurers &#8594;</a></li>
            </ul>
          </div>
        </aside>
      </div>
    </div>
  </main>
</Layout>

<style>
  .review-wrap {{ padding-top: 1.5rem; padding-bottom: 5rem; }}
  .breadcrumb ol {{ display: flex; align-items: center; gap: .4rem; list-style: none; flex-wrap: wrap; margin-bottom: 1.5rem; }}
  .breadcrumb li {{ font-size: .8rem; color: var(--muted); }}
  .breadcrumb a {{ color: var(--muted); transition: color var(--ease); }}
  .breadcrumb a:hover {{ color: var(--text); }}
  .review-header {{ margin-bottom: 2rem; }}
  .page-tag {{ display: inline-block; font-size: .72rem; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; color: var(--red); background: var(--red-lt); padding: 3px 10px; border-radius: 999px; margin-bottom: .75rem; }}
  h1 {{ font-size: clamp(1.6rem, 3.5vw, 2.4rem); font-weight: 800; letter-spacing: -.04em; line-height: 1.1; margin-bottom: .6rem; }}
  .review-tagline {{ font-size: 1rem; color: var(--muted); line-height: 1.65; max-width: 600px; margin-bottom: .75rem; }}
  .meta-row {{ display: flex; gap: 1.25rem; flex-wrap: wrap; }}
  .meta-item {{ font-size: .8rem; color: var(--muted); font-weight: 500; }}
  .review-grid {{ display: grid; grid-template-columns: 1fr 260px; gap: 2.5rem; align-items: start; }}
  .scores-card {{ background: #fff; border: 1.5px solid var(--border); border-radius: var(--radius); padding: 1.25rem 1.5rem; margin-bottom: 1.75rem; display: grid; grid-template-columns: repeat(2, 1fr); gap: .85rem; box-shadow: var(--sh-sm); }}
  .score-item {{ display: flex; flex-direction: column; gap: .15rem; }}
  .score-label {{ font-size: .72rem; font-weight: 700; letter-spacing: .05em; text-transform: uppercase; color: var(--muted); }}
  .score-stars {{ font-size: .95rem; color: #f59e0b; }}
  .review-body {{ font-size: 1rem; line-height: 1.8; color: #3a3a42; }}
  .review-body h2 {{ font-size: 1.25rem; font-weight: 800; letter-spacing: -.02em; color: var(--text); margin: 2rem 0 .6rem; }}
  .review-body p {{ margin-bottom: 1rem; }}
  .review-body ul {{ margin: .5rem 0 1.25rem 1.25rem; }}
  .review-body li {{ margin-bottom: .5rem; padding-left: .25rem; }}
  .review-body table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: .9rem; border: 1px solid var(--border); border-radius: 8px; overflow: hidden; }}
  .review-body th {{ background: var(--bg); padding: .6rem .9rem; text-align: left; font-size: .75rem; font-weight: 700; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); border-bottom: 1px solid var(--border); }}
  .review-body td {{ padding: .6rem .9rem; border-bottom: 1px solid var(--border); vertical-align: top; }}
  .review-body tr:last-child td {{ border-bottom: none; }}
  .cta-inline {{ background: var(--red-lt); border: 1px solid rgba(30,138,154,.2); border-radius: var(--radius); padding: 1.25rem 1.5rem; margin-top: 2rem; display: flex; align-items: center; justify-content: space-between; gap: 1rem; flex-wrap: wrap; }}
  .cta-inline p {{ font-size: .93rem; color: var(--text); font-weight: 500; margin: 0; }}
  .sidebar-card {{ background: #fff; border: 1.5px solid var(--border); border-radius: var(--radius); overflow: hidden; box-shadow: var(--sh-sm); margin-bottom: 1rem; }}
  .sc-top {{ height: 4px; background: var(--red); }}
  .sc-body {{ padding: 1.1rem 1.25rem; }}
  .sc-eyebrow {{ font-size: .7rem; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; color: var(--red); margin-bottom: .75rem; }}
  .quick-facts {{ display: grid; grid-template-columns: auto 1fr; gap: .3rem .75rem; font-size: .83rem; margin-bottom: 1rem; }}
  .quick-facts dt {{ color: var(--muted); font-weight: 500; }}
  .quick-facts dd {{ color: var(--text); font-weight: 600; }}
  .sc-btn {{ display: flex; align-items: center; justify-content: center; gap: 6px; background: var(--red); color: #fff; font-size: .83rem; font-weight: 700; padding: .65rem 1rem; border-radius: 8px; transition: background var(--ease); width: 100%; text-decoration: none; }}
  .sc-btn:hover {{ background: var(--red-dk); }}
  .sidebar-nav-card {{ background: #fff; border: 1.5px solid var(--border); border-radius: var(--radius); padding: 1.1rem 1.25rem; box-shadow: var(--sh-sm); }}
  .sidebar-label {{ font-size: .7rem; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; color: var(--muted); margin-bottom: .65rem; }}
  .sidebar-nav-card ul {{ list-style: none; display: flex; flex-direction: column; gap: .2rem; }}
  .sidebar-nav-card a {{ display: block; font-size: .84rem; color: var(--muted); padding: .25rem 0; padding-left: .6rem; border-left: 2px solid transparent; transition: color var(--ease), border-color var(--ease); }}
  .sidebar-nav-card a:hover {{ color: var(--red); border-left-color: var(--red); }}
  @media (max-width: 800px) {{ .review-grid {{ grid-template-columns: 1fr; }} .review-sidebar {{ order: -1; }} .scores-card {{ grid-template-columns: repeat(4, 1fr); }} }}
  @media (max-width: 500px) {{ .scores-card {{ grid-template-columns: repeat(2, 1fr); }} }}
</style>
"""

for ins in insurers:
    content = make_astro(ins)
    path = os.path.join(base_dir, f"{ins['slug']}.astro")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created: {ins['slug']}.astro")

print("Done!")
