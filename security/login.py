import json

from flask import Blueprint, request
from pain_crud import methods
from connections import connection

loginres = Blueprint('loginres',__name__, template_folder='security')

@loginres.route('/v1/login',methods=['POST'])
def login():
    obj = request.get_json()
    ret = validalogin(obj)
    return json.dumps(ret)


def validalogin(obj):
    cnpj = obj.get('cnpj')
    login = obj.get('login')
    senha = obj.get('senha')

    con = connection.new_connection("adonais1_tickets_0")
    idbanco = methods.getOne(f"select COUNT(id) as contagem from pessoa where cnpjcpf = '{cnpj}'", con)
    if(idbanco['contagem'] == 0):
        ret = {
            "ret": "unsuccess",
            "motivo": "Dados de Login estão incorretos",
            "obj": ""
        }
        return ret