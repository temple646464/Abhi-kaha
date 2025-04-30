
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "TXT Uploader is running."

@app.route("/upload", methods=["POST"])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']
    if not file.filename.endswith('.txt'):
        return jsonify({"error": "Only .txt files allowed"}), 400
    content = file.read().decode("utf-8")
    return jsonify({"filename": file.filename, "content": content})
