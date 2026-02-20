from langchain_community.document_loaders import TextLoader

def load_text_file(file_path: str):
    """
    Load a single text file and return LangChain Documents.
    """
    loader = TextLoader(file_path)
    documents = loader.load()
    return documents
