import json

CATALOG_PATH = "data/shl_product_catalog.json"

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    catalog = json.load(f)


def search(query, top_k=10):
    """
    Lightweight search for Render Free.
    Uses keyword scoring instead of loading SentenceTransformer.
    """

    query = query.lower()

    scored = []

    for item in catalog:

        text = (
            item.get("name", "")
            + " "
            + item.get("description", "")
            + " "
            + " ".join(item.get("keys", []))
        ).lower()

        score = 0

        for word in query.split():
            if word in text:
                score += 1

        scored.append((score, item))

    scored.sort(key=lambda x: x[0], reverse=True)

    results = []

    for _, item in scored[:top_k]:
        results.append({
            "entity_id": item.get("entity_id"),
            "name": item.get("name"),
            "url": item.get("link"),
            "description": item.get("description", ""),
            "job_levels": item.get("job_levels", []),
            "languages": item.get("languages", []),
            "duration": item.get("duration"),
            "remote": item.get("remote"),
            "adaptive": item.get("adaptive"),
            "status": item.get("status"),
            "keywords": item.get("keys", [])
        })

    return results