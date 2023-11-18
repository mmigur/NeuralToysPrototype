import os
from dotenv import load_dotenv

load_dotenv()

KIDS_MODE = os.environ.get("KIDS_MODE")

GPT_MODEL_NAME = os.environ.get("GPT_MODEL_NAME")
STREAM = bool(os.environ.get("STREAM"))

ADVICE_TEMPLATE = os.environ.get("ADVICE_TEMPLATE")