from flask import Flask, request, jsonify, render_template
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch

app = Flask(__name__)

# Load Pegasus model and tokenizer
model_name = 'google/pegasus-xsum'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name)

# Route to render the main summarization page (we'll make this later)
@app.route('/')
def index():
    return render_template('summarize.html')

# API endpoint for summarization
@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()
    input_text = data.get('text', '')
    if not input_text:
        return jsonify({'error': 'No text provided'}), 400

    # Tokenize and summarize
    tokens = tokenizer(input_text, truncation=True, padding='longest', return_tensors="pt")
    summary_ids = model.generate(**tokens, max_length=60, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
