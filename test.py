from pdf_utils.pdf_parser import extract_text_chunks
from pdf_utils.faiss_indexer import build_faiss_index

chunks = extract_text_chunks("data/test1.pdf")
build_faiss_index(chunks)
exit()
