import json
import mysql
from flask import Blueprint, request

from connections import connection
from controller.PessoaUsuarioController import PessoaUsuarioController
from model.Pessoa import Pessoa
from model.PessoaUsuario import PessoaUsuario

usuariores = Blueprint('usuariores',__name__, template_folder='resources')

@usuariores.route('/api/v1/usuario',methods=['POST'])
def save():
    obj = request.get_json()
    controller = PessoaUsuarioController()
    try:
        con = connection.new_connection("adonais1_tickets_0")
        obj = controller.save(obj,con)
        ret = {
            "ret": "success",
            "motivo": "Dados de Login estão incorretos",
            "obj": json.dumps(obj.__dict__)
        }
    except mysql.connector.Error as er:
        ret = {
            "ret": "unsuccess",
            "motivo": er.msg
        }
    finally:
        con.close()
    return json.dumps(ret)

@usuariores.route('/api/v1/usuario', methods=['GET'])
def getById():
    controller = PessoaUsuarioController()
    id = request.args.get("id")
    try:
        con = connection.new_connection("adonais1_tickets_0")
        if int(id) == -100:
            obj = PessoaUsuario('')
        else:
            obj = controller.get(con, id)

        ret = {
            "ret": "success",
            "motivo": "Dados de Login estão incorretos",
            "obj": obj.toJson()
        }
    except mysql.connector.Error as er:
        ret = {
            "ret": "unsuccess",
            "motivo": er.msg
        }
    finally:
        if con != None:
            con.close()

    return json.dumps(ret)