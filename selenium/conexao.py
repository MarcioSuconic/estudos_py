import sqlite3 as con
import os

pasta_App = os.path.dirname(__file__) 

def executa_DML(sql):

    try:
        conexao = con.connect(pasta_App + r'\preco_passagens.db')
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
        conexao = con.connect(pasta_App + r'\cervejaria.db')
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
