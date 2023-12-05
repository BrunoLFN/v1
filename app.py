from flask import Flask, render_template,redirect,request,make_response
from main import *
usuarios = [
    {'nome':'bruno','idade': 24,'email':'bruno@gmail'},
    {'nome':'teste','idade':10000,'email':'teste@gmail'}
]
documentos = visualizar_tarefas()
app = Flask(__name__)
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
@app.route('/')
def index(): 
    return render_template('index.html',documentos=documentos)
@app.route('/inserirdados',  methods=['POST'])
def cadastro2(): 
    
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    data_vencimento = request.form['prazo']
    adicionar_tarefa(titulo,descricao,data_vencimento)
    return redirect('/')
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
@app.route('/delete/<tarefa_del>', methods=['GET'])
def deletar(tarefa_del: str):
    excluir_tarefas(tarefa_del)
    return redirect('/')
@app.route('/deleteAll')
def deleteAll():
    excluir_tudo()
    return redirect('/cadastro')
# @app.route('/v1/nome/<nome>', methods=['GET'])
# def retorna_nome(nome: str):
#    for i  in range(len(usuarios)):
#     if nome == usuarios[i]['nome']:
#          return usuarios[i]
#     else:
#     	return 'usuario não encontrado'
# @app.route('/v1/email/<email>', methods=['GET'])
# def retorna_email(email: str):
#    for i  in range(len(usuarios)):
#     if email == usuarios[i]['email']:
#          return usuarios[i]
#     else:
#     	return 'usuario não encontrado'
# @app.route('/v1/login/<login>', methods=['GET'])
# def retorna_login(login: str):
#    for i  in range(len(usuarios)):
#     if login == usuarios[i]['email'] or login == usuarios[i]['nome']:
#          return usuarios[i]
#     else:
#     	return 'usuario não encontrado'    
if __name__ == '__main__':
    app.run(debug=True)
