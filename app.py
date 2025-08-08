from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import requests
import tempfile

from pdf_utils.pdf_parser import parse_pdf_to_chunks
from pdf_utils.faiss_indexer import build_faiss_index, load_faiss_index
from pipeline import run_pipeline

# Load API_KEY from .env or environment
load_dotenv()
API_KEY = os.getenv("API_KEY")

app = FastAPI()

# Allow CORS if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    documents: str
    questions: list[str]

class QueryResponse(BaseModel):
    answers: list[str]

@app.post("/hackrx/run", response_model=QueryResponse)
async def run_hackrx_pipeline(request: Request, query: QueryRequest):
    # 🔐 1. Auth check
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing Bearer Token")

    token = auth_header.split(" ")[1]
    if token != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    # 📄 2. Download PDF from URL
    pdf_url = query.documents
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(response.content)
            pdf_path = tmp_file.name
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"PDF download failed: {e}")

    # 🧩 3. Parse PDF and chunk
    try:
        chunks = parse_pdf_to_chunks(pdf_path)
        build_faiss_index(chunks)  # saves to vectorstore/faiss_index.pkl
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PDF parsing/indexing failed: {e}")

    # 🧠 4. Run full agent pipeline for each question
    try:
        index = load_faiss_index()
        answers = []
        for question in query.questions:
            answer = run_pipeline(question, chunks, index)
            answers.append(answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Pipeline failed: {e}")

    return {"answers": answers}

#C:\Python312\python.exe -m uvicorn app:app --reload