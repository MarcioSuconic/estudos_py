import pandas as pd
import os
from utilitarios import executa_DML, executa_DQL
from tkinter import messagebox
from fator import volta_valor_insumo
from menu_pdf import criar_linhas_menu, criar_pdf

def criar_dados(excel=True, menu=True):

    pastaApp = os.path.dirname(__file__)
    caminho = rf'{pastaApp}/dados'
    if os.path.isdir(caminho): # vemos de este diretorio ja existe
        print ('Ja existe uma pasta com esse nome!')
    else:
        os.mkdir(caminho) # aqui criamos a pasta caso nao exista
        print ('Pasta criada com sucesso!')
    
    # grandezas   
    tabela = "grandezas_fisicas"
    campos = ['id','grandeza']
    nms = ['id','grandeza']

    sufixo = 'grd'
    nomes=[]
    for item in nms:
        nomes.append(f'{item}_{sufixo}')

    texto = ""
    ultimo_campo = campos[-1]

    for item in campos:
        texto += f"`{item}`"
        if item != ultimo_campo:
            texto += ', '

    sql = f"SELECT {texto} FROM `{tabela}`"

    lista_1 = []
    lista_2 = []

    result = executa_DQL(sql)
    for item in result:
        lista_1.append(item[0])
        lista_2.append(item[1])

    df_grandezas = pd.DataFrame(data=[lista_1, lista_2]).transpose()
    df_grandezas.columns = nomes

    # unidades
    tabela = "unidades"
    campos = ['id_unidade','unidade','simbolo','grandeza_id']
    nms = ['id_unidade','unidade','simbolo','grandeza_id']

    sufixo = 'uni'
    nomes=[]
    for item in nms:
        nomes.append(f'{item}_{sufixo}')

    texto = ""
    ultimo_campo = campos[-1]

    for item in campos:
        texto += f"`{item}`"
        if item != ultimo_campo:
            texto += ', '

    sql = f"SELECT {texto} FROM `{tabela}` WHERE `ativo` = '1'"

    lista_1 = []
    lista_2 = []
    lista_3 = []
    lista_4 = []
    

    result = executa_DQL(sql)
    for item in result:
        lista_1.append(item[0])
        lista_2.append(item[1])
        lista_3.append(item[2])
        lista_4.append(item[3])
        

    df_unidades = pd.DataFrame(data=[lista_1, lista_2, lista_3,lista_4]).transpose()
    df_unidades.columns = nomes

    # insumos
    sufixo = 'ins'
    tabela = "insumos"
    campos = ['id_insumo','insumo','unidade_id','preco_ref','qtde_ref','peso_uma_unidade_ref']
    nms = ['id_insumo','insumo','unidade_id','preco_ref','qtde_ref','peso_uma_unidade_ref']

    sufixo = 'ins'
    nomes=[]
    for item in nms:
        nomes.append(f'{item}_{sufixo}')

    texto = ""
    ultimo_campo = campos[-1]

    for item in campos:
        texto += f"`{item}`"
        if item != ultimo_campo:
            texto += ', '

    sql = f"SELECT {texto} FROM `{tabela}` WHERE `ativo` = '1'"

    lista_1 = []
    lista_2 = []
    lista_3 = []
    lista_4 = []
    lista_5 = []
    lista_6 = []    

    result = executa_DQL(sql)

    for item in result:
        lista_1.append(item[0])
        lista_2.append(item[1])
        lista_3.append(item[2])
        lista_4.append(item[3])
        lista_5.append(item[4])
        lista_6.append(item[5])        

    df_insumos = pd.DataFrame(data=[lista_1, lista_2, lista_3, lista_4, lista_5, lista_6]).transpose()
    df_insumos.columns = nomes

    # tipos sub produtos
    tabela = "tipos_sub_produtos"
    campos = ['id_tipo_sub_produto','tipo_sub_produto','markup_minimo']
    nms = ['id_tipo_sub_produto','tipo_sub_produto','markup_minimo']

    sufixo = 'tsp'
    nomes=[]
    for item in nms:
        nomes.append(f'{item}_{sufixo}')

    texto = ""
    ultimo_campo = campos[-1]

    for item in campos:
        texto += f"`{item}`"
        if item != ultimo_campo:
            texto += ', '

    sql = f"SELECT {texto} FROM `{tabela}` WHERE `ativo` = '1'"

    lista_1 = []
    lista_2 = []
    lista_3 = []    

    result = executa_DQL(sql)
    for item in result:
        lista_1.append(item[0])
        lista_2.append(item[1])
        lista_3.append(item[2])
        

    df_tipos_sub_produtos = pd.DataFrame(data=[lista_1, lista_2, lista_3]).transpose()
    df_tipos_sub_produtos.columns = nomes

    # sub_produtos
    tabela = 'sub_produtos'
    campos = ['id_sub_produto','sub_produto','tipo_sub_produto_id','markup','ativo']
    nms = ['id_sub_produto','sub_produto','tipo_sub_produto_id','markup','ativo']

    sufixo = 'spr'
    nomes=[]
    for item in nms:
        nomes.append(f'{item}_{sufixo}')

    texto = ""
    ultimo_campo = campos[-1]

    for item in campos:
        texto += f"`{item}`"
        if item != ultimo_campo:
            texto += ', '

    sql = f"SELECT {texto} FROM `{tabela}` WHERE `ativo` = '1'"

    lista_1 = []
    lista_2 = []
    lista_3 = []
    lista_4 = []
    lista_5 = []    

    result = executa_DQL(sql)
    for item in result:
        lista_1.append(item[0])
        lista_2.append(item[1])
        lista_3.append(item[2])
        lista_4.append(item[3])
        lista_5.append(item[4])        

    df_sub_produtos = pd.DataFrame(data=[lista_1, lista_2, lista_3, lista_4, lista_5]).transpose()
    df_sub_produtos.columns = nomes


    # sub_produtos_x_insumos
    tabela = 'sub_produtos_x_insumos'
    campos = ['id_sub_produto_x_insumo','sub_produto_id','insumo_id','percentual','rendimento']
    nms = ['id_sub_produto_x_insumo','sub_produto_id','insumo_id','percentual','rendimento']

    sufixo = 'spi'
    nomes=[]
    for item in nms:
        nomes.append(f'{item}_{sufixo}')

    texto = ""
    ultimo_campo = campos[-1]

    for item in campos:
        texto += f"`{item}`"
        if item != ultimo_campo:
            texto += ', '

    sql = f"SELECT {texto} FROM `{tabela}` WHERE `ativo` = '1'"

    lista_1 = []
    lista_2 = []
    lista_3 = []
    lista_4 = []
    lista_5 = []    

    result = executa_DQL(sql)
    for item in result:
        lista_1.append(item[0])
        lista_2.append(item[1])
        lista_3.append(item[2])
        lista_4.append(item[3])
        lista_5.append(item[4])        

    df_sub_produtos_x_insumos = pd.DataFrame(data=[lista_1, lista_2, lista_3, lista_4, lista_5]).transpose()
    df_sub_produtos_x_insumos.columns = nomes

    # tipos produtos
    tabela = 'tipos_produtos'
    campos = ['id_tipo_produto','tipo_produto','markup','descricao_tipo_produto']
    nms = ['id_tipo_produto','tipo_produto','markup','descricao_tipo_produto']

    sufixo = 'tpr'
    nomes=[]
    for item in nms:
        nomes.append(f'{item}_{sufixo}')

    texto = ""
    ultimo_campo = campos[-1]

    for item in campos:
        texto += f"`{item}`"
        if item != ultimo_campo:
            texto += ', '

    sql = f"SELECT {texto} FROM `{tabela}` WHERE `ativo` = '1'"

    lista_1 = []
    lista_2 = []
    lista_3 = []
    lista_4 = []    

    result = executa_DQL(sql)
    for item in result:
        lista_1.append(item[0])
        lista_2.append(item[1])
        lista_3.append(item[2])
        lista_4.append(item[3])       

    df_tipos_produtos = pd.DataFrame(data=[lista_1, lista_2, lista_3, lista_4]).transpose()
    df_tipos_produtos.columns = nomes

    # sub_produtos_x_insumos
    tabela = 'sub_produtos_x_insumos'
    campos = ['id_sub_produto_x_insumo','sub_produto_id','insumo_id','percentual','rendimento']
    nms = ['id_sub_produto_x_insumo','sub_produto_id','insumo_id','percentual','rendimento']

    sufixo = 'spi'
    nomes=[]
    for item in nms:
        nomes.append(f'{item}_{sufixo}')

    texto = ""
    ultimo_campo = campos[-1]

    for item in campos:
        texto += f"`{item}`"
        if item != ultimo_campo:
            texto += ', '

    sql = f"SELECT {texto} FROM `{tabela}`  WHERE `ativo` = '1'"

    lista_1 = []
    lista_2 = []
    lista_3 = []
    lista_4 = []
    lista_5 = []    

    result = executa_DQL(sql)
    for item in result:
        lista_1.append(item[0])
        lista_2.append(item[1])
        lista_3.append(item[2])
        lista_4.append(item[3])
        lista_5.append(item[4])       

    df_sub_produtos_x_insumos = pd.DataFrame(data=[lista_1, lista_2, lista_3, lista_4, lista_5]).transpose()
    df_sub_produtos_x_insumos.columns = nomes

    # produtos
    tabela = 'produtos'
    campos = ['id_produto','produto','tipo_produto_id','descricao_cardapio','nome_cardapio','apenas_revenda']
    nms = ['id_produto','produto','tipo_produto_id','descricao_cardapio','nome_cardapio','apenas_revenda']

    sufixo = 'pro'
    nomes=[]
    for item in nms:
        nomes.append(f'{item}_{sufixo}')

    texto = ""
    ultimo_campo = campos[-1]

    for item in campos:
        texto += f"`{item}`"
        if item != ultimo_campo:
            texto += ', '

    sql = f"SELECT {texto} FROM `{tabela}` WHERE `ativo` = '1'"

    lista_1 = []
    lista_2 = []
    lista_3 = []
    lista_4 = []
    lista_5 = []
    lista_6 = []    

    result = executa_DQL(sql)
    for item in result:
        lista_1.append(item[0])
        lista_2.append(item[1])
        lista_3.append(item[2])
        lista_4.append(item[3])
        lista_5.append(item[4])
        lista_6.append(item[5])

    df_produtos = pd.DataFrame(data=[lista_1, lista_2, lista_3, lista_4, lista_5, lista_6]).transpose()
    df_produtos.columns = nomes
    df_produtos['id_produto_pro'] = df_produtos['id_produto_pro'].astype('int')

    # produtos x sub produtos
    tabela = 'produtos_x_sub_produtos'
    campos = ['id_produtos_x_sub_produtos','produto_id','sub_produto_id','peso','unidade_id']
    nms = ['id_produtos_x_sub_produtos','produto_id','sub_produto_id','peso','unidade_id']

    sufixo = 'psp'
    nomes=[]
    for item in nms:
        nomes.append(f'{item}_{sufixo}')

    texto = ""
    ultimo_campo = campos[-1]

    for item in campos:
        texto += f"`{item}`"
        if item != ultimo_campo:
            texto += ', '

    sql = f"SELECT {texto} FROM `{tabela}` WHERE `ativo` = '1'"

    lista_1 = []
    lista_2 = []
    lista_3 = []
    lista_4 = []
    lista_5 = []    

    result = executa_DQL(sql)
    for item in result:
        lista_1.append(item[0])
        lista_2.append(item[1])
        lista_3.append(item[2])
        lista_4.append(item[3])
        lista_5.append(item[4])        

    df_produtos_x_sub_produtos = pd.DataFrame(data=[lista_1, lista_2, lista_3, lista_4, lista_5]).transpose()
    df_produtos_x_sub_produtos.columns = nomes

    # finalizacao_produtos
    tabela = 'finalizacao_produtos'
    campos = ['id_fpr','produto_id','insumo_id','mensuracao','unidade_id','cfpr','ativo']
    nms = ['id_fpr','produto_id','insumo_id','mensuracao','unidade_id','cfpr','ativo']

    sufixo = 'fpr'
    nomes=[]
    for item in nms:
        nomes.append(f'{item}_{sufixo}')

    texto = ""
    ultimo_campo = campos[-1]

    for item in campos:
        texto += f"`{item}`"
        if item != ultimo_campo:
            texto += ', '

    sql = f"SELECT {texto} FROM `{tabela}` WHERE `ativo` = '1'"
    lista_1 = []
    lista_2 = []
    lista_3 = []
    lista_4 = []
    lista_5 = []
    lista_6 = []
    lista_7 = []

    result = executa_DQL(sql)
    for item in result:
        lista_1.append(item[0])
        lista_2.append(item[1])
        lista_3.append(item[2])
        lista_4.append(item[3])
        lista_5.append(item[4])        
        lista_6.append(item[5])  
        lista_7.append(item[6])  

    df_finalizacao_produtos = pd.DataFrame(data=[lista_1, lista_2, lista_3, lista_4, lista_5, lista_6, lista_7]).transpose()
    df_finalizacao_produtos.columns = nomes
    df_finalizacao_produtos['produto_id_fpr'] = df_finalizacao_produtos['produto_id_fpr'].astype('int')

    # processo feitura produtos_energia
    tabela = 'processo_feitura_produtos_energia'
    campos = ['id_pfe','produto_id','ativo','potencia_w','tempo_energia_eletrica','cel']
    nms = ['id_pfe','produto_id','ativo','potencia_w','tempo_energia_eletrica','cel']

    sufixo = 'pfe'
    nomes=[]
    for item in nms:
        nomes.append(f'{item}_{sufixo}')

    texto = ""
    ultimo_campo = campos[-1]

    for item in campos:
        texto += f"`{item}`"
        if item != ultimo_campo:
            texto += ', '

    sql = f"SELECT {texto} FROM `{tabela}` WHERE `ativo` = '1'"
    lista_1 = []
    lista_2 = []
    lista_3 = []
    lista_4 = []
    lista_5 = []
    lista_6 = []

    result = executa_DQL(sql)
    for item in result:
        lista_1.append(item[0])
        lista_2.append(item[1])
        lista_3.append(item[2])
        lista_4.append(item[3])
        lista_5.append(item[4])
        lista_6.append(item[5])  

    df_pfe = pd.DataFrame(data=[lista_1, lista_2, lista_3, lista_4, lista_5, lista_6]).transpose()
    df_pfe.columns = nomes
    df_pfe['produto_id_pfe'] = df_pfe['produto_id_pfe'].astype('int')



    # processo feitura produtos_insumos
    tabela = 'processo_feitura_produtos_insumos'
    campos = ['id_pfp','produto_id','insumo_id','mensuracao','unidade_id','cpfp','ativo']
    nms = ['id_pfp','produto_id','insumo_id','mensuracao','unidade_id','cpfp','ativo']

    sufixo = 'pfi'
    nomes=[]
    for item in nms:
        nomes.append(f'{item}_{sufixo}')

    texto = ""
    ultimo_campo = campos[-1]

    for item in campos:
        texto += f"`{item}`"
        if item != ultimo_campo:
            texto += ', '

    sql = f"SELECT {texto} FROM `{tabela}` WHERE `ativo` = '1'"
    lista_1 = []
    lista_2 = []
    lista_3 = []
    lista_4 = []
    lista_5 = []
    lista_6 = []
    lista_7 = []

    result = executa_DQL(sql)
    for item in result:
        lista_1.append(item[0])
        lista_2.append(item[1])
        lista_3.append(item[2])
        lista_4.append(item[3])
        lista_5.append(item[4])
        lista_6.append(item[5])  
        lista_7.append(item[6])


    df_pfi = pd.DataFrame(data=[lista_1, lista_2, lista_3, lista_4, lista_5, lista_6, lista_7]).transpose()
    df_pfi.columns = nomes
    df_pfi['produto_id_pfi'] = df_pfi['produto_id_pfi'].astype('int')



    # produtos x m.o.
    tabela = 'produtos_x_mo'
    campos = ['id_produto_x_mo','produto_id','tempo_min_grau_1_mo','tempo_min_grau_2_mo','tempo_min_grau_3_mo','cpmo','ativo']
    nms = ['id_produto_x_mo','produto_id','tempo_min_grau_1_mo','tempo_min_grau_2_mo','tempo_min_grau_3_mo','cpmo','ativo']

    sufixo = 'pmo'
    nomes=[]
    for item in nms:
        nomes.append(f'{item}_{sufixo}')

    texto = ""
    ultimo_campo = campos[-1]

    for item in campos:
        texto += f"`{item}`"
        if item != ultimo_campo:
            texto += ', '

    sql = f"SELECT {texto} FROM `{tabela}` WHERE `ativo` = '1'"

    lista_1 = []
    lista_2 = []
    lista_3 = []
    lista_4 = []
    lista_5 = []
    lista_6 = []
    lista_7 = []

    result = executa_DQL(sql)
    for item in result:
        lista_1.append(item[0])
        lista_2.append(item[1])
        lista_3.append(item[2])
        lista_4.append(item[3])
        lista_5.append(item[4])
        lista_6.append(item[5])  
        lista_7.append(item[6])  

    df_produtos_x_mo = pd.DataFrame(data=[lista_1, lista_2, lista_3, lista_4, lista_5, lista_6, lista_7]).transpose()
    df_produtos_x_mo.columns = nomes
    df_produtos_x_mo['produto_id_pmo'] = df_produtos_x_mo['produto_id_pmo'].astype('int')

    # df_geral
    tipo_juncao = "inner"

    df_geral = pd.merge(left=df_produtos, right=df_tipos_produtos, left_on="tipo_produto_id_pro", right_on="id_tipo_produto_tpr", how=tipo_juncao)
    df_geral = pd.merge(left=df_geral, right=df_produtos_x_sub_produtos, left_on="id_produto_pro", right_on="produto_id_psp", how=tipo_juncao)
    df_geral = pd.merge(left=df_geral, right=df_sub_produtos, left_on="sub_produto_id_psp", right_on="id_sub_produto_spr", how=tipo_juncao)
    df_geral = pd.merge(left=df_geral, right=df_tipos_sub_produtos, left_on="tipo_sub_produto_id_spr", right_on="id_tipo_sub_produto_tsp", how=tipo_juncao)
    
    df_base = df_geral.copy()

    df_geral = pd.merge(left=df_geral, right=df_sub_produtos_x_insumos, left_on="id_sub_produto_spr", right_on="sub_produto_id_spi", how=tipo_juncao)
    
    df_geral = pd.merge(left=df_geral, right=df_insumos, left_on="insumo_id_spi", right_on="id_insumo_ins", how=tipo_juncao)
    df_geral = pd.merge(left=df_geral, right=df_unidades, left_on="unidade_id_ins", right_on="id_unidade_uni", how=tipo_juncao)
    df_geral = pd.merge(left=df_geral, right=df_grandezas, left_on="grandeza_id_uni", right_on="id_grd", how=tipo_juncao)

    df_geral = df_geral.drop(['tipo_produto_id_pro','produto_id_psp','sub_produto_id_psp','id_tipo_sub_produto_tsp','sub_produto_id_spi','insumo_id_spi','unidade_id_ins','grandeza_id_uni'],axis=1)

    df_geral['cip'] = 0.00
    df_geral['cip'] = df_geral['cip'].astype('float')

    df_geral['pv'] = 0.00
    df_geral['pv'] = df_geral['pv'].astype('float')
    
    df_cip = df_geral[['id_sub_produto_x_insumo_spi','tipo_produto_tpr','produto_pro','sub_produto_spr','markup_spr','markup_minimo_tsp','peso_psp','unidade_id_psp','percentual_spi','rendimento_spi','id_insumo_ins','insumo_ins','cip','pv']].copy()   

    for linha in df_cip.itertuples(index=True):
        
        id_sub_produto_x_insumo_spi = linha.id_sub_produto_x_insumo_spi

        rendimento = linha.rendimento_spi
        percentual = linha.percentual_spi/100
        peso_produto = linha.peso_psp
        markup = linha.markup_spr
        markup_minimo = linha.markup_minimo_tsp

        markup = float(markup)
        markup_minimo = float(markup_minimo)

        if markup_minimo > markup:
            markup = markup_minimo

        insumo_id = linha.id_insumo_ins
        peso_insumo = percentual*peso_produto
        unidade_id = linha.unidade_id_psp
        result = volta_valor_insumo(insumo_id, peso_insumo, unidade_id, rendimento)
        cip = result[0]
        cip = round(cip,2)
        df_cip.loc[linha.Index,'cip'] = cip
        pv = (1+markup/100)*cip
        pv = round(pv,2)
        df_cip.loc[linha.Index,'pv'] = pv

        sql = f"UPDATE `sub_produtos_x_insumos` SET `cip` = '{cip}', pv_cip = '{pv}' WHERE id_sub_produto_x_insumo = '{id_sub_produto_x_insumo_spi}';"
        executa_DML(sql)

    df_cip_sum = df_cip[['tipo_produto_tpr','produto_pro','sub_produto_spr','cip','pv']].copy()
    df_cip_sum = df_cip_sum.groupby(['tipo_produto_tpr','produto_pro','sub_produto_spr']).sum()

    df_pfe = pd.merge(left=df_base,right=df_pfe, left_on='id_produto_pro', right_on="produto_id_pfe", how=tipo_juncao)
    df_pfe = pd.merge(left=df_pfe, right=df_insumos, left_on="insumo_id_pfe", right_on="id_insumo_ins", how=tipo_juncao)
    df_pfe = pd.merge(left=df_pfe, right=df_unidades, left_on="unidade_id_ins", right_on="id_unidade_uni", how=tipo_juncao)
    df_pfe= pd.merge(left=df_pfe, right=df_grandezas, left_on="grandeza_id_uni", right_on="id_grd", how=tipo_juncao)
    df_pfe = df_pfe.drop(['tipo_produto_id_pro','produto_id_psp','sub_produto_id_psp','id_tipo_sub_produto_tsp','produto_id_pfe','unidade_id_ins','grandeza_id_uni'],axis=1)


    df_pfi = pd.merge(left=df_base, right=df_pfi, left_on='id_produto_pro', right_on="produto_id_pfi", how=tipo_juncao)
    df_pfi = pd.merge(left=df_pfi, right=df_insumos, left_on="insumo_id_pfi", right_on="id_insumo_ins", how=tipo_juncao)
    df_pfi = pd.merge(left=df_pfi, right=df_unidades, left_on="unidade_id_ins", right_on="id_unidade_uni", how=tipo_juncao)
    df_pfi= pd.merge(left=df_pfi, right=df_grandezas, left_on="grandeza_id_uni", right_on="id_grd", how=tipo_juncao)
    df_pfi = df_pfi.drop(['tipo_produto_id_pro','produto_id_psp','sub_produto_id_psp','id_tipo_sub_produto_tsp','produto_id_pfi','unidade_id_ins','grandeza_id_uni'],axis=1)

    #df_geral = pd.merge(left=df_geral, right=df_processo_feitura_produtos, left_on="id_produto_pro", right_on="produto_id_pfp", how=tipo_juncao)

    for linha in df_pfe.itertuples(index=True):
        id_tabela = linha.id_pfe_pfe
        sql = f"SELECT `quilowatt_hora` FROM dados_gerais WHERE `id_dados` = '1'"
        result = executa_DQL(sql)
        custo_por_hora_energia_reais = result[0][0]
        custo_por_hora_energia_reais = str(custo_por_hora_energia_reais)
        custo_por_hora_energia_reais = custo_por_hora_energia_reais.replace(",",".")
        custo_por_hora_energia_reais = float(custo_por_hora_energia_reais)

        potencia = linha.potencia_w_pfe
        tempo = linha.tempo_energia_eletrica_pfe
        tempo = tempo/60
        potencia = potencia/1000
        kwh = potencia * tempo * custo_por_hora_energia_reais
        kwh = round(kwh,2)
        df_pfe.loc[linha.Index,'cel_pfe'] = kwh

    for linha in df_pfe.itertuples(index=True):
        id_tabela = linha.id_pfi_pfi
        rendimento = 100
        peso_insumo = linha.mensuracao_pfi
        insumo_id = linha.insumo_id_pfi
        unidade_id = linha.unidade_id_pfi
        result = volta_valor_insumo(insumo_id, peso_insumo, unidade_id, rendimento)
        cpfi = result[0]
        cpfi = round(cpfi,2)
        df_pfi.loc[linha.Index,'cpfi_pfi'] = cpfi

        sql = f"UPDATE `processo_feitura_produtos` SET `cpfp` = '{cpfp}', cel = '{kwh}' WHERE id_pfp = '{id_tabela}';"
        executa_DML(sql)

    df_fpr = pd.merge(left=df_base, right=df_finalizacao_produtos, left_on='id_produto_pro', right_on="produto_id_fpr", how=tipo_juncao)
    df_fpr = pd.merge(left=df_fpr, right=df_insumos, left_on="insumo_id_fpr", right_on="id_insumo_ins", how=tipo_juncao)
    df_fpr = pd.merge(left=df_fpr, right=df_unidades, left_on="unidade_id_fpr", right_on="id_unidade_uni", how=tipo_juncao)
    df_fpr = pd.merge(left=df_fpr, right=df_grandezas, left_on="grandeza_id_uni", right_on="id_grd", how=tipo_juncao)
    df_fpr = df_fpr.drop(['tipo_produto_id_pro','insumo_id_fpr','produto_id_psp','sub_produto_id_psp','id_tipo_sub_produto_tsp','produto_id_fpr','unidade_id_ins','grandeza_id_uni'],axis=1)

    for linha in df_fpr.itertuples(index=True):
        
        id_tabela = linha.id_fpr_fpr

        rendimento = 100
        peso_insumo = linha.mensuracao_fpr
        insumo_id = linha.id_insumo_ins
        unidade_id = linha.unidade_id_psp
        result = volta_valor_insumo(insumo_id, peso_insumo, unidade_id, rendimento)
        cfpr = result[0]
        cfpr = round(cfpr,2)
        df_fpr.loc[linha.Index,'cfpr_fpr'] = cfpr

        sql = f"UPDATE `finalizacao_produtos` SET `cfpr` = '{cfpr}' WHERE id_fpr = '{id_tabela}';"
        executa_DML(sql)

    sql = "SELECT `salario_nv_1`,`salario_nv_2`,`salario_nv_3`,`fator_nao_pv` FROM `dados_gerais` WHERE `id_dados` = '1'"
    result = executa_DQL(sql)
    
    salario_nv_1 = result[0][0]
    salario_nv_2 = result[0][1]
    salario_nv_3 = result[0][2]
    fator_nao_pv = result[0][3]

    sql = "SELECT `id_produto` FROM `produtos`"
    result_produto = executa_DQL(sql)
    
    for item in result_produto:
        produto_id = item[0]

        try:
            sql = f"SELECT `tempo_min_grau_1_mo`,`tempo_min_grau_2_mo`,`tempo_min_grau_3_mo` from `produtos_x_mo` WHERE `produto_id` = '{produto_id}'"
            result = executa_DQL(sql)
            tempo_min_nv_1 = result[0][0]
            tempo_min_nv_2 = result[0][1]
            tempo_min_nv_3 = result[0][2]
        except:
            tempo_min_nv_1 = 0
            tempo_min_nv_2 = 0
            tempo_min_nv_3 = 0

        custo_mo_nv_1 = tempo_min_nv_1/(22*8*60)*salario_nv_1
        custo_mo_nv_2 = tempo_min_nv_2/(22*8*60)*salario_nv_2
        custo_mo_nv_3 = tempo_min_nv_3/(22*8*60)*salario_nv_3

        custo_total_mo = custo_mo_nv_1 + custo_mo_nv_2 + custo_mo_nv_3
        custo_total_mo = round(custo_total_mo,2)

        sql = f"UPDATE `produtos_x_mo` SET `cpmo` = '{custo_total_mo}' WHERE `produto_id` = '{produto_id}';"
        executa_DML(sql)     

        #'total_cip'
        sql = f"SELECT `sub_produto_id` FROM `produtos_x_sub_produtos` where `produto_id` = '{produto_id}'"
        result_psp = executa_DQL(sql)

        cip = 0
        pv_cip = 0

        for item in result_psp:
            sub_produto_id = item[0]

            sql = f"SELECT sum(`cip`) FROM sub_produtos_x_insumos WHERE `sub_produto_id` = '{sub_produto_id}'"
            result = executa_DQL(sql)
            soma_1 = result[0][0]
            soma_1 = float(soma_1)
            cip += soma_1

            sql = f"SELECT sum(`pv_cip`) FROM sub_produtos_x_insumos WHERE `sub_produto_id` = '{sub_produto_id}'"
            result = executa_DQL(sql)
            soma_2 = result[0][0]
            try:
                soma_2 = float(soma_2)
            except:
                soma_2 = float(0)

            pv_cip += soma_2

        #'total_cfpr'
        sql = f"SELECT sum(`cfpr`) FROM `finalizacao_produtos` WHERE `produto_id` = '{produto_id}'"
        result = executa_DQL(sql)
        cfpr = result[0][0]

        #'total_cpfp'
        sql = f"SELECT sum(`cpfp`) FROM `processo_feitura_produtos` WHERE `produto_id` = '{produto_id}'"
        result = executa_DQL(sql)
        cpfp = result[0][0]        
        
        #'total_cpmo'
        cpmo = custo_total_mo
        
        #'total_cel',
        sql = f"SELECT sum(`cel`) FROM `processo_feitura_produtos` WHERE `produto_id` = '{produto_id}'"
        result = executa_DQL(sql)
        cel = result[0][0] 

        #'pv'
        try:
            pv = pv_cip
        except:
            pv = 0

        try:
            pv += cel*fator_nao_pv
        except:
            pv += 0

        try:
            pv += cpmo*fator_nao_pv
        except:
            pv += 0

        try:
            pv += cpfp*fator_nao_pv
        except:
            pv += 0

        try:
            pv += cfpr*fator_nao_pv
        except:
            pv += 0

        #pv = pv_cip + (cel+cpmo+cpfp+cfpr)*fator_nao_pv

        pv = int(pv)+1
        pv = round(pv,2)
        print(pv)

        sql = f"UPDATE `centro_custos_produto` SET `total_cpmo` = '{cpmo}', `total_cip`='{cip}', `total_cfpr` = '{cfpr}', `total_cpfp` = '{cpfp}', `total_cel` = '{cel}', `pv`='{pv}' WHERE `produto_id` = '{produto_id}';"
        executa_DML(sql)

        sql = f"UPDATE `produtos` SET `pv`='{pv}' WHERE `id_produto` = '{produto_id}';"
        executa_DML(sql)

    if menu == True:
        lista = criar_linhas_menu()

        if len(lista)>=1:
            criar_pdf(lista)

    if excel == True:
        caminho_salvar = fr'{pastaApp}\dados\dados.xlsx'

        try:
            with pd.ExcelWriter(caminho_salvar, engine="openpyxl") as writer:
                df_grandezas.to_excel(writer, sheet_name="grandezas")
                df_unidades.to_excel(writer, sheet_name="unidades")
                df_insumos.to_excel(writer, sheet_name="insumos")
                df_tipos_sub_produtos.to_excel(writer, sheet_name="tipos_sub_produtos")
                df_sub_produtos.to_excel(writer, sheet_name="sub_produtos")
                df_tipos_produtos.to_excel(writer, sheet_name="tipos_produtos")
                df_produtos.to_excel(writer, sheet_name="produtos")
                df_sub_produtos_x_insumos.to_excel(writer, sheet_name="sub_produtos_x_insumos")
                df_produtos_x_sub_produtos.to_excel(writer, sheet_name="produtos_x_sub_produtos")
                df_processo_feitura_produtos.to_excel(writer, sheet_name="proc_feitura_prods")
                df_finalizacao_produtos.to_excel(writer, sheet_name="finalizacao_prods")
                df_produtos_x_mo.to_excel(writer, sheet_name="produtos_x_mo")
                df_geral.to_excel(writer, sheet_name="geral")
                df_cip.to_excel(writer, sheet_name="cip")
                df_cip_sum.to_excel(writer, sheet_name="cip_sum")
                #df_menu.to_excel(writer, sheet_name="menu")
                df_pfp.to_excel(writer, sheet_name="pfp")
                df_fpr.to_excel(writer, sheet_name="fpr")
        except:
            messagebox.showinfo("ERRO","Arquivo .xlsx está aberto. Feche-o e tente de novo.")
