import string
import random
import base64

def encode(id, login):
    token = str(id) + '&' + login
    encodeByte = base64.b64encode(token.encode("utf-8"))
    token = str(encodeByte, "utf-8")
    return token

def decode(token):
    code = base64.b64decode(token)
    codea = code.split("&")
    id = codea[0]
    return id