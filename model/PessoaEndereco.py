class PessoaEndereco():
    def __init__(self,obj):
        if obj != '':
            self.add = obj.get("add")
            self.edit = obj.get("edit")
            self.dele = obj.get("del")
            self.endereco = obj.get("endereco")
            self.idpessoa = obj.get("idpessoa")
            self.idcidade = obj.get("idcidade")
            self.complemento = obj.get("complemento")
            self.id = obj.get("id")
            self.bairro = obj.get("bairro")
            self.cep = obj.get("cep")
            self.numero = obj.get("numero")
        else:
            self.add = True
            self.edit = False
            self.dele = False
            self.endereco = ''
            self.idpessoa = ''
            self.idcidade = ''
            self.complemento = ''
            self.id = ''
            self.bairro = ''
            self.cep = ''
            self.numero = ''
    def toJson(self):
        return self.__dict__
