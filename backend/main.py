from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from retriever import load_products, retrieve_products
from groq_agent import BajajAgent
from voice_personaplex import VoiceGenerator
import os

from typing import Optional, List

app = FastAPI(title="Bajaj Life PersonaPlex Sales Assistant")

# CORS setup for Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all for MVP functionality in Docker
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
print("Loading Product Database...")
PRODUCTS = load_products()
print(f"Loaded {len(PRODUCTS)} products.")

print("Initializing Groq Agent...")
agent = BajajAgent()
voice_gen = VoiceGenerator()

class ChatRequest(BaseModel):
    query: str
    enable_voice: bool = False

class ChatResponse(BaseModel):
    response: str
    audio_base64: Optional[str] = None
    products_found: List[str] = []

@app.get("/")
def health_check():
    return {"status": "active", "service": "Bajaj Life Assistant"}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    query = request.query
    
    # 1. Retrieve Context
    relevant_products = retrieve_products(query, PRODUCTS)
    
    # 2. Generate Logic Response (Gemini)
    # Format context for the LLM
    context_str = "\n".join([str(p) for p in relevant_products])
    
    ai_response_text = agent.generate_response(query, context_str)
    
    # 3. Voice Generation (Optional)
    audio_data = None
    if request.enable_voice:
        audio_data = voice_gen.generate_audio(ai_response_text)

    return ChatResponse(
        response=ai_response_text,
        audio_base64=audio_data,
        products_found=[p['product_name'] for p in relevant_products]
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
