from PyAtom.methods import insertone,updateone,getOne,deletedone
class PessoaUsuarioController():

    def save(self, obj,con):
        if(obj.add):
            id = insertone(obj.pessoa,"pessoa",con)
        return "OK"

    def getByID(self,con,id):
        return "OK"