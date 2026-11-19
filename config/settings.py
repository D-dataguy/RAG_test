"""Centralized configuration settings."""
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://rahulshettyacademy.com/rag-ui/")
HEADLESS = os.getenv("HEADLESS", "True").lower() == "true"
TIMEOUT = int(os.getenv("TIMEOUT", "30000"))
