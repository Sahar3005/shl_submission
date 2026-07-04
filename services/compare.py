import json

CATALOG_PATH = "data/shl_product_catalog.json"

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    catalog = json.load(f)


def find_assessment(name):

    name = name.lower()

    # direct match
    for item in catalog:
        if name in item["name"].lower():
            return item

    # keyword match
    for item in catalog:
        keywords = " ".join(item.get("keys", [])).lower()
        if name in keywords:
            return item

    return None


def compare(name1, name2):

    a = find_assessment(name1)
    b = find_assessment(name2)

    if a is None or b is None:
        return {
            "reply": "Sorry, I could not find one or both assessments in the SHL catalog."
        }

    return {
        "reply": f"""
Comparison

Assessment 1
-------------
Name: {a['name']}
Duration: {a.get('duration', 'N/A')}
Remote: {a.get('remote', 'N/A')}
Description:
{a.get('description', '')}

====================================

Assessment 2
-------------
Name: {b['name']}
Duration: {b.get('duration', 'N/A')}
Remote: {b.get('remote', 'N/A')}
Description:
{b.get('description', '')}
"""
    }