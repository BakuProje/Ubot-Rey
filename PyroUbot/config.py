  GNU nano 6.2                                            config.py *                                                   import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "60"))

DEVS = list(map(int, os.getenv("DEVS", "6659520088").split()))

API_ID = int(os.getenv("API_ID", "26530660"))

API_HASH = os.getenv("API_HASH", "85fed9fcd1c4ad6c9fda8d41d010e7d1")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7831941318:AAHQR5qNfTwNxqkdvvDa47NZUSJWkBj1G-U")

OWNER_ID = int(os.getenv("OWNER_ID", "6659520088"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://apalah:apalah@cluster0.j8mb4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT","-1002457551830"))

USER_GROUP = os.getenv("USER_GROUP", "@allubotrey")
