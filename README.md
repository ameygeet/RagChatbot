
# 📚 RAG-Based Local Document Chatbot

A **Streamlit web app** that allows you to upload your own documents and chat with them using **Retrieval-Augmented Generation (RAG)** — all powered by **local LLMs** via [Ollama](https://ollama.com). No internet or external API keys required!

---

## 🚀 Features

- 📄 Upload `.pdf`, `.txt`, `.docx`, or `.md` files
- 🔍 Uses **LangChain** and **FAISS** to chunk and embed documents
- 🧠 Powered by **Gemma:2b** via Ollama for question-answering
- 📑 Auto-generates a summary of your uploaded document
- 💬 Ask natural language questions about the content
- 🖥️ Fully local – no external API calls

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: LangChain, FAISS, Ollama LLM
- **LLM Model**: Gemma:2b (via Ollama)
- **Embeddings**: nomic-embed-text
- **Document Support**: PDF, TXT, DOCX, MD

---

## 📂 Project Structure

```
📁 your_project/
├── app.py               # Main Streamlit UI
├── loader.py            # Handles document loading and chunking
├── rag_chain.py         # Builds vector store and QA/summarization chain
├── docs/                # Uploaded documents
└── README.md            # Project README
```

---

## 📦 Installation

1. **Install Python dependencies**:
   ```bash
   pip install streamlit langchain faiss-cpu unstructured
   ```

2. **Install and run Ollama**:  
   Follow [https://ollama.com](https://ollama.com) to install Ollama, then run:
   ```bash
   ollama pull gemma:2b
   ```

3. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

---

## 📸 Demo

![screenshot](https://via.placeholder.com/800x400.png?text=Upload+your+doc+and+chat+with+it)

---

## 🔗 GitHub Project

Feel free to check out and contribute:  
**[👉 GitHub Repo](https://github.com/your-username/rag-chatbot)**

---

## 📃 License

This project is licensed under the MIT License.
