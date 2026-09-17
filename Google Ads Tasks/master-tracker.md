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

## Full Setup Checklist (ground-up, research through launch)

### Phase 1: Research
- [x] Competitor research (July 2026 report - pricing now stale, see Phase 4)
- [x] Pre-launch website audit (structure, collections, Merchant Center readiness)
- [x] Tracking audit - confirmed nothing live (GTM/GA4/Ads tag/Meta pixel/GSC), re-confirmed Sep 16 2026 via source + DNS check
- [ ] Re-verify current pricing across all 10 products before writing any ad copy (July report pricing is stale - Walter moved from $374 to $449-$548)
- [ ] Confirm whether "new staging site" mentioned in the original July research report has landed, or if signeesigns.com.au is still the one to build against (seems to be current live site as of Sep 16, but worth a direct confirm with Kim)

### Phase 2: Account & Access Setup
- [x] Google Ads account created (Signee, CID 715-970-4117) under JDD Bartolome MCC
- [x] Search campaign draft built (goal = Purchases, Locations = Australia, keyword themes populated)
- [x] Admin invites sent to Kim and Nic
- [ ] **Waiting on Kim/Nic to accept the Google Ads invite** (sent Sep 16 2026) - check status each session
- [ ] **Waiting on Kim/Nic to complete billing setup** (Admin > Billing > Create new payments profile, Billing Country = Australia, their real business address + card) - this is what actually locks in the correct AUD/Sydney time zone. Until done, the account sits in draft with Philippine Standard Time as a placeholder.
- [ ] Once billing is confirmed done: verify via **Admin > Account settings** (not the wizard screens) that Time zone shows an Australian zone and currency is AUD - do not trust the wizard's live preview, it has shown wrong/stale info before
- [ ] Set up Google Ads MCP connection for Signee (mirrors Kenny Fuels/Ninja Digital pattern) once account access is fully live

### Phase 3: Tracking Setup
- [x] Create GA4 property (Signee account, property "Signee - signeesigns.com.au", Measurement ID G-16K9H45R2V, Melbourne time/AUD, under jddbartolome@gmail.com)
- [x] Build GTM container (container ID GTM-NFD4DZ2H, GA4 Configuration tag built and published firing on all pages)
- [ ] Get website (Shopify) edit access from Nic to install the GTM snippet
- [ ] Set up the purchase/conversion event in GA4
- [ ] Import the GA4 conversion into Google Ads as the primary conversion action (currently set to manual/code-based, per the account build)
- [ ] Test end to end with a real test order before trusting any reported number
- [ ] Google Search Console - verify the domain (optional but useful for organic visibility alongside paid)

### Phase 4: Campaign Build
- [x] Full strategy document written: `Google Ads Tasks/campaign-strategy.md` (Sep 17 2026) - covers campaign structure, keyword research, negative keywords, audience/geo targeting, bidding strategy, budget phasing, ad extensions, measurement plan, and launch timeline. Decided: hybrid structure (product-type ad groups AND use-case ad groups, not either/or) since the Sep 15 audit found the live site supports both.
- [ ] Build out ad groups in Google Ads per the strategy doc's Section 6 structure (blocked on tracking going live first, see strategy doc Section 13 risks)
- [ ] Write ad copy (headlines/descriptions) per group, using re-verified pricing from Phase 1
- [ ] Finalize negative keyword list in Google Ads (draft categories already in strategy doc Section 7)
- [ ] Ad extensions (sitelinks, callouts, structured snippets) - draft plan in strategy doc Section 10, needs Kim's sign-off on callout wording
- [ ] Set budget and bid strategy per strategy doc Sections 9 and 11 (Stage 1 $1,200/month Search only, once tracking is live)
- [ ] Consider a Shopping campaign - Merchant Center basics already looked ready per the website audit, worth a separate feed/eligibility check when we get here

### Phase 5: Launch & Monitor
- [ ] QA the full campaign before going live (tracking firing correctly, budget/targeting correct, ads approved)
- [ ] Launch
- [ ] First-week monitoring check
- [ ] Weekly reporting moves from task-summary format to real performance metrics once there's live spend/conversion data (see `kf-google-weekly.md` in the Kenny Fuels project for what that format looks like)

### Open side-note
- [ ] They use **Klaviyo** for email marketing (verification TXT record present, found during the Phase 1 tracking audit) - worth knowing for any future customer-list/retargeting work with Meta

## Lessons learned (Sep 16 2026 Google Ads setup)

- **Google Ads account time zone and currency lock permanently at account creation and can never be changed.** If it's wrong, the only fix is discarding the account and starting over.
- The "Create your first campaign" wizard's billing-country screen is **unreliable** - it can display "Australia / Sydney Time / AUD" as if the change was accepted, but this does not always actually commit to the account. Always double check via **Admin > Account settings** directly, not the wizard.
- New account creation defaults Locations, Billing Country, and Time zone to the **MCC's own country** (Philippines, in this case) unless explicitly overridden at every step - check this at every screen, not just once.
- The wizard defaults to **Performance Max** as campaign type when the goal is "Purchases" - if Search is wanted, you must explicitly click "view other campaign types" and select Search.
- **Google Ads blocks sending user invites until the account has a payments profile** (even an incomplete/shell one) - confirmed by testing 3 different invite emails, all failing identically ("An error occurred. Please try again later.") until a payments profile existed.
- Kim's email (kim@alphalewissigns.com.au) is Microsoft/Outlook-hosted, not Google Workspace - she and Nic will likely need to go through Google's "create account using my current email" flow to accept the Ads invite, not sign in directly.

## Completed

- **Sep 17 2026:** Built GA4 property and GTM container ahead of Google Ads account access going live (these don't depend on Kim/Nic accepting the Ads invite). GA4: account "Signee", property "Signee - signeesigns.com.au", Australia/Melbourne time zone, AUD currency, Business & Industrial category, objectives Generate leads + Drive sales, web data stream "Signee Website" (stream ID 15792513870, Measurement ID G-16K9H45R2V), Enhanced measurement on. GTM: account "Signee" (Australia), container "signeesigns.com.au" (GTM-NFD4DZ2H, Web), GA4 Configuration tag built pointing to G-16K9H45R2V firing on Initialization - All Pages, published as Version 2. Both built under jddbartolome@gmail.com to mirror the existing Ads MCC pattern; Kim and Nic can be added as Administrators on both once they have Google identities tied to their business emails (same friction as the pending Ads invite - kim@/nic@alphalewissigns.com.au are Outlook-hosted, not Google Workspace). Next tracking step: get Shopify edit access from Nic to paste the GTM snippet into the site's `<head>`/`<body>`.
- **Sep 17 2026:** Kim confirmed (verbally, per Josette) she's working through the Sep 16 Ads invite/billing email - that email does not cover Shopify access. Drafted a follow-up (not sent) to kim@/nic@ flagging the separate Shopify collaborator/theme access need for the GTM install, framed as no rush until Ads access clears. Waiting on reply.
- **Sep 17 2026:** Kim hit the predicted "not a Google Workspace email" friction while trying to accept the Ads invite (WhatsApp screenshot 10:05-10:06 AM: personal email rejected as not matching the invite, then signing in directly with kim@alphalewissigns.com.au loops back to the sign-in page). This confirms the Sep 16 "Lessons learned" prediction. Fix relayed to Josette to send Kim: use accounts.google.com/signup > "Use my current email address instead" to create a Google Account on kim@alphalewissigns.com.au (not a new @gmail.com), verify via the code sent to that inbox, then re-click Accept on the original invite. Same will apply for Nic. Not yet confirmed resolved, waiting on Kim to try it.
- **Sep 17 2026:** Wrote the full campaign strategy document (`Google Ads Tasks/campaign-strategy.md`), grounded in the July 2026 competitor/keyword research, the Sep 15 website audit, and today's GA4/GTM build. Covers competitive landscape, keyword and demand data (flagged as needing a re-pull, it's 2 months old), pricing position (flagged as stale, needs Section 3's re-verification before ad copy is written), the hybrid product-type + use-case campaign structure, negative keyword categories, audience/geo targeting, bidding strategy progression, budget phasing (Stage 1 $1,200/month Search, Stage 2 $2,000 to $3,500/month adding Shopping), ad extensions plan, the measurement plan tying to today's tracking build, and a full risk/open-items list. This is a planning document, not yet built in the live account, several sections explicitly call out what's still blocked (tracking not live, pricing not re-verified, Shopify access pending).
- **Sep 15 2026:** Deal closed, Josette handling Google Ads. Pre-launch website audit done (website-audit-sep15-2026.md).
- **Sep 16 2026:** Google Ads account created (Signee, CID 715-970-4117) under JDD Bartolome MCC. Search campaign draft built: goal = Purchases (manual conversion setup, not URL-based), Locations = Australia, keywords/search themes populated. Admin invites sent to Kim and Nic. Step-by-step instructional email sent to Kim covering invite acceptance + billing setup.
- **Sep 16 2026:** Local project folder set up (`Desktop/Personal/Alpha Lewis Signs`, cloned from GitHub). Confirmed no GTM/GA4/Ads tag/Meta pixel/GSC verification live on site (see "Immediate - Outstanding" for detail). Built three session skills: `/signee-startup`, `/signee-wrapup`, `/signee-weekly`. Reorganized tracker into `Google Ads Tasks/` to mirror the Kenny Fuels project structure. Pulled Signee's real brand identity from signeesigns.com.au (cream/brown/sky-blue/lavender palette, Poppins typeface, logo colors) and built the first weekly report as a branded HTML page (`weekly-reports/week-sep-14-18-2026.html`), live at the repo's GitHub Pages site. All pushed to `jdbartolome0023/alpha-lewis-signs`.
- **Sep 16 2026:** Redesigned the weekly report after visually reviewing the live site (not just its CSS values) - real design uses bold full-bleed color-blocked sections (cream/lavender/dark brown), not small accent pills. Expanded the report's "Next Up" into the full 5-phase ground-up checklist (Research through Launch & Monitor), and restructured this tracker's outstanding items into the same 5 phases so the two stay in sync. Fixed a layout bug where the top marquee strip rendered as a full-height sidebar instead of a horizontal bar.
- **Sep 16 2026:** Fixed slash-command discoverability - `/signee-startup`, `/signee-wrapup`, `/signee-weekly` were pushed to the repo but not actually invocable, since Claude Code only discovers commands from `Desktop/Personal/.claude/commands/` (session-level) and `~/.claude/commands/` (global), not arbitrary project subfolders. Copied all three there too, matching exactly how `kf-startup`/`kf-wrapup` are set up for Kenny Fuels. Confirmed working.
