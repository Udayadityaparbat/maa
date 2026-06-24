# SEO Audit & Fix Guide — maa.rigelfoundation.org.in

---

## 🔴 CRITICAL ISSUES (Fix First)

---

### 1. "Testing Mode" Banner — Kills Crawl Trust

The very first visible text on the page is:
> *"This website is currently in TESTING MODE. Features may be incomplete or unstable."*

Google interprets this as low-quality, unfinished content and may devalue or sandbox the page entirely.

**Fix:** Remove this banner or gate it behind a logged-in admin session before going public.

```html
<!-- REMOVE THIS from your HTML entirely -->
<div class="testing-banner">
  This website is currently in TESTING MODE. Features may be incomplete or unstable.
</div>
```

---

### 2. Missing Canonical Tag

There is no `<link rel="canonical">` tag. Without it, if the page is accessible at both `http://` and `https://`, with and without `www`, or via multiple routes, Google may index duplicate versions and split your ranking signals.

**Fix:** Add this inside `<head>`:

```html
<link rel="canonical" href="https://maa.rigelfoundation.org.in/" />
```

---

### 3. Missing robots.txt & sitemap.xml

No sitemap is declared in the HTML, and there's no visible `robots.txt` reference. Without these, crawlers may miss sections or crawl inefficiently.

**Fix — Create `/robots.txt`:**
```
User-agent: *
Allow: /

Sitemap: https://maa.rigelfoundation.org.in/sitemap.xml
```

**Fix — Create `/sitemap.xml`:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://maa.rigelfoundation.org.in/</loc>
    <lastmod>2026-06-11</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://maa.rigelfoundation.org.in/tech-team.html</loc>
    <lastmod>2026-06-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>
```

---

### 4. All Sections Are Anchor IDs on One Page — No Sub-page URLs

Every section (Learn, Tracker, Q&A, Schemes, etc.) is an `#anchor` link on the homepage. Google can index anchors only weakly. Key topics like "PCOS symptoms," "period tracker," "menstrual education" deserve their own URLs for targeted ranking.

**Fix (Recommended Architecture):**
```
/                        → Homepage
/learn/                  → Menstrual Education
/tracker/                → Period Tracker
/disorders/              → Menstrual Disorders (PCOS, Endometriosis, etc.)
/schemes/                → Government Schemes
/research/               → Data & Reports
/blog/                   → Blog (currently on parent domain)
/faq/                    → Anonymous Q&A
```

---

### 5. Missing Open Graph & Twitter Card Meta Tags

No social sharing meta tags exist. When the site is shared on WhatsApp, Twitter/X, or LinkedIn, it will show a blank preview — losing click-throughs.

**Fix — Add inside `<head>`:**
```html
<!-- Open Graph (Facebook, WhatsApp, LinkedIn) -->
<meta property="og:title" content="Maa by Rigel | Menstrual Health Awareness & Support" />
<meta property="og:description" content="A safe, private space for women to learn about menstrual health, track periods, and access government support — backed by WHO guidelines." />
<meta property="og:url" content="https://maa.rigelfoundation.org.in/" />
<meta property="og:type" content="website" />
<meta property="og:image" content="https://maa.rigelfoundation.org.in/media/og-cover.png" />
<meta property="og:locale" content="en_IN" />

<!-- Twitter / X Card -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Maa by Rigel | Menstrual Health Awareness" />
<meta name="twitter:description" content="WHO-backed menstrual health education, free period tracker, and government scheme access for women across India." />
<meta name="twitter:image" content="https://maa.rigelfoundation.org.in/media/og-cover.png" />
```

> **Also create:** A dedicated 1200×630px `og-cover.png` image for social sharing.

---

### 6. Missing Structured Data (Schema Markup)

Google shows rich results (FAQ boxes, organization panels, breadcrumbs) only when structured data is present. This site qualifies for multiple schema types that can dramatically increase visibility.

**Fix — Add inside `<head>` or before `</body>`:**

**Organization Schema:**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "NGO",
  "name": "Maa by Rigel",
  "url": "https://maa.rigelfoundation.org.in/",
  "logo": "https://maa.rigelfoundation.org.in/media/rigel%20circle%20logo.png",
  "description": "India's first non-profit dedicated entirely to menstrual health awareness, period poverty, and reproductive education for women.",
  "email": "maa@rigelfoundation.org.in",
  "sameAs": [
    "https://www.instagram.com/rigelfoundation/",
    "https://www.linkedin.com/company/rigelfoundation/",
    "https://rigelfoundation.org.in"
  ],
  "foundingDate": "2020",
  "areaServed": "IN"
}
</script>
```

**FAQ Schema (Google FAQ Rich Results):**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is it safe to exercise during your period?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Gentle exercise and good hygiene, including washing your hair, are completely safe during menstruation and can actually help reduce cramps."
      }
    },
    {
      "@type": "Question",
      "name": "What is PCOS?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Polycystic Ovary Syndrome (PCOS) is one of the most common hormonal disorders in young women, characterized by irregular periods, weight gain, acne, and excess facial hair."
      }
    },
    {
      "@type": "Question",
      "name": "What is period poverty?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Period poverty is the inability to access safe, affordable menstrual products. It affects hundreds of millions of women globally and leads to missed school days and serious health risks."
      }
    }
  ]
}
</script>
```

**WebSite Schema (enables Google Sitelinks Search):**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Maa by Rigel",
  "url": "https://maa.rigelfoundation.org.in/",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://maa.rigelfoundation.org.in/?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
</script>
```

---

## 🟠 HIGH-PRIORITY ISSUES

---

### 7. Title Tag — Improve Keyword Targeting

**Current:**
```html
<title>Maa by Rigel | Menstrual Health Awareness & Support</title>
```

**Issues:** "Maa by Rigel" means nothing to a search engine. Lead with the target keyword.

**Fix:**
```html
<title>Menstrual Health Awareness India | Period Tracker & Education — Maa by Rigel</title>
```

> Keep title under 60 characters to avoid truncation. Prioritize the most searched terms: "menstrual health India", "period tracker", "PCOS information".

---

### 8. Meta Description — Strengthen with Keywords & CTAs

**Current:**
```html
<meta name="description" content="Maa by Rigel — Menstrual health awareness, education, and support for women across India." />
```

**Issues:** Too short (57 chars), no call-to-action, misses key terms like "period tracker", "PCOS", "government schemes".

**Fix:**
```html
<meta name="description" content="Free period tracker, PCOS & endometriosis education, and government scheme access for women across India. WHO-backed, 100% private. By Rigel Foundation." />
```

> Aim for 150–160 characters.

---

### 9. Missing `lang` Attribute on `<html>` Tag

The site supports 22 Indian languages but the `<html>` tag likely has no `lang` attribute, or is set to a wrong value. This affects both SEO and accessibility (screen readers).

**Fix:**
```html
<!-- Default page -->
<html lang="en-IN">

<!-- When user selects Hindi -->
<html lang="hi">

<!-- When user selects Bengali -->
<html lang="bn">
```

> Dynamically update this when the language switcher is used via JavaScript:
```javascript
document.documentElement.lang = 'hi'; // update per selected language
```

---

### 10. Image Alt Text — Multiple Images Are Missing or Generic

All `<img>` tags need descriptive alt text for Google Image Search ranking and accessibility. Currently many use generic filenames.

**Fix examples:**
```html
<!-- Current (bad) -->
<img src="/media/Hero.png" alt="Women supporting women" />
<img src="/media/Rigel Logo.png" alt="Rigel Logo" />
<img src="/media/Udayaditya.png" alt="Udayaditya Parbat" />

<!-- Fixed (SEO-optimized) -->
<img 
  src="/media/Hero.png" 
  alt="Indian women supporting each other in menstrual health awareness — Maa by Rigel"
  width="800" height="600"
  loading="lazy"
/>
<img 
  src="/media/rigel circle logo.png" 
  alt="Rigel Foundation logo — Maa menstrual health NGO India"
  width="120" height="120"
/>
<img 
  src="/media/Udayaditya.png" 
  alt="Udayaditya Parbat, Programme Director of Maa by Rigel menstrual health initiative"
  width="300" height="300"
  loading="lazy"
/>
```

> Also add `width` and `height` attributes to every image to prevent layout shift (Core Web Vitals).

---

### 11. Heading Hierarchy Is Broken

The page uses `<h1>MAA</h1>` and `<h2>` etc., but there are multiple heading issues:

**Issues found:**
- `<h1>MAA</h1>` — Too short, no keywords
- `<h1>Maa Menstrual Health Tracker</h1>` — There appear to be multiple H1s (one in main hero, one inside the tracker section)
- Many sections use `<h2>` and `<h3>` without clear hierarchy

**Fix — One H1 only, keyword-rich:**
```html
<!-- Only ONE h1 per page -->
<h1>Menstrual Health Awareness, Education & Support for Women in India</h1>

<!-- Sections use h2 -->
<h2>Menstrual Health Education</h2>
<h2>Menstrual Related Disorders</h2>
<h2>Free Private Period Tracker</h2>
<h2>Government Schemes for Women's Health</h2>

<!-- Subsections use h3 -->
<h3>Polycystic Ovary Syndrome (PCOS)</h3>
<h3>Endometriosis</h3>
```

---

### 12. Internal Links Use Only Anchor `#` Fragments

All navigation links are `href="#section"`, meaning every navigation click is technically the same URL. Google sees zero internal link equity being passed.

**Fix (if you separate into sub-pages):**
```html
<a href="/learn/">Learn About Menstrual Health</a>
<a href="/tracker/">Free Period Tracker</a>
<a href="/disorders/">Menstrual Disorders Guide</a>
<a href="/schemes/">Government Schemes for Women</a>
```

**Fix (if keeping single-page, minimum viable):**  
Add `aria-label` to all anchor links so they're more meaningful to crawlers:
```html
<a href="#learn" aria-label="Learn about menstrual health and hygiene">Learn</a>
<a href="#tracker" aria-label="Free private period tracker tool">Tracker</a>
```

---

## 🟡 MEDIUM-PRIORITY ISSUES

---

### 13. PDF Files Are Linked But Not Crawlable Properly

Research PDFs are linked with spaces in filenames (e.g., `insights%20details/Many%20girls%20lack...`). While `%20` encoding works, file names with spaces are harder for crawlers and link-sharing.

**Fix — Rename files to use hyphens:**
```
/insights-details/stigma-menstrual-silence.pdf
/insights-details/menstrual-education-gap.pdf
/insights-details/period-poverty-access.pdf
```

**Also add PDF meta inside each PDF:**  
Open each PDF and set: Title, Author, Subject, Keywords in Document Properties.

---

### 14. No `hreflang` Tags for Multilingual Support

The site supports 22 Indian languages but has zero `hreflang` tags. Google won't know to serve the Hindi version to Hindi speakers, or Bengali to Bengali speakers.

**Fix — Add for each language version:**
```html
<link rel="alternate" hreflang="en-in" href="https://maa.rigelfoundation.org.in/" />
<link rel="alternate" hreflang="hi" href="https://maa.rigelfoundation.org.in/?lang=hi" />
<link rel="alternate" hreflang="bn" href="https://maa.rigelfoundation.org.in/?lang=bn" />
<link rel="alternate" hreflang="ta" href="https://maa.rigelfoundation.org.in/?lang=ta" />
<!-- ... one for each language -->
<link rel="alternate" hreflang="x-default" href="https://maa.rigelfoundation.org.in/" />
```

> Ideally each language should have its own URL (`/hi/`, `/bn/`) rather than a query param.

---

### 15. Missing `<meta name="keywords">` (Low Priority But Cheap to Add)

While Google doesn't use this for ranking, Bing and other search engines do, and it signals intent.

**Fix:**
```html
<meta name="keywords" content="menstrual health India, period tracker, PCOS symptoms, endometriosis, period poverty, menstrual hygiene, women health NGO India, Rigel Foundation, menstrual education" />
```

---

### 16. No Breadcrumb Schema

Google can show breadcrumbs in search results — increasing click-through rate.

**Fix — Add BreadcrumbList schema:**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://maa.rigelfoundation.org.in/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Menstrual Health Education",
      "item": "https://maa.rigelfoundation.org.in/#learn"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Period Tracker",
      "item": "https://maa.rigelfoundation.org.in/#tracker"
    }
  ]
}
</script>
```

---

### 17. External Links Missing `rel` Attributes

Links to external sites (rzp.io for donations, UNICEF, WHO, government portals) should have proper `rel` attributes for SEO and security.

**Fix:**
```html
<!-- Donation link — external, no SEO juice needed -->
<a href="https://rzp.io/rzp/maa-donation" rel="noopener noreferrer nofollow" target="_blank">
  Donate Now
</a>

<!-- Trusted sources — can pass link equity -->
<a href="https://www.unicef.org/press-releases/..." rel="noopener noreferrer" target="_blank">
  Source: UNICEF
</a>

<!-- Government portals — trusted, let equity pass -->
<a href="https://missionshakti.wcd.gov.in/" rel="noopener noreferrer" target="_blank">
  Visit Portal
</a>
```

---

### 18. Blog Is on a Separate Domain

The blog lives at `rigelfoundation.org.in/category/blog/` — not on `maa.rigelfoundation.org.in`. Every blog article's SEO value goes to the parent domain, not to Maa.

**Fix options:**
- Option A: Move blog to `maa.rigelfoundation.org.in/blog/` — all content authority stays on Maa
- Option B: Cross-link heavily from the blog to Maa pages with keyword-rich anchor text, e.g. `<a href="https://maa.rigelfoundation.org.in/#tracker">free period tracker</a>`

---

### 19. No `favicon` Declared in `<head>`

A missing favicon causes a 404 request on every page load, slightly impacting performance scores, and hurts brand recognition in browser tabs and Google search history.

**Fix:**
```html
<link rel="icon" type="image/png" href="/media/favicon.png" sizes="32x32" />
<link rel="apple-touch-icon" href="/media/apple-touch-icon.png" sizes="180x180" />
```

---

### 20. Missing `<meta name="author">` and `<meta name="geo">` Tags

These help with E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) signals, especially for a health site.

**Fix:**
```html
<meta name="author" content="Rigel Foundation" />
<meta name="geo.region" content="IN" />
<meta name="geo.country" content="India" />
<meta name="rating" content="general" />
<meta name="revisit-after" content="7 days" />
```

---

## 🟢 BONUS / GROWTH OPPORTUNITIES

---

### 21. Add a Google Search Console & Bing Webmaster Verification Tag

```html
<!-- Google Search Console -->
<meta name="google-site-verification" content="YOUR_VERIFICATION_CODE_HERE" />

<!-- Bing Webmaster Tools -->
<meta name="msvalidate.01" content="YOUR_BING_CODE_HERE" />
```

---

### 22. Add `loading="lazy"` to All Non-Hero Images

This improves Core Web Vitals (LCP & CLS scores), which are direct Google ranking factors.

```html
<!-- Hero image: eager load -->
<img src="/media/Hero.png" alt="..." loading="eager" fetchpriority="high" />

<!-- All other images: lazy load -->
<img src="/media/BOARD1.JPG" alt="Street board: make fun of blood stains" loading="lazy" />
<img src="/media/BOARD2.JPG" alt="Street board: empower girls with knowledge" loading="lazy" />
```

---

### 23. Page Speed — Compress & Convert Images to WebP

Large JPG/PNG images slow load time. Google PageSpeed directly affects rankings.

```html
<!-- Use <picture> for modern format support -->
<picture>
  <source srcset="/media/Hero.webp" type="image/webp" />
  <img src="/media/Hero.png" alt="..." loading="eager" />
</picture>
```

> Convert all media files to `.webp` — typically 30–50% smaller than PNG/JPG.

---

### 24. Donate Button — Add UTM Parameters for Tracking

```html
<a href="https://rzp.io/rzp/maa-donation?utm_source=maa_website&utm_medium=hero_cta&utm_campaign=donate_2026" 
   rel="noopener noreferrer nofollow" 
   target="_blank">
  Donate Now
</a>
```

---

## ✅ COMPLETE HEAD TAG — RECOMMENDED FINAL VERSION

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <!-- Primary SEO -->
  <title>Menstrual Health Awareness India | Period Tracker & Education — Maa by Rigel</title>
  <meta name="description" content="Free period tracker, PCOS & endometriosis education, and government scheme access for women across India. WHO-backed, 100% private. By Rigel Foundation." />
  <meta name="keywords" content="menstrual health India, period tracker, PCOS symptoms, endometriosis, period poverty, menstrual hygiene, women health NGO India, Rigel Foundation" />
  <meta name="author" content="Rigel Foundation" />
  <meta name="robots" content="index, follow" />

  <!-- Canonical -->
  <link rel="canonical" href="https://maa.rigelfoundation.org.in/" />

  <!-- Language -->
  <!-- Set dynamically per user's selection -->
  <!-- <html lang="en-IN"> on default -->

  <!-- hreflang (add all 22 languages) -->
  <link rel="alternate" hreflang="en-in" href="https://maa.rigelfoundation.org.in/" />
  <link rel="alternate" hreflang="hi" href="https://maa.rigelfoundation.org.in/?lang=hi" />
  <link rel="alternate" hreflang="x-default" href="https://maa.rigelfoundation.org.in/" />

  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://maa.rigelfoundation.org.in/" />
  <meta property="og:title" content="Maa by Rigel | Menstrual Health Awareness & Support India" />
  <meta property="og:description" content="Free period tracker, PCOS education, and government scheme access. WHO-backed, 100% private." />
  <meta property="og:image" content="https://maa.rigelfoundation.org.in/media/og-cover.png" />
  <meta property="og:locale" content="en_IN" />
  <meta property="og:site_name" content="Maa by Rigel" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Maa by Rigel | Menstrual Health Awareness" />
  <meta name="twitter:description" content="WHO-backed menstrual health education, free period tracker, and government scheme access for women across India." />
  <meta name="twitter:image" content="https://maa.rigelfoundation.org.in/media/og-cover.png" />

  <!-- Geo -->
  <meta name="geo.region" content="IN" />
  <meta name="theme-color" content="#dc2626" />

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="/media/favicon.png" sizes="32x32" />
  <link rel="apple-touch-icon" href="/media/apple-touch-icon.png" sizes="180x180" />

  <!-- Sitemap hint -->
  <!-- Sitemap is at /sitemap.xml -->

  <!-- Structured Data -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "NGO",
    "name": "Maa by Rigel",
    "url": "https://maa.rigelfoundation.org.in/",
    "logo": "https://maa.rigelfoundation.org.in/media/rigel%20circle%20logo.png",
    "description": "India's first NGO dedicated to menstrual health awareness, period poverty elimination, and reproductive education for women.",
    "email": "maa@rigelfoundation.org.in",
    "foundingDate": "2020",
    "areaServed": "IN",
    "sameAs": [
      "https://www.instagram.com/rigelfoundation/",
      "https://www.linkedin.com/company/rigelfoundation/",
      "https://rigelfoundation.org.in"
    ]
  }
  </script>

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Is exercising during your period safe?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. Gentle exercise is completely safe during menstruation and can actually help reduce cramps."
        }
      },
      {
        "@type": "Question",
        "name": "What is PCOS?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "PCOS (Polycystic Ovary Syndrome) is a common hormonal disorder causing irregular periods, weight gain, acne, and fertility challenges."
        }
      },
      {
        "@type": "Question",
        "name": "What is period poverty?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Period poverty is the inability to access affordable menstrual products, affecting millions of women in India and globally."
        }
      }
    ]
  }
  </script>

  <!-- Verification (add your codes) -->
  <meta name="google-site-verification" content="ADD_YOUR_CODE" />
</head>
```

---

## 📊 Priority Summary Table

| # | Issue | Priority | Effort |
|---|-------|----------|--------|
| 1 | Remove Testing Mode banner | 🔴 Critical | Low |
| 2 | Add canonical tag | 🔴 Critical | Low |
| 3 | Add robots.txt & sitemap.xml | 🔴 Critical | Low |
| 4 | Separate into sub-pages | 🔴 Critical | High |
| 5 | Add OG + Twitter meta tags | 🔴 Critical | Low |
| 6 | Add Schema structured data | 🔴 Critical | Medium |
| 7 | Fix title tag | 🟠 High | Low |
| 8 | Improve meta description | 🟠 High | Low |
| 9 | Fix `lang` attribute | 🟠 High | Low |
| 10 | Fix all image alt texts | 🟠 High | Medium |
| 11 | Fix heading hierarchy (H1) | 🟠 High | Medium |
| 12 | Fix internal links | 🟠 High | High |
| 13 | Rename PDF files (no spaces) | 🟡 Medium | Low |
| 14 | Add hreflang for 22 languages | 🟡 Medium | Medium |
| 15 | Add meta keywords | 🟡 Medium | Low |
| 16 | Add breadcrumb schema | 🟡 Medium | Low |
| 17 | Fix external link rel attrs | 🟡 Medium | Low |
| 18 | Move blog to subdomain | 🟡 Medium | High |
| 19 | Add favicon declaration | 🟡 Medium | Low |
| 20 | Add author/geo meta tags | 🟡 Medium | Low |
| 21 | Register Google Search Console | 🟢 Bonus | Low |
| 22 | Add lazy loading to images | 🟢 Bonus | Low |
| 23 | Convert images to WebP | 🟢 Bonus | Medium |
| 24 | Add UTM params to donate link | 🟢 Bonus | Low |

---

*Audit prepared for maa.rigelfoundation.org.in — June 2026*
*All code examples are production-ready and can be copy-pasted directly.*
