# 📄 RAG Document Q&A with Groq and Llama3 🚀

An AI-powered **Document Question Answering System** built using **Retrieval-Augmented Generation (RAG)**.
Upload documents and ask questions — the system retrieves relevant context and generates accurate answers using **Groq + Llama3**.

---

## ✨ Features

* 📄 Upload and process documents (PDF, text, etc.)
* 🔍 Semantic search using vector embeddings
* 🧠 Context-aware answers using LLM (Llama3 via Groq)
* ⚡ Fast inference with Groq API
* 💬 Chat-based interface (Streamlit)
* 📚 Supports multiple documents
* 🎯 Reduced hallucination using RAG

---

## 🛠️ Tech Stack

* **LLM:** Groq (Llama3)
* **Framework:** LangChain
* **Frontend:** Streamlit
* **Embeddings:** HuggingFace / Sentence Transformers
* **Vector DB:** ChromaDB / FAISS
* **Backend:** Python

---

## 🧠 What is RAG?

Retrieval-Augmented Generation (RAG) combines:

1. **Retrieval**

   * Finds relevant chunks from uploaded documents

2. **Generation**

   * LLM generates answers using retrieved context

👉 Result: More accurate and grounded responses

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/RAG-Document-Q-A-with-Groq-and-Llama3.git
cd RAG-Document-Q-A-with-Groq-and-Llama3
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. Upload document(s)
2. Text is split into chunks
3. Embeddings are created
4. Stored in vector database
5. User asks a question
6. Relevant chunks are retrieved
7. LLM generates final answer

---

## 🧱 Architecture

```
User Query
   ↓
Retriever (Vector DB)
   ↓
Relevant Chunks
   ↓
Groq LLM (Llama3)
   ↓
Final Answer
```

---

## ⚡ Key Advantages

* ✔ More accurate than normal chatbots
* ✔ Uses your own data
* ✔ Reduces hallucination
* ✔ Fast responses with Groq

---

## 📸 Screenshot

*Add your UI screenshot here*

---

## 🚀 Future Improvements

* 📄 Support for more file types (DOCX, CSV)
* 🔊 Voice-based Q&A
* 🌐 Web-based document ingestion
* 💾 Persistent vector storage
* 📊 Source highlighting in answers

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and submit PRs.

---

---

## 👨‍💻 Author

**Prathmesh Wavhal**
AI & Data Science Enthusiast 🚀

---

⭐ Star this repo if you found it useful!
