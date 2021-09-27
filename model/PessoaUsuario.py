import json

from model.Pessoa import Pessoa


class PessoaUsuario():
    def __init__(self,obj):
        if obj != '':
            self.add = obj.get("add")
            self.edit = obj.get("edit")
            self.dele = obj.get("del")
            self.senha = obj.get("senha")
            self.idpessoa = obj.get("idpessoa")
            self.login = obj.get("login")
            self.id = obj.get("id")
            self.pessoa = Pessoa(obj.get("pessoa"))
        else:
            self.add = True
            self.edit = False
            self.dele = False
            self.senha = ''
            self.idpessoa = ''
            self.login = ''
            self.id = ''
            self.pessoa = Pessoa('').toJson()
    def toJson(self):
        return self.__dict__
