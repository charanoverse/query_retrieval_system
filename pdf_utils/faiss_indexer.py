import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')  # Fast + good accuracy

def build_faiss_index(chunks, save_path="vectorstore/faiss_index.pkl"):
    # Embed all chunks
    embeddings = model.encode(chunks)

    # Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # Save the index and chunks
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "wb") as f:
        pickle.dump((index, chunks), f)

def load_faiss_index(path="vectorstore/faiss_index.pkl"):
    with open(path, "rb") as f:
        index, chunks = pickle.load(f)
    return index, chunks
