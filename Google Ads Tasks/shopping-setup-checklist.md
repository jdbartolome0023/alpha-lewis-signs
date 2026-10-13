# Signee Google Shopping: setup checklist (prepared Oct 13 2026)

Budget rule (Josette, Oct 12): Shopping runs INSIDE the A$1,200/month envelope. At go-live change Search to about A$28/day and set Shopping to about A$12/day in the same sitting. Do NOT tell Kim and Nic until after it is set up. Build the campaign Paused. Never remove the last Merchant Center administrator.

## 1. Create the Merchant Center (Josette)
- Sign in as jddbartolome@gmail.com at `https://merchants.google.com/`. Do NOT use the existing Designer Blooms Canada Merchant Center (another client).
- Business name: Signee. Country: Australia. Website: `https://signeesigns.com.au/`.
- Note: the Ads account 966-837-5188 already shows a product link to Merchant Center ID 553528757, which nobody can open. Leave it, link the new one, then review the old link.

## 2. Verify and claim the website (Josette, Shopify theme edit)
- Merchant Center > Settings > Business information > Website > Verify and claim. Choose the HTML tag method.
- Paste the meta tag into `layout/theme.liquid` inside `<head>` (same file that holds the Tag Manager snippet). Save, then click Verify in Merchant Center.

## 3. Shipping and tax settings
- Shipping: one service, Australia, Standard, free, all products. Handling time: Walter dispatches in about 2 weeks, other blank signs 1 to 2 business days (check the live Shipping & Returns policy before entering).
- Tax: prices are GST-inclusive, no extra tax setting needed for Australia.

## 4. Product feed
- File: `shopping-feed-oct-13-2026.tsv` (22 rows, one per colour of every blank sign, built from the live store).
- Merchant Center > Products > Data sources > Add product data > Upload file (or Google Sheets, then set a daily fetch).
- Deliberately excluded: the "Add Artwork = Yes" variants (higher price). The listed price is the blank-sign price, which matches what the product link opens.
- Check before upload: titles read well; `google_product_category` should be confirmed in the Merchant Center category picker; `identifier_exists` is `no` (own brand, no barcodes); the plain image (`SIGNEE_1800x1800_*.png`) may show one colour only.

## 5. Link and build (after approval, usually days to about 2 weeks)
- Google Ads: Tools > Data manager or Linked accounts > Google Merchant Center > link the new account.
- New campaign: Sales > Shopping > Standard Shopping, Australia, English, Search network only if offered, budget A$12/day, bidding Maximize clicks with a max cost per click near A$2.50, built Paused.
- Product groups: split by product so Walter and Winnie (higher profit) can be bid separately later.
- Then, same sitting: set Search budget to about A$28/day, enable Shopping, recheck in 3 to 4 days.

## Before enabling
- Check Walter page speed fixes (largest contentful paint 9.3 s on Oct 13), since Shopping clicks land on product pages.
