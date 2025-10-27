'''import pandas as pd

#serie é basicamente uma tabela de uma coluna só;
serie = pd.Series([10,20,30,40],
                  index=["a", "b", "c", "d"])
print(serie)

#DataFrame é uma tabela completa, com mais colunas e linhas;
data = {"produto": ["cafe", "Acucar", "Arroz"],
        "preco": [10,5,22],
        "estoque": [100, 200, 150]}

df = pd.DataFrame(data)

print(df)
#Quantas colunas e lnahs
print(df.shape)
#Comeco, quantos possuem, variacao entre cada index;
print(df.index)
#Quais as colunas da tabela
print(df.columns)
#Tipo de cada objeto
print(df.dtypes)
#Printa somente os primeiros números, a serem definidos;
print(df.head())
#Printa somente os últimos números, a serem definidos;
print(df.tail())
#Mostrar informacoes acerca do DataFrame
print(df.info)
#Qauntos valores unicos cada coluna possui
print(df.nunique())
#seleciona a coluna pelo index;
print(df[["produto", "preco"]])
#Seleciona uma linha pelo index;
print(df.loc[0:1])
#Seleciona a linha pela posicao;
print(df.iloc[1:2])
#seleciona o valor referente a coluna e linha escolhida;
print(df.loc[2, "produto"])
#Seleciona valores  de estoque maiores do que foi definido;
print(df[df["estoque"] > 120])
#Adionar uma coluna;
df["Valor"] = df["preco"] * df["estoque"]
print(df)
#Contagem estatistica;
print(df.describe())'''





#aminho = r"C:\Users\flavi\Downloads\DADOS_CEO.xlsx"
'''
import pandas as pd
df = pd.read_excel(aminho)           #Apenas puxa os dados da tabela excel
print(df)

df2 = df[df["educ_business"]==1]     #Na coluna edc_business, puxará todos os q tiver 1
print(df2)
df2.to_excel("arquivo2.xlsx")        #Jogará pra um arquivo excel

df.at[0, "ticker"] = "NOVAEMPRESA"   #Na linha 0, vai sobreescrever o que esta escrito
df.to_excel()#arquivo3.xlsx

#df.drop()        #Dropar linhas a partir do que definir
#df.dropna()      #Dropar linhas vazias
#df.fillna()      #preeencher as que estao vazias com o que eu quiser

df = df.dropna()
df.to_excel()#arquivo3.xlsx
'''






#exercicio exemplo
'''
data = {"aluno": ["ana", "Bruno", "Carla", "Diego", "Eva"],
        "Matemática": [8, 7, 9, 6, 5],
        "Portugues": [7, 8, 6, 9, 5]}

df = pd.DataFrame(data)
print(f"{df}\n")

a1 = df["Matemática"]   #localizar matematica
print(a1)

a2 = df[df["Portugues"]>=7]   #localizar colunas em que tenha nota maior ou igual a 7
print(a2)

a3 = df.loc[3]
print(a3)'''







'''import pandas as pd
#caminho = r"C:\\flavi\Downloads\BASE_FINAL.xlsx"
df = pd.read_excel(caminho)

print(f"\n{df.shape}\n")
#------------------------------------------------------------------
print(df.columns)
#-----------------------------------------------------------------
print(df.head(5))
#-----------------------------------------------------------------
print(df.info()) #Ativo é a unica coluna que nao tem valores nulos
#-----------------------------------------------------------------
print(df.describe())
#-----------------------------------------------------------------
a1 = df["ROE"].max()
print(df[df["ROE"]==a1])
#----------------------------------------------------------------
print(df["RECEITA"].sum())
#----------------------------------------------------------------
print(f"--------------------------------\n LUCRO LIQUIDO")
print(df[df["LUCRO LIQUIDO"] > 0])
#----------------------------------------------------------------
df["ISE"] = 0
print(df["ISE"])
#----------------------------------------------------------------
df.dropna()
print(df)
#----------------------------------------------------------------
print(df["ISE"])   #lenght = 5553 (quantidade de obs)
#----------------------------------------------------------------
df["SITUAÇAO FINANCEIRA"] = 0
for i in range(len(df)):
    if df.at[i, "LUCRO LIQUIDO"] > 0:
        df.at[i, "SITUAÇAO FINANCEIRA"] = "Lucro"
    if df.at[i, "LUCRO LIQUIDO"] < 0:
        df.at[i, "SITUAÇAO FINANCEIRA"] = "Prejuizo"
    else:
        df.at[i, "SITUAÇAO FINANCEIRA"] = "Neutro"

print(df["SITUAÇAO FINANCEIRA"])'''


'''
import pandas as pd

serie = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])

print(serie)

data = {"produto": ["Cafe", "açucar", "Arroz"], "Preço": [10, 5, 22], "Estoque": [100,200,150]}

df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.index)   #Linha
print(df.columns)'''


'''
import pandas as pd
                                                         #INNER = SO O QUE COMBINA, LEFT/right = VAI PUXAR O DA ESQUERDA/DIREITA AO QUE CORRESPONDE NO DA DIREITA/ESQUERDA, outer = junta tudo
clientes = pd.DataFrame({"id_cliente": [1, 2, 3],
                         "nome": ["ana", "Bruno", "Carlos"]})

pedidos = pd.DataFrame({"id_cliente": [1, 2, 2, 4],                #MERGE = utiliza uma comparacao com base em uma coluna
                         "valor": [100, 200, 300, 400]})

#-------------------------------MERGE---------------------------------------
df1 = pd.merge(clientes, pedidos, on="id_cliente", how="inner")    #INNER = SO O QUE COMBINA
print(df1)
df2 = pd.merge(clientes, pedidos, on="id_cliente", how="left")     #LEFT/right = VAI PUXAR TUDO DA ESQUERDA/DIREITA, E O QUE CORRESPONDE NO DA DIREITA/ESQUERDA
print(df2)
df3 = pd.merge(clientes, pedidos, on="id_cliente", how="outer")    #outer = junta tudo

#-------------------------------JOIN--------------------------------------
a1 = pd.DataFrame({"nome": ["ana", "Bruno", "Carlos"]}, index=[1, 2, 3])
a2 = pd.DataFrame({"idade": [25, 30, 22]}, index=[1, 2, 4])

a_junto = a1.join(a2, how="inner")                      #JOIN = juntar com base no index
print(a_junto)

#-----------------------------CONCAT--------------------------------------

b1 = pd.DataFrame({"mes":["janeiro", "fevereiro"], "vendas":[100, 150]})
b2 = pd.DataFrame({"mes":["mar", "abr"], "vendas":[200, 250]})

b_tudo = pd.concat([b1, b2],axis = 0, ignore_index=True)        #axis = 0: empina por linha, 1: empina por coluna
print(b_tudo)


#--------------------------EX EXCEL--------------------------
print("--------------------------------------------------")
xls = pd.ExcelFile(r"C:\\flavi\Downloads\aula_pandas_joins.xlsx")
clientes = pd.read_excel(xls, "clientes")
pedidos = pd.read_excel(xls, "pedidos")
pop = pd.read_excel(xls, "populacao").set_index("cidade")
area = pd.read_excel(xls, "area").set_index("cidade")
jan = pd.read_excel(xls, "vendas_jan")
fev = pd.read_excel(xls, "vendas_fev")
mar = pd.read_excel(xls, "vendas_mar")

merge = pd.merge(clientes, pedidos, on="id_cliente", how="left")   #MERGE = juntou as 2 tabelas completas, "cliente" e "pedidos"
print(merge)

join_inner = pop.join(area, how="inner")
print(join_inner)

concat_vendas = pd.concat([jan, fev, mar], axis=0, ignore_index=True)
print(concat_vendas)
'''


'''
#-------------------------------DESAFIO------------------------------------
#-------------------------(join, merge, concat)----------------------------
import pandas as pd

xls = pd.ExcelFile(r"C:\Users\flavi\Downloads\universidade_joins.xlsx")
alunos = pd.read_excel(xls, "alunos")
matr_sem1 = pd.read_excel(xls, "matriculas_sem1")
matr_sem2 = pd.read_excel(xls, "matriculas_sem2")
cidades = pd.read_excel(xls, "cidades")
disciplinas = pd.read_excel(xls, "disciplinas")


c1 = pd.concat([matr_sem1, matr_sem2], axis=0, ignore_index=True)
print(c1)
m1= pd.merge(c1, alunos, on="matricula", how="outer")
m2 = pd.merge(m1, cidades, on="cidade", how= "inner")
m3 = pd.merge(m2, disciplinas, on="cod_disc", how = "inner")
m3.to_excel("dever.xlsx")'''


print("emanuel")