from flask import Flask, request, jsonify, send_file
from transformers import AutoProcessor, MusicgenForConditionalGeneration
import torch
import io
from scipy.io.wavfile import write

app = Flask(__name__)

processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")

@app.route('/generate-music', methods=['POST'])
def generate_music():
    data = request.json
    text_prompt = data.get('prompt')

    if not text_prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    inputs = processor(
        text=[text_prompt],
        padding=True,
        return_tensors="pt",
    )

    audio_values = model.generate(**inputs, max_new_tokens=256)
    sampling_rate = model.config.audio_encoder.sampling_rate

    audio_array = audio_values[0].cpu().numpy()

    # Create an in-memory WAV file
    audio_io = io.BytesIO()
    write(audio_io, sampling_rate, audio_array)
    audio_io.seek(0)

    return send_file(
        audio_io, 
        mimetype="audio/wav",
        as_attachment=True, 
        download_name="generated_music.wav"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
