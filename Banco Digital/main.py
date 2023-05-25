import os

import Conta as Conta
import Conta as Conta

import Conta as Conta

class ORM:
    def __init__(self):
        pass

    def create(self, conta, nome, renda, debito, saldo, orm):
        conta = Conta(conta, nome, renda, debito, saldo, orm)
        return conta

    def read(self, id):
        ...

    def update(self, entity):
        ...
    
    def delete(self, entity):
        ...

    def list(self):
        ...
import Banco as banco
import Conta

controler = ORM()

users = [controler.list]

loop = True
while(loop):
    os.system("cls")
    print("===========================")
    print("Digite o comando:")

    cmd = input(">>> ")
    cmd.lower()
    cmd.split()

    if(cmd[0] == 'x'):
        loop = False

    if(cmd[0] == "add"):
        conta = int(cmd[1])
        nome = cmd[2]
        renda = int(cmd[3])
        saldo = int(cmd[4])
        orm = controler
        users.append(controler.Create(conta, nome, renda, saldo, orm))

    m = input()