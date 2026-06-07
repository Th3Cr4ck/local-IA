import requests
url = "http://localhost:11434/api/generate"

payload = {
    "model": "phi4-mini",
    "prompt": "Saludame en varios idiomas",
    "stream": False
}

response = requests.post(url, json=payload)
print(response.json()["response"])
