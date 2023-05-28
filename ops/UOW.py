from .ORM import ORM as orm
from flask import session

users = orm.list()

def validar_cpf(cpf):
    # Remover caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificar se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificar se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Verificar o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto

    if int(cpf[9]) != digito_verificador_1:
        return False

    # Verificar o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto

    if int(cpf[10]) != digito_verificador_2:
        return False

    return True

def Criar(p_nome, u_nome, cpf, email, senha):
    global users
    id_conta = orm.get_new_id()
    
    for conta in orm.get_contas():
        if conta['cpf'] == cpf:
            session['msg'] == "Não foi possível criar conta. CPF já utilizado."
            return 'cpf'
        
        elif conta['email'] == email:
            return 'email'
    
    users.append(orm.create(id_conta, p_nome, u_nome, cpf, email, senha))
    return True
    
def verificar_credenciais(email, senha):
    print(orm.list())
    for conta in orm.get_contas():
        if conta['email'] == email and conta['senha'] == senha:
            print('aaaaaaaaaaaaaaaa')
            print(conta['conta'])
            return conta['conta']
    return None

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