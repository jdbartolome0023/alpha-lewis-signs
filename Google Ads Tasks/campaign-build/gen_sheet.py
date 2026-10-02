import io,contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import build as b
SL=[('Cafe & Coffee Shop Signs','A-frames, blade and pole signs','Free shipping Australia-wide','/collections/cafe-coffee-shop-signage'),
    ('Restaurant & Bar Signs','Signs for hospitality venues','Free shipping Australia-wide','/collections/restaurant-bar-signage'),
    ('Retail Store Signs','Blade signs, A-frames, door signs','Free shipping Australia-wide','/collections/retail-store-signage'),
    ('Salon & Studio Signs','Door signs and blade signs','Free shipping Australia-wide','/collections/salon-studio-signage'),
    ('Hotel & Accommodation','Lobby, entrance and footpath','Free shipping Australia-wide','/collections/hotel-accommodation-signage'),
    ('FAQs','Lead times, discounts, artwork','Questions answered','/pages/frequently-asked-questions')]
CO=['Free Aus-Wide Shipping','Powdercoated Aluminium','Add Your Logo in Vinyl','Volume Discounts','No Minimum Order','Dispatched From Melbourne']
for t,d1,d2,u in SL: assert len(t)<=25 and len(d1)<=35 and len(d2)<=35,(t,d1,d2)
for c in CO: assert len(c)<=25,c
o=[]
w=o.append
w("# Signee Search AU: copy-and-paste sheet (built 2 Oct 2026)\n")
w("Do not enable the campaign until a test purchase lands in GA4. Prices in headlines were verified on 2 Oct 2026 (see `../pricing-verified-oct-2-2026.md`); re-check before launch.\n")
w("## 1. Campaign settings\n- Account: Signee 966-837-5188 (check top-left before every change)\n- Type: Search. Goal: Sales / Purchases. Name: **Signee Search AU**\n- Networks: tick Google search only. Untick Search Partners and Display Network.\n- Locations: Australia (Presence: people in or regularly in the location, not 'interest').\n- Language: English\n- Budget: $40.00 per day\n- Bidding: Maximize conversions (no target CPA)\n- EU political ads: No\n- Status after creating: **Paused**\n")
w("## 2. Ad groups (create 8). For each: keywords, then the ad.\n")
for g in b.G:
    w(f"### {g['name']}\n- Final URL: {g['url']}\n- Display path: /{g['p'][0]}\n")
    w("Keywords (paste all lines; phrase and exact are both included):\n```")
    for k in g['kw']: w(f'"{k}"')
    for k in g['kw']: w(f'[{k}]')
    w("```")
    hs=g['h']+b.common_h; ds=g['d']+b.common_d
    w("Headlines (paste one per box):\n```"); [w(x) for x in hs]; w("```")
    w("Descriptions:\n```"); [w(x) for x in ds]; w("```\n")
w("## 3. Campaign negative keywords (paste in as phrase match)\n```")
for n in b.NEG: w(f'"{n}"')
w("```\nThe last two (`george and willy`, `piece of sign`) exclude competitor brand searches. Delete them if Kim wants to bid on competitors.\n")
w("## 4. Sitelinks (campaign level; text / description 1 / description 2 / URL)\n")
for t,d1,d2,u in SL: w(f"- {t} | {d1} | {d2} | https://signeesigns.com.au{u}")
w("\n## 5. Callouts\n"); [w(f"- {c}") for c in CO]
w("\n## 6. Structured snippet\n- Header: Types\n- Values: A-Frame Signs, Blade Signs, Illuminated Signs, Indoor Signage\n")
open('copy-paste-sheet.md','w').write('\n'.join(o))
print('ok',len('\n'.join(o)))
