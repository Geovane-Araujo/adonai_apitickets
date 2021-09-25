import json

import mysql.connector
from flask import Blueprint, request

from connections import connection
from PyAtom import methods


explorerdyn = Blueprint('explorerdyn',__name__, template_folder='dynamic_explorer')

@explorerdyn.route('/api/v1/explorer',methods=['POST'])
def dynamicExplorer():
    obj = request.get_json()
    token = request.headers.get('Authorization')
    db = "adonais1_tickets_0"
    resutl = explorerdynamic(obj,db)
    return json.dumps(resutl)

@explorerdyn.route('/api/v1/explorerdeleted',methods=['DELETE'])
def dynamicDeletedExplorer():
    token = request.headers.get('Authorization')
    id = request.args.get("id")
    campo = request.args.get("campo")
    db = "adonais1_tickets_0"
    resutl = deletedynamic(id,campo,db)
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
        cursor.execute(f"select query,tablebase from dynamic where route = '{route}'")
        rs = cursor.fetchone()
        sql = rs[0]
        tablebase = rs[1]
        cursor.close()

        try:
            sql = sql + ' ' + filters + ' ' + order
            result = methods.getAll(sql, con1)

            sql = "SELECT COUNT(id) as count from " + tablebase + " " + filters
            cursor = con1.cursor()
            cursor.execute(sql)
            rs = cursor.fetchone()
            totalRecords = rs[0]
            con1.close()
            con.close()

            result = {
                "ret": "success",
                "motivo": "OK",
                "totalRecords": totalRecords,
                "obj": result
            }

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


def deletedynamic(id, campo, db):
    con = connection.new_connection(db)
    try:

        cursor = con.cursor()
        cursor.execute(f"DELETE FROM {campo} where id = {id}")
        cursor.close()

        result = {
            "ret": "success",
            "motivo": "OK",
        }
    except mysql.connector.Error as er:
        result = {
            "ret": "unsuccess",
            "motivo": er.msg
        }

    return result