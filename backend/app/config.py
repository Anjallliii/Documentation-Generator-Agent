import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SCALEDOWN_API_KEY = os.getenv("SCALEDOWN_API_KEY")
    SCALEDOWN_API_URL = "https://api.scaledown.ai/v1/chat/completions"

settings = Settings()
