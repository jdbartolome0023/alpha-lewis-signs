# Signee: Merchant Center walkthrough with Kim (Wed Oct 14 2026)

Purpose: Kim creates the Signee Merchant Center on her own login and adds Josette as administrator, so Josette can do everything else herself. Same pattern as the Google Ads account (Sep 23). Menu names below are from memory of Google's current layout and may differ slightly on screen: follow the closest match.

Rules for the call:
- Do NOT mention the Shopping budget split (Search about A$28/day, Shopping about A$12/day). Josette's rule: tell them after Shopping is set up.
- Do NOT use the Designer Blooms Canada Merchant Center (another client).
- Never remove the last administrator on the account.
- Kim does the account creation herself on her screen; Josette only guides. Josette never asks for Kim's password or verification codes.

## Before the call (Josette)
1. Book the time with Kim on WhatsApp (see message below). Confirm the time zone in the message (Sydney vs Manila).
2. Have ready: `jddbartolome@gmail.com` (the address to add as administrator), the business details below, and `shopping-feed-oct-13-2026.tsv`.
3. Check you are logged in to the Shopify store `signee-2` with theme edit access (you need it for the verification tag).
4. Open `https://merchants.google.com/` in a different Chrome profile from Kim's share, so you do not mix accounts.

Business details Kim will be asked for:
- Business name: Signee
- Country: Australia
- Website: https://signeesigns.com.au/
- Address: 242 Dryburgh Street, North Melbourne VIC 3051
- Phone: 03 9329 1244 (Alpha Lewis Signs main line). Google may ask to verify by call or text: that goes to whoever answers, so warn Kim first.
- Contact email: kim@alphalewissigns.com.au

## On the call, Kim's screen (about 10 minutes)
1. Kim signs in to Google as `kim@alphalewissigns.com.au` (the Google account created Sep 17, Microsoft-hosted email).
2. Kim opens `https://merchants.google.com/` and clicks **Get started** (or **Sign up**).
3. Business name: type `Signee`. Country: Australia. Continue.
4. Enter the website URL `https://signeesigns.com.au/` and the address and phone above when asked. Accept the terms.
5. **Add Josette as administrator first, before anything else:** click the gear icon (Settings and tools) > **People and access** > **Add person** > type `jddbartolome@gmail.com` > access level **Admin** > **Add** / **Send invitation**.
6. Josette checks the invitation arrived in jddbartolome Gmail and accepts it in the other Chrome profile. Expected result: Josette sees the Signee account in her account list.
7. Stop here. Everything else Josette can do alone.

## After the call, Josette alone
Follow `shopping-setup-checklist.md` from step 2 (the Designer Blooms creation in step 1 is superseded):
1. Verify and claim the website: Settings > Business information > Website > Verify and claim > HTML tag. Paste the meta tag in `layout/theme.liquid` inside `<head>`, save, click Verify.
2. Shipping: one service, Australia, Standard, free, all products. Check handling time against the live policy first (Walter about 2 weeks, others 1 to 2 business days).
3. Upload the feed `shopping-feed-oct-13-2026.tsv`. Confirm `google_product_category` in the picker first.
4. Link to Google Ads 966-837-5188 (Josette is admin there, so she can send and accept the link). The old unexplained link to 553528757 gets reviewed afterwards.
5. Wait for product approval (days to about 2 weeks), then build the paused Shopping campaign.

## Optional talking points with Kim (only if time, none need a decision)
- Bidding was changed to Maximize clicks on Oct 8 (Nic knows about the Call asset and brand bidding answers; the bidding change itself is not yet told).
- Do not discuss the budget split.

## WhatsApp message to Kim (draft, Josette sends)
Hi Kim, thanks for offering to do the walkthrough. It will take about 10 minutes. I need you to create a free Google Merchant Center account for Signee (this is what lets the signs show up with photos and prices in Google Shopping), and add me as an administrator so I can do the rest myself. Does [time, with Sydney and Manila times] work for you tomorrow? Please have your laptop and the kim@alphalewissigns.com.au login ready. Your phone may get a verification code, which is normal. I will never ask you to read me a code or a password.
