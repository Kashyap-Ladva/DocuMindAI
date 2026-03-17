# 🧠 DocuMind AI

A full-stack **RAG (Retrieval-Augmented Generation)** application that lets users upload PDFs and ask intelligent questions — answers are grounded in the actual document content.

---

## 🚀 Features

- 📄 Upload and index PDF documents
- 🔍 Semantic search using FAISS vector store
- 🤖 LLM-powered answers via Groq API
- 🧠 LangChain-based RAG pipeline
- ⚡ FastAPI backend with REST endpoints
- 🎨 React + Vite frontend (custom dark UI)

---

## 🏗 Tech Stack

### Backend
| Tool | Usage |
|------|-------|
| Python 3.12 | Core logic |
| FastAPI | REST API |
| LangChain | RAG pipeline |
| FAISS | Vector similarity search |
| HuggingFace Embeddings | Text embeddings |
| Groq LLM | Language model inference |
| Pydantic v2 | Data validation |

### Frontend
| Tool | Usage |
|------|-------|
| React + Vite | UI framework |
| CSS | Custom dark theme |

---

## 🔁 How It Works
```
PDF Upload → Text Extraction → Chunking → Embeddings (HuggingFace)
→ FAISS Index → User Query → Semantic Search → Groq LLM → Grounded Answer
```

---

## ⚙️ Setup Instructions

### Backend
```bash
cd rag-backend
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
python -m api.app
```

> Backend runs at: `http://localhost:8000`

### Frontend
```bash
cd rag-frontend
npm install
npm run dev
```

> Frontend runs at: `http://localhost:5173`

---

## 🔑 Environment Variables

Create a `.env` file in `rag-backend/`:
```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free Groq API key at: [console.groq.com](https://console.groq.com)

---

## 🧪 Example Workflow

1. Open the app in browser
2. Upload any PDF document
3. Wait for indexing to complete
4. Ask questions in natural language
5. Receive grounded answers with source references

---

## 👥 Authors

| Name | Role |
|------|------|
| **Kashyap Ladva** | AI & Data Science |
| **Manan** | Full Stack |
| **Kaushal** | AI & Data Science |

---

## 🧑‍💻 Connect

**Kashyap Ladva** — CE Student @ GEC Gandhinagar  
[GitHub](https://github.com/Kashyap-Ladva)
