class PessoaUsuario():
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
        else:
            self.add = obj.get("add")
            self.edit = obj.get("edit")
            self.dele = obj.get("del")
            self.foto = ''
            self.nome = ''
            self.cnpjcpf = ''
            self.rgie = ''
            self.id = ''
