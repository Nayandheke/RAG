# Professional RAG System with Gemini and LangChain

A robust Retrieval-Augmented Generation (RAG) system that allows you to chat with your PDF documents using Google's Gemini AI and LangChain.

## 🚀 Features

- **PDF Processing**: Seamlessly load and split PDF documents.
- **Vector Search**: High-performance similarity search using FAISS and HuggingFace embeddings.
- **AI Generation**: Context-aware answers powered by Google Gemini 1.5 Flash.
- **Modular Design**: Clean, maintainable code structure suitable for production.

## 🛠️ Project Structure

```text
RAG/
├── src/                # Source code
│   ├── config.py       # Configuration management
│   ├── document_loader.py # PDF processing
│   ├── vector_store.py  # FAISS index management
│   ├── generator.py     # Gemini AI integration
│   └── main.py          # Main application entry point
├── data/               # Documents folder
├── notebook/           # Experimental notebooks
├── .env.example        # Environment variables template
├── .gitignore          # Git exclusion rules
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

## 📋 Prerequisites

- Python 3.8+
- Google Gemini API Key

## ⚙️ Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd RAG
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   - Copy `.env.example` to `.env`.
   - Add your [Google Gemini API Key](https://aistudio.google.com/app/apikey) to the `.env` file.
   ```bash
   GEMINI_API_KEY=your_actual_api_key_here
   ```

## 🏃 Usage

Run the main script to start the interactive chat session:

```bash
python -m src.main
```

The system will:
1. Load and process `data/sample.pdf` if no index exists.
2. Build a local FAISS vector store.
3. Prompt you to ask questions based on the document's content.

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
