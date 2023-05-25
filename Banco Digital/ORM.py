from Conta import Conta as Conta
import json

def user_to_json(user):
    obj = {
        "conta": user.Conta,
        "nome": user.Nome,
        "saldo": user.Saldo,
        "renda": user.Renda,
        "debito": user.Debito
    }
    return obj

def json_to_user(json):
    user = Conta(json["conta"], json["nome"], json["renda"], json["saldo"], ORM(), json["debito"])
    return user


class ORM:
    def __init__(self):
        pass

    def create(conta, nome, renda, saldo, orm):
        user = Conta(conta, nome, renda, saldo, orm)
        
        with open('users.json', 'r+') as f:
            newUser = user_to_json(user)
            obj = json.loads(f.read())
            obj.append(newUser)
            f.seek(0)
            f.write(json.dumps(obj, indent=2))
            f.truncate()
        
        user.Apresentar()
        return user

    def read():
        print("Usuário tal")

    def update():
        print("Usuario tal atualizado")
    
    def delete():
        print("Usuário tal deletado")

    def list():
        resp = []
        with open('users.json', 'r') as f:
            obj = json.loads(f.read())
            for user_json in obj:
                resp.append(json_to_user(user_json))
        
        print('')
        for user in resp:
            print("-------------------------")
            user.Apresentar()
            print("-------------------------\n")
        
        return resp