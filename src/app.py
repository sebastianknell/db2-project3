from flask import Flask, Response, request
from flask import request
from flask_cors import CORS
import images
import base64, json

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
SAVE_FOLDER = './data/saved'

app = Flask(__name__)
cors = CORS(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_image():
    data = json.loads(request.data)
    if 'file' not in data:
        return 'File not found'
    imageParts = data['file'].split(';base64,')
    file = base64.b64decode(imageParts[1])
    with open('{}/uploaded-file.jpeg'.format(SAVE_FOLDER), 'wb+') as f:
        f.write(file)
    return 'Ok'


def processImage(img):
    encoding = images.getEncoding(img)
    print(encoding)