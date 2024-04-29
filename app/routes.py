from flask import request, jsonify
from app import app
from .models import translate_text

@app.route('/')
def index():
    return "TEST"

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text')
    target_language = data.get('target_language')

    if not text or not target_language:
        return jsonify({'error': 'Missing required fields'}), 400

    translated_text = translate_text(text, target_language)
    return jsonify({'translated_text': translated_text})
