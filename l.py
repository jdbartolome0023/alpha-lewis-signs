from google.ads.googleads.client import GoogleAdsClient
c=GoogleAdsClient.load_from_storage("/Users/josette/.google-ads-mcp-signee/google-ads.yaml",version="v22")
s=c.get_service("GoogleAdsService");cid="9668375188"
for q in ["select product_link.merchant_center.merchant_center_id,product_link.resource_name from product_link","select customer.id,customer.conversion_tracking_setting.conversion_tracking_status from customer"]:
    try:
        for r in s.search(customer_id=cid,query=q): print(r)
    except Exception as e: print("ERR",str(e)[:300])
