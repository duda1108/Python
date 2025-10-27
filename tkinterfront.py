import tkinter as tk
from tkinter import filedialog

'''
#funcao do botao abaixo
def clique():
    resposta = entrada.get()
    print(resposta)

#selecionar um arquivo (botao2)
def arquivo():
    arquivo = filedialog.askopenfilename()
    label.config(text=arquivo)

#criar a janela
janela = tk.Tk() #criou
janela.geometry("400x300") #tamanho
janela.title("minha primiera janela") #titulo

#criar um input na janela
entrada = tk.Entry(janela)
entrada.pack() #pra aparecer, se n n aparece

#criar o botao
botao = tk.Button(janela, text="clique aqui", command=clique)
botao.pack()
botao2 = tk.Button(janela, text="selecione um arquivo", command=arquivo)
botao2.pack()

#linha escrita a mais apenas
label = tk.Label(janela, text="aiai papai")
label.pack()

#rodar a janela
janela.mainloop()'''

# calculadora

'''def somar():
    resposta1 = float(numero1.get())
    resposta2 = float(numero2.get())
    soma = resposta2 + resposta1
    resp.config(text=soma)


janela = tk.Tk() #criou
janela.geometry("400x300") #tamanho
janela.title("calculadora") #titulo

label = tk.Label(janela, text="insira o primeiro numero")
label.pack()
numero1 = tk.Entry(janela)
numero1.pack()
label2 = tk.Label(janela, text="agora o segundo")
label2.pack()
numero2 = tk.Entry(janela)
numero2.pack()


botao = tk.Button(text="somar", command=somar)
botao.pack()

resp = tk.Label(janela, text="")
resp.pack()
janela.mainloop()'''

# desafio json
'''import json

def jonson(arquivo):
    with open(arquivo, "r") as json_file:
        person = json.load(json_file)
    label.config(text=person)
    print(person)

def arquivo():
    arquivo = filedialog.askopenfilename()
    jonson(arquivo)

janela = tk.Tk()
janela.geometry("400x300")
janela.title("Abra um arquivo JSON")

botao = tk.Button(text="Selecione um arquvio Json", command=arquivo)
botao.pack()

label = tk.Label(janela, text="")
label.pack()

janela.mainloop()'''

'''
#desafio verificacao de conta
def verificacao():
    USUARIO = usu.get()
    SENHA = float(senha.get())

    if USUARIO in conta["usuario"]:
        if conta["senha"] == SENHA:
            label.config(text="voce esta logado")
        else:
            label.config(text="senha incorreta")
    else:
        label.config(text="usuario ou senha incorreto")

conta = {"usuario":"dudu", "senha":123}

janela = tk.Tk()
janela.geometry("400x300")
janela.title("Login/Cadastro")

label1 = tk.Label(text="usuario:")
label1.pack()
usu = tk.Entry(janela)
usu.pack()
label2= tk.Label(text="senha:")
label2.pack()
senha = tk.Entry(janela)
senha.pack()

botaoS = tk.Button(text="confirmar", command=verificacao)
botaoS.pack()

label = tk.Label(janela, text="")
label.pack()

janela.mainloop()
'''

# desafio validacao de cpf

'''def verificacao():
    CPF = cpf.get()
    x = ((int(CPF[0:1]) * 10 + int(CPF[1:2]) * 9 + int(CPF[2:3]) * 8 + int(CPF[3:4]) * 7 + int(CPF[4:5]) * 6 + int(CPF[5:6]) * 5 + int(CPF[6:7]) * 4 + int(CPF[7:8]) * 3 + int(CPF[8:9]) * 2) * 10 % 11)
    if x < 2:
        p = 0
    else:
        p = 11 - x

    y = ((int(CPF[0:1]) * 11 + int(CPF[1:2]) * 10 + int(CPF[2:3]) * 9 + int(CPF[3:4]) * 8 + int(CPF[4:5]) * 7 + int(CPF[5:6]) * 6 + int(CPF[6:7]) * 5 + int(CPF[7:8]) * 4 + int(CPF[8:9]) * 3 + int(CPF[9:10]) * 2) * 10 % 11)
    if y < 2:
        b = 0
    else:
        b = 11 - y

    if p == int(CPF[9:10]):
        if b == int(CPF[10:11]):
            label.config(text="cpf valido")
        else:
            label.config(text="cpf invalido")
    else:
        label.config(text="cpf invalido")


janela = tk.Tk()
janela.geometry("400x300")
janela.title("Validacao de CPF")

label = tk.Label(text="Insira o CPF")
label.pack()

cpf = tk.Entry(janela)
cpf.pack()

botao = tk.Button(text="verificar", command=verificacao)
botao.pack()

label1 = tk.Label(janela, text="")
janela.mainloop()'''

# -----------------------PROVA 1 BIMESTRE---------------------------
# -------------------------FRONT: CAMBIO----------------------------

import tkinter as tk
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait


def esconder():
    # esconder botoes do cadastro
    label_usu.pack_forget()
    usuario.pack_forget()
    label_senha.pack_forget()
    senha.pack_forget()
    fim.pack_forget()
    botao_back.forget()

    # mostrar botoes principais
    botao_cadastro.pack()
    botao_login.pack()


# cadastro
def cadastro():
    # Mostra os input e os botoes
    label_usu.pack()
    usuario.pack()
    label_senha.pack()
    senha.pack()
    fim.pack()
    fim.config(command=confirmar_cadastro)

    # temporariamente esquece o menu principal
    botao_cadastro.pack_forget()
    botao_login.pack_forget()
    botao_back.pack()


def confirmar_cadastro():
    x = usuario.get()
    y = senha.get()
    if not x or not y:
        labelmenu.config(text="voce deve preeencher o login e a senha!")
        return
    Contas["usuarios"].append(x)
    Contas["senhas"].append(y)
    labelmenu.config(text=f"Cadastro efetuado com sucesso {x}")
    esconder()


# LOGIN
def login():
    # esconder temporariamente botoes do menu
    botao_cadastro.pack_forget()
    botao_login.pack_forget()

    # mostrar coisas para login
    label_usu.pack()
    usuario.pack()
    label_senha.pack()
    senha.pack()
    labelmenu.config(text="")
    fim.pack()
    fim.config(command=confirmar_senha)
    botao_back.pack()


def confirmar_senha():
    # efetuar login
    x = usuario.get()
    y = senha.get()
    if x in Contas["usuarios"]:
        if y in Contas["senhas"]:
            labelmenu.config(text="login efetuado com sucesso!")
            esconder()
            novo_menu()
        else:
            labelmenu.config(text="senha nao encontrada...")
    else:
        labelmenu.config(text="usuario ou senha nao encontrados...")


def novo_menu():
    botao_cadastro.forget()
    botao_login.forget()

    botao_cambio = tk.Button(text="botao", command=cambio)
    botao_cambio.pack()


def dolar():
    # quantidade de reais
    P1 = float(input("me informe o valor que deseja converter:"))
    Pesquisa = f"{P1}"

    # executar o codigo
    path = r"C:\Users\flavi\Downloads\chromedriver.exe"
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
    espera = WebDriverWait(driver, 15)
    driver.get("https://www.xe.com")

    # colocar a quantidade de reais
    valor = driver.find_element(By.XPATH,
                                '//*[@id="__next"]/div/div[5]/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div')
    valor.click()
    time.sleep(3)
    v1 = driver.find_element(By.XPATH, '//*[@id="amount"]')
    time.sleep(1)
    v1.send_keys(Keys.DELETE)
    v1.send_keys(Pesquisa)
    time.sleep(4)

    # real
    US = driver.find_element(By.XPATH, '//*[@id="midmarketFromCurrency"]/div[2]/div[1]/input')
    US.send_keys("brazilian")
    time.sleep(2)
    US.send_keys(Keys.ENTER)

    # dolar
    dolar = driver.find_element(By.XPATH, '//*[@id="midmarketToCurrency"]/div[2]/div/input')
    dolar.send_keys("USD")
    time.sleep(3)
    dolar.send_keys(Keys.ENTER)
    time.sleep(2)

    # resultado
    resultado = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[5]/div/div[1]/div[1]/div/div[2]/div[3]/button')
    resultado.click()
    time.sleep(4)

    presso = driver.find_element(By.XPATH,
                                 '//*[@id="__next"]/div/div[5]/div/div[1]/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/p[2]')
    time.sleep(3)

    print(presso.text)
    # driver.quit()


def cambio():
    Valor = tk.Label(text="digite o valor de reais")
    Valor.pack()
    text_valor = tk.Label(text="")
    text_valor.pack()
    Valor1 = tk.Entry(janela)
    Valor1.pack()


# parte menu
Contas = {"usuarios": [], "senhas": []}

janela = tk.Tk()
janela.geometry("600x400")
janela.title("prova de python")

botao_cadastro = tk.Button(janela, text="Cadastro", command=cadastro)
botao_cadastro.pack()

botao_login = tk.Button(janela, text="Login", command=login)
botao_login.pack()

botao_back = tk.Button(text="Back", command=esconder)
# CADASTRO
label_usu = tk.Label(text="Digite seu usuário")
usuario = tk.Entry(janela, text="usuário")
label_senha = tk.Label(text="Digite sua senha")
senha = tk.Entry(janela, text="senha")

labelmenu = tk.Label(janela, text="")
labelmenu.pack()

fim = tk.Button(text="Confirmar", command=esconder)

janela.mainloop()
