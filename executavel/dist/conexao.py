import sqlite3 as con
import os
from tkinter import messagebox

pasta_App = os.path.dirname(__file__) 
pasta_App = pasta_App + r'\preco_passagens.db'

messagebox.showinfo("Aviso pasta",pasta_App)

def executa_DML(sql):

    try:
        conexao = con.connect(pasta_App)
        cursor = conexao.cursor()
        cursor.execute(sql)
        result=True

    except con.DatabaseError as erro:
        print('Erro no Banco de dados: ', erro)
        result=False

    finally:
        if conexao:
            conexao.commit()
            conexao.close()

    return(result)

def executa_DQL(sql):

    try:
        conexao = con.connect(pasta_App)
        cursor = conexao.cursor()

        res = cursor.execute(sql)
        result = res.fetchall()

    except con.DatabaseError as erro:
        print('Erro no Banco de dados: ', erro)
        result=['ERRO']

    finally:
        if conexao:
            conexao.close()

    return(result)
