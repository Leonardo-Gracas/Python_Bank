import os
import UOW as uow

os.system("cls")

def func():
    pass

loop = True

def close_loop():
    global loop
    loop = False

command_list = [
    ('x', close_loop),
    ('list', uow.Listar),
    ('add', uow.Criar),
    ('get', uow.Ler),
    ('act', uow.Atualizar),
    ('del', uow.Deletar),
    ('bank', uow.Apresentar_Banco),
    # ('collect', uow.Cobrar_Anuidade),
    ('pass', uow.Passar_Mes)
]

while(loop):
    
    print('#    #    #    #    #    #')
    print("Digite o comando:")

    cmd = input(">>> ")
    cmd = cmd.lower()
    cmd = cmd.split()

    for command in command_list:
        if(command[0] == cmd[0]):
            function = command[1]
            if (len(cmd) > 1):
                args = " ".join(cmd[1:])
                function(args)
            else:                
                function()
            break
    else:
        print("Comando Inexistente!")
    
    print('#    #    #    #    #    #')