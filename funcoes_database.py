import pyodbc
import pandas as pd

producao = ('Driver={SQL Server Native Client 11.0};Server=localhost;Database=Linkedin;UID=chapolin;PWD=123@mudar;')


def conectar():
    conexao = pyodbc.connect(producao)
    return conexao

def realizar_consulta(query):
    conexao = conectar()
    tabela = pd.read_sql(query, conexao)
    return tabela

query = 'select * from post'
result = realizar_consulta(query)
print(result)

