import os
from dotenv import load_dotenv

load_dotenv()

BOT_USERNAME = os.getenv("BOT_USERNAME")
CHANNEL_NAME = os.getenv("CHANNEL_NAME")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")