from flask import Flask, request, send_file, jsonify
import requests
import io
from PIL import Image

app = Flask(__name__)

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

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({"error": "Invalid request, 'prompt' key is required"}), 400

    prompt = data['prompt']
    image_bytes = query_huggingface_api(prompt)

    if image_bytes:
        try:
            # Return the image as a response
            return send_file(io.BytesIO(image_bytes), mimetype='image/png')
        except Exception as e:
            return jsonify({"error": f"Error processing image: {e}"}), 500
    else:
        return jsonify({"error": "Failed to generate image"}), 500

if __name__ == '__main__':
    app.run(debug=True)
