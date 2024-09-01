import os

YOUTUBE_API_KEY =os.getenv("YOUTUBE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SCRAPER_API_KEY = YOUTUBE_API_KEY

if not OPENAI_API_KEY:
    raise ValueError("L'API Key d'OpenAI n'est pas définie. Assurez-vous qu'elle est correcte")

if not YOUTUBE_API_KEY:
    raise ValueError("L'API Key de YouTube n'est pas définie. Assurez-vous qu'elle est correcte.")