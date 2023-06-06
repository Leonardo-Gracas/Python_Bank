from flask import *
import math
import json

from ops import UOW as uow
# from ops import ORM as orm

App = Flask(__name__)
App.debug = True

@App.route("/", methods=['GET', 'POST'])
def index():
    get = request.args.get('get')
    
    if request.method == 'POST':
        conta1 = request.form['idConta1']
        conta2 = request.form['idConta2']
    
    # arg_base = request.form['arg-base']
    # arg_act = request.form['arg_act']
    
    # valor = request.form['valor']
    
    # if arg_base != None:
    #     if arg_base in 'act':
    #         if arg_act in 'd':
    #             # FUNCAO DEPOSITO
    #             pass
    #         elif arg_act in 's':
    #             # FUNCAO SAQUE
    #             pass
    #         elif arg_act in 't':
    #             # FUNCAO TRANSACAO
    #             pass
    #         elif arg_act in 'p':
    #             # FUNCAO PAGAR
    #             pass
    #         elif arg_act in 'e':
    #             # EMPRESTIMO
    #             pass
    #     else: 
    #         uow.Passar_Mes
    
            
    if get != None:
        
        pass
    else:
        pagina = request.args.get('pagina')
        
        if pagina == None:
            pagina = 1
        else:
            pagina = int(pagina)
            
        users = uow.Listar()
        
        numero_users = len(users)
        num_pags = math.ceil(numero_users/6)
        
        users = users[( 6*(pagina - 1) ):( 6*pagina )]
        
        return render_template('index.html', contas=users, num_pags=num_pags, pag_atual = pagina)
    
@App.route('/alt_users', methods=['GET'])
def alt():
    get = request.args.get('get')
    
    if get != None:
        
        pass
    else:
        pagina = request.args.get('pagina')
        
        if pagina == None:
            pagina = 1
        else:
            pagina = int(pagina)
            
        users = uow.Listar()
        
        numero_users = len(users)
        num_pags = math.ceil(numero_users/12)
        
        users = users[( 12*(pagina - 1) ):( 12*pagina )]
        
        return render_template('alt_users.html', contas=users, num_pags=num_pags, pag_atual = pagina)
    
    return render_template('alt_users.html')

@App.route('/alt_create', methods=['POST'])
def create_proc():
    if request.method == 'POST':
        nome = request.form['nome']
        renda = request.form['renda']
        
        # FUNCAO CREATE

@App.route('/alt_del', methods=['GET'])
def del_proc():
    if request.method == 'GET':
        conta = request.args.get('id')
        
        # FUNCAO DELETE arg: CONTA = ID
        
    return render_template('alt_users.html')
    
@App.route('/rotaAjax', methods=['GET'])
def minha_rota():
    id = request.args.get('id')
    id = int(id)
    
    return uow.Ler(id, True)

App.run()