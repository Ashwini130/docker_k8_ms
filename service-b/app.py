# service-b/app.py
from flask import Flask, jsonify

app = Flask(__name__)

counter = 0

@app.route("/data")
def data():
    global counter
    counter += 1
    return jsonify({"counter": counter})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
