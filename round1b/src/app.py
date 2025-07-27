from flask import Flask, jsonify
from utils import analyze_document

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Round 1B Analyzer"})

@app.route('/analyze')
def analyze():
    result = analyze_document()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
