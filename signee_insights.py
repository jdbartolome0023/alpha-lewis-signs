#!/usr/bin/env python3
"""Signee campaign insights (read only). Run:

cd "/Users/josette/Desktop/Personal/Alpha Lewis Signs"
"/Users/josette/Desktop/Personal/Google Ads MCP/google_ads_mcp-main/.venv/bin/python3" signee_insights.py

Uses only the Signee credentials:
  Google Ads: ~/.google-ads-mcp-signee/google-ads.yaml (customer 966-837-5188)
  GA4: ~/.ga4-mcp-signee/token.json (property 553528757)
Makes no changes to any account.
"""
import json
import os
from datetime import date, timedelta

CUSTOMER_ID = "9668375188"
GA4_PROPERTY = "553528757"
START = "2026-10-07"  # launch day
TODAY = date.today()
LAST7 = (TODAY - timedelta(days=7)).isoformat()
YDAY = (TODAY - timedelta(days=1)).isoformat()


def money(micros):
    return f"A${micros / 1_000_000:,.2f}"


def pct(x):
    return f"{x * 100:.1f}%"


def heading(text):
    print(f"\n=== {text} ===")


def ads_section():
    from google.ads.googleads.client import GoogleAdsClient

    client = GoogleAdsClient.load_from_storage(
        os.path.expanduser("~/.google-ads-mcp-signee/google-ads.yaml")
    )
    svc = client.get_service("GoogleAdsService")

    def run(q):
        return list(svc.search(customer_id=CUSTOMER_ID, query=q))

    heading(f"Campaigns, {START} to {TODAY}")
    rows = run(f"""
        SELECT campaign.name, campaign.status, campaign_budget.amount_micros,
               metrics.impressions, metrics.clicks, metrics.cost_micros,
               metrics.conversions, metrics.conversions_value,
               metrics.search_impression_share,
               metrics.search_rank_lost_impression_share,
               metrics.search_budget_lost_impression_share
        FROM campaign
        WHERE segments.date BETWEEN '{START}' AND '{TODAY.isoformat()}'
          AND campaign.status != 'REMOVED'
    """)
    for r in rows:
        m = r.metrics
        ctr = m.clicks / m.impressions if m.impressions else 0
        cpc = m.cost_micros / m.clicks if m.clicks else 0
        print(f"{r.campaign.name} [{r.campaign.status.name}] budget {money(r.campaign_budget.amount_micros)}/day")
        print(f"  impressions {m.impressions:,.0f}, clicks {m.clicks:,.0f}, CTR {pct(ctr)}, "
              f"cost {money(m.cost_micros)}, avg CPC {money(cpc)}")
        print(f"  conversions {m.conversions:.1f}, value A${m.conversions_value:,.2f}")
        if m.search_impression_share:
            print(f"  impression share {pct(m.search_impression_share)}, lost to rank "
                  f"{pct(m.search_rank_lost_impression_share)}, lost to budget "
                  f"{pct(m.search_budget_lost_impression_share)}")

    heading(f"Daily, last 7 days ({LAST7} to {YDAY})")
    rows = run(f"""
        SELECT segments.date, campaign.name, metrics.clicks, metrics.cost_micros,
               metrics.impressions, metrics.conversions
        FROM campaign
        WHERE segments.date BETWEEN '{LAST7}' AND '{TODAY.isoformat()}'
          AND campaign.status != 'REMOVED'
        ORDER BY segments.date DESC
    """)
    for r in rows:
        m = r.metrics
        print(f"{r.segments.date}  {r.campaign.name:<22} clicks {m.clicks:>4.0f}  "
              f"impr {m.impressions:>5.0f}  cost {money(m.cost_micros):>9}  conv {m.conversions:.1f}")

    heading("Search ad groups since launch")
    rows = run(f"""
        SELECT ad_group.name, ad_group.status, metrics.impressions, metrics.clicks,
               metrics.cost_micros, metrics.conversions
        FROM ad_group
        WHERE segments.date BETWEEN '{START}' AND '{TODAY.isoformat()}'
          AND campaign.advertising_channel_type = 'SEARCH'
          AND ad_group.status != 'REMOVED'
        ORDER BY metrics.cost_micros DESC
    """)
    for r in rows:
        m = r.metrics
        ctr = m.clicks / m.impressions if m.impressions else 0
        print(f"{r.ad_group.name:<28} [{r.ad_group.status.name}] impr {m.impressions:>5.0f} "
              f"clicks {m.clicks:>4.0f} CTR {pct(ctr):>6} cost {money(m.cost_micros):>9} conv {m.conversions:.1f}")

    heading("Shopping by product since launch")
    try:
        rows = run(f"""
            SELECT segments.product_title, metrics.impressions, metrics.clicks,
                   metrics.cost_micros, metrics.conversions
            FROM shopping_performance_view
            WHERE segments.date BETWEEN '{START}' AND '{TODAY.isoformat()}'
            ORDER BY metrics.clicks DESC
        """)
        for r in rows:
            m = r.metrics
            ctr = m.clicks / m.impressions if m.impressions else 0
            print(f"{r.segments.product_title[:40]:<40} impr {m.impressions:>5.0f} clicks {m.clicks:>3.0f} "
                  f"CTR {pct(ctr):>5} cost {money(m.cost_micros):>8} conv {m.conversions:.1f}")
    except Exception as e:
        print("Shopping view not read:", str(e)[:200])

    heading("Device split (Search) since launch")
    rows = run(f"""
        SELECT segments.device, metrics.clicks, metrics.cost_micros, metrics.conversions
        FROM campaign
        WHERE segments.date BETWEEN '{START}' AND '{TODAY.isoformat()}'
          AND campaign.advertising_channel_type = 'SEARCH'
    """)
    for r in rows:
        m = r.metrics
        print(f"{r.segments.device.name:<10} clicks {m.clicks:>4.0f}  cost {money(m.cost_micros):>9}  conv {m.conversions:.1f}")

    heading("Top search terms by cost, last 7 days")
    rows = run(f"""
        SELECT search_term_view.search_term, metrics.clicks, metrics.cost_micros, metrics.conversions
        FROM search_term_view
        WHERE segments.date BETWEEN '{LAST7}' AND '{TODAY.isoformat()}'
        ORDER BY metrics.cost_micros DESC
        LIMIT 15
    """)
    for r in rows:
        m = r.metrics
        print(f"{r.search_term_view.search_term[:45]:<45} clicks {m.clicks:>3.0f} cost {money(m.cost_micros):>8} conv {m.conversions:.1f}")


def ga4_section():
    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.analytics.data_v1beta.types import (
        DateRange, Dimension, Filter, FilterExpression, FilterExpressionList, Metric, RunReportRequest,
    )
    from google.oauth2.credentials import Credentials

    with open(os.path.expanduser("~/.ga4-mcp-signee/token.json")) as f:
        t = json.load(f)
    creds = Credentials(
        token=None, refresh_token=t["refresh_token"], client_id=t["client_id"],
        client_secret=t["client_secret"], token_uri=t.get("token_uri", "https://oauth2.googleapis.com/token"),
    )
    client = BetaAnalyticsDataClient(credentials=creds)

    paid = FilterExpression(and_group=FilterExpressionList(expressions=[
        FilterExpression(filter=Filter(field_name="sessionSource", string_filter=Filter.StringFilter(value="google"))),
        FilterExpression(filter=Filter(field_name="sessionMedium", string_filter=Filter.StringFilter(value="cpc"))),
    ]))

    def report(dims, mets, start, end=TODAY.isoformat(), flt=paid, limit=15):
        return client.run_report(RunReportRequest(
            property=f"properties/{GA4_PROPERTY}",
            date_ranges=[DateRange(start_date=start, end_date=end)],
            dimensions=[Dimension(name=d) for d in dims],
            metrics=[Metric(name=m) for m in mets],
            dimension_filter=flt, limit=limit,
        ))

    heading(f"GA4 paid (google / cpc) funnel events, {START} to today")
    keep = {"page_view", "view_item", "add_to_cart", "begin_checkout", "purchase", "form_start", "form_submit"}
    for r in report(["eventName"], ["eventCount", "totalUsers"], START, limit=60).rows:
        if r.dimension_values[0].value in keep:
            print(f"{r.dimension_values[0].value:<15} events {r.metric_values[0].value:>5}  users {r.metric_values[1].value:>5}")

    heading(f"GA4 paid sessions by device, last 7 days")
    for r in report(["deviceCategory"], ["sessions", "engagementRate", "averageSessionDuration"], LAST7).rows:
        print(f"{r.dimension_values[0].value:<10} sessions {r.metric_values[0].value:>4}  "
              f"engaged {float(r.metric_values[1].value) * 100:.0f}%  avg {float(r.metric_values[2].value):.0f}s")

    heading("GA4 paid landing pages, last 7 days")
    for r in report(["landingPage"], ["sessions", "engagementRate"], LAST7).rows:
        print(f"{r.dimension_values[0].value[:50]:<50} sessions {r.metric_values[0].value:>4}  "
              f"engaged {float(r.metric_values[1].value) * 100:.0f}%")

    heading("GA4 every purchase since 28 Oct (any source), for the attribution check")
    rep = client.run_report(RunReportRequest(
        property=f"properties/{GA4_PROPERTY}",
        date_ranges=[DateRange(start_date="2026-10-28", end_date=TODAY.isoformat())],
        dimensions=[Dimension(name="transactionId"), Dimension(name="sessionSource"), Dimension(name="sessionMedium")],
        metrics=[Metric(name="purchaseRevenue")],
        dimension_filter=FilterExpression(filter=Filter(
            field_name="eventName", string_filter=Filter.StringFilter(value="purchase"))),
    ))
    if not rep.rows:
        print("No purchases.")
    for r in rep.rows:
        d = [v.value for v in r.dimension_values]
        print(f"order {d[0]}  {d[1]} / {d[2]}  A${float(r.metric_values[0].value):,.2f}")


if __name__ == "__main__":
    for name, fn in (("Google Ads", ads_section), ("GA4", ga4_section)):
        try:
            fn()
        except Exception as e:
            print(f"\n!!! {name} section failed: {str(e)[:600]}")
            print("If this says invalid_grant or unauthorized, the token needs renewing (expires about 9 Nov).")
