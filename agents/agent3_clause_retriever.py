import pickle
from sentence_transformers import SentenceTransformer

def retrieve_clause(query: str, index_path="vectorstore/faiss_index.pkl", top_k=1):
    with open(index_path, "rb") as f:
        data = pickle.load(f)

    index = data["index"]
    chunks = data["chunks"]
    model = data["model"]

    query_vec = model.encode([query])
    D, I = index.search(query_vec, top_k)

    return chunks[I[0][0]] if I[0][0] < len(chunks) else "No clause found"
