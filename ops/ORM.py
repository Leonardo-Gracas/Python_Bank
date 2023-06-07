from ops.Conta import Conta as Conta
from ops.Banco import Banco as Banco
import json
import os


# Obter o caminho completo do arquivo atualmente em execução
caminho_atual = os.path.abspath(__file__)

# Extrair o diretório pai do caminho do arquivo
diretorio_atual = os.path.dirname(caminho_atual)

# Combinar o diretório atual com o nome do arquivo JSON
caminho_arquivo = os.path.join(diretorio_atual, '../users.json')

# Combinar o diretório atual com o nome do arquivo system.json
caminho_system = os.path.join(diretorio_atual, '../system.json')


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
        ...

    def get_new_id():
        with open(caminho_system, 'r+') as system:
            obj = json.loads(system.read())
            obj['id_fabric'] += 1
            conta = obj['id_fabric']
            system.seek(0)
            system.write(json.dumps(obj, indent=2))
            system.truncate()
        return conta

    def create(conta, nome, renda, saldo):
        user = Conta(conta, nome, renda, saldo)
        
        with open(caminho_arquivo, 'r+') as f:
            newUser = user_to_json(user)
            obj = json.loads(f.read())
            obj.append(newUser)
            f.seek(0)
            f.write(json.dumps(obj, indent=2))
            f.truncate()
        
        return user

    def read(id):
        with open(caminho_arquivo, 'r') as f:
            obj = json.loads(f.read())
            for user in obj:
                if(user['conta'] == id):
                    return user
            else:
                print("Usuário não encontrado!")
                return False

    def update(users):
        with open(caminho_arquivo, 'w') as f:
            newData = [user_to_json(user) for user in users]
            f.seek(0)
            f.write(json.dumps(newData, indent=2))
            f.truncate()

    def delete(id):
        old_user = ''
        with open(caminho_arquivo, 'r+') as f:
            obj = json.loads(f.read())
            for user in obj:
                if(user['conta'] == id):
                    obj.remove(user)
                    old_user = json_to_user(user)
                    f.seek(0)
                    f.write(json.dumps(obj, indent=2))
                    f.truncate()
                    return old_user.Nome
            else: return "Usuário não encontrado"

    def list():
        resp = []
        with open(caminho_arquivo, 'r') as f:
            obj = json.loads(f.read())
            for user_json in obj:
                resp.append(json_to_user(user_json))
        
        return resp

    def get_bank():
        with open(caminho_system, 'r') as f:
            data = json.loads(f.read())
        with open(caminho_arquivo, 'r') as f:
            users = []
            users_json = json.loads(f.read())
            for user_json in users_json:
                users.append(json_to_user(user_json))

        bank = Banco(data['nome'], data['agencia'], data['saldo_banco'], users)
        return bank
    
    def set_bank(bank):
        with open(caminho_system, 'w') as f:
            newData = {
                "id_fabric": 105,
                "nome": "Banco Digital",
                "agencia": 99,
                "saldo_banco": bank.Saldo,
                "saldo_corrente": bank.Saldo_Corrente
            }
            f.seek(0)
            f.write(json.dumps(newData, indent=2))
            f.truncate()