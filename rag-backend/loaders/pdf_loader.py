import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from config.settings import RAW_DATA_DIR


def load_single_pdf(file_path: str):
    """
    Load a single PDF file.
    Each page becomes a Document with metadata.
    """
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents


def load_single_txt(file_path: str):
    """
    Load a single TXT file.
    Entire file becomes a single Document.
    """
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()
    return documents


def load_all_documents():
    """
    Load all supported documents (PDF, TXT)
    from the raw data directory.
    """
    all_documents = []

    for filename in os.listdir(RAW_DATA_DIR):
        file_path = os.path.join(RAW_DATA_DIR, filename)

        if filename.lower().endswith(".pdf"):
            print(f"Loading PDF: {filename}")
            docs = load_single_pdf(file_path)

        elif filename.lower().endswith(".txt"):
            print(f"Loading TXT: {filename}")
            docs = load_single_txt(file_path)

        else:
            continue

        all_documents.extend(docs)

    print(f"Total documents/pages loaded: {len(all_documents)}")
    return all_documents