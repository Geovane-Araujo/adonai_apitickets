import os
import uuid

from flask import Blueprint, request, Flask
from werkzeug.utils import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER_IMAGES = '../static/imagens'
app.config['UPLOAD_FOLDER_IMAGES'] = UPLOAD_FOLDER_IMAGES

utilsupload = Blueprint('utilsupload',__name__, template_folder='utils')

@utilsupload.route('/upload', methods = ['GET', 'POST'])
def upload_arquivos():
    #verifica se tem arquivo na requisição
    if 'file' not in request.files:
        return 'Não há arquivo'
    basedir = os.path.abspath(os.path.dirname(__file__))
    file = request.files['file']
    filename = secure_filename(file.filename)
    extension = filename.split('.')
    name_file = f'{uuid.uuid4()}.{extension[len(extension) -1]}'
    file.save(os.path.join(basedir,app.config['UPLOAD_FOLDER_IMAGES'],name_file))
    return f'{name_file}'