from flask import Flask
from security.login import loginres
from flask_cors import CORS
app = Flask(__name__)
CORS(app)



@app.route('/')
def hello_world():
    return 'Não Autorizado'

app.register_blueprint(loginres)

if __name__ == '__main__':
    app.run()
