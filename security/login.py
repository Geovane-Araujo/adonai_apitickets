import json
import mysql.connector
from flask import Blueprint, request
from utils import security

from PyAtom import methods
from connections import connection

loginres = Blueprint('loginres',__name__, template_folder='security')

@loginres.route('/api/v1/login',methods=['POST'])
def login():
    obj = request.get_json()
    ret = validalogin(obj)
    return json.dumps(ret)


def validalogin(obj):
    cnpj = obj.get('doc')
    login = obj.get('nome')
    senha = obj.get('senha')

    con = connection.new_connection("adonais1_tickets_0")
    idbanco = methods.getOne(f"select id from pessoa where cnpjcpf = '{cnpj}'", con)
    if(idbanco == None):
        ret = {
            "ret": "unsuccess",
            "motivo": "Dados de Login estão incorretos",
            "obj": ""
        }
        return ret
    else:
        con.close()
        if(idbanco['id'] == 1):
            idbanco['id'] = 0
        con = connection.new_connection("adonais1_tickets_"+ str(idbanco['id']))
        try:
            login = methods.getOne(
                f"select pessoa.id,login,nome from pessoa_usuario inner join pessoa on pessoa.id = pessoa_usuario.idpessoa "
                f"where login like '{login}'and senha = '{senha}'", con)
        except mysql.connector.Error as err:
            ret = {
                "ret": "unsuccess",
                "motivo": err.msg,
                "obj": ""
            }
            return ret

        if(login == None):
            ret = {
                "ret": "unsuccess",
                "motivo": "Dados de Login estão incorretos",
                "obj": ""
            }
            return ret
        else:
            token = security.encode(idbanco['id'],login['login'])
            ret = {
                "ret": "success",
                "motivo": "OK",
                "obj": json.dumps(login),
                "token": token
            }
            con.close()
            return ret