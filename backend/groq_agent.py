from groq import Groq
import os

# Initialize Groq Client
API_KEY = os.getenv("GROQ_API_KEY")
client = None

if API_KEY:
    print(f"Groq API Key found: {API_KEY[:5]}...{API_KEY[-3:]}")
    client = Groq(api_key=API_KEY)
else:
    print("CRITICAL: Groq API Key NOT found in environment!")

# Use a fast, capable model
MODEL_NAME = "llama-3.3-70b-specdec" # Powerful Llama 3 variant on Groq

class BajajAgent:
    def __init__(self):
        self.history = []

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
"""
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ]
        
        try:
            chat_completion = client.chat.completions.create(
                messages=messages,
                model=MODEL_NAME,
            )
            response_text = chat_completion.choices[0].message.content
            return response_text
        except Exception as e:
            return f"Error generating response from Groq: {str(e)}"
