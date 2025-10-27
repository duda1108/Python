'''import json
import os

#ler o arquivo ja existente
def CarregarUsuarios():
    if os.path.exists("person.json"):
        with open("person.json", "r") as arquivo:
            return json.load(arquivo)
    else:
        return {}
def ArmazenarUsuarios(usuarios):
    with open("person.json", "w") as arquivo:
        json.dump(usuarios, arquivo)
def CriarUsuario(usuarios):
    nome = input("Diga um nome para seu usuário: ")
    if nome in usuarios:
        print("Este nome ja esta em uso")
        return
    senha = input("Crie uma senha: ")
    usuarios[username] = senha
    ArmazenarUsuarios(usuarios)
    print("Seu cadastro foi concluido ")
def login(usuarios):
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if username in usuarios and usuarios[username] == senha:
        print("Você foi logado na sua conta")
    else:
        print("Usuario ou senha foram digitados errado")
#feito para chamar a função e arnazenar o dicionario nos usuarios
def menu():
    usuarios = carregar_usuarios()
    while True:
        print("Para cadastrar digite 1, para fazer login digite 2, e para sair digite 3")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            CriarUsuario(usuarios)
        elif opcao == "2":
            login(usuarios)
        elif opcao == "3":
            print("Encerrarei o comando")
            break
        else:
            print("Opção inválida!")
if __name__ == "__main__":
    menu()'''