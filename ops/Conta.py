class Conta:
    def __init__(self, conta, nome, renda, saldo,  debito=0):
        self.Conta = conta
        self.Nome = nome.capitalize()
        self.Renda = renda
        self.Debito = debito
        self.Saldo = saldo
        self.Faltas = 0

    def Sacar(self, quantia):
        if(self.Saldo < 0):
            return "Saque negado! --- Cliente negativado"
        
        if(quantia > self.Saldo):
            return "Saque negado! --- Saldo insuficiente"
        
        self.Saldo -= quantia
        return f"Saque de R${quantia:.2f} realizado por {self.Nome}."
    
    def Depositar(self, quantia, show=True):
        if quantia <= 0:
            return'---Depósito está abaixo do valor mínimo!!---'
        
        self.Saldo += quantia
        return f"Depósito de R${quantia:.2f} realizado por {self.Nome}."
    
    def Transacao(self, quantia, destinatario):
        if(self.Saldo < 0):
            return "Transação negada! --- Cliente negativado"
        
        if(quantia > self.Saldo):
            return "Transação negada! --- Saldo insuficiente"
        
        if(quantia <= 0):
            return '---Valor inválido para transação!---'

        destinatario.Depositar(quantia, show=False)
        self.Saldo -= quantia
        return f"Transação de R${quantia:.2f} feita de {self.Nome} para {destinatario.Nome}"

    def Emprestimo(self, valor, show=True):
        limite = self.Renda * 0.6

        if(valor > limite):
            return f"Empréstimo negado! --- Crédito insuficiente Valor máximo para conta: R${(limite):.2f}."


        if(self.Debito + valor * 1.1 > limite):
            parcial = limite - self.Debito
            if(parcial == 0):
                return "Empréstimo negado! --- Débitos pendentes"
            parcial /= 1.1
            self.Saldo += parcial
            self.Debito = limite
            return f"Empréstimo parcial de R${parcial:.2f} liberado"
        
        self.Debito += valor * 1.1

        self.Saldo += valor

        return f"Empréstimo de {valor} realizado por {self.Nome} sob débito de {self.Debito}"

    def PagarDebito(self):
        if(self.Debito > self.Saldo):
            self.Debito -= self.Saldo
            self.Saldo = 0
            return f"Débito restante de R${self.Debito:.2f}. Conta zerada"
        else:
            self.Saldo -= self.Debito
            self.Debito = 0
            return f"Débito zerado!"

    def Pagar_Anuidade(self):
        anuidade = 20 + self.Renda * 0.14
        self.Saldo -= anuidade
        if(self.Saldo < 0): self.Emprestimo(self.Saldo * -1, show=False)
        return anuidade
    
    def Passar_Mes(self):
        if self.Saldo < 0:
            self.Faltas += 1
            print(' x ' * self.Faltas)
        else:
            self.Faltas = 0
        
        if self.Faltas == 3:
            print('Acabaram as faltas!!!')
            return False

        self.Depositar(self.Renda)
        limite = self.Renda * 0.6
        juros = (1 + self.Debito/limite) ** 2
        print(f"Juros: {juros:.1f}x para o valor de R${(juros * self.Debito):.2f}")
        self.Debito *= juros
        if self.Debito > limite:
            extra = self.Debito - limite
            self.Debito = limite
            self.Saldo -= extra