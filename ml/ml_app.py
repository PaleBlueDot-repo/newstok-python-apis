from flask import Blueprint, request, jsonify, send_file
from functools import wraps
import io
import json
from PIL import Image
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from ml.summarization_gemei_api import process_text
from ml.generate_image_api import query_huggingface_api
from ml.reels_recommendation_api import get_item_based_recommendations
from ml.Reels_music_api import audio_to_base64 ,query,limit_base64_string

from dotenv import load_dotenv
import os

ml_bp = Blueprint('ml_bp', __name__)


load_dotenv()
api_key_auth = os.getenv("AUTH_API_KEY")

VALID_API_KEYS = {api_key_auth}

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if not api_key or api_key not in VALID_API_KEYS:
            return jsonify({"error": "Invalid or missing API key"}), 401
        return f(*args, **kwargs)
    return decorated_function

@ml_bp.route('/process-data', methods=['POST'])
@require_api_key
def process():
    data = request.get_json()
    input_text = data.get('input_text', '')
    if not input_text:
        return jsonify({"error": "No input_text provided"}), 400

    result = process_text(input_text)
    return jsonify(json.loads(result))

@ml_bp.route('/generate-image', methods=['POST'])
@require_api_key
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

@ml_bp.route('/recommendReels', methods=['POST'])
@require_api_key
def recommend():
    data = request.json
    print(data)
    user_id = data['user_id']
    interactions = data['interactions']

    df = pd.DataFrame(interactions)
    user_item_matrix = df.pivot_table(index='user_id', columns='reels_id', values='score').fillna(0)

    item_similarity = cosine_similarity(user_item_matrix.T)
    item_similarity_df = pd.DataFrame(item_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns)

    recommendations = get_item_based_recommendations(user_id, user_item_matrix, item_similarity_df)

    return jsonify({
        'user_id': user_id,
        'recommendations': recommendations
    })


@ml_bp.route('/generate-music', methods=['POST'])
@require_api_key
def generateMusic():
    data = request.json
    print(data)
    text = data['text']
   
    audio_bytes = query({
           "inputs": text,
     })

    audio_base64 = audio_to_base64(audio_bytes)

    audio_base64_limited = limit_base64_string(audio_base64, 600)


    return jsonify({
        'music': audio_base64_limited
    })