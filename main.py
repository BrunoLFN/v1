from pymongo import MongoClient
from datetime import datetime
from werkzeug.security import generate_password_hash
client = MongoClient('mongodb+srv://admin:hAx8Pbn4k5GxEcjZ@projeto-tarefas.gt2mfkg.mongodb.net/?retryWrites=true&w=majority')
# client = MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.1.0')
db = client["tarefas"]
conexao = db["task"]
conexao_user = db["users"]


def entrar(nome):        
    usuario = conexao_user.find_one({'nome': nome})
    return usuario
def criar_usuario(nome, psw):
    usuario = {
        'nome': nome,
        'senha': generate_password_hash(psw) 
    }
    usuario_exist = conexao_user.find({'nome':nome})
    if usuario_exist == usuario['nome']:
        print(f'usuario {nome} já existe')
    else:
        conexao_user.insert_one(usuario)
        print('usuario cadastrado com sucesso!!!')
def adicionar_tarefa(titulo,descricao,data_vencimento):
    try: 
        data_vencimento = datetime.strptime(data_vencimento, "%Y-%m-%d")
    except ValueError:
        print('Formato de data invalido')
        return
    if titulo != '':
        conexao.insert_one({'titulo':titulo,'descricao':descricao,'data':data_vencimento,'status': False})
        print('Tarefa inserida com sucesso!!!') 
    else:
        print('o titulo da tarefa não pode ser vazio!!!')   
def visualizar_tarefas():
    documentos = conexao.find({})
    return documentos
    
def excluir_tarefas(tarefa_del):
    query = {'titulo': tarefa_del}
    conexao.delete_one(query)
def editar_tarefa(filtro):
    query = {'titulo': filtro}
    conexao.update_one(query,{'$set':{'status':True}})
def excluir_tudo():
    query = {}
    conexao.delete_many(query)
    print('TODAS AS TAREFAS FORAM EXCLUIDAS!!!!')
# while True:
#         print("\n### Gerenciador de Tarefas ###")
#         print("1. Adicionar Tarefa")
#         print("2. Visualizar Tarefas")
#         print("3. Marcar Tarefa como Concluída")
#         print("4. Excluir Tarefa")
#         print('5. Excluir Todas as Tarefas')
#         print("0. Sair")

#         opcao = input("Escolha uma opção: ")

#         if opcao == "1":
#             adicionar_tarefa()
#         elif opcao == "2":
#             visualizar_tarefas()
#         elif opcao == "3":
#             concluir_tarefa()
#         elif opcao == "4":
#             excluir_tarefas()
#         elif opcao == "5":
#             excluir_tudo()    
#         elif opcao == "0":
#             print("Saindo do Gerenciador de Tarefas. Até logo!")
#             break
#         else:
#             print("Opção inválida. Tente novamente.")