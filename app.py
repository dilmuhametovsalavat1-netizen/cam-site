from flask import Flask, request, jsonify, send_from_directory
import base64, time, os

app = Flask('cam', static_folder='static')
SAVE_DIR = 'shots'
os.makedirs(SAVE_DIR, exist_ok=True)

@app.route('/')
def index():
return send_from_directory('static', 'index.html')

@app.route('/upload', methods=['POST'])
def upload():
data = request.get_json(force=True)
img = data['image'].split(',')[1]
name = str(int(time.time())) + '.jpg'
path = os.path.join(SAVE_DIR, name)
f = open(path, 'wb')
f.write(base64.b64decode(img))
f.close()
return jsonify({'ok': True})

@app.route('/shots')
def shots():
files = sorted(os.listdir(SAVE_DIR), reverse=True)
html = '<h2>Snimki: ' + str(len(files)) + '</h2>'
for f in files:
html += '<div><a href=/shots/' + f + '>' + f + '</a>
'
html += '<img src=/shots/' + f + ' width=200></div>'
return html

@app.route('/shots/<name>')
def shot_file(name):
return send_from_directory(SAVE_DIR, name)
