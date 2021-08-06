import re
from flask import Flask, Response, request
from flask import request
from flask_cors import CORS
from facerec_rtree import KNNRtree
import base64, json

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
SAVE_FOLDER = './data/saved'
fileCount = 1

app = Flask(__name__)
cors = CORS(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_image():
    global fileCount
    data = json.loads(request.data)
    if 'file' not in data:
        return 'File not found'
    if data['file'] == None:
        return 'Invalid file'
    imageParts = data['file'].split(';base64,')
    file = base64.b64decode(imageParts[1])
    filename = '{}/uploaded-file-{}.jpeg'.format(SAVE_FOLDER, str(fileCount))
    with open(filename, 'wb+') as f:
        f.write(file)
    fileCount += 1
    # Process image
    result = list(KNNRtree(2, filename, 2000))
    name = result[0]['name']
    nameParts = name.split('_')
    name = nameParts[0] + ' ' + nameParts[1]
    msg = {'name': name}
    return Response(json.dumps(msg), 200)


def processImage(img):
    encoding = images.getEncoding(img)
    print(encoding)
