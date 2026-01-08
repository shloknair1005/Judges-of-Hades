import os
from dotenv import load_dotenv

load_dotenv()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
HF_API_URL = os.getenv("HF_API_URL")

# Models go here
OPS_MODEL = "google/gemma-3-270m"
FINANCE_MODEL = "google/gemma-3-270m"
SALES_MODEL = "google/gemma-3-270m"
HADES_MODEL = "google/gemma-3-270m"


