# LLM Chatbot (Gradio + Python + GPT-5)

This is a simple **LLM-powered chatbot** built with Python (backend) and Gradio (frontend).
It connects to OpenAI's GPT-5 model through the API and returns responses in a conversational interface.

---

## 🚀 Features
- Frontend: **Gradio** for chat UI
- Backend: **Python** with OpenAI API
- LLM: **GPT-5**
- Example queries included ("Hello, how are you?", "What is the capital of France?")

---

## ⚙️ Tech Stack
- Python 3.9+
- Gradio
- OpenAI SDK
- dotenv (for managing API keys)

---

## 🛠️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/llm-chatbot.git
   cd llm-chatbot

2. Create a virtual environment
    python3 -m venv level1-100x
    source ./level1-100x/bin/activate   # Mac/Linux
    .\level1-100x\Scripts\activate      # Windows

3. Install dependencies
    Set manually in .py file

4. Set your OpenAI API key
    Create a .env file in the root folder:
    OPENAI_API_KEY=your_api_key_here

5. Run the app
    python3 app.py



