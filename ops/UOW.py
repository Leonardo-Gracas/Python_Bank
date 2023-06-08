from contextlib import nullcontext
import json
from ops.ORM import ORM as orm
from ops.Conta import Conta as Conta

users = orm.list()
banco = orm.get_bank()

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

def get_args(args, message):
    if(args == False):
        print(message)
        args = input('>>> ')
    args = args.lower()
    args = args.split()
    return args

def Criar(nome, renda):
    global users
    conta = orm.get_new_id() 
    saldo = 0
    users.append(orm.create(conta, nome, renda, saldo)) 

def Depositar(contaId, valor):
    for user in users:
        if(user.Conta == contaId):
            message = user.Depositar(valor)
            orm.update(users)
            return message
    else:
        return "Usuário não encontrado"

def Sacar(contaId, valor):
    for user in users:
        if(user.Conta == contaId):
            message = user.Sacar(valor)
            orm.update(users)
            return message
    else:
        return "Usuário não encontrado"

def Transferencia(contaId, valor, destinatario):
    for user in users:
        if(user.Conta == destinatario):
            destinatario = user
            break
    else:
        return "Destinatario não encontrado"
    for user in users:
        if(user.Conta == contaId):
            message = user.Transacao(valor, destinatario)
            orm.update(users)
            return message
    else:
        return "Usuário não encontrado"
        
def Emprestimo(contaId, valor):
    for user in users:
        if(user.Conta == contaId):
            message = user.Emprestimo(valor)
            orm.update(users)
            return message
    else:
        return "Usuário não encontrado"

def Pagar_Debitos(contaId):
    for index, user in enumerate(users):
        if(user.Conta == contaId):
            message = user.PagarDebito()
            orm.update(users)
            return message

def Ler(id, show=True):
    response = orm.read(id)
    return response

def Deletar(contaId):
    global users
    message = orm.delete(contaId)
    users = orm.list()
    return f'Usuário {message} deletado!'

def Listar():
    users = orm.list()
    resp = []
    for user in users:
        resp.append(user_to_json(user) )
    return resp

def Pegar_Banco():
    banco = orm.get_bank()
    response = {
        "nome": banco.Nome,
        "agencia": banco.Agencia,
        "saldo": banco.Saldo,
        "saldoCorrente": banco.Saldo_Corrente
    }
    return response

def Cobrar_Anuidade():
    banco.cobrar_anuidade(users)
    orm.update(users)
    orm.set_bank(banco)

def Passar_Mes():
    # recebe o valor de rendimento e divide entre os usuários tendo o saldo parado como parâmetro
    # renda = 300
    # saldo1 = 100 (2/5)
    # saldo2 = 150 (3/5)
    # saldototal = 250
    # parte1 = 100/250 = 2/5
    # saldo1 += renda * parte1 = 120

    renda_user = banco.passar_mes()
    saldo_total = 0
    for user in users:
        saldo_total += user.Saldo

    tres_meses_negativo = False
    for user in users:
        print(user.Nome)
        if(saldo_total != 0):
            renda_mes = user.Saldo / saldo_total
            renda_mes *= renda_user
            if user.Debito >= renda_mes:
                renda_mes = 0
                user.Debito -= renda_mes
            else:
                renda_mes -= user.Debito
                user.Debito = 0
            user.Depositar(renda_mes, show=False)
        if user.Passar_Mes() == tres_meses_negativo:
            Deletar(str(user.Conta))
            users.remove(user)

    banco.cobrar_anuidade(users)

    orm.set_bank(banco)
    orm.update(users)
    return "Sucesso"