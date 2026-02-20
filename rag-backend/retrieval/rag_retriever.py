from vectorstore.faiss_store import load_faiss_index


def retrieve_context(query: str, k: int = 3):
    """
    Retrieve relevant documents with similarity scores.
    Returns a list of tuples: (Document, score)
    """
    db = load_faiss_index()
    results_with_score = db.similarity_search_with_score(query, k=k)

    return results_with_score
