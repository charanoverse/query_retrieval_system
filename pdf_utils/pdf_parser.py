import fitz  # PyMuPDF

def extract_text_chunks(pdf_path, max_tokens=500):
    import tiktoken
    tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")
    
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    
    # Chunking
    chunks, current_chunk = [], []
    token_count = 0
    for para in full_text.split("\n\n"):
        tokens = tokenizer.encode(para)
        if token_count + len(tokens) > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk, token_count = [], 0
        current_chunk.append(para)
        token_count += len(tokens)
    
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    
    return chunks
