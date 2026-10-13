# Signee Google Ads: fixes from the Oct 13 2026 zero-conversion review

Account 966-837-5188, campaign "Signee Search AU". Josette clicks, Claude verifies afterwards by query.

## Fix 1: send General Business to a product page, not the homepage
Why: 45 of 113 clicks (A$125, 43% of spend) land on the homepage. The General Business ad group is the only ad group whose ad points there.
Page to use: `https://signeesigns.com.au/collections/retail-store-signage` (returns 200, lists all 10 products).
Click path:
1. Campaigns > Signee Search AU > Ads > filter to ad group "General Business Signage".
2. Tick the ad > Edit (pencil) > Edit ad.
3. Change Final URL to the page above. Leave the display path as is. Save.
4. Check the ad status returns to Approved (a URL edit can send it back for review for a short time).
Do NOT change the ad group's keywords at the same time as this, so the effect of each change can be told apart.

## Fix 2: pause the broad "custom" keywords in General Business (judgement call, optional)
Why: "custom business signage" (17 clicks, A$45) and "custom shop sign" (116 impressions) attract people wanting bespoke work, while Signee sells 10 ready-made signs. No conversion data says they are bad yet, so this is a reasoned call, not a proven one. Skipping it is fine.
Keywords to pause (not remove): custom business signage (phrase), custom business sign (phrase and exact), custom shop sign (phrase and exact).
Keep "outdoor signage" and "business signage".
Click path: Audiences, keywords and content > Search keywords > filter ad group "General Business Signage" > tick the rows > Edit > Pause.

## Fix 3: search terms review about Oct 15
Pull search terms again, add phrase negatives for any new off-target themes. Remember negatives do not match plurals or close variants.

## Fix 4: funnel events (see `funnel-pixel-ga4.js`)
Separate new custom pixel, the purchase pixel stays untouched.

## Do not change yet
Bidding (stay on Maximize clicks, A$5 cap), budget, Search Partners, recommendations (do not apply "Finish setting up conversion tracking", it would duplicate the GA4 import).

## Site findings (desktop read, Oct 13)
- Product page (Walter): price from A$449, Add to cart, "Add Artwork? (+$99)" opens an artwork editor that asks for a vector file and shows "ADD YOUR ARTWORK TO CONTINUE". The page text shows no delivery time, reviews or returns wording. Free shipping appears only in the site banner.
- Illuminated collection has only 1 product (Lottie), A-frame collection 3, Blade 4.
- NOT checked: a true phone view (the browser window could not be narrowed and Shopify blocks framing), and checkout (Shopify asked for account verification).
