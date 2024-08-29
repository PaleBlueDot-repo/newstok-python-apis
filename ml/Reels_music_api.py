import base64
import requests
import os


API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
API_KEY = os.getenv("HUGGINGFACE_API_KEY")
headers = {"Authorization": f"Bearer {API_KEY}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

def audio_to_base64(audio_bytes):
    return base64.b64encode(audio_bytes).decode('utf-8')

def limit_base64_string(base64_str, max_size_kb):
    max_size_bytes = max_size_kb * 1024
    if len(base64_str) > max_size_bytes:
        return base64_str[:max_size_bytes]
    return base64_str