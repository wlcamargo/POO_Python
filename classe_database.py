import pyodbc
import pandas as pd

#config do banco de dados
linkedin = ('Driver={SQL Server Native Client 11.0};Server=localhost;Database=Linkedin;UID=chapolin;PWD=123@mudar;')

class Database:
    def iniciar(self):
        self.conectar()
        self.receber_query()
        self.realizar_consulta()
        self.exibir_tabela()

    def conectar(self):
        self.conexao = pyodbc.connect(linkedin)

    def receber_query(self):
        self.query = input('realize a query: ')

    def realizar_consulta(self):
        self.tabela = pd.read_sql(self.query, self.conexao)

    def exibir_tabela(self):
        print()
        print(self.tabela)

start = Database()
start.iniciar()
