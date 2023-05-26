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
    renda = float(args[1])
    conta = orm.get_new_id()
    saldo = 0
    users.append(orm.create(conta, nome, renda, saldo))

def Atualizar(args=False):
    def Depositar(args):
        args = args.split()
        contaId = args[0]
        valor = float(args[1])
        conta = Ler(contaId, show=False)
        conta.Depositar(valor)
        for index, user in enumerate(users):
            if(user.Conta == conta.Conta):
                users[index] = conta
    
    def Sacar(args):
        args = args.split()
        contaId = args[0]
        valor = float(args[1])
        conta = Ler(contaId, show=False)
        conta.Sacar(valor)
        for index, user in enumerate(users):
            if(user.Conta == conta.Conta):
                users[index] = conta

    def Transferencia(args):
        args = args.split()
        contaId = args[0]
        valor = float(args[1])
        destinatario = Ler(args[2], show=False)
        conta = Ler(contaId, show=False)
        conta.Transacao(destinatario, valor)
        for index, user in enumerate(users):
            if(user.Conta == conta.Conta):
                users[index] = conta
        for index, user in enumerate(users):
            if(user.Conta == destinatario.Conta):
                users[index] = destinatario
        
    def Emprestimo(args):
        args = args.split()
        valor = float(args[1])
        contaId = args[0]
        conta = Ler(contaId, show=False)
        conta.Enprestimo(valor)
        for index, user in enumerate(users):
            if(user.Conta == conta.Conta):
                users[index] = conta

    def Pagar_Debitos(contaId):
        conta = Ler(contaId, show=False)
        conta.PagarDebito()
        for index, user in enumerate(users):
            if(user.Conta == conta.Conta):
                users[index] = conta

    cmd_list = [
        ('d', Depositar),
        ('s', Sacar),
        ('t', Transferencia),
        ('e', Emprestimo),
        ('p', Pagar_Debitos)
    ]
    
    if(args == False):
        print('---([D]epositar, [S]acar, [T]ransferir, [P]agar, [E]mpréstimo), Numero da conta, parametros---')
        args = input('>>> ')
    args = args.lower()
    args = args.split()

    for command in cmd_list:
        if (command[0] == args[0]):
            if(command[0] == args[0]):
                function = command[1]
                if (len(args) > 1):
                    args = " ".join(args[1:])
                    function(args)
                else:                
                    function()
                break
    orm.update(users)

def Ler(args=False, show=True):
    if(args == False):
        print('---Digite o número da conta a ser lida:')
        args = input('>>> ')
    args = args.lower()
    args = args.split()

    response = orm.read(float(args[0]))
    if response == False:
        return

    if(show == True):
        print('---------------------')
        response.Apresentar()
        print('---------------------\n')
    

    return response

def Deletar(params=False):
    global users

    args = ''
    if(params != False):
        args = params
    else:
        print('---Digite o número da conta a ser deletada:')
        args = input('>>> ')
    args = args.lower()
    args = args.split()

    try:
        numConta = int(args[0])
    except:
        print("---Entrada inválida!---")
        return

    old = orm.delete(numConta)
    old.Apresentar()
    print('---Deletado---')

def Listar():
    users = orm.list()