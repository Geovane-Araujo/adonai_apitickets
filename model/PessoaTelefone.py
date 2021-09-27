class PessoaTelefone():
    def __init__(self,obj):
        if obj != '':
            self.add = obj.get("add")
            self.edit = obj.get("edit")
            self.dele = obj.get("del")
            self.id = obj.get("id")
            self.idpessoa = obj.get("idpessoa")
            self.fone = obj.get("fone")
            self.tipo = obj.get("tipo")
        else:
            self.add = True
            self.edit = False
            self.dele = False
            self.id = ''
            self.idpessoa = ''
            self.fone = ''
            self.tipo = ''
    def toJson(self):
        return self.__dict__
    def toArray(self,obj):
        arra = []
        for fl in obj:
            arra.append(PessoaTelefone(fl))
        return arra
