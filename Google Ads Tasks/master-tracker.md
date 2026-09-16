# Signee (Alpha Lewis Signs) - Master Tracker

## Account Details

- **Business:** Alpha Lewis Signs (parent/manufacturer, est. Melbourne 1969) - **Signee** is the DTC product brand
- **Website:** https://signeesigns.com.au/ (Shopify)
- **Corporate site (not for Ads):** https://alphalewissigns.com.au/ (services/B2B/council work - separate site, do not build campaigns against this one)
- **Contacts:** Kim Lewis (kim@alphalewissigns.com.au), Nic (nic@alphalewissigns.com.au) - business owners
- **Management fee:** 40,000 PHP/month, invoiced fortnightly (10th and 25th), paid via Wise
- **Google Ads MCC:** JDD Bartolome, CID 989-282-6805 (login: jddbartolome@gmail.com)
- **Google Ads client account:** Signee, CID **715-970-4117**
  - First attempt CID 838-398-4347 was discarded Sep 16 2026 - locked to Philippine Standard Time/PHP by mistake, unrecoverable, see "Lessons learned" below.

## Immediate - Outstanding

- [ ] **Waiting on Kim/Nic to accept Google Ads invite** (sent Sep 16 2026, Admin access, both kim@alphalewissigns.com.au and nic@alphalewissigns.com.au) - check acceptance status each session
- [ ] **Waiting on Kim/Nic to complete billing setup** on the Signee account (Admin > Billing > Create new payments profile, Billing Country = Australia, their real business address + card) - this is what will actually lock in the correct AUD/Sydney time zone. Until this is done the account is still in draft with Philippine Standard Time as a placeholder.
- [ ] Once billing is confirmed done: verify via **Admin > Account settings** (not the wizard screens) that Time zone shows an Australian zone and currency is AUD - do not trust the "Enter payment details" wizard screen's live preview, it has shown wrong/stale info before
- [ ] Build GTM + GA4 + Google Ads conversion tag - **nothing is live on the site yet**, confirmed twice now (initial website-audit-sep15-2026.md, and a second direct re-check Sep 16 2026 covering homepage source, a product page, and DNS TXT records). No GTM container ID, no GA4 measurement ID, no Google Ads AW- tag, no Meta pixel, no Search Console verification (no meta tag, no `google-site-verification=` DNS TXT record) anywhere. This resolves Kim's "not sure if a GA4 property already exists" open question from the original email thread - there is nothing live to find, whether or not an orphaned property exists in someone's GA4 admin panel, none is connected to the site.
- [ ] Side-finding from the DNS check: they use **Klaviyo** for email marketing (verification TXT record present) - worth knowing for any future customer-list/retargeting work with Meta
- [ ] Re-verify current pricing across all 10 products before writing any ad copy (July report pricing is stale - Walter moved from $374 to $449-$548)
- [ ] Decide campaign structure: product-type groups (Walter/Winnie/Theodore/Flossy etc.) vs. use-case groups (cafe/restaurant/retail/salon/hotel collections) vs. both
- [ ] Confirm whether "new staging site" mentioned in the original July research report has landed, or if signeesigns.com.au is still the one to build against (seems to be current live site as of Sep 16, but worth a direct confirm with Kim)
- [ ] Set up Google Ads MCP connection for Signee (mirrors Kenny Fuels/Ninja Digital pattern) once account access is fully live

## Lessons learned (Sep 16 2026 Google Ads setup)

- **Google Ads account time zone and currency lock permanently at account creation and can never be changed.** If it's wrong, the only fix is discarding the account and starting over.
- The "Create your first campaign" wizard's billing-country screen is **unreliable** - it can display "Australia / Sydney Time / AUD" as if the change was accepted, but this does not always actually commit to the account. Always double check via **Admin > Account settings** directly, not the wizard.
- New account creation defaults Locations, Billing Country, and Time zone to the **MCC's own country** (Philippines, in this case) unless explicitly overridden at every step - check this at every screen, not just once.
- The wizard defaults to **Performance Max** as campaign type when the goal is "Purchases" - if Search is wanted, you must explicitly click "view other campaign types" and select Search.
- **Google Ads blocks sending user invites until the account has a payments profile** (even an incomplete/shell one) - confirmed by testing 3 different invite emails, all failing identically ("An error occurred. Please try again later.") until a payments profile existed.
- Kim's email (kim@alphalewissigns.com.au) is Microsoft/Outlook-hosted, not Google Workspace - she and Nic will likely need to go through Google's "create account using my current email" flow to accept the Ads invite, not sign in directly.

## Completed

- **Sep 15 2026:** Deal closed, Josette handling Google Ads. Pre-launch website audit done (website-audit-sep15-2026.md).
- **Sep 16 2026:** Google Ads account created (Signee, CID 715-970-4117) under JDD Bartolome MCC. Search campaign draft built: goal = Purchases (manual conversion setup, not URL-based), Locations = Australia, keywords/search themes populated. Admin invites sent to Kim and Nic. Step-by-step instructional email sent to Kim covering invite acceptance + billing setup.
