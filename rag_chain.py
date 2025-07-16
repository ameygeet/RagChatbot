from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chains.summarize import load_summarize_chain

def build_vectorstore(docs):
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return FAISS.from_documents(docs, embeddings)

def get_rag_chain(vectorstore):
    llm = Ollama(model="gemma:2b")  # lighter LLM
    retriever = vectorstore.as_retriever()
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def generate_summary(docs):
    llm = Ollama(model="gemma:2b")  # lighter LLM
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    return chain.run(docs)
