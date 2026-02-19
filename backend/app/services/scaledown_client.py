import requests
from app.config import settings

def generate_documentation(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {settings.SCALEDOWN_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "scaledown-gpt",
        "messages": [
            {"role": "system", "content": "You are a professional technical documentation generator."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4
    }

    response = requests.post(
        settings.SCALEDOWN_API_URL,
        headers=headers,
        json=payload,
        timeout=30
    )

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
