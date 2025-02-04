from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Hugging Face 모델 로딩 (예: GPT-2)
model = pipeline('text-generation', model='gpt2')

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.get_json()
    prompt = data.get('prompt', '')
    result = model(prompt, max_length=50)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
