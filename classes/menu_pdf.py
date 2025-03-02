from tkinter import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os
from tkinter import ttk, messagebox
from utilitarios import executa_DML,executa_DQL

def modo_mm(modo):

    if modo == 'nome':
        mm = 10

    if modo == 'tipo':
        mm = 5

    if modo == 'descricao_tipo':
        mm = 7.5

    if modo == 'descricao':        
        mm = 12.5

    if modo == 'titulo':
        mm = 90

    if modo == 'harmonizacao':
        mm = 15

    return(mm)

def mm_p_pts(milimetros):
    pontos = milimetros/0.352777
    return(pontos)

def criar_pdf(lista):
    pastaApp = os.path.dirname(__file__)
    n_linhas = lista[-1]
    ultima_linha = int(n_linhas['linha'])
    
    qtde_linhas_paginas = 44

    qtde_paginas = (ultima_linha/qtde_linhas_paginas)
    sobra = ultima_linha%qtde_linhas_paginas
    if sobra == 0:
        qtde_paginas = int(qtde_paginas)
    else:
        qtde_paginas = int(qtde_paginas) + 1

    titulo_menu = lista[0]['texto']

    lista_mm = []
    lista_mm.append(290)

    for n in range(276,11,-6):
        lista_mm.append(n)

    print(lista_mm)

    for pagina in range(1,qtde_paginas+1):

        arquivo_salvar = pastaApp + rf"\dados\MVB_{pagina}.pdf"
        cnv = canvas.Canvas(arquivo_salvar, pagesize=A4)
        print(arquivo_salvar)

        for item in lista:
            texto = item['texto']
            linha = item['linha']
            modo = item['modo']
            cnv.drawString(mm_p_pts(modo_mm(modo)), mm_p_pts(lista_mm[linha]), texto)
            
        try:
            cnv.save()
            messagebox.showinfo("OK","O arquivo menu .pdf foi salvo.")
        except:
            messagebox.showinfo("ERRO","O arquivo menu .pdf não foi salvo.")

def criar_linhas_menu():

    lista = []
    
    sql = "SELECT `nome_estabelecimento` FROM `dados_gerais` WHERE `id_dados` = '1';"
    result = executa_DQL(sql)
    nome_estabelecimento = result[0][0]

    dict_temp = dict()
    dict_temp['linha'] = 0
    dict_temp['modo'] = 'titulo'
    dict_temp['texto'] = nome_estabelecimento
    lista.append(dict_temp)

    sql = f"SELECT `id_tipo_produto`,`tipo_produto`,`descricao_tipo_produto` FROM `tipos_produtos` ORDER BY `posicao`"
    result = executa_DQL(sql)

    if len(result) == 0:
        return()

    if result[0][0] == 'ERRO':
        return()

    linha = 0

    for item in result:

        linha += 1

        tipo_produto_id = item[0]

        dict_temp = dict()
        dict_temp['linha'] = linha
        dict_temp['modo'] = 'tipo'
        dict_temp['texto'] = item[1]
        lista.append(dict_temp)
        linha += 1

        dict_temp = dict()
        dict_temp['linha'] = linha
        dict_temp['modo'] = 'descricao_tipo'
        dict_temp['texto'] = item[2]
        lista.append(dict_temp)
        linha += 1

        sql = f"SELECT `nome_cardapio`,`descricao_cardapio`,`pv`,`id_produto` FROM `produtos` WHERE `tipo_produto_id` = '{tipo_produto_id}' ORDER BY `nome_cardapio`"
        result_2 = executa_DQL(sql)

        for item in result_2:
            linha += 1
            nome=  item[0]    
            pv = item[2]
            id_produto = item[3]

            dict_temp = dict()
            dict_temp['linha'] = linha
            dict_temp['modo'] = 'nome'
            dict_temp['texto'] = f'{nome}'
            lista.append(dict_temp)
            linha += 1

            descricao = item[1]
            dict_temp = dict()
            dict_temp['linha'] = linha
            dict_temp['modo'] = f'descricao'
            dict_temp['texto'] = f'{descricao} - R$ {pv}0'
            lista.append(dict_temp)
            linha += 1

            lista_produto_id = []
            
            sql = f"SELECT `produto_id_1` FROM `harmonizacoes` WHERE `produto_id_2` = '{id_produto}'"
            result_3 = executa_DQL(sql)

            for item in result_3:
                lista_produto_id.append(item[0])

            sql = f"SELECT `produto_id_2` FROM `harmonizacoes` WHERE `produto_id_1` = '{id_produto}'"
            result_4 = executa_DQL(sql)

            for item in result_4:
                lista_produto_id.append(item[0])

            texto = "harmoniza com: "
            qtde_harmonizacoes = 0
            
            for id_prod in lista_produto_id:
                sql = f"SELECT `nome_cardapio` FROM `produtos` WHERE `id_produto` = '{id_prod}'"
                result_5 = executa_DQL(sql)
                nome = result_5[0][0]

                texto += f"{nome}, "
                qtde_harmonizacoes += 1

            if qtde_harmonizacoes >= 1:
                descricao = item[1]
                dict_temp = dict()
                dict_temp['linha'] = linha
                dict_temp['modo'] = 'harmonizacao'
                dict_temp['texto'] = texto
                lista.append(dict_temp)
                linha += 1                
            


    print(lista)

    for linha in lista:
        print(linha['linha'], linha['texto'])

    return(lista)

