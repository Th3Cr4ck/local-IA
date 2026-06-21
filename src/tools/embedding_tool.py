from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    device="cpu"
)

def generate_embeddings(texts):
    return model.encode(
        texts,
        show_progress_bar=True
    )

def enrich_index(index):
    texts = [
        (entry["text"], entry["file"])
        for entry in index
    ]

    embeddings = generate_embeddings(texts)

    for entry, emb in zip(index, embeddings):
        entry["embedding"] = emb.tolist()

    return index

def similarity(emb1, emb2):
    return util.cos_sim(emb1, emb2).item()
