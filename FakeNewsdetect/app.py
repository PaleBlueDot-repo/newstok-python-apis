from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize Flask application
app = Flask(__name__)

# Load the model and tokenizer
MODEL = "jy46604790/Fake-News-Bert-Detect"
clf = pipeline("text-classification", model=MODEL, tokenizer=MODEL)

# Define a route for the text classification
@app.route('/classify', methods=['POST'])
def classify_text():
    data = request.get_json()
    text = data['text']
    
    # Perform classification
    result = clf(text)
    
    # Return the result as JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
