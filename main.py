from flask import Flask, render_template, request, session, redirect
import hashlib
import sys
import os

# Adicionar o caminho da pastas ao sys.path
sys.path.append('ops')

from ops import UOW as uow
from ops import ORM as orm


app = Flask(__name__)
app.debug = True
app.secret_key = 'sua_chave_secreta_aqui'

dados_json_path = os.path.join(os.path.dirname(__file__), 'dados.json')

@app.route('/')
def index():
    return render_template('index.html')


# LOGIN 

@app.route('/login', methods=['GET'])
def login():
    if(session.get('id_conta') is not None):
        return render_template('conta.html')
    else:
        return render_template('login.html')

@app.route('/login_process', methods=['POST'])
def login_proc():
    email = request.form['email']
    password = request.form['password']
    
    # SE VERIFICAR CREDENCIAIS RETORNAR UM ID, É FEITO O LOGIN E A SESSÃO
    id_conta = uow.verificar_credenciais(email, hashlib.sha1(password.encode()).hexdigest())
    if(id_conta != None):
        session['id'] = id_conta
        return redirect('/conta')
    
    return '<script>alert("Email ou senha incorretos.");window.location="/login"</script>'


# CADASTRO

@app.route('/cadastro', methods=['GET'])
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastro_process', methods=['POST'])
def cadastro_proc():
    f_name = request.form['f_name']
    l_name = request.form['l_name']
    cpf = request.form['cpf']
    email = request.form['email']
    password = request.form['password']

    # SE CPF VÁLIDO TENTA CRIAR A CONTA
    if (uow.validar_cpf(cpf) == True):
        retorno = uow.Criar(f_name, l_name, cpf, email, password)
        
        # VERIFICAÇÃO SE CPF E EMAIL JÁ ESTÃO CADASTRADOS
        if retorno == True:
            return redirect('/login')
        elif retorno == 'cpf':
            return '<script>alert("CPF já cadastrado.");window.location="/cadastro"</script>'
        elif retorno == 'email':
            return '<script>alert("Email já cadastrado.");window.location="/cadastro"</script>'
    else:
        return '<script>alert("CPF inválido.");window.location="/cadastro"</script>'
    
# CONTA

@app.route('/conta')
def conta():
    if session.get('id') is None:
        return  '<script>alert("Usúario não logado.");window.location="/"</script>'
    
    for conta in orm.ORM.get_contas():
        if conta['conta'] == session.get('id'):
            if conta['funcao'] == "":
                return render_template('conta.html', conta = conta)
            elif conta['funcao'] == "1":
                return render_template('contaAdmin.html', conta = conta)
    

@app.route('/deslogar/<delog>')
def deslogar(delog):
    if (delog == "True"):
        session.clear()
        
    return redirect('/')


if __name__ == '__main__':
    app.run()
