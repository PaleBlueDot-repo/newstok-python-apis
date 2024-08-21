import json
import io
from PIL import Image
from flask import Blueprint, request, jsonify, request, send_file, jsonify
from ml.summarization_gemei_api import process_text
# from ml.fake_news_detect_api import indentify_fake_news
from ml.generate_image_api import query_huggingface_api
import pandas as pd
from ml.reels_recommendation_api import get_item_based_recommendations
from sklearn.metrics.pairwise import cosine_similarity

ml_bp = Blueprint('ml_bp', __name__)

@ml_bp.route('/process-data', methods=['POST'])
def process():
    data = request.get_json()
    input_text = data.get('input_text', '')
    if not input_text:
        return jsonify({"error": "No input_text provided"}), 400

    result = process_text(input_text)
    return jsonify(json.loads(result))

# @ml_bp.route('/classify', methods=['POST'])
# def classify_text():
#     data = request.get_json()
#     text = data['text']
#     print(text)
    
#     result = indentify_fake_news(text)
    
#     # Return the result as JSON
#     return jsonify(result)
  
@ml_bp.route('/generate-image', methods=['POST'])
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



