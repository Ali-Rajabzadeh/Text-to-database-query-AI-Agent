import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found!")

llm = init_chat_model("nvidia/nemotron-3-ultra-550b-a55b:free", 
                      model_provider="openrouter",
                      api_key=OPENROUTER_API_KEY, 
                      temperature=0
                      )

