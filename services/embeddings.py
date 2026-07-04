import json
import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

CATALOG_PATH = "data/shl_product_catalog.json"
INDEX_PATH = "data/faiss.index"
EMBEDDING_PATH = "data/embeddings.npy"

model = SentenceTransformer("all-MiniLM-L6-v2")


def load_catalog():
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def build_embeddings():
    catalog = load_catalog()

    texts = []

    for item in catalog:

        text = f"""
        {item.get("name","")}
        {item.get("description","")}
        {' '.join(item.get("job_levels",[]))}
        {' '.join(item.get("languages",[]))}
        {' '.join(item.get("test_types",[]))}
        """

        texts.append(text)

    embeddings = model.encode(texts, convert_to_numpy=True)

    np.save(EMBEDDING_PATH, embeddings)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, INDEX_PATH)

    print("Embeddings Created Successfully")


if __name__ == "__main__":
    build_embeddings()