import os
import base64
import json

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv(dotenv_path=".env")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_receipt_data(image_bytes,mime_type="image/jpeg"):
    base64_image = base64.b64encode(image_bytes).decode("utf-8")


    response = client.responses.create(
        model="gpt-5.5",
        input=[
            {
                "role":"user",
                "content": [
                    {
                        "type":"input_text",
                        "text": """


                        Extract the receipt information from this image.

    Return ONLY valid JSON with these keys:
    store_name, amount, date, return_window, warranty_until, warranty_info.

    If a field is missing, use null.
    """
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:{mime_type};base64,{base64_image}",
                    }
                ]
            }
        ]
    )

    return json.loads(response.output_text)