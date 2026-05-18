import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
GENERATIVE_MODEL_NAME = "gemini-1.5-flash"
FAISS_INDEX_PATH = "faiss_index"
DATA_PATH = "data/sample.pdf"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100
