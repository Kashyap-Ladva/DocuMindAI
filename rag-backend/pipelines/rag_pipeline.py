import os
from retrieval.rag_retriever import retrieve_context
from llm.groq_llm import get_groq_response


def ask_question(question: str):
    print("Retrieving context...")
    results = retrieve_context(question)

    # Extract context, metadata, and scores
    context_list = []
    sources_list = []
    scores = []

    for doc, score in results:
        context_list.append(doc.page_content)
        scores.append(score)

        # Source Attribution
        metadata = doc.metadata

        page_num = metadata.get("page")
        if page_num is not None:
            page_num += 1

        source_entry = {
            "document": os.path.basename(metadata.get("source", "Unknown")),
            "page": page_num,
            "excerpt": doc.page_content[:200].replace("\n", " ") + "..."
        }

        # Deduplicate sources based on document and page
        exists = False
        for s in sources_list:
            if s["document"] == source_entry["document"] and s["page"] == source_entry["page"]:
                exists = True
                break

        if not exists:
            sources_list.append(source_entry)

    context = "\n\n".join(context_list)

    # Calculate Confidence Score (0-100%)
    # Using L2 distance from FAISS (lower is better)
    # Cosine Similarity approximation: S = 1 - d^2 / 2
    if scores:
        best_score = min(scores) # Best match (lowest distance)
        similarity = 1 - (best_score ** 2) / 2
        confidence = max(0, min(100, int(similarity * 100)))
    else:
        confidence = 0

    print(f"Confidence Score: {confidence}%")

    print("Generating answer...")
    answer = get_groq_response(context, question)

    return answer, sources_list, confidence
