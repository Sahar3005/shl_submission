import json

with open("data/shl_product_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

print(catalog[0].keys())