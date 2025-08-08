from fastapi import FastAPI
from pydantic import BaseModel
from pipeline import run_chain

app = FastAPI()

class QueryInput(BaseModel):
    query: str

@app.post("/hackrx/run")
def run_pipeline(input: QueryInput):
    result = run_chain(input.query)
    return result

#C:\Python312\python.exe -m uvicorn app:app --reload