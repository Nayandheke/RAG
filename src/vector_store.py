from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from src import config
import os

def get_embeddings():
    return HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL_NAME)

def create_vector_store(chunks):
    embeddings = get_embeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(config.FAISS_INDEX_PATH)
    return vector_store

def load_vector_store():
    if os.path.exists(config.FAISS_INDEX_PATH):
        embeddings = get_embeddings()
        return FAISS.load_local(config.FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
    return None
