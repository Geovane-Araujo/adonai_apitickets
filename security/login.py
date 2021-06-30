import json

from flask import Blueprint, request
from pain_crud import methods
from connections import connection

loginres = Blueprint('loginres',__name__, template_folder='security')

@loginres.route('/v1/getAll',methods=['GET'])
def login():
    con = connection.new_connection("adonais1_tickets_0")
    ret = methods.getAll("select * from teste", con)
    return json.dumps(ret)