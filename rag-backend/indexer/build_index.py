from loaders.main_loader import load_all_documents
from preprocessing.chunker import chunk_documents
from vectorstore.faiss_store import build_faiss_index, save_faiss_index


def run_indexing_pipeline():
    print("Starting RAG indexing pipeline...")

    # Step 1: Load documents (PDFs and Text files)
    documents = load_all_documents()

    # Step 2: Chunk documents
    chunks = chunk_documents(documents)

    # Step 3: Build FAISS index
    db = build_faiss_index(chunks)

    # Step 4: Save index
    save_faiss_index(db)

    print("RAG indexing pipeline completed successfully!")


if __name__ == "__main__":
    run_indexing_pipeline()
