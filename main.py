from flask import Flask, render_template, request, jsonify

import ops.UOW as uow

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', users=uow.Listar())

@app.route('/listar', methods=["GET"])
def listar():
    response = []
    response.append(uow.Pegar_Banco())
    response.append(uow.Listar())
    return jsonify(response)

@app.route('/add-user', methods=["POST"])
def criar():
    data = request.get_json()
    nome = data.get('nome')
    renda = data.get('renda')
    uow.Criar(nome, renda)

    return 'Sucesso'

@app.route('/selecionar', methods=["POST"])
def selecionar():
    data = request.get_json()
    userId = data.get('id')
    user = uow.Ler(userId)
    return user

@app.route('/sacar', methods=["POST"])
def sacar():
    data = request.get_json()
    userId = int(data.get('id'))
    valor = float(data.get('value'))
    message = uow.Sacar(userId, valor)
    response = {"message": message}
    return jsonify(response)

@app.route('/depositar', methods=["POST"])
def depositar():
    data = request.get_json()
    userId = int(data.get('id'))
    valor = float(data.get('value'))
    message = uow.Depositar(userId, valor)
    response = {"message": message}
    return jsonify(response)

@app.route('/transferir', methods=["POST"])
def transferir():
    data = request.get_json()
    userId = int(data.get('id'))
    valor = float(data.get('value'))
    outroId = int(data.get('otherId'))
    message = uow.Transferencia(userId, valor, outroId)
    response = {"message": message}
    return jsonify(response)

@app.route('/emprestimo', methods=["POST"])
def emprestimo():
    data = request.get_json()
    userId = int(data.get('id'))
    valor = float(data.get('value'))
    message = uow.Emprestimo(userId, valor)
    response = {"message": message}
    return jsonify(response)

@app.route('/pagar', methods=["POST"])
def pagar():
    data = request.get_json()
    userId = int(data.get('id'))
    message = uow.Pagar_Debitos(userId)
    response = {"message": message}
    return jsonify(response)

@app.route('/deletar', methods=["POST"])
def deletar():
    data = request.get_json()
    userId = int(data.get('id'))
    message = uow.Deletar(userId)
    response = {"message": message}
    return jsonify(response)

@app.route('/passar-mes', methods=["GET"])
def passarMes():
    response = uow.Passar_Mes()
    return jsonify(response)

if __name__ == '__main__':
    app.run()