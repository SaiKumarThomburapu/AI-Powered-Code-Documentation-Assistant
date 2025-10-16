import os

class Settings:
    GEMINI_API_KEY: str = os.environ.get("GEMINI_API_KEY", "")

settings = Settings()

