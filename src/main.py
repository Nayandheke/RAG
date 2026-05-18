from src.document_loader import load_and_split_pdf
from src.vector_store import create_vector_store, load_vector_store
from src.generator import generate_response
from src import config
import os

def main():
    # Check if index exists, otherwise create it
    if not os.path.exists(config.FAISS_INDEX_PATH):
        print("Creating vector store index...")
        chunks = load_and_split_pdf()
        vector_store = create_vector_store(chunks)
    else:
        print("Loading existing vector store index...")
        vector_store = load_vector_store()

    if not vector_store:
        print("Error: Could not load or create vector store.")
        return

    while True:
        query = input("\nAsk a question (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        
        # Retrieval
        results = vector_store.similarity_search(query, k=3)
        context = "\n".join([doc.page_content for doc in results])
        
        # Generation
        try:
            answer = generate_response(query, context)
            print(f"\nAnswer:\n{answer}")
        except Exception as e:
            print(f"Error generating response: {e}")

if __name__ == "__main__":
    main()
