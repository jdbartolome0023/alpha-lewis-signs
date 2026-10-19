# Signee: why no conversions yet (diagnosis, Oct 19 2026)

Data: Google Ads account 966-837-5188, campaign "Signee Search AU", Oct 8 to Oct 18 2026, read only. Not yet available: GA4 (token expired), Shopify Analytics (no permission). Internal working document, not for the client.

## Immediate actions
1. Check Shopify Orders for any order after Oct 6 (https://admin.shopify.com/store/signee-2/orders). Zero real orders means "no sales", not "tracking missing".
2. Renew the GA4 token for Signee (expired, `invalid_grant`) so GA4 sessions, device and funnel can be read. Ads token also expires about Oct 21.
3. Ask Nic for Shopify Analytics access (Reports: sessions by device, conversion funnel). Greyed out for Josette, it is the only complete funnel view.
4. Landing page experience is rated Below average on every rated keyword. Review the pages ads land on (list below) on a phone, before spending more.
5. Read the funnel pixel numbers (view item, add to cart, begin checkout) in GA4 on about Oct 22.

## Numbers (Oct 8 to Oct 18)
- 3,069 impressions, 218 clicks, A$542.83 spent, 0 conversions. Click-through rate 7.1%, average cost per click A$2.49.
- Impression share 10%. Lost to ad rank 69%, lost to budget 21%.
- Device: mobile 189 clicks (87%, A$468), desktop 20 clicks, tablet 9 clicks.
- Spend by ad group: General Business 193.56 (75 clicks), Illuminated 138.65 (54), A-Frame 101.88 (45), Retail & Salon 37.83 (15), Wall & Hanging 30.44 (12), Cafe & Restaurant 28.91 (12), Open Closed 9.25 (4), Hotel & Accommodation 2.31 (1).

## Findings, most likely cause first
1. **Post-click landing page experience is Below average on every keyword Google has rated** (examples: "outdoor signage" and "sandwich board" in General Business and A-Frame, "illuminated sign" in Illuminated Signs, "shop sign" in Wall & Hanging). Impact: people click and then do not find what they expected, and Google also charges more for poor pages. Landing pages in use: collection pages (retail-store-signage 22 clicks, a-frame-signs 27, illuminated-signs 15, cafe-coffee-shop-signage 6), the home page (27) and products/henry. The pages respond fast (about 0.6 seconds) so the issue is content, layout or price clarity on phones, not server speed. Not yet checked on a real phone.
2. **Small sample.** 218 clicks on A$259 to A$900 signs. At a normal 0.5% to 1% purchase rate, 0 sales happens about 11% to 33% of the time by chance alone. Zero is not yet proof of a fault, but it is also not yet proof of health.
3. **Mobile heavy for a considered purchase.** 87% of clicks are mobile; desktop is 20 clicks. Buyers of A$450+ signs often finish on desktop. Needs GA4 device breakdown to confirm.
4. **Bidding is Maximize clicks (A$5 cap).** It buys the cheapest clicks, not buyers. Switching back to Maximize conversions is planned after about 30 purchases, which is a long way off at this rate.
5. **Weak ad rank.** Impression share 10%, 69% lost to rank. Low Quality Scores (for example "buy a frame sign" in A-Frame is 2, "shop sign" in Wall & Hanging is 3). The ads mostly appear in low positions.
6. **Some off-target searches** (examples: "a frame adelaide", "custom banner australia", "mcknight signs tamworth", "acrylic letters manufacturers", "giant light box hire", "banner teardrop"). A rough estimate is one in five of the top-spend terms. Impact: small money, but it dilutes learning.
7. **Measurement gaps (do not explain zero sales, but will matter later):** iPhone clicks arrive with a `gbraid` identifier, not `gclid`, so the purchase pixel's click identifier field will be empty for them; the Shop Pay checkout may not run the pixels; the GA4 to Google Ads purchase import path has never been tested by a real ad sale.
8. **Not the cause (checked):** campaign enabled and eligible, Search network only, Australia presence targeting, all 9 ads approved, purchase is the only primary conversion that counts, no conversion actions are double counting, store in live mode per Nic (Oct 15).

## Housekeeping found
- Ad group "Hotel & Accommodation Signage" exists (1 click so far), not in the tracker's list of 8. An old removed "Ad group 1" still shows an enabled ad.
- The Google Ads Python library in use only supports API version v22, which Google is deprecating. Some queries (landing page view, day of week) already fail with UNSUPPORTED_VERSION. The Signee connection will need a library upgrade soon.

## Update: GA4 read (Oct 7 to Oct 19, GA4 token renewed Oct 19)
- Google paid traffic: 195 sessions (vs 218 Ads clicks), 137 engaged (70%), average 79 seconds, bounce rate 30%. Mobile 169 sessions (120 engaged, 74 seconds); desktop 22 sessions (15 engaged, 122 seconds); tablet 4.
- Other traffic: direct 51 sessions (only 14 engaged), Google organic 24, alphalewissigns.com.au referral 7, Google Business Profile 2.
- Paid sessions: 192 sessions logged 377 page views (about 2 pages each), 122 scrolled, 42 started a form (22%), 2 submitted a form (4 form submits in total on the site). No `purchase` event from any source since Oct 7.
- Landing pages, paid sessions (average time): illuminated-signs 44 (57 s), home page 41 (37 s), retail-store-signage 41 (47 s), a-frame-signs 40 (199 s, strongest), blade-signs 10 (84 s), cafe-coffee-shop-signage 9 (34 s), **products/henry 4 sessions, 0 engaged, 4 seconds average** (page in stock, A$119 and A$138, so cause unknown, watch).
- `view_item`, `add_to_cart`, `begin_checkout` cannot be read for ad visitors before Oct 19 (the funnel pixel only started that morning; the first numbers there are Josette's tests).

### What this changes
- Ad visitors are not bouncing at once (70% engaged, A-frame page averages over 3 minutes). The Below average landing page rating is therefore not proof that the pages repel people; it may be relative to competitors, or about intent.
- **New leading suspect: intent mismatch.** The biggest ad group by spend is General Business Signage and its terms are "custom" searches (custom business signage, custom shop sign, custom sign, custom signage online). People may want a made-to-order quote, while the store sells ready-made products you add to a cart. 22% of paid sessions started a form: **identify which form that is** (newsletter popup or quote form). If it is a quote or contact form, people are asking for custom work, not buying.
- Still unknown: the add to cart rate of ad visitors (needs the funnel pixel, read about Oct 22) and whether there were real Shopify orders (Josette checks).
