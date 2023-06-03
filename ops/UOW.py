from .ORM import ORM as orm

users = orm.list()
banco = orm.get_bank()

def get_args(args, message):
    if(args == False):
        print(message)
        args = input('>>> ')
    args = args.lower()
    args = args.split()
    return args

def Criar(args=False):
    global users
    args = get_args(args, '---Digite os dados "nome, renda"---')

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
    
    args = get_args(args, '---([D]epositar, [S]acar, [T]ransferir, [P]agar, [E]mpréstimo), Numero da conta, parametros---')

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

def Ler(id, return_json=False):
    response = orm.read(id, return_json)
    if response == False:
        return
    
    return response

def Deletar(args=False):
    global users

    args = get_args(args, '---Digite o número da conta a ser deletada:')

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
    return users

def Apresentar_Banco():
    banco = orm.get_bank()
    banco.apresentar()

# def Cobrar_Anuidade():
#     banco.cobrar_anuidade(users)
#     orm.update(users)
#     orm.set_bank(banco)

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