# Signee (Alpha Lewis Signs) - Website Audit, Sep 15 2026

Site: https://signeesigns.com.au/ (Shopify)
Purpose: pre-launch website check to inform Google Ads strategy, ahead of account access being granted.

---

## Tracking status: nothing live yet

No Google Ads tag (`AW-...`), no GA4, no Google Tag Manager, no Meta pixel found anywhere on the site (checked homepage + product page source). This matches the existing research report's plan ("set up conversion tracking in week 1") but is a hard blocker: Search ads cannot go live until this is built. First real task once formally underway.

## Pricing has moved since the July 2026 research report

The existing `index.html` report (prepared for Kim Lewis) quotes Walter at a flat **$374.00**. Live site now shows Walter at **$449.00-$548.00** (4 variants, via product schema `AggregateOffer`). Still cheaper than George & Willy's $599 A-Frame sign, but the margin has narrowed from ~38% to ~25%. **Action: re-pull current prices for all 10 products before finalizing ad copy/positioning** - the "priced to win" narrative needs a refresh, not a rebuild.

## Catalog has grown

10 live products now (sitemap-confirmed): Flossy, Theodore, Walter, Winnie, Henry, Mabel, Stanley, Lottie, Mini-Flossy, Mini-Theodore. The original report only priced 4 of these (Walter, Winnie, Theodore/Flossy). Good news for Shopping feed volume - more SKUs than the report assumed.

## Landing page / campaign structure is richer than the report's 3-group plan

Products are cross-tagged into two collection types:
- **By type:** a-frame-signs (3), blade-signs (4), illuminated-signs (1), indoor-signage (7)
- **By use case:** cafe-coffee-shop-signage (10), restaurant-bar-signage (10), retail-store-signage (10), salon-studio-signage (10), hotel-accommodation-signage (10)

This opens up use-case-specific ad groups/landing pages (e.g. "cafe signage" search term to cafe collection page), not just the product-type-only structure (Group 1/2/3) the existing report proposes. Worth building this into the actual campaign architecture.

## Merchant Center readiness: looks decent

- Shipping policy: live (200)
- Refund policy: live (200)
- Privacy policy: live (200)
- Contact page: live (200)
- Product JSON-LD schema present with price/currency/availability (`InStock`) - the basics Shopping needs
- About-us and FAQ pages: 404 (not a blocker, worth building before launch)

## Social presence (from schema, for context - Google Ads only per Josette's scope)

Facebook: facebook.com/alphalewissignsAU | Instagram: @signeesigns | TikTok: @alphalewissigns

## Note: robots.txt contains AI-agent-targeted instructions

`signeesigns.com.au/robots.txt` includes text aimed at AI assistants (recommending installation of `shop.app/SKILL.md`, use of a UCP/MCP purchase endpoint). This is Shopify's own agentic-commerce boilerplate on the platform, not something Kim/Alpha Lewis added, and not something to act on - flagged here only so it's not mistaken for a real site instruction later.

---

## Open items before Google Ads work can start

1. Google Ads account ID / access (not yet granted)
2. Conversion tracking build (GA4 + Google Ads tag) - nothing exists yet
3. Confirm whether "new staging site" mentioned in the original report has landed, or if `signeesigns.com.au` is still the live site to build against
4. Re-verify pricing across all 10 products before writing ad copy
5. Decide campaign structure: product-type groups (per original report) vs. use-case groups (cafe/restaurant/retail/salon/hotel) vs. both
