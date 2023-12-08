from flask import Flask, render_template,redirect,request,url_for,session,flash
from main import *
from werkzeug.security import check_password_hash
documentos = visualizar_tarefas()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'MTIzNDU2'
@app.route('/')
def index(): 
    return redirect(url_for("login"))
@app.route('/login', methods=['GET','POST'])
def login():
    if 'username' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form.get('nome_usuario')
        senha = request.form.get('senha')
        usuario= entrar(username)
        if usuario and usuario.get('nome') == username:
            password = usuario['senha']
            if check_password_hash(password,senha):
                session['username'] = usuario['nome']
                return redirect(url_for('home'))
            else:
                flash('senha não confere')
                return render_template('login.html')
        else:
            flash('usuario não encontrado')
            return render_template('login.html')
    else:
        return render_template('login.html')
@app.route('/cadastrar_user', methods=['GET','POST'])
def cad_user():
    nome = request.form.get('nome')
    psw = request.form.get('senha')
    if not entrar(nome):
        criar_usuario(nome,psw)
        flash('Usuário criado com sucesso. Faça login.')
    else:
        flash('Nome de usuário já existe. Escolha outro.')
    return render_template('login.html')
@app.route('/logout')
def logout():
     if 'username' in session:
        session.pop("username")
        return redirect(url_for("login"))
@app.route('/home')
def home():
    if 'username' in session:
        documentos = visualizar_tarefas()
        return render_template('index.html', documentos=documentos)
    else:
        flash('voce não está authenticado, faça login!!')
        redirect(url_for("login"))
@app.route('/inserirdados',  methods=['POST'])
def cadastro2(): 
    
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    data_vencimento = request.form['prazo']
    adicionar_tarefa(titulo,descricao,data_vencimento)
    return redirect(url_for("home"))
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
@app.route('/delete/<tarefa_del>', methods=['GET'])
def deletar(tarefa_del: str):
    excluir_tarefas(tarefa_del)
    return redirect(url_for("home"))
@app.route('/deleteAll')
def deleteAll():
    excluir_tudo()
    return redirect('/cadastro')
if __name__ == '__main__':
    app.run(debug=True)
