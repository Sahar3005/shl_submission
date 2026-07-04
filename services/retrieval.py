# Search logic will come here
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

CATALOG_PATH = "data/shl_product_catalog.json"
INDEX_PATH = "data/faiss.index"

model = SentenceTransformer("all-MiniLM-L6-v2")

# Load catalog
with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    catalog = json.load(f)

# Load FAISS index
index = faiss.read_index(INDEX_PATH)


def search(query, top_k=10):
    """
    Search top matching SHL assessments
    """

    embedding = model.encode([query])

    distances, indices = index.search(
        np.array(embedding).astype("float32"),
        top_k
    )

    results = []

    for idx in indices[0]:
        if idx < len(catalog):
            item = catalog[idx]

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


if __name__ == "__main__":

    query = input("Enter query: ")

    results = search(query)

    print("\nTop Matches:\n")

    for r in results:
        print("----------------------------------")
        print("Name :", r["name"])
        print("URL  :", r["url"])