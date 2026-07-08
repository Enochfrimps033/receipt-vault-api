import os
import base64
import json

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv(dotenv_path=".env")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_receipt_data(image_bytes, mime_type="image/jpeg"):
    return {
        "store_name": "Walmart",
        "amount": 25.79,
        "date": "2026-06-06",
        "return_window": "30 days",
        "warranty_until": None,
        "warranty_info": "Manufacturer warranty for 1 year",
        "image_url": None
    }