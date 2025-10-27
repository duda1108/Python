'''class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print(f"olá, {self.nome}, você tem {self.idade}")

p1 = pessoa ("joao", 25)

print(p1.saudacao())
print(p1.nome)

p2 = pessoa("melissa", 18)
print(p2.saudacao())
print(p2.nome)'''
from anaconda3.Lib.logging import exception

'''class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de {valor} concluido")

    def sacar(self, valor):
        self.saldo -= valor
        print(f"saque de {valor} realizado")

    def es(self):
        print(f"O saldo é de {self.saldo}")

conta1 = Conta(f"Octavio", 0)
conta2 = Conta("duda", 0)
print(conta1)

conta1.depositar(500)
conta1.sacar(230)
conta2.depositar(1000)
conta1.depositar(500)
conta2.sacar(300)
conta1.es()
conta2.es()'''

'''class Produto:
    def __init__(self, nome, PU, quantidade=0):
#PU = preõ Unitario
        self.nome = nome
        self.PU = PU
        self.quantidade = quantidade

    def removerQ(self, valor):
        self.quantidade -= valor
        print(f"Remoção de {valor} concluido...")

    def adicionarQ(self, valor):
        self.quantidade += valor
        print(f"Adição de {valor} concluido...")

    def VT(self):
        self.quantidade * self.PU = self
        print(f"O valor total em estoque é de {} unidades")

x = input("informe a quantdade de shampoos que deseja")
y = input("informe a quantidade de Serras elétricasque deseja")

produto1 = Produto("shampoo", x , 20)
produto2 = Produto("Serra Elétrica", y, 115)

pergunta = int(input(f"deseja remover algo: (1=sim) (2=nao)"))
if pergunta = 1:
    L = int(input("qual produto deseja remover? (1=shampoo) (2=Serra Elétrica"))
    if L = 1:
        quant = int(input("quantos produtos deseja remover?"))'''

# CLASSE DESAFIO
'''class Produto:
    def __init__(self, nome, PU, quantidade=0):  # PU = Preço Unitário
        self.nome = nome
        self.PU = float(PU)
        self.quantidade = int(quantidade)

    def removerQ(self, valor):
        valor = int(valor)
        if valor <= 0:
            print("Quantidade escolhida para remover deve ser positiva.")
            return
        if valor > self.quantidade:
            print(f"Estoque insuficiente de {self.nome}. Tem-se em estoque {self.quantidade} unidades.")
            return
        self.quantidade -= valor
        print(f"Remoção de {valor} concluída")

    def adicionarQ(self, valor):
        valor = int(valor)
        if valor <= 0:
            print("Quantidade escolhida para adicionar deve ser positiva.")
            return
        self.quantidade += valor
        print(f"Adição de {valor} concluída")

    def VT(self):
        total = self.quantidade * self.PU
        print(f"O valor total do estoque de {self.nome} é de R$ {total}")
        return total


x = int(input("Informe a quantidade inicial de Shampoos: "))
y = int(input("Informe a quantidade inicial de Serras Elétricas: "))

produto1 = Produto("Shampoo", 20, x)
produto2 = Produto("Serra Elétrica", 115, y)


pergunta = int(input("Deseja remover ou adicionar algo? (1=remover) (2=adicionar) (3=não): "))

if pergunta == 1:
    L = int(input("Qual produto deseja remover? (1=Shampoo) (2=Serra Elétrica): "))
    quant = int(input("Quantos deseja remover? "))
    if L == 1:
        produto1.removerQ(quant)
    elif L == 2:
        produto2.removerQ(quant)
    else:
        print("inválida...")
elif pergunta == 2:
    L = int(input("Qual produto deseja adicionar? (1=Shampoo) (2=Serra Elétrica): "))
    quant = int(input("Quantos deseja adicionar? "))
    if L == 1:
        produto1.adicionarQ(quant)
    elif L == 2:
        produto2.adicionarQ(quant)
    else:
        print("inválida...")
else:
    print("Sem alterações.")

print("---------------------------------------------------------------------")
print(f"{produto1.nome} no preço de R$ {produto1.PU}, com {produto1.quantidade} unidades")
produto1.VT()
print(f"{produto2.nome} no preço de R$ {produto2.PU}, com {produto2.quantidade} unidades")
produto2.VT()'''

# MAIS DE UMA CLASSE
'''class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome 
        self.salario = salario

class Gestor(Funcionario):
    def bonus(self):
        return self.salario * 0.10

class adm(Funcionario):
    def bonus(self):
        return self.salario * 0,20

fun1 = Funcionario("joao", 2500)
fun2 = Funcionario("andre", 3500)
gest1 = Gestor("melissa", 5000)
adm1 = adm("kaua", 6000)'''

# Desafio
'''class veiculos:
    def __init__(self, marca, modelo, ano, valor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = float(valor)

class moto(veiculos):
    def IPVA(self):
        return self.valor * 0.02

class carro(veiculos):
    def IPVA(self):
        return self.valor * 0.04

mot1 = moto("HONDA" ,"HONDA CG 160 Start","2024", "13000")
mot2 = moto("Yamaha", "Yamaha Fazer 250 ABS", "2024", "21000")
carr1 = carro("Fiat", "Fiat Mobi Like 1.0", "2022", "70000")
carr2 = carro("Toyota", "Toyota Corolla Altis 2.0", "2014", "160000")


print(f"O {carr1.modelo}, no valor de R${carr1.valor}, tem de pagar um IPVA de R${carr1.IPVA()}")
print(f"O {mot1.modelo}, no valor de R${mot1.valor}, tem de pagar um IPVA de R${mot1.IPVA()}")
'''

# Desafio
'''
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self._notas = float(notas)

    @property
    def notas(self):
        return self._notas

    @notas.setter
    def notas(self, valor):
        if valor < 0:
            raise ValueError("A nota digitada não pode ser negativa!")
        if valor > 10:
            raise ValueError("A nota digitada não pode ser maior que 10!")
        self._notas = valor


c = Aluno(f"Eduardo", 0)
c.notas = 12
print(c.notas)



class livros:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self._quant = int(quant)

    @property
    def quant(self):
        return self._quant

    @quant.setter
    def quant(self, valor):
        if valor < self._quant:
            self._quant -= valor
        else:
            raise ValueError("Quantidade nao pode ser negativa")

c = livros("aventuras de PI", 200)
c.quant = 30
'''

'''
class aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = float(nota1)
        self.nota2 = float(nota2)

    def __repr__(self):
        #Representação mais técnica, geralmente mais para desenvolvedores
        return f"aluno(nome='{self.nome}', nota1={self.nota1}, nota2={self.nota2})"

    def __str__(self):
        #Representação mais bonitinha e de facil entendimento
        return f"Nome: {self.nome}, Nota 1: {self.nota1}, Nota 2: {self.nota2}"

    #Propriedade em que é necessario validação paa o acesso
    @property
    def nota1(self):
        return self._nota1

    #Propriedade em que se pode modificar algum dos objetos da função self
    @nota1.setter
    def nota1(self, valor):
        if valor < 0:
            raise ValueError("A nota digitada não pode ser negativa!")
        if valor > 10:
            raise ValueError("A nota digitada não pode ser maior que 10!")
        self._nota1 = float(valor)

    @property
    def nota2(self):
        return self._nota2

    @nota2.setter
    def nota2(self, valor):
        if valor < 0:
            raise ValueError("A nota digitada não pode ser negativa!")
        if valor > 10:
            raise ValueError("A nota digitada não pode ser maior que 10!")
        self._nota2 = float(valor)

    def media(self):
        return (self._nota1 + self._nota2) / 2

    def aprovado(self, corte=6.0):
        return self.media() >= corte

alunos = []
while True:
    print("caso deseje ecerrar o processo, apenas aperte ENTER")
    nome = input(f"me informe seu nome").strip()
    if not nome:
        break
    nota1 = float(input("me informe sua primeira nota"))
    nota2 = float(input("me informe sua segunda nota"))
    alunos.append(aluno(nome, nota1, nota2))

#tirei duvidas na internet quanto esta parte pois nao sabia como resoover este problema
corte = 6.0
aprovados = [a for a in alunos if a.aprovado(corte)]
reprovados = [a for a in alunos if not a.aprovado(corte)]

print("Aprovados")
for a in aprovados:
    print(f"{a.nome} pssui uma média de {a.media():.1f}")

print("Reprovados")
for a in reprovados:
    print(f"{a.nome} possui uma média de {a.media():.1f}")

if alunos:
    aluno1 = alunos[-1]  # último aluno cadastrado
    #exemplos de apresentações:
    print(aluno1)  #Como não foi especificado, a preferencia utiliza __str__
    print(str(aluno1))   #Ao solicitar utiliza __str__
    print(repr(aluno1))  #Ao utilizar utiliza __repr__
'''

'''
class Veiculo():
    def _init_(self, marca, modelo, ano, valor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

# classe carro específica
class Carro(Veiculo):
    def Mover
        print("O carro esta se movendo")
    def _init_(self, marca, modelo, ano, valor, portas):
        super()._init_(marca, modelo, ano, valor)              ###retorna definindo pro novo def os atributos anteriores
        self.portas = portas                                     ###define o atributo novo que é diferente dos anteriores
    def calcular(self):
        return self.valor*0.04

#Classe especifica para moto
class Moto(Veiculo):
    def _init_(self, marca, modelo, ano, valor, cilindradas):
        super()._init_(marca, modelo, ano, valor)
        self.cilindradas = cilindradas
    def calcular(self):
        return self.valor*0.02

car1 = Carro("Wolksvage", "RS", 2023, 57000)
car2 = Carro("Fiat", "Uno", 2000, 38000)
mot1 = Moto("Kawasaki", "Ninja", 2020, 29000)

print(car1.calcular())
print(car2.calcular())
print(mot1.calcular())'''

'''
class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def descr(self):
        print(f"{self.nome}, Salário de R${self.salario}")


class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def descr(self):
        print(f"Gerente {self.nome}, Salário de R${self.salario}, Departamnto {self.departamento}")

pedro = Gerente("pedro", 12000, "vendas")
pedro.descr()

guilerme = Gerente("guilerme", 666, "trair")
guilerme.descr()

duda = Funcionario("duda", 6000)
duda.descr()
'''

# DESAFIO COM POLIMORFIA
'''
class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso
    def discr(self):
        print(f"Aluno: {self.nome} \nIdade:{self.idade} anos \nMatrícula: {self.matricula} \nCurso: {self.curso}")

class Professor(Pessoa):
    def __init__(self, nome, idade, salario, disciplina):
        super().__init__(nome, idade)
        self.salario = salario
        self.disciplina = disciplina

    def discr(self):
        print(f"Professor: {self.nome} \nIdade: {self.idade} anos \nSalário: {self.salario} \nDisciplina: {self.disciplina}")

otavio = Professor("otavio", 27, 320000, "ciencias de dados\n")
otavio.discr()

guilerme = Aluno("guilerme", 18, 202527666, "traição e ver o amigo apanhando e nao fazer nada\n")
guilerme.discr()

duda = Aluno("nome", 19, 2025276969, "amar demais\n")
duda.discr()'''

#   ABSTRACT METHOD
'''
from abc import ABC, abstractmethod

class Pagamento(ABC):
    instancia = []
    instancia_sub = []

    def __init__(self, data):
        self.data = data
        Pagamento.instancia.append(self)
        self.__class__.instancia_sub.append(self)

    @abstractmethod
    def pagar(self, valor):
        pass

class CartaoCredito(Pagamento):
    instancia_sub = []
    def __init__(self, data, valor):
        super().__init__(data)
        self.valor = valor

    def pagar(self):
        return f"pagamento efetuado no valor de {self.valor}"

class PIX(Pagamento):
    instancia_sub = []
    def __init__(self, data, valor):
        super().__init__(data)
        self.valor = valor

    def pagar(self):
        return f"pagamento efetuado no valor de {self.valor}"

o1 = CartaoCredito("01", 500)
o2 = CartaoCredito("01", 550)
o3 = PIX("01", 600)

for i in PIX.instancia_sub:
    print(i.data, i.valor)




'''
'''
from abc import ABC, abstractmethod

class mensagem(ABC):
    def __init__(self, corpo):
        self.corpo = corpo                 #obriga as funções posteriores a ter o metodo enviar
    @abstractmethod                        #nao é possivel criar uma variavel "c1 = mensagem(..)" por exemplo, apenas com sms ou email
    def enviar(self):
        pass

class email(mensagem):
    def __init__(self, corpo, destinatario):
        self.destinatario = destinatario
        self.corpo = corpo

    def enviar(self):
        print(f"{self.corpo} \nEmail enviado para {self.destinatario} com sucesso!\n")

class SMS(mensagem):
    def __init__(self, corpo, numero):
        self.numero = numero
        self.corpo = corpo

    def enviar(self):
        print(f"{self.corpo} \nSMS enviado para {self.numero} com sucesso!\n")

c1 = email("sou delicia", "jose")
c1.enviar()

c2 = SMS("voce é sensacional", 27999872380)
c2.enviar()'''

from abc import ABC, abstractmethod


class chamado(ABC):
    instancia = []

    def __init__(self, titulo, descrição, data_abertura):
        self.titulo = titulo
        self.descrição = descrição
        self.data_abertura = data_abertura
        chamado.instancia.append(self)

    @abstractmethod
    def resumo(self):
        pass


class hardware(chamado):
    # diferencial: codigo do equipamento
    # grupo de chamados para o hardware
    instancia_hardware = []

    def __init__(self, titulo, descrição, data_abertura, codigo):
        self.codigo = codigo
        super().__init__(titulo, descrição, data_abertura)
        hardware.instancia_hardware.append(self)

    def resumo(self):
        print(
            f"Chamado: {self.titulo} \nDescrição: {self.descrição} \nStatus: Aberto \nData de abertura: {self.data_abertura} \nCódigo do equipamento: {self.codigo}")


class software(chamado):
    # diferencial: sistema
    # grupo de chamados para o software
    instancia_software = []

    def __init__(self, titulo, descrição, data_abertura, sistema):
        self.sistema = sistema
        super().__init__(titulo, descrição, data_abertura)
        software.instancia_software.append(self)

    def resumo(self):
        print(
            f"Chamado: {self.titulo} \nDescrição: {self.descrição} \nStatus: Aberto \n Data de abertura: {self.data_abertura} \nSistema: {self.sistema}")


l = 0
while True:
    print(f"Bem vindo a lista de chamados, selecione o que deseja:")
    try:
        n = int(input(
            f"1 - Abrir chamado Hardware \n2 - Abrir chamado Software \n3 - Listar todos os chamados \n4 - Listar chamados de Hardware \n5 - Listar chamados de Software \n0 - "
            f"Sair \n"))
        l += 1
        nome = "j" + str(l)

        if n == 1:
            tit = input("Informe o que seria seu chamado:")
            descr = input("Informe a descrição do problema:")
            data = input("Informe a data do chamado:")
            codg = input("Informe o codigo do equipamento:")
            nome = hardware(tit, descr, data, codg)
            nome.resumo()
            continue

        if n == 2:
            print("-----------------------------------------------------------------------")
            tit = input("Informe o que seria seu chamado:")
            descr = input("Informe a descrição do problema:")
            data = input("Informe a data do chamado:")
            sist = input("Informe o sistema utilizado:")
            nome = software(tit, descr, data, sist)
            nome.resumo()
            continue

        if n == 3:
            if not chamado.instancia:
                print("Nenhum chamado de software")
                continue
            else:
                for i in chamado.instancia:
                    print(f"Chamado:{i.titulo}, Descrição: {i.descrição}, Data: {i.data_abertura}")
                    continue

        if n == 4:
            if not hardware.instancia_hardware:
                print("Nenhum chamado de software")
                continue
            else:
                for i in hardware.instancia_hardware:
                    print(f"Chamado:{i.titulo}, Descrição: {i.descrição}, Data: {i.data_abertura}, Código: {i.codigo}")
                    continue

        if n == 5:
            if not software.instancia_software:
                print("Nenhum chamado de software")
                continue
            else:
                for i in software.instancia_software:
                    print(
                        f"Chamado:{i.titulo}, Descrição: {i.descrição}, Data: {i.data_abertura}, Sistema: {i.sistema}")
                    continue

        if n == 0:
            print(f"encerrando...")
            break

        else:
            print("Você deve digitar um dos numeros da lista\n")
            continue
    except ValueError:
        print("voce deve digitar um número..")

# ------------------------------prova(abstract, etc)-----------------------------------

import pandas as pd
from abc import ABC, abstractmethod

caminho = r"C:\Users\flavi\Downloads\lista_vendedores.xlsx"
df = pd.read_excel(caminho)


class vendedores(ABC):
    instancia = []

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = int(valor)

    @abstractmethod
    def calcular_bonus(self):
        pass


class vendedor1(vendedores):
    instancia_vendedor1 = []

    def __init__(self, nome, valor, nivel1):
        self.nivel1 = nivel1
        super().__init__(nome, valor)
        vendedor1.instancia_vendedor1.append(self)

    def calcular_bonus(self):
        print(f"{self.nome} é vendedor nível 1, e receberá um bonus 5% = {self.valor * 0.05}$\n")


class vendedor2(vendedores):
    instancia_vendedor2 = []

    def __init__(self, nome, valor, nivel2):
        self.nivel2 = nivel2
        super().__init__(nome, valor)
        vendedor2.instancia_vendedor2.append(self)

    def calcular_bonus(self):
        print(f"{self.nome} é vendedor nivel 2. e receberá um bonus 3% = {self.valor * 0.03}$\n")


l = 0
for i in range(0, 4):
    l += 1
    nom = "j" + str(l)

    if df.iloc[i, 1] == 1:
        nome = df.iloc[i, 0]
        valor = df.iloc[i, 2]
        nivel1 = 0
        nom = vendedor1(nome, valor, nivel1)
        nom.calcular_bonus()

    elif df.iloc[i, 1] == 2:
        nome = df.iloc[i, 0]
        valor = df.iloc[i, 2]
        nivel2 = 2
        nom = vendedor2(nome, valor, nivel2)
        nom.calcular_bonus()


