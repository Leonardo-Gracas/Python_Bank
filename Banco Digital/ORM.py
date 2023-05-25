import Conta as Conta

class ORM:
    def __init__(self):
        pass

    def create(self, conta, nome, renda, debito, saldo, orm):
        print('a')
        conta = Conta(conta, nome, renda, debito, saldo, orm)
        return conta

    def read(self, id):
        ...

    def update(self, entity):
        ...
    
    def delete(self, entity):
        ...

    def list(self, entity):
        print("A")