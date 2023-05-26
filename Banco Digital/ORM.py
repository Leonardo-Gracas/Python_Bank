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
    user = Conta(json["conta"], json["nome"], json["renda"], json["saldo"], json["debito"])
    return user


class ORM:
    def __init__(self):
        pass

    def get_new_id():
        with open('system.json', 'r+') as system:
            obj = json.loads(system.read())
            obj['id_fabric'] += 1
            conta = obj['id_fabric']
            system.seek(0)
            system.write(json.dumps(obj, indent=2))
            system.truncate()
        return conta

    def create(conta, nome, renda, saldo):
        user = Conta(conta, nome, renda, saldo)
        
        with open('users.json', 'r+') as f:
            newUser = user_to_json(user)
            obj = json.loads(f.read())
            obj.append(newUser)
            f.seek(0)
            f.write(json.dumps(obj, indent=2))
            f.truncate()
        
        user.Apresentar()
        return user

    def read(id):
        with open('users.json', 'r') as f:
            obj = json.loads(f.read())
            for user in obj:
                if(user['conta'] == id):
                    account = json_to_user(user)
                    return account
            else:
                print("Usuário não encontrado!")
                return False

    def update(users):
        with open('users.json', 'w') as f:
            newData = [user_to_json(user) for user in users]
            f.seek(0)
            f.write(json.dumps(newData, indent=2))
            f.truncate()

    def delete(id):
        old_user = ''
        with open('users.json', 'r+') as f:
            obj = json.loads(f.read())
            for user in obj:
                if(user['conta'] == id):
                    obj.remove(user)
                    old_user = json_to_user(user)
                    break
            f.seek(0)
            f.write(json.dumps(obj, indent=2))
            f.truncate()
        return old_user
        

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