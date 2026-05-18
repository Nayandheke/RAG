import streamlit as st
import os
import sys

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.document_loader import load_and_split_pdf
from src.vector_store import create_vector_store, load_vector_store
from src.generator import generate_response
from src import config

st.set_page_config(page_title="RAG Chatbot")

st.title("RAG Chatbot with Gemini")
st.markdown("Chat with your PDF documents using Retrieval-Augmented Generation.")

# API Key check
if not config.GEMINI_API_KEY or "your_api_key" in config.GEMINI_API_KEY:
    st.error("Please set a valid `GEMINI_API_KEY` in your `.env` file.")
    st.info("You can get an API key from [Google AI Studio](https://aistudio.google.com/app/apikey).")
    st.stop()

# Sidebar for configuration and status
with st.sidebar:
    st.header("Settings")
    if st.button("Rebuild Index"):
        with st.spinner("Processing PDF..."):
            chunks = load_and_split_pdf()
            create_vector_store(chunks)
            st.success("Index rebuilt successfully!")

# Initialize vector store
if 'vector_store' not in st.session_state:
    if os.path.exists(config.FAISS_INDEX_PATH):
        st.session_state.vector_store = load_vector_store()
    else:
        with st.spinner("Initial setup: Processing PDF..."):
            chunks = load_and_split_pdf()
            st.session_state.vector_store = create_vector_store(chunks)
            st.success("Initial index created!")

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question about your document"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Retrieval
            results = st.session_state.vector_store.similarity_search(prompt, k=3)
            context = "\n".join([doc.page_content for doc in results])
            
            # Generation
            try:
                response = generate_response(prompt, context)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Error: {e}")
