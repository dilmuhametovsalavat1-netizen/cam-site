from flask import Flask, request, jsonify, send_from_directory
import base64, time, os

app = Flask(name, static_folder='static')
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

@app.route("/shots")
def shots():
files = sorted(os.listdir(SAVE_DIR), reverse=True)
links = "".join(f'<div><a href="/shots/{f}">{f}</a>
<img src="/shots/{f}" width="200"></div>' for f in files)
return f"<h2>Снимки ({len(files)})</h2>{links}"

@app.route("/shots/<name>")
def shot_file(name):
return send_from_directory(SAVE_DIR, name)

if name == "main":
app.run()
