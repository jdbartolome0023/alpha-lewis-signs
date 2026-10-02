import csv
B='https://signeesigns.com.au'
C='Signee Search AU'
common_h=['Signee Business Signs','Powdercoated Aluminium Signs','Add Your Logo at Checkout','Order Blank or With Artwork','Free Shipping Australia-Wide']
common_d=['Order blank, or add your logo at checkout and we apply it in vinyl before it ships.',
          'Powdercoated aluminium built to hold up outdoors. Shop the full Signee range online.']
G=[
 dict(name='A-Frame & Sidewalk Signs',url=B+'/collections/a-frame-signs',p=('a-frame-signs',''),
  kw=['a frame sign','sandwich board sign','sidewalk sign','footpath sign','a frame sign for business','aluminium a frame sign','outdoor a frame sign'],
  h=['A-Frame Signs From $259','Walter A-Frame From $449','Winnie Acrylic A-Frame $319','Footpath Signs for Business','Swap the Vinyl, Keep the Frame'],
  d=['Walter: full aluminium A-frame, black or white. Add vinyl graphics at checkout.','Winnie: vivid coloured acrylic A-frame in five colours. Double-sided panels.']),
 dict(name='Wall & Hanging Signs',url=B+'/collections/blade-signs',p=('blade-signs',''),
  kw=['blade sign','hanging shop sign','projecting wall sign','business wall sign','round blade sign','square blade sign','wall mounted business sign','shop sign'],
  h=['Blade Signs From $159','Round & Square Blade Signs','Wall-Bracket Mounted Signs','Flossy Round Blade Sign $229','Theodore Square Blade $229'],
  d=['Round or square blade signs in black or white. Sizes from 200mm to 500mm.','Finished to hold up in Australian sun and rain. Arrives ready to go up.']),
 dict(name='Illuminated Signs',url=B+'/collections/illuminated-signs',p=('illuminated',''),
  kw=['illuminated sign','light up business sign','lightbox sign','led lightbox sign','backlit sign','illuminated business sign'],
  h=['Illuminated Sign From $329','Lottie Illuminated Lightbox','4500K LED, Even Lighting','Plug-In Power, No Electrician','Light Up Your Business Sign'],
  d=['Lottie: 3mm opal acrylic face, aluminium frame and a 4500K LED panel.','Five-sided illumination with no hot spots. Keyhole bracket wall mounting.']),
 dict(name='Cafe & Restaurant Signage',url=B+'/collections/cafe-coffee-shop-signage',p=('cafe-signage',''),
  kw=['cafe signage','cafe sign','coffee shop sign','restaurant signage','restaurant sign','bar signage','cafe a frame sign'],
  h=['Cafe & Restaurant Signs','Signs for Cafes & Coffee Shops','Signs for Restaurants & Bars','Open/Closed Sign From $119','A-Frames, Blade & Pole Signs'],
  d=['Footpath A-frames, wall blade signs and counter signs made for hospitality venues.','Shop the range online, with your logo applied in vinyl if you want it.']),
 dict(name='Retail & Salon Signage',url=B+'/collections/retail-store-signage',p=('retail-signage',''),
  kw=['shop signage','retail store signage','retail shop sign','salon sign','salon signage','studio signage','boutique shop sign'],
  h=['Shop & Retail Signage','Salon & Studio Signs','Signs for Shopfronts','Blade Signs From $159','Door Signs From $159'],
  d=['Blade signs, A-frames and door signs for shopfronts, salons and studios.','Order blank or add your logo at checkout. Shop the full range online.']),
 dict(name='Hotel & Accommodation Signage',url=B+'/collections/hotel-accommodation-signage',p=('hotel-signage',''),
  kw=['hotel signage','accommodation signage','hotel lobby sign','boutique hotel sign','hotel sign'],
  h=['Hotel & Accommodation Signs','Signs for Boutique Hotels','Hotel Lobby Signage','Mabel Indoor A-Frame $259','Walter A-Frame From $449'],
  d=['Refined indoor and outdoor signs for hotel lobbies, entrances and footpaths.','Slim indoor A-frames, freestanding pole signs and premium aluminium A-frames.']),
 dict(name='General Business Signage',url=B+'/',p=('business-signs',''),
  kw=['business signage','outdoor business sign','small business signage','indoor signage','custom shop sign','custom business sign'],
  h=['Business Signs From $119','Signs for Small Business','Shop the Signee Range','10 Signs, Black or White','Outdoor & Indoor Signage'],
  d=['Open/closed signs, blade signs, A-frames, pole signs and a lightbox sign.','Order blank or add your logo at checkout. Shop the full Signee range online.']),
 dict(name='Open Closed Sign',url=B+'/products/henry',p=('open-closed',''),
  kw=['open closed sign','open sign for shop window','open closed sign for door','shop window open closed sign','business open closed sign'],
  h=['Henry Open/Closed Sign $119','Slide to Switch Open/Closed','No Drilling, Tape Mount','Black or White Open Sign','Open/Closed Sign for Doors'],
  d=['Henry: powdercoated aluminium open/closed sign with a sliding panel.','Mounts to glass doors, windows or walls with tape. No drilling needed.']),
]
NEG=['sign writer','signwriting services','sign installation','sign installer near me','commercial signage company','vehicle wraps','vehicle signage','council signage','regulatory signage','safety signage','sign maker near me','custom neon sign installer',
 'how to make a sign','diy sign','free sign template','sign clipart','sign stencil','print your own sign','sign design software',
 'sign making jobs','sign painter salary','signage company careers',
 'for sale sign','real estate sign','political sign','yard sale sign','parking sign','road sign','traffic sign','license plate sign','name plate engraving',
 'sign meaning','sign language','astrology sign','zodiac sign','sign in','sign up',
 'george and willy','piece of sign']
# validate
bad=[]
for g in G:
    hs=common_h+g['h']
    ds=g['d']+common_d
    if len(hs)>15: bad.append((g['name'],'headlines>15'))
    for x in hs:
        if len(x)>30: bad.append((g['name'],'H',x,len(x)))
    for x in ds:
        if len(x)>90: bad.append((g['name'],'D',x,len(x)))
    for x in g['p']:
        if len(x)>15: bad.append((g['name'],'path',x))
    assert '—' not in str(g)
print('problems:',bad)
cols=['Campaign','Campaign Type','Networks','Budget','Budget type','Bid Strategy Type','Campaign Status','EU political ads','Languages','Location','Ad Group','Ad Group Status','Keyword','Criterion Type','Ad type','Final URL','Path 1','Path 2']+[f'Headline {i}' for i in range(1,16)]+[f'Description {i}' for i in range(1,5)]+['Status']
rows=[]
def r(**k): rows.append({c:k.get(c,'') for c in cols})
r(**{'Campaign':C,'Campaign Type':'Search','Networks':'Google search','Budget':'40.00','Budget type':'Daily','Bid Strategy Type':'Maximize conversions','Campaign Status':'Paused','EU political ads':"Doesn't have EU political ads",'Languages':'en'})
r(**{'Campaign':C,'Location':'Australia'})
for n in NEG: r(**{'Campaign':C,'Keyword':n,'Criterion Type':'Negative Phrase'})
for g in G:
    r(**{'Campaign':C,'Ad Group':g['name'],'Ad Group Status':'Enabled'})
    for k in g['kw']:
        r(**{'Campaign':C,'Ad Group':g['name'],'Keyword':k,'Criterion Type':'Phrase'})
        r(**{'Campaign':C,'Ad Group':g['name'],'Keyword':k,'Criterion Type':'Exact'})
    hs=g['h']+common_h; ds=g['d']+common_d
    row={'Campaign':C,'Ad Group':g['name'],'Ad type':'Responsive search ad','Final URL':g['url'],'Path 1':g['p'][0],'Path 2':g['p'][1],'Status':'Enabled'}
    for i,x in enumerate(hs,1): row[f'Headline {i}']=x
    for i,x in enumerate(ds,1): row[f'Description {i}']=x
    r(**row)
with open('signee-search-au-upload.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=cols); w.writeheader(); w.writerows(rows)
print(len(rows),'rows; ad groups',len(G),'keywords',sum(len(g['kw']) for g in G),'negatives',len(NEG))
