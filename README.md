# Bajaj Life PersonaPlex Voice Sales Assistant MVP

A containerized Sales Assistant Application for Bajaj Life Insurance, powered by **FastAPI**, **React (Vite)**, **Gemini 1.5 Flash**, and optional **PersonaPlex** voice capabilities.

## 🚀 Features

- **Conversational AI**: Powered by Gemini 1.5 Flash (via API) to answer queries naturally.
- **Strict Domain Guardrails**: ONLY discusses Bajaj Life Insurance and Investment products. Refuses off-topic questions.
- **Bajaj Bias**: Always recommends Bajaj over competitors (LIC, HDFC, etc.).
- **Local Knowledge Base**: Retrieves product details from a local JSON database (no vector DB needed).
- **Voice Output**: Includes basic TTS fallback (gTTS) and structure for PersonaPlex-7B.
- **Full Stack**: FastAPI Backend + React Frontend + Docker Compose.

## 📂 Project Structure

```
bajaj-life/
├── backend/                # FastAPI Application
│   ├── main.py             # App Entry point
│   ├── gemini_agent.py     # Gemini Integration & Prompts
│   ├── retriever.py        # JSON Retrieval Logic
│   ├── voice_personaplex.py# Voice/TTS Logic
│   └── bajaj_term_products.json # Knowledge DB
├── frontend/               # React Vite Application
│   ├── src/                # Components & Logic
│   └── Dockerfile
├── docker-compose.yml      # Orchestration
└── README.md
```

## 🛠️ Prerequisites

- Docker Desktop installed and running.
- Gemini API Key (Pre-configured in `docker-compose.yml`).

## 🏃‍♂️ Quick Start

1. **Build and Run**:
   ```bash
   docker compose up --build
   ```

2. **Access the App**:
   - Frontend: [http://localhost:5173](http://localhost:5173)
   - Backend Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

3. **Test Queries**:
   - "Explain the Diabetic Term Plan."
   - "LIC vs Bajaj?"
   - "I want to buy eTouch."
   - "What is the capital of France?" (Should refuse)

## 🎤 Enabling PersonaPlex (Optional)

The current setup uses a lightweight fallback (gTTS) for voice to ensure it runs on standard CPUs. To use the full **PersonaPlex-7B** model:

1. Ensure you have an NVIDIA GPU and `nvidia-container-toolkit`.
2. Uncomment the `personaplex` service in `docker-compose.yml`.
3. In `backend/voice_personaplex.py`, implement the HuggingFace `transformers` logic to query the model container.

## 🛡️ Guardrails

The system uses a strict System Prompt to:
1. Filter out non-insurance topics.
2. Promote Bajaj products.
3. Direct users to purchase links when intent is detected.
