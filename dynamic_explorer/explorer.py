import json

import mysql.connector
from flask import Blueprint, request

from connections import connection
from pain_crud import methods


explorerdyn = Blueprint('explorerdyn',__name__, template_folder='dynamic_explorer')

@explorerdyn.route('/v1/explorer',methods=['GET'])
def dynamicExplorer():
    obj = request.get_json()
    token = request.headers.get('Authorization')
    db = "adonais1_tickets_0"
    resutl = explorerdynamic(obj,db)
    return json.dumps(resutl)


def explorerdynamic(obj, db):
    con = connection.new_connection("adonais1_tickets_0")
    con1 = connection.new_connection(db)
    filters = obj.get("filters")
    paging = obj.get("paging")
    order = obj.get("orders")
    route = obj.get("router")

    try:
        cursor = con.cursor()
        cursor.execute(f"select query from dynamic where route = '{route}'")
        rs = cursor.fetchone()
        sql = rs[0]
        cursor.close()

        try:
            sql = sql + ' ' + filters + ' ' + order
            result = methods.getAll(sql, con1)
            con1.close()
            con.close()
        except mysql.connector.Error as er:
            result = {
                "ret": "unsuccess",
                "motivo": er.msg
            }
    except mysql.connector.Error as er:
        result = {
            "ret": "unsuccess",
            "motivo": er.msg
        }

    return result