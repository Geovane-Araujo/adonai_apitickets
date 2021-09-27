import os
import uuid

from flask import Flask, request
from werkzeug.utils import secure_filename

from security.login import loginres
from dynamic_explorer.explorer import explorerdyn
from resources.PessoaUsuarioResource import usuariores
from utils.upload import utilsupload
from flask_cors import CORS
app = Flask(__name__)

CORS(app)

@app.route('/')
def hello_world():
    return 'Não Autorizado'

app.register_blueprint(loginres)
app.register_blueprint(explorerdyn)
app.register_blueprint(usuariores)
app.register_blueprint(utilsupload)

if __name__ == '__main__':
    app.run()
