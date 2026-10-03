from flask import Flask, request, jsonify, send_from_directory
import base64, time, os

app = Flask(__name__, static_folder='static')
SAVE_DIR = "shots"
os.makedirs(SAVE_DIR, exist_ok=True)

@app.route("/")
def index():
    return send_from_directory('static', 'index.html')

@app.route("/upload", methods=["POST"])
def upload():
    data = request.get_json(force=True)
    img = data["image"].split(",")[1]
    name = f"{int(time.time())}.jpg"
    with open(os.path.join(SAVE_DIR, name), "wb") as f:
        f.write(base64.b64decode(img))
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run()
