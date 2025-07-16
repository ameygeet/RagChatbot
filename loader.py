import os
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredMarkdownLoader,
    UnstructuredFileLoader,
    Docx2txtLoader
)
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == ".pdf":
        loader = PyPDFLoader(file_path)
    elif ext == ".txt":
        loader = TextLoader(file_path)
    elif ext == ".md":
        loader = UnstructuredMarkdownLoader(file_path)
    elif ext == ".docx":
        loader = Docx2txtLoader(file_path)
    else:
        loader = UnstructuredFileLoader(file_path)  # fallback
    return loader.load()

def split_documents(docs, chunk_size=800, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(docs)
