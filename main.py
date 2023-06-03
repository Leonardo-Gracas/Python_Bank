from flask import *
import math
import json

from ops import UOW as uow
# from ops import ORM as orm

App = Flask(__name__)
# App.debug = True

@App.route("/", methods=['GET', 'POST'])
def index():
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
        num_pags = math.ceil(numero_users/6)
        
        users = users[( 6*(pagina - 1) ):( 6*pagina )]
        
        return render_template('index.html', contas=users, num_pags=num_pags, pag_atual = pagina)
    
@App.route('/alt_users', methods=['GET'])
def alt():
    pass
    
    
@App.route('/rotaAjax', methods=['GET'])
def minha_rota():
    id = request.args.get('id')
    id = int(id)
    
    return uow.Ler(id, True)

App.run()