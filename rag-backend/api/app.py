from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import shutil
import os
import pypdf
from io import BytesIO

from pipelines.rag_pipeline import ask_question
from indexer.build_index import run_indexing_pipeline
from config.settings import (
    MAX_PDF_SIZE_MB, MAX_TEXT_SIZE_MB, MAX_PDF_PAGES, MAX_TEXT_CHARS, RAW_DATA_DIR
)

app = FastAPI(title="RAG Backend API")

# 🔓 Allow React frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Request & Response Schemas ----------

class QuestionRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    answer: str
    sources: list
    confidence: float


# ---------- API ENDPOINT ----------

@app.post("/ask", response_model=AnswerResponse)
def ask_rag(request: QuestionRequest):
    answer, sources, confidence = ask_question(request.question)
    return {
        "answer": answer,
        "sources": sources,
        "confidence": confidence
    }


@app.get("/")
def health_check():
    return {"status": "RAG backend running"}


UPLOAD_DIR = RAW_DATA_DIR


@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files allowed")

    # Check file size (approximate using seek/tell)
    file.file.seek(0, 2)
    size = file.file.tell()
    file.file.seek(0)

    if size > MAX_PDF_SIZE_MB * 1024 * 1024:
        raise HTTPException(status_code=413, detail=f"File too large. Max size is {MAX_PDF_SIZE_MB}MB")

    # Check page count
    try:
        # We need to read the file content to count pages without saving first
        # Or we can use pypdf on the file object directly if it supports it
        # UploadFile.file is a SpooledTemporaryFile which behaves like a file
        reader = pypdf.PdfReader(file.file)
        if len(reader.pages) > MAX_PDF_PAGES:
            raise HTTPException(status_code=400, detail=f"PDF exceeds maximum allowed pages ({MAX_PDF_PAGES})")

        # Reset file pointer for saving
        file.file.seek(0)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid PDF file or error reading: {str(e)}")

    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_name = os.path.basename(file.filename)
    file_path = os.path.join(UPLOAD_DIR, file_name)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 🔁 Rebuild index after upload
    run_indexing_pipeline()

    return {
        "message": "PDF uploaded and indexed successfully",
        "filename": file_name
    }

@app.post("/upload-text")
async def upload_text(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .txt files allowed")

    # Check file size
    file.file.seek(0, 2)
    size = file.file.tell()
    file.file.seek(0)

    if size > MAX_TEXT_SIZE_MB * 1024 * 1024:
        raise HTTPException(status_code=413, detail=f"File too large. Max size is {MAX_TEXT_SIZE_MB}MB")

    # Check content length
    content = await file.read()
    text_content = content.decode("utf-8", errors="ignore")

    if len(text_content) > MAX_TEXT_CHARS:
        raise HTTPException(status_code=400, detail=f"Text file exceeds maximum allowed characters ({MAX_TEXT_CHARS})")

    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_name = os.path.basename(file.filename)
    file_path = os.path.join(UPLOAD_DIR, file_name)

    with open(file_path, "wb") as buffer:
        buffer.write(content)

    # 🔁 Rebuild index after upload
    run_indexing_pipeline()

    return {
        "message": "Text file uploaded and indexed successfully",
        "filename": file_name
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.app:app", host="127.0.0.1", port=8000)
