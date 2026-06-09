import base64
from openai import OpenAI


load_dotenv(dotenv_path=".env")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extract_receipt_data(image_bytes):
    base64_image = base64.b64encode(image_bytes).decode("utf-8")
    
    return {
        "store_name": "Test Store",
        "amount": 25.79,
        "date": "2026-06-06",
        "return_window": "30 days",
        "warranty_until": None,
        "warranty_info": "Test warranty info",
        "image_base64_preview": base64_image[:50]
    }