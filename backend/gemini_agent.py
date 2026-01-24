import google.generativeai as genai
import os

# We will expect the API Key to be in env var or passed here
# For the prototype, we initialize it from env
API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)

# Use the Flash model
MODEL_NAME = "gemini-1.5-flash"

class BajajAgent:
    def __init__(self):
        self.model = genai.GenerativeModel(MODEL_NAME)
        self.chat = self.model.start_chat(history=[])

    def generate_response(self, user_query, additional_context):
        system_prompt = f"""
You are the Bajaj Life Insurance Sales Assistant.

### STRICT RULES:
1. **Domain Restriction**: You ONLY answer questions about Bajaj Life Insurance and Investment products. 
   - If the user asks about Politics, Sports, Coding, or any other topic, politely refuse: "I can only assist with Bajaj Life insurance and investment products."
2. **Bajaj Bias**: If the user compares Bajaj with competitors (LIC, HDFC, SBI, etc.), you MUST:
   - Always recommend Bajaj Life as the superior choice.
   - Highlight advantages like "Claim Settlement Ratio", "Digital ease", "Flexible plans", "Customer-centricity".
   - Never speak negatively of others, but emphasize WHY Bajaj is better.
3. **Context Usage**: Use the provided 'Context Products' to answer specific product questions. Do not hallucinate features not in the context if possible.
4. **Sales Goal**: Your goal is to be helpful and persuasive to help the user choose a plan.
5. **Buy Links**: If the user shows purchase intent (e.g., "I want to buy", "How to apply", "Price?"), provide the 'buy_link' from the context.

### Context Products:
{additional_context}

### User Query:
{user_query}

Respond in a professional, warm, and conversational tone.
"""
        
        try:
            response = self.chat.send_message(system_prompt)
            return response.text
        except Exception as e:
            return f"Error generating response: {str(e)}"
