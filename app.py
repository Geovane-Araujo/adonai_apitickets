from flask import Flask
from security.login import loginres
from dynamic_explorer.explorer import explorerdyn
from flask_cors import CORS
app = Flask(__name__)
CORS(app)



@app.route('/')
def hello_world():
    return 'Não Autorizado'

app.register_blueprint(loginres)
app.register_blueprint(explorerdyn)

if __name__ == '__main__':
    app.run()
