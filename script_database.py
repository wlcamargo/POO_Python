import pyodbc
import pandas as pd

conexao = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                     "Server=localhost;"
                     "Database=Linkedin;"
                     "UID=chapolin;"
                     "PWD=123@mudar;")

tabela = pd.read_sql("select * from post",conexao)
print(tabela)