# UPDATE: Import from the unified new SDK namespace
from google import genai
from src import config

def generate_response(query, context):
    if not config.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not set.")
        
    # UPDATE: The new SDK initializes a stateless Client object
    client = genai.Client(api_key=config.GEMINI_API_KEY)
    
    prompt = f"""
    Answer the question only using the provided context. If the answer is not in the context, say you don't know.
    
    Context:
    {context}
    
    Question:
    {query}
    """
    
    try:
        # UPDATE: Call client.models.generate_content directly
        response = client.models.generate_content(
            model=config.GENERATIVE_MODEL_NAME,
            contents=prompt
        )
        return response.text
    except Exception as e:
        # Better fallback debugging
        if "404" in str(e) or "not found" in str(e).lower():
            raise Exception(f"Model '{config.GENERATIVE_MODEL_NAME}' could not be reached. Ensure your API key is correct. Error: {e}")
        raise e