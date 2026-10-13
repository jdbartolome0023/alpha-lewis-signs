// Signee: GA4 funnel events (view_item, add_to_cart, begin_checkout)
// Paste into Shopify Admin > Settings > Customer events > Add custom pixel (name: "GA4 Funnel Events").
// This is a SEPARATE pixel. Do not edit or remove the existing "GA4 Purchase Tracking" pixel.
// Permission: Required, Analytics only (same as the purchase pixel).
// Replace PASTE_API_SECRET_HERE with the same Measurement Protocol API secret the purchase pixel uses.
// Do not commit the real secret to the repo.

const MEASUREMENT_ID = 'G-8LB953WBW4';
const API_SECRET = 'PASTE_API_SECRET_HERE';
const ENDPOINT = `https://www.google-analytics.com/mp/collect?measurement_id=${MEASUREMENT_ID}&api_secret=${API_SECRET}`;
const COOKIE_SUFFIX = MEASUREMENT_ID.replace('G-', '');

async function getClientId() {
  try {
    const ga = await browser.cookie.get('_ga');
    if (ga) {
      const parts = ga.split('.');
      if (parts.length >= 4) return parts[2] + '.' + parts[3];
    }
  } catch (e) {}
  return String(Math.floor(Math.random() * 1e10)) + '.' + String(Math.floor(Date.now() / 1000));
}

async function getSessionId() {
  try {
    const c = await browser.cookie.get('_ga_' + COOKIE_SUFFIX);
    if (!c) return null;
    if (c.startsWith('GS1')) return Number(c.split('.')[2]) || null;
    const m = c.match(/s(\d+)/);
    return m ? Number(m[1]) : null;
  } catch (e) {
    return null;
  }
}

async function send(name, params) {
  try {
    const clientId = await getClientId();
    const sessionId = await getSessionId();
    const p = Object.assign({ engagement_time_msec: 100 }, params);
    if (sessionId) p.session_id = sessionId;
    const body = JSON.stringify({ client_id: clientId, events: [{ name, params: p }] });
    browser.sendBeacon(ENDPOINT, body);
  } catch (e) {}
}

analytics.subscribe('product_viewed', async (event) => {
  const v = event.data.productVariant;
  if (!v) return;
  await send('view_item', {
    currency: v.price.currencyCode,
    value: v.price.amount,
    items: [{ item_id: v.product.id, item_name: v.product.title, price: v.price.amount, quantity: 1 }],
  });
});

analytics.subscribe('product_added_to_cart', async (event) => {
  const line = event.data.cartLine;
  if (!line) return;
  const m = line.merchandise;
  await send('add_to_cart', {
    currency: m.price.currencyCode,
    value: m.price.amount * line.quantity,
    items: [{ item_id: m.product.id, item_name: m.product.title, price: m.price.amount, quantity: line.quantity }],
  });
});

analytics.subscribe('checkout_started', async (event) => {
  const c = event.data.checkout;
  if (!c) return;
  await send('begin_checkout', {
    currency: c.currencyCode,
    value: c.totalPrice.amount,
    items: c.lineItems.map((li) => ({
      item_id: li.variant && li.variant.product ? li.variant.product.id : undefined,
      item_name: li.title,
      price: li.variant ? li.variant.price.amount : undefined,
      quantity: li.quantity,
    })),
  });
});
