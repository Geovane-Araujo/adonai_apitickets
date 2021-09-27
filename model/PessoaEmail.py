class PessoaEmail():
    def __init__(self,obj):
        if obj != '':
            self.add = obj.get("add")
            self.edit = obj.get("edit")
            self.dele = obj.get("del")
            self.tipo = obj.get("tipo")
            self.id = obj.get("id")
            self.idpessoa = obj.get("idpessoa")
            self.email = obj.get("email")
        else:
            self.add = True
            self.edit = False
            self.dele = False
            self.tipo = ''
            self.id = ''
            self.idpessoa = ''
            self.email = ''
    def toJson(self):
        return self.__dict__
