from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")

    try:
        response = requests.post(OLLAMA_URL, json={
            "model": "tinyllama",
            "prompt": prompt,
            "stream": False
        }, timeout=60)

        result = response.json()
        return jsonify({"response": result.get("response", "No response received.")})

    except requests.exceptions.ConnectionError:
        return jsonify({"response": "AI model is still starting up. Please wait a moment and try again."}), 503
    except requests.exceptions.Timeout:
        return jsonify({"response": "The model took too long to respond. Please try again."}), 504

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
