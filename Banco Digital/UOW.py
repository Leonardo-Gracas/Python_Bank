from ORM import ORM as orm

users = orm.list()

def Criar(params=False):
    global users

    args = ''
    if(params != False):
        args = params
    else:
        print('---Digite os dados "nome, renda"---')
        args = input('>>> ')
    args = args.lower()
    args = args.split()

    nome = args[0]
    renda = int(args[1])
    numConta = len(users) + 100
    saldo = 0
    users.append(orm.create(numConta, nome, renda, saldo, orm))

def Atualizar():
    orm.update()

def Ler():
    orm.update()

def Deletar():
    orm.delete()

def Listar():
    users = orm.list()