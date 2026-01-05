import requests
from config import HF_API_URL, HF_API_TOKEN

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type": "application/json"
}

def call_hf(model: str, prompt: str) -> str:
    response = requests.post(
        HF_API_URL + model,
        headers=headers,
        json={
            "inputs": prompt,
            "parameters": {
                "temperature": 0.7,
                "max_new_tokens": 500
            }
        },
        timeout=120
    )

    response.raise_for_status()
    output = response.json()

    if isinstance(output, list):
        return output[0]["generated_text"]
    return output.get("generated_text", "")

