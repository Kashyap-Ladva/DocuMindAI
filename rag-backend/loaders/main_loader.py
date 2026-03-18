import os
from config.settings import RAW_DATA_DIR
from loaders.pdf_loader import load_single_pdf
from loaders.text_loader import load_text_file

def load_all_documents():
    """
    Load all supported documents from the raw data directory.
    """
    all_documents = []

    if not os.path.exists(RAW_DATA_DIR):
        print(f"Directory {RAW_DATA_DIR} does not exist.")
        return []

    for filename in os.listdir(RAW_DATA_DIR):
        file_path = os.path.join(RAW_DATA_DIR, filename)

        if filename.lower().endswith(".pdf"):
            print(f"Loading PDF: {filename}")
            try:
                docs = load_single_pdf(file_path)
                all_documents.extend(docs)
            except Exception as e:
                print(f"Error loading PDF {filename}: {str(e)}")

        elif filename.lower().endswith(".txt"):
            print(f"Loading Text: {filename}")
            try:
                docs = load_text_file(file_path)
                all_documents.extend(docs)
            except Exception as e:
                print(f"Error loading text file {filename}: {str(e)}")

    print(f"Total documents/pages loaded: {len(all_documents)}")
    return all_documents
