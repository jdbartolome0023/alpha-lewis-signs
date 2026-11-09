# Signee theme change plan, 6 Nov 2026 (NOT APPLIED, waiting on approval)

Prepared read only from the public pages. Nothing in Shopify has been opened or changed.

Theme found on the live store: "signee-shopify-theme/master", built on Jaffle 1.1.5, theme id 162617032933, role main. The name suggests it may be linked to a GitHub branch. Check Online Store > Themes for a GitHub icon before editing, because a later sync could overwrite edits made in the Shopify editor.

Theme editor: https://admin.shopify.com/store/signee-2/themes/162617032933/editor
Themes list (for the backup): https://admin.shopify.com/store/signee-2/themes

## Approvals needed before any change

1. Dispatch line on product pages: Nic said yes in principle (6 Nov, "as per your notes") and asked to see a draft before publishing. Draft sent to Josette to show Nic. Do not publish until Nic says yes to the draft.
2. Prices on collection pages and moving the grid up: Kim and Nic have not answered (as at 6 Nov). Do not change until they say yes.

## Change 1: dispatch line under Add to cart (product pages)

Wording to show Nic (matches https://signeesigns.com.au/policies/shipping-policy):
- All products except Walter: "Dispatched within 1 to 2 business days (add about 2 to 3 business days if you add your logo). Free shipping Australia-wide."
- Walter: "Dispatched in approximately 2 weeks (add about 2 to 3 business days if you add your logo). Free shipping Australia-wide."

How, with no code: all products share one product template, so Walter needs its own template.
1. Back up the theme (Actions > Duplicate).
2. In the editor, open Products > Default product, add a Text block directly under the Buy buttons block with the standard wording, Save.
3. Create a second product template (Templates > Create template, "walter", based on Default product), change the text block to the Walter wording, Save.
4. Shopify Admin > Products > Walter > Theme template > select "walter", Save.
5. Check the live pages for Flossy and Walter. Mobile too.

Checks before step 2: confirm the editor offers a Text block in the main product section. If not, a small code edit is needed instead.

## Change 2: prices on collection pages

Finding: the collection page cards are not standard Shopify product cards. Each card is a manual block (image, name, one line of text, CHECK IT OUT button) inside a "featured collection" section, and none shows a price. So the price has to be typed into each card's text, per product, for the six collections. Risk: typed prices go stale if a price changes. Current prices (verified 2 Oct, re-check before typing): Flossy from $229, Theodore from $229, Walter $449 to $548, Winnie $319 to $418. Re-read every price from the live product page before typing.

## Change 3: move the grid up on collection pages

Finding (blade-signs, same pattern likely on the other five): sections run in this order: (1) intro text about 123 words, (2) 7 word banner "RETAIL SIGNAGE, REDEFINED.", (3) product grid, (4) long "What is a Blade Sign?" text about 255 words. So the long text is already below the grid. The only move needed is the grid above the 123 word intro, or above both the intro and the banner. In the editor this is a drag of the section, no code. Re-check each of the six collections, since the order may differ.

## Not planned
- Goods and Services Tax line: Nic said not needed.
- Returns line near Add to cart: Nic said leave as is.
- Reviews: none exist yet.
- 10% pop-up delay: Nic agrees to a slight delay. Parked by Josette on 2 Nov, likely set in Klaviyo. Unconfirmed who holds the login.
