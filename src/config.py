import os
from dotenv import load_dotenv

load_dotenv()

# Дополнение к промтам chat-gpt
KIDS_MODE = os.environ.get("KIDS_MODE")
ADVICE_TEMPLATE = os.environ.get("ADVICE_TEMPLATE")
INTERESTING_FACT = os.environ.get("INTERESTING_FACT")

# Настройки запроса
GPT_MODEL_NAME = os.environ.get("GPT_MODEL_NAME")
STREAM = bool(os.environ.get("STREAM"))

# Переменные для генерации сказки
STORY_PROMT_PART_1 = os.environ.get("STORY_PROMT_PART_1")
STORY_PROMT_PART_2 = os.environ.get("STORY_PROMT_PART_2")
STORY_PROMT_PART_3 = os.environ.get("STORY_PROMT_PART_3")
STORY_PROMT_PART_4 = os.environ.get("STORY_PROMT_PART_4")