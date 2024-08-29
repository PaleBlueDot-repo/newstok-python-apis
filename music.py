import base64
import requests

# Define the API URL and headers for authentication
API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
headers = {"Authorization": "Bearer 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"}

# Function to query the model and get audio bytes
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Function to convert audio bytes to Base64
def audio_to_base64(audio_bytes):
    return base64.b64encode(audio_bytes).decode('utf-8')

# Function to limit Base64 string to a certain size in bytes
def limit_base64_string(base64_str, max_size_kb):
    max_size_bytes = max_size_kb * 1024
    if len(base64_str) > max_size_bytes:
        return base64_str[:max_size_bytes]
    return base64_str

# Generate audio based on input text
audio_bytes = query({
    "inputs": "liquid drum and bass, atmospheric synths, airy sounds",
})

# Convert audio bytes to Base64 string
audio_base64 = audio_to_base64(audio_bytes)

# Limit the Base64 string to 200 KB
audio_base64_limited = limit_base64_string(audio_base64, 600)

# Save Base64 string to a text file
with open("audio_base642.txt", "w") as file:
    file.write(audio_base64_limited)

print("Base64 audio string saved to audio_base64.txt")
