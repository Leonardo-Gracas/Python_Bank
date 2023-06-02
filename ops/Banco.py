from random import randint


class Banco:
    def __init__(self, nome, agencia, saldoProprio, users):
        self.Nome = nome
        self.Agencia = agencia
        self.Saldo = saldoProprio
        self.Saldo_Corrente = 0
        self.calcular_saldo_corrente(users)

    def cobrar_anuidade(self, users):
        anuidade_total = 0
        for user in users:
            anuidade_total += user.Pagar_Anuidade()
        self.Saldo += anuidade_total
        self.calcular_saldo_corrente(users)
        print(f'Anuidade recolhida de R${anuidade_total:.2f}')

    def calcular_saldo_corrente(self, users):
        sc = 0
        for user in users:
            sc += user.Saldo
        self.Saldo_Corrente = sc
        return sc

    def apresentar(self):
        print(f'{self.Nome} --- {self.Agencia}')
        print(f'Saldo próprio: R${self.Saldo:.2f}')
        print(f'Saldo corrente: R${self.Saldo_Corrente:.2f}')
        return {
            'nome': self.Nome,
            'agencia': self.Agencia,
            'saldo': self.Saldo,
            'saldo': self.Saldo_Corrente,
        }

    def passar_mes(self):
        custos = randint(0, 10) * 100
        self.Saldo -= custos
        if self.Saldo_Corrente < 0:
            self.Saldo -= self.Saldo_Corrente

        porcentagem_renda = randint(1, 30) / 100
        print(f'{porcentagem_renda:.2f}%')
        parte_banco = self.Saldo_Corrente * porcentagem_renda * (8/10)
        parte_users = self.Saldo_Corrente * porcentagem_renda * (2/10)
        self.Saldo += parte_banco
        return parte_users