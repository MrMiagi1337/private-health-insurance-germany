import { client } from './sanity';

export async function getPageBySlug(slug: string) {
  if (!client) return null;
  return client.fetch(
    `*[_type == "page" && slug.current == $slug][0]{
      title,
      seoTitle,
      seoDescription,
      "slug": slug.current,
      sections[]{
        _type,
        _key,
        // heroBlock
        headline, subheadline, ctaLabel, ctaHref, ctaSecondaryLabel, ctaSecondaryHref,
        // statsBlock
        stats[]{value, label},
        // faqBlock, insurersBlock, testimonialsBlock
        kicker,
        items[]{question, answer},
        insurers[]{name, tag, reason, href},
        testimonials[]{quote, name, role},
        // ctaBlock
        body,
        // shared
        "image": image{asset->{url}},
        cards[]{...},
        usps[]{...},
        policyItems[]{...},
      }
    }`,
    { slug }
  );
}

export async function getAllPageSlugs(): Promise<string[]> {
  if (!client) return [];
  const pages = await client.fetch(`*[_type == "page"]{ "slug": slug.current }`);
  return pages.map((p: { slug: string }) => p.slug).filter(Boolean);
}
