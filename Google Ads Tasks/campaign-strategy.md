# Signee Google Ads Campaign Strategy

Prepared Sep 17 2026. This is the working strategy document that will guide the actual campaign build in Google Ads once account access is fully live. It supersedes the original 3-group structure in the July 2026 research report (`index.html`) where the September 2026 website audit found a richer site structure to build against, and flags every figure that needs re-verification before launch.

**Data sources used:** July 2026 competitor/keyword research (`index.html`), September 15 2026 website audit (`website-audit-sep15-2026.md`), Kim's Sep 2026 goals brief (`CLAUDE.md`), and the GA4/GTM tracking build completed Sep 17 2026 (this tracker).

**What is confirmed vs. what needs refresh:** search volume, cost per click, and product pricing below are from July 2026. Two months old, and pricing is already known to have moved (see Section 3). Treat the numbers as directional, not final, re-pull before setting live budgets or bids.

---

## 1. Objectives

- **Primary conversion goal:** Purchases (online sales), tracked via the manual GA4 conversion event still to be built (Phase 3, master tracker). Not lead form, not phone, there is no phone number published on the site.
- **Average order value:** $200 to $300 AUD.
- **Main site action:** buy a sign.
- **Secondary interest:** customer data capture for a future Meta retargeting audience. This should be captured as a non-primary conversion action (e.g. "Newsletter Signup") for reporting only, it should not compete with Purchases for Smart Bidding optimization.
- **Geographic scope:** all of Australia, matching Signee's national shipping reach (per the July report, unconfirmed if this has changed).

## 2. Competitive Landscape

Confirmed via live Google Shopping results and site-level tracking code checks (July 2026):

| Competitor | Shopping ads | Search (text) ads | Notes |
|---|---|---|---|
| George and Willy | Confirmed running | No evidence found | A-Frame Business Sign at $599 AUD. Site carries Google Ads tracking code, Shopify + Klaviyo + Intelligems + Gorgias stack, a well-resourced operation. Instagram/Facebook ad activity suspected but unconfirmed (Meta's ad library blocks unauthenticated checks). |
| Piece of Sign | Confirmed running | No evidence found | Custom Shop Sign appeared 3 times for "custom shop sign" AU searches, priced $345 to $395. Closest product match to Signee. |
| Made of Tomorrow | No evidence | No evidence | Signage is a minor side category for them. Not a real competitor, deprioritize. |

**Implication for the ad account:** both real competitors are Shopping-only, neither has confirmed text Search ads. This is an opening. A well-built Search campaign may face less direct ad-auction competition than the Shopping placement will, at least until they expand into Search themselves.

## 3. Pricing Position (needs re-verification before copy is written)

| Product type | Signee item | July price (report) | Current site price (Sep 15 audit) | Competitor item | Competitor price |
|---|---|---|---|---|---|
| Roadside A-frame | Walter | $374.00 | $449.00 to $548.00 (4 variants) | George and Willy A-Frame Sign | $599.00 |
| Roadside A-frame, smaller | Winnie | $264.00 | Not yet re-pulled | George and Willy A-Frame Sign | $599.00 |
| Wall or hanging sign | Theodore / Flossy | $176.00 | Not yet re-pulled | Piece of Sign Custom Shop Sign | $345.15 to $395 |

Walter's margin over George and Willy narrowed from about 38% to about 25% as pricing moved. Still a real price advantage, but the "priced to win" ad copy angle needs the actual current numbers before it goes live, not the July figures. **Action: re-pull all 10 products' current prices before finalizing ad copy** (already an open Phase 1 item on the master tracker).

## 4. Product Catalog (10 SKUs, per Sep 15 audit)

Flossy, Theodore, Walter, Winnie, Henry, Mabel, Stanley, Lottie, Mini-Flossy, Mini-Theodore.

The July report only priced/planned around 4 of these. The catalog has grown, which is good news for Shopping feed volume once Stage 2 launches.

## 5. Keyword and Demand Research (July 2026, Australia, needs re-pull)

| Search term | Monthly searches (AU) | Cost per click |
|---|---|---|
| a-frame sign | 2,400 | $3.42 |
| business signage | 1,600 | $4.62 |
| shop signage | 880 | $5.87 |
| cafe signage | 720 | $3.24 |
| outdoor business sign | 590 | $6.00 |
| sandwich board sign | 390 | $3.88 |
| custom shop sign | 40 | $5.50 |

Over 6,500 monthly searches across just these seven terms, before longer-tail variants. This is the demand base Stage 1's budget is sized against. Re-pull via Keyword Planner once the Google Ads MCP connection is live (Phase 2, master tracker) to confirm these haven't shifted, and to expand the list against the use-case collections found in the September audit (see Section 6).

**Additional keyword themes to research once account access is live** (not yet volume-checked, inferred from the site's use-case collections):
- "cafe sign", "restaurant sign", "salon sign", "hotel sign", "retail store sign"
- "blade sign", "illuminated sign", "light up business sign", "indoor signage"
- Brand-adjacent generic terms: "signage Melbourne", "custom business sign Australia"

## 6. Campaign Architecture

The original July report proposed 3 ad groups by product type only. The September 2026 website audit found the live site is cross-tagged into two structures, which supports a richer, hybrid build:

- **By product type:** a-frame-signs (3 products), blade-signs (4), illuminated-signs (1), indoor-signage (7)
- **By use case:** cafe-coffee-shop-signage (10), restaurant-bar-signage (10), retail-store-signage (10), salon-studio-signage (10), hotel-accommodation-signage (10)

### Recommended structure: one Search campaign, hybrid ad groups

**Campaign: Signee Search AU** (Australia, national, Purchases goal)

| Ad group | Products | Landing page | Sample search terms |
|---|---|---|---|
| A-Frame & Sidewalk Signs | Walter, Winnie | a-frame-signs collection | "a-frame sign", "sidewalk sign", "sandwich board sign" |
| Wall & Hanging Signs | Flossy, Theodore, Minis | blade-signs / indoor-signage collection | "business signage", "shop sign", "blade sign" |
| Illuminated Signs | (1 product) | illuminated-signs collection | "illuminated sign", "light up business sign" |
| Cafe & Restaurant Signage | Full range, use-case landing | cafe-coffee-shop-signage / restaurant-bar-signage collections | "cafe signage", "restaurant sign" |
| Retail & Salon Signage | Full range, use-case landing | retail-store-signage / salon-studio-signage collections | "shop signage", "salon sign", "retail store sign" |
| Hotel & Accommodation Signage | Full range, use-case landing | hotel-accommodation-signage collection | "hotel signage", "accommodation sign" |
| General Business Signage (broad/awareness) | Full range | homepage or general collection | "business signage", "outdoor business sign", "custom shop sign" |

This sends each click to the most specific matching page, product-type pages for people who already know what kind of sign they want, use-case pages for people searching by their business type. That match between search intent and landing page is what tends to convert, per the July report's own logic, just extended to match the real site structure instead of the original 3-group plan.

**Do not build this in Google Ads until:**
1. Pricing is re-verified (Section 3)
2. GTM snippet is live on Shopify and the GA4 purchase event is built (tracker Phase 3), so Smart Bidding has real conversion data from day one rather than a blind start

### Stage 2: Shopping campaign

Standard Shopping campaign, once Merchant Center is set up and the 10-product feed is approved (see Section 11 for phasing). Per the audit, Merchant Center basics already look ready (shipping, refund, privacy, contact pages live, product JSON-LD schema present with price and availability). This meaningfully shortens the Merchant Center approval runway the July report estimated at 1 to 2 weeks.

## 7. Negative Keywords

Build this list before Search campaign launch, then review the search terms report weekly for the first month.

**Signwriting / trade services** (Signee is a DTC product brand, not a signwriting or installation service; that's the separate alphalewissigns.com.au corporate site):
sign writer, signwriting services, sign installation, sign installer near me, commercial signage company, vehicle wraps, vehicle signage, council signage, regulatory signage, safety signage, sign maker near me, custom neon sign installer

**DIY / free intent** (people looking to make their own, not buy):
how to make a sign, diy sign, free sign template, sign clipart, sign stencil, print your own sign, sign design software

**Jobs / careers:**
sign making jobs, sign painter salary, signage company careers

**Wrong vertical:**
for sale sign, real estate sign, political sign, yard sale sign, parking sign, road sign, traffic sign, license plate sign, name plate engraving

**Generic low-intent:**
sign meaning, sign language, astrology sign, zodiac sign, sign in, sign up (these routinely leak into signage broad match and are pure waste)

**Competitor brand terms:** decide with Kim whether to exclude "george and willy" and "piece of sign" as negatives, or deliberately bid on them. Default recommendation is exclude unless Kim wants to compete head-on for their brand searches, that's a budget and risk-tolerance call, not a technical one.

## 8. Audience and Geographic Targeting

- **Geography:** all of Australia, no state exclusions, matching current national shipping. Confirm with Kim/Nic this hasn't changed since the July report.
- **Search campaigns are keyword-led**, not audience-led, but layer these as **observation only** (not exclusion) to inform bid adjustments once volume supports it:
  - In-market audiences: Business Services, Retail, Home and Office Furniture (as a proxy, there is no exact "business signage" in-market segment)
  - Detailed demographics: Business decision-makers, Small business owners
  - Affinity: Shoppers, Business Professionals
- **Remarketing:** cannot build until the GTM snippet is live and collecting visitor data (Phase 3, master tracker). Once live, a "visited product page, did not purchase" audience is the first one to build, feeding both a future Google Ads remarketing campaign and the Meta retargeting audience Kim already wants (per the customer data capture goal in Section 1).

## 9. Bidding Strategy

- **Launch (Weeks 1 to 4 to 6):** Maximize Conversions, no target CPA, while the account builds a real conversion history. Manual CPC as a fallback only if Smart Bidding behaves erratically on near-zero data, which is a real risk at this budget and volume level.
- **Once conversion volume is established (typically 30+ conversions in a rolling 30 day window):** move to Target CPA, set from the account's own observed cost per purchase, not a guess.
- **Do not use Target ROAS** until there is real order-value data flowing from GA4 e-commerce tracking, which does not exist yet (Section 6, dependency).

## 10. Ad Extensions and Assets

Build alongside the first campaign, not as an afterthought:
- **Sitelinks:** direct links to the 5 use-case collections (cafe, restaurant, retail, salon, hotel) plus About/FAQ once those pages exist (currently 404 per the site audit, worth flagging to Kim/Nic as a pre-launch fix)
- **Callouts:** priced to compete claim (once re-verified), Australia-wide shipping, [order tracking / guarantee claims, confirm exact wording with Kim before using]
- **Structured snippets:** Type: A-Frame Signs, Blade Signs, Illuminated Signs, Indoor Signage; Brand: Signee

## 11. Budget Phasing

Carried forward from the July report's staging logic, since it was built against real search volume and remains sound in structure even though the dollar figures should be re-validated against current CPCs before locking in:

| Stage | Budget | Trigger | What it covers |
|---|---|---|---|
| Stage 1 | $1,200/month | Immediately once tracking is live and campaign is approved | Search ads only, conservative spend to get real conversion data flowing before committing more |
| Stage 2 | $2,000 to $3,500/month | Once Stage 1 data shows Search is converting (targeted at the Week 4 to 6 mark) | Adds Shopping ads once the Merchant Center feed is approved, this is the stage where Signee competes directly with George and Willy and Piece of Sign on Shopping listings |

This is ad spend paid directly to Google, separate from the 40,000 PHP/month management fee. The move from Stage 1 to Stage 2 is data-triggered, not date-triggered.

**Before either stage can start spending:** the account needs billing fully confirmed in AUD/Australian time zone (Phase 2, still pending Kim/Nic), and Merchant Center needs to be created and the feed submitted (Stage 2 dependency, not yet started).

## 12. Measurement Plan

This ties directly to the tracking infrastructure built Sep 17 2026 (see master tracker):

1. GA4 property "Signee - signeesigns.com.au" and GTM container GTM-NFD4DZ2H are built and published, but **not yet installed on the live site**. No real data can flow until the snippet is pasted into Shopify (blocked on Nic's access).
2. Once installed, build the **purchase conversion event** in GA4, either via Shopify's native GA4 integration or dataLayer events pushed at checkout.
3. Import that GA4 purchase event into Google Ads as the **primary conversion action**, replacing the current manual/code-based placeholder set up in the Sep 16 account build.
4. **Test end to end with a real test order** before trusting any reported number, per the standing tracker item.
5. Once live, this is what unlocks Section 9's bidding strategy progression and Section 8's remarketing audience build.

## 13. Risks and Open Items

- **Pricing is stale.** Do not write or approve ad copy referencing specific prices until all 10 products are re-verified (Section 3).
- **Tracking is not live.** Nothing in Sections 6, 8, or 9 can start until the GTM snippet is on the site and the purchase event is built, this is the single biggest blocker to launch timing right now, ahead of even the Ads billing setup.
- **Shopping feed still needs a dedicated Merchant Center eligibility check.** The site basics look ready per the audit, but nothing has actually been submitted yet.
- **About Us and FAQ pages return 404.** Not a paid-ads blocker, but worth raising with Kim/Nic before launch, since sitelinks and general site credibility benefit from having them live.
- **Confirm the "new staging site" question is resolved.** The July report was written anticipating a site relaunch that, per the Sep 15 audit, does not appear to have landed. Confirm signeesigns.com.au is still the build target before finalizing landing page mapping in Section 6.
- **Competitor brand bidding decision** (Section 7) needs a call from Kim, not a default assumption.

## 14. Suggested Launch Timeline

Adapted from the July report's phasing, adjusted to reflect what's actually still open as of Sep 17 2026:

1. **Now to Ads-access-live:** Kim/Nic accept the Ads invite and complete billing (Phase 2, in progress). In parallel, re-verify pricing (Section 3) and get Shopify access sorted for the GTM install (Phase 3, ask sent Sep 17).
2. **Once Shopify access is granted:** install the GTM snippet, build the GA4 purchase event, import into Google Ads as the primary conversion action, test with a real order.
3. **Once tracking is verified working:** finalize keyword research re-pull (Section 5), lock ad copy with current pricing, build the campaign structure from Section 6, build negatives from Section 7, launch Stage 1 at $1,200/month.
4. **Week 4 to 6 post-launch:** first real performance read. Decide on Stage 2 (Shopping) based on actual Search conversion data, not the calendar.
5. **In parallel from day one of Stage 1:** start the Merchant Center setup and product feed submission, so it's ready the moment Stage 2 is triggered rather than adding another 1 to 2 week delay after the decision is made.
