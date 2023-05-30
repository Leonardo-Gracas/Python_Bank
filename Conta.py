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
            print("Saque negado! --- Cliente negativado")
            return 
        
        if(quantia > self.Saldo):
            print("Saque negado! --- Saldo insuficiente")
            return 
        
        self.Saldo -= quantia
        print(f"Saque de R${quantia:.2f} realizado por {self.Nome}.")
    
    def Depositar(self, quantia, show=True):
        if quantia <= 0:
            if show:
                print('---Depósito está abaixo do valor mínimo!!---')
            return
        self.Saldo += quantia
        if(show):
            print(f"Depósito de R${quantia:.2f} realizado por {self.Nome}.")
    
    def Transacao(self, destinatario, quantia):
        if(self.Saldo < 0):
            print("Transação negada! --- Cliente negativado")
        
        if(quantia > self.Saldo):
            print("Transação negada! --- Saldo insuficiente")
        
        if(quantia <= 0):
            print('---Valor inválido para transação!---')

        destinatario.Depositar(quantia, show=False)
        self.Saldo -= quantia
        print(f"Transação de R${quantia:.2f} feita de {self.Nome} para {destinatario.Nome}")

    def Enprestimo(self, valor, show=True):
        limite = self.Renda * 0.6

        if(valor > limite):
            if(show):
                print("Empréstimo negado! --- Crédito insuficiente")
                print(f"Valor máximo para conta: R${(limite):.2f}.")
            return


        if(self.Debito + valor * 1.1 > limite):
            parcial = limite - self.Debito
            if(parcial == 0):
                if(show):
                    print("Empréstimo negado! --- Débitos pendentes")
                return
            parcial /= 1.1
            if(show):
                print(f"Empréstimo parcial de R${parcial:.2f} liberado")
            self.Saldo += parcial
            self.Debito = limite
            return
        
        self.Debito += valor * 1.1

        self.Saldo += valor

        if(show):
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
            self.Saldo -= self.Debito
            self.Debito = 0

    def Apresentar(self):
        print(f'{self.Conta} - {self.Nome}.\nSaldo: R${self.Saldo:.2f}\nRenda mensal: R${self.Renda:.2f}')
        if(self.Debito > 0):
            print(f'Débito: R${self.Debito:.2f}')

    def Pagar_Anuidade(self):
        anuidade = 20 + self.Renda * 0.14
        self.Saldo -= anuidade
        if(self.Saldo < 0): self.Enprestimo(self.Saldo * -1, show=False)
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