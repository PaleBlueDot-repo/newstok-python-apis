from flask import Flask, request, jsonify
import google.generativeai as genai
import json

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
api_key = os.getenv("Gemini_API_KEY")
GeminiModel = os.getenv("Gemini_model")

genai.configure(api_key=api_key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

def split_on_delimiters(text):
    # Split the input text on '||' and strip whitespace
    lines = text.split('||')
    # Filter out empty strings after splitting and strip leading/trailing spaces
    return [line.strip() for line in lines if line.strip()]

model = genai.GenerativeModel(
    model_name=GeminiModel,
    generation_config=generation_config,
)

def process_text(input_text):
    prompt = (f"Input text: '{input_text}'\n"
              "Tasks:\n"
              "1. Summarize Input text in 50 words.Summarize it in Bangla language if the orginal input text is in bangla\n"
              "2. Provide a font color based on the text context (HTML color code).\n"
              "3. Provide a background color based on the text context (HTML color code).\n"
              "4. Provide a font family based on the text context \n"
              "5. Generate a music prompt based on the text content in english 20 words\n"
              "6. Generate a Image prompt based on the text content in english  20 words\n"
              "please Do it must Give each task responses || separted no numbering . No extra word"
              )

    # Start a chat session
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)
    Text = response.text
    print(Text)
    # parts = [part.strip() for part in Text.split("||")]
    parts=split_on_delimiters(Text)


    default_summary = "Default summary content."
    default_font_color = "#000000"  # Black
    default_background_color = "#FFFFFF"  # White
    default_font_family = "Arial"
    default_music_prompt = "Compose a short music track that complements a breaking news story."
    default_image_prompt = "Generate a striking image that captures the essence of the news story."
    
    res = {
        "summary": default_summary,
        "font_color": default_font_color,
        "background_color": default_background_color,
        "font_family": default_font_family,
        "music_prompt": default_music_prompt,
        "image_prompt": default_image_prompt
    }
    
    if len(parts) > 0:
        res["summary"] = parts[0]
    if len(parts) > 1:
        res["font_color"] = parts[1]
    if len(parts) > 2:
        res["background_color"] = parts[2]
    if len(parts) > 3:
        res["font_family"] = parts[3]
    if len(parts) > 4:
        res["music_prompt"] = parts[4]
    if len(parts) > 5:
        res["image_prompt"] = parts[5]

    print(res)

    res_json = json.dumps(res, ensure_ascii=False, indent=4)
    return res_json
