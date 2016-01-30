from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import pprint
from flask.ext.cors import CORS, cross_origin
from os import getcwd
from functions import generate_name, thumbnail

UPLOAD_FOLDER = getcwd()+"/images"
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])



# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

app = Flask(__name__)
#app.wsgi_app = StreamConsumingMiddleware(app.wsgi_app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
CORS(app)

@cross_origin(origin='*')
@app.route('/get_ip', methods=['GET'])
def get_ip():
    return request.remote_addr

@app.route('/images/<path:path>')
def send_js(path):
    return send_from_directory(UPLOAD_FOLDER, path)

@cross_origin(origin='*')
@app.route('/upload', methods=[ 'POST'])
def upload_file():

    f = request.files['file']

    gname = generate_name()
    path = getcwd()
    print(path)
    pprint.pprint(request.files['file'])
    f.save(UPLOAD_FOLDER+'/'+gname+'.jpg')
    thumbnail(UPLOAD_FOLDER+'/'+gname+'.jpg', UPLOAD_FOLDER+'/thumbs/'+gname+'.jpg')

    return gname+'.jpg'

if __name__ == '__main__':
    app.run( debug=True, host='0.0.0.0')
