import google.generativeai as genai
from src import config

def configure_gemini():
    genai.configure(api_key=config.GEMINI_API_KEY)

def generate_response(query, context):
    configure_gemini()
    model = genai.GenerativeModel(config.GENERATIVE_MODEL_NAME)
    
    prompt = f"""
    Answer the question only using the provided context. If the answer is not in the context, say you don't know.
    
    Context:
    {context}
    
    Question:
    {query}
    """
    
    response = model.generate_content(prompt)
    return response.text
