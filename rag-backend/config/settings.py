import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# ===============================
# API KEYS
# ===============================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if GROQ_API_KEY is None:
    raise ValueError(" GROQ_API_KEY not found. Check your .env file.")

# ===============================
# DATA PATHS
# ===============================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
VECTOR_DB_DIR = os.path.join(BASE_DIR, "vectorstore", "faiss_index")

# ===============================
# CHUNKING CONFIG
# ===============================
CHUNK_SIZE = 500          # characters per chunk
CHUNK_OVERLAP = 100       # overlap between chunks

# ===============================
# EMBEDDING CONFIG
# ===============================
# NOTE:
# Groq does NOT provide embeddings.
# We will use HuggingFace embeddings for indexing.
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"


# ===============================
# VECTOR STORE CONFIG
# ===============================
VECTOR_DB_TYPE = "faiss"


# ===============================
# UPLOAD LIMITS
# ===============================
MAX_PDF_SIZE_MB = int(os.getenv("MAX_PDF_SIZE_MB", 10))
MAX_TEXT_SIZE_MB = int(os.getenv("MAX_TEXT_SIZE_MB", 5))
MAX_PDF_PAGES = int(os.getenv("MAX_PDF_PAGES", 100))
MAX_TEXT_CHARS = int(os.getenv("MAX_TEXT_CHARS", 100000))
