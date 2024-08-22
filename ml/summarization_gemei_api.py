from flask import Flask, request, jsonify
import google.generativeai as genai
import json

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
api_key = os.getenv("Gemini_API_KEY")
genai.configure(api_key=api_key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

def process_text(input_text):
    prompt = (f"Input text: '{input_text}'\n"
              "Tasks:\n"
              "1. Summarize this text in 20 words.\n"
              "2. Provide a font color based on the text context (HTML color code).\n"
              "3. Provide a background color based on the text context (HTML color code).\n"
              "4. Provide a font family based on the text context (e.g., Arial, Times New Roman).\n"
              "5. Generate a music prompt based on the text content in english.\n"
              "6. Generate a Image prompt based on the text content in english.\n"

              "Note must follow: If the input text is in Bangla, provide the response in Bangla for only summarization. If it is in English, give the response in English for summarization."
              "Give response in a  ||  separated just response do not need to give name of each tasks "
              )

    # Start a chat session
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)
    Text = response.text
    parts = [part.strip() for part in Text.split("||")]

    res = {
        "summary": parts[0],
        "font_color": parts[1],
        "background_color": parts[2],
        "font_family": parts[3],
        "music_prompt": parts[4],
        "image_prompt": parts[5]
    }

    res_json = json.dumps(res, ensure_ascii=False, indent=4)
    return res_json
