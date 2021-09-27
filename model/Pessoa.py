import json
from array import array

from model.PessoaEmail import PessoaEmail
from model.PessoaEndereco import PessoaEndereco
from model.PessoaTelefone import PessoaTelefone


class Pessoa():
    def __init__(self,obj):
        if obj != '':
            self.add = obj.get("add")
            self.edit = obj.get("edit")
            self.dele = obj.get("del")
            self.foto = obj.get("foto")
            self.nome = obj.get("nome")
            self.cnpjcpf = obj.get("cnpjcpf")
            self.rgie = obj.get("rgie")
            self.id = obj.get("id")
            self.datanascimento = obj.get("datanascimento")

            self.email = PessoaEmail.toArray(None,obj.get("email"))
            self.telefone = PessoaTelefone.toArray(None,obj.get("telefone"))
            self.endereco = PessoaEndereco(obj.get("endereco"))
        else:
            self.add = True
            self.edit = False
            self.dele = False
            self.foto = ''
            self.nome = ''
            self.cnpjcpf = ''
            self.rgie = ''
            self.id = ''
            self.datanascimento = ''
            self.email = [PessoaEmail('').toJson(),PessoaEmail('').toJson()]
            self.telefone = [PessoaTelefone('').toJson(), PessoaTelefone('').toJson()]
            self.endereco = PessoaEndereco('').toJson()
    def toJson(self):
        return self.__dict__