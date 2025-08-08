from sentence_transformers import SentenceTransformer
import faiss
import pickle

def build_faiss_index(chunks, save_path="vectorstore/faiss_index.pkl"):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    vectors = model.encode(chunks)

    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)

    faiss_data = {
        "index": index,
        "chunks": chunks,
        "model": model
    }

    with open(save_path, "wb") as f:
        pickle.dump(faiss_data, f)
