# service-a/app.py
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    try:
        # Call service-b via Kubernetes DNS name
        # hardcode this to "http://localhost:6000/data" to test locally
        response = requests.get("http://service-b:6000/data").json()
        return jsonify({
        "message": "Received from Service B",
        "data": response})
    except Exception as e:
        return f"Error reaching Service B: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
