
import requests


API_URL = "https://api-inference.huggingface.co/models/ZB-Tech/Text-to-Image"
headers = {"Authorization": "Bearer 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"}

def query_huggingface_api(prompt):
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error querying API: {e}")
        return None



