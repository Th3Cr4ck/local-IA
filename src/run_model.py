# Sin usar libreria ollama de python
import requests
url = "http://localhost:11434/api/generate"

payload = {
    "model": "phi4-mini",
    "prompt": "Saludame en chino y en japones con solo dos renglones",
    "stream": False
}

response = requests.post(url, json=payload)
print(response.json()["response"])
