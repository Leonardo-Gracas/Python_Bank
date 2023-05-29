import hashlib

class Conta:
    def __init__(self, conta, p_nome, u_nome, cpf, email, senha, funcao = False, renda = False, saldo = False, debito = False):
        self.Conta = conta
        
        self.P_nome = p_nome.capitalize()
        self.U_nome = u_nome.capitalize()
        
        self.Cpf = cpf
        self.Email = email
        
        self.Senha = hashlib.sha1(senha.encode()).hexdigest()
        
        self.Funcao = funcao
        self.Renda = renda
        self.Debito = debito
        self.Saldo = saldo

    def Sacar(self, quantia):
        if(self.Saldo < 0):
            print("Saque negado! --- Cliente negativado")
            return 
        
        if(quantia > self.Saldo):
            print("Saque negado! --- Saldo insuficiente")
            return 
        
        self.Saldo -= quantia
        print(f"Saque de R${quantia:.2f} realizado por {self.P_nome}.")
    
    def Depositar(self, quantia, show=True):
        if quantia <= 0:
            print('---Depósito está abaixo do valor mínimo!!---')
            return
        self.Saldo += quantia
        if(show):
            print(f"Depósito de R${quantia:.2f} realizado por {self.P_nome}.")
    
    def Transacao(self, destinatario, quantia):
        if(self.Saldo < 0):
            print("Transação negada! --- Cliente negativado")
        
        if(quantia > self.Saldo):
            print("Transação negada! --- Saldo insuficiente")
        
        if(quantia <= 0):
            print('---Valor inválido para transação!---')

        destinatario.Depositar(quantia, show=False)
        self.Saldo -= quantia
        print(f"Transação de R${quantia:.2f} feita de {self.P_nome} para {destinatario.P_nome}")

    def Enprestimo(self, valor):
        if(self.Saldo < 0):
            print("Empréstimo negado! --- Cliente negativado")
            return

        if(valor > self.Renda * 0.6):
            print("Empréstimo negado! --- Crédito insuficiente")
            print(f"Valor máximo para conta: R${(self.Renda * 0.6):.2f}.")
            return

        if(self.Debito > 0):
            print("Empréstimo negado! --- Débitos pendentes")
            return

        self.Debito += valor * 1.1
        self.Saldo += valor

        print("Empréstimo realizado!")
        print(f"Saldo atual: R${self.Saldo:.2f}")
        print(f"Débito atual: R${self.Debito:.2f}")

    def PagarDebito(self):
        if(self.Debito > self.Saldo):
            print(f"Débito abatido em R${self.Saldo:.2f}. Conta zerada.")
            self.Debito -= self.Saldo
            self.Saldo = 0
            print(f"Débito restante: R${self.Debito:.2f}.")
        else:
            print(f"Débito de R${self.Debito:.2f} zerado!")
            self.Debito = 0
            self.Saldo -= self.Debito
        

    def Apresentar(self):
        print(f'{self.Conta} - {self.P_nome}.\nSaldo: R${self.Saldo:.2f}\nRenda mensal: R${self.Renda:.2f}')
        if(self.Debito > 0):
            print(f'Débito: R${self.Debito:.2f}')
        pass