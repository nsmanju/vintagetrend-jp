from flask import Flask, jsonify, render_template
import json, os
app = Flask(__name__)
JSON_PATH = os.path.join(os.path.dirname(__file__), "trends.json")

@app.route("/api/trends")
def api():
    if not os.path.exists(JSON_PATH): return jsonify([])
    with open(JSON_PATH) as f: return jsonify(json.load(f))

@app.route("/")
def home(): return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
