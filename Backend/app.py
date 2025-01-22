

from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import openai
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Load Hugging Face Emotion Detection Model
emotion_pipeline = pipeline("sentiment-analysis", model="j-hartmann/emotion-english-distilroberta-base")

# OpenAI API Key from environment variable
openai.api_key = os.getenv("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")

# Route to analyze user input
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    user_input = data.get("text", "")

    # Input validation
    if not user_input.strip():
        return jsonify({"error": "Input text cannot be empty."}), 400

    # Emotion detection
    emotion_result = emotion_pipeline(user_input)
    emotion = emotion_result[0]['label']

    # GPT-4 response
    gpt_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"The user is feeling {emotion}. Provide a supportive message."}]
    )

    response_text = gpt_response["choices"][0]["message"]["content"]

    return jsonify({
        "emotion": emotion,
        "response": response_text
    })

# Sample Input-Output Testing Route
@app.route('/test-sample', methods=['GET'])
def test_sample():
    sample_input = "I feel so stressed and overwhelmed lately."
    
    # Emotion detection
    emotion_result = emotion_pipeline(sample_input)
    emotion = emotion_result[0]['label']

    # GPT-4 response
    gpt_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"The user is feeling {emotion}. Provide a supportive message."}]
    )

    response_text = gpt_response["choices"][0]["message"]["content"]

    # Output for demonstration
    return jsonify({
        "sample_input": sample_input,
        "emotion_detected": emotion,
        "gpt_response": response_text
    })

if __name__ == '__main__':
    app.run(debug=True)
