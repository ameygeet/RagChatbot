import os
import streamlit as st
from loader import load_documents, split_documents
from rag_chain import build_vectorstore, get_rag_chain, generate_summary

st.set_page_config(page_title="📚 AI Chat for Your Docs (Local LLM)")

st.title("🤖 Local Chat with Your Document")
st.write("Runs on **Ollama** — no internet, no API key needed!")

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt", "md", "docx"])

if uploaded_file:
    file_path = f"docs/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("📄 Reading and chunking your document..."):
        raw_docs = load_documents(file_path)
        chunks = split_documents(raw_docs)
        vectorstore = build_vectorstore(chunks)
        rag_chain = get_rag_chain(vectorstore)

    with st.spinner("📝 Generating summary..."):
        summary = generate_summary(raw_docs)
        st.success("✅ Summary ready!")
        st.write(summary)

    st.markdown("---")
    st.subheader("💬 Ask a question about your document")

    query = st.text_input("Your question:")
    if query:
        with st.spinner("🤖 Thinking..."):
            response = rag_chain.run(query)
        st.write("🧠 **AI Answer:**", response)
