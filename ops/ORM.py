from .Conta import Conta as Conta
import json
import os


# Obter o caminho completo do arquivo atualmente em execução
caminho_atual = os.path.abspath(__file__)

# Extrair o diretório pai do caminho do arquivo
diretorio_atual = os.path.dirname(caminho_atual)

# Combinar o diretório atual com o nome do arquivo JSON
caminho_arquivo_users = os.path.join(diretorio_atual, 'users.json')
caminho_arquivo_id = os.path.join(diretorio_atual, 'system.json')


def user_to_json(user):
    obj = {
        "conta": user.Conta,
        "p_nome": user.P_nome,
        "u_nome" : user.U_nome,
        "cpf" : user.Cpf,
        "email" : user.Email,
        "senha" : user.Senha,
        "saldo": "",
        "renda": "",
        "debito": ""
        
        # "saldo": user.Saldo,
        # "renda": user.Renda,
        # "debito": user.Debito
    }
    
    return obj

def json_to_user(json):
    user = Conta(json["conta"], json["p_nome"], json["u_nome"],
                 json["cpf"], json["email"], json["senha"],
                 json["renda"], json["saldo"], json["debito"]
                )
    return user


class ORM:
    def __init__(self):
        pass

    def get_new_id():
        with open(caminho_arquivo_id, 'r+') as system:
            obj = json.loads(system.read())
            obj['id_fabric'] += 1
            conta = obj['id_fabric']
            system.seek(0)
            system.write(json.dumps(obj, indent=2))
            system.truncate()
        return conta

    def create(id_conta, p_nome, u_nome, cpf, email, senha):
        user = Conta(id_conta, p_nome, u_nome, cpf, email, senha)
        
        with open(caminho_arquivo_users, 'r+') as f:
            newUser = user_to_json(user)
            obj = json.loads(f.read())
            obj.append(newUser)
            f.seek(0)
            f.write(json.dumps(obj, indent=2))
            f.truncate()
        
        user.Apresentar()
        return user

    def read(id):
        with open(caminho_arquivo_users, 'r') as f:
            obj = json.loads(f.read())
            for user in obj:
                if(user['conta'] == id):
                    account = json_to_user(user)
                    return account
            else:
                print("Usuário não encontrado!")
                return False

    def update(users):
        with open(caminho_arquivo_users, 'w') as f:
            newData = [user_to_json(user) for user in users]
            f.seek(0)
            f.write(json.dumps(newData, indent=2))
            f.truncate()

    def delete(id):
        old_user = ''
        with open(caminho_arquivo_users, 'r+') as f:
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
        with open(caminho_arquivo_users, 'r') as f:
            obj = json.loads(f.read())
            for user_json in obj:
                resp.append(json_to_user(user_json))
        
        return resp
    
    def get_contas():
        with open(caminho_arquivo_users, 'r') as f:
            obj = json.loads(f.read())
            return obj
