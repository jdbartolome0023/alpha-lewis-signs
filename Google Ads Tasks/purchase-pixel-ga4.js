// Signee: GA4 Purchase Tracking (corrected Oct 19 2026)
// Paste into Shopify Admin > Settings > Customer events > Custom pixels > "GA4 Purchase Tracking" (replace the existing code).
// Permission: Required, Analytics only.
// Replace PASTE_API_SECRET_HERE with the Measurement Protocol API secret. Do not commit the real secret to the repo.
//
// Changes vs the version live before Oct 19 2026:
// - Sends session_id (from the _ga_ cookie) so GA4 ties the purchase to the session that carried the ad click.
// - Adds engagement_time_msec.
// - Adds gclid (from the _gcl_aw cookie) as a diagnostic custom parameter.
// - item_id now uses product id, matching the funnel pixel.
// - Removed the pixel_checkout_fired / pixel_purchase_sent debug pings (each created a junk random user).

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
  return crypto.randomUUID();
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

async function getGclid() {
  try {
    const c = await browser.cookie.get('_gcl_aw');
    if (!c) return null;
    const parts = c.split('.');
    return parts.length >= 3 ? parts.slice(2).join('.') : null;
  } catch (e) {
    return null;
  }
}

analytics.subscribe('checkout_completed', async (event) => {
  try {
    const checkout = event.data.checkout;
    const clientId = await getClientId();
    const sessionId = await getSessionId();
    const gclid = await getGclid();

    const params = {
      engagement_time_msec: 100,
      transaction_id: checkout.order.id,
      value: checkout.totalPrice.amount,
      currency: checkout.totalPrice.currencyCode,
      tax: checkout.totalTax?.amount || 0,
      shipping: checkout.shippingLine?.price?.amount || 0,
      items: checkout.lineItems.map((item) => ({
        item_id: item.variant && item.variant.product ? item.variant.product.id : String(item.variant.id),
        item_name: item.variant.product.title,
        price: item.variant.price.amount,
        quantity: item.quantity
      }))
    };
    if (sessionId) params.session_id = sessionId;
    if (gclid) params.gclid = gclid;

    browser.sendBeacon(ENDPOINT, JSON.stringify({
      client_id: clientId,
      events: [{ name: 'purchase', params }]
    }));
  } catch (e) {
    browser.sendBeacon(ENDPOINT, JSON.stringify({
      client_id: crypto.randomUUID(),
      events: [{ name: 'pixel_purchase_error', params: { msg: String(e).slice(0, 90) } }]
    }));
  }
});
