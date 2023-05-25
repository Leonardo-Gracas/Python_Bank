import ORM

class Conta:
    def __init__(self, conta, nome, renda, saldo, orm):
        self.Nome = nome
        self.Conta = conta
        self.Renda = renda
        self.Debito = 0
        self.Saldo = saldo
        self.ORM = orm

        self.Apresentar()

    def Sacar(self, quantia):
        if(self.Saldo < 0):
            return "Saque negado! --- Cliente negativado"
        
        if(quantia > self.Saldo):
            return "Saque negado! --- Saldo insuficiente"
        
        self.Saldo -= quantia
        self.ORM.Update(self)
        
        return "Saque concluído"
    
    def Depositar(self, quantia):
        self.Saldo += quantia
        self.ORM.Update(self)

        return "Depósito concluído"
    
    def Transacao(self, conta, quantia):
        if(self.Saldo < 0):
            return "Transação negada! --- Cliente negativado"
        
        if(quantia > self.Saldo):
            return "Transação negada! --- Saldo insuficiente"

        destinatario = self.orm.Read(conta)
        destinatario.Depositar(quantia)

        self.Sacar(quantia)

        return "Transação concluida."

    def Enprestimo(self, valor):
        if(self.Saldo < 0):
            return "Empréstimo negado! --- Cliente negativado"

        if(valor > self.Renda * 0.6):
            return "Empréstimo negado! --- Crédito insuficiente"

        if(self.Debito > 0):
            return "Empréstimo negado! --- Débitos pendentes"

        self.Debito += (valor * 1.1)
        self.Depositar(valor)

        return "Empréstimo realizado!"

    def PagarDebito(self):
        if(self.Debito > self.Saldo):
            self.Debito -= self.Saldo
            self.Sacar(self.Saldo)
        else:
            self.Debito = 0
            self.Sacar(self.Debito)

    def Apresentar(self):
        print(f'{self.Conta} - {self.Nome} - {self.Saldo} - {self.Renda} - {self.Debito}')