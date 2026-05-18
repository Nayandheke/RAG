import os
from dotenv import load_dotenv

load_dotenv()

# Base directory (project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# UPDATE: Shifted to the recommended production model
GENERATIVE_MODEL_NAME = "gemini-2.5-flash"

# Use absolute paths
FAISS_INDEX_PATH = os.path.join(BASE_DIR, "faiss_index")
DATA_PATH = os.path.join(BASE_DIR, "data", "sample.pdf")

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100