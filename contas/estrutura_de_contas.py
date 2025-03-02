import pandas as pd
from conexao import ConexaoBD

def criando_df_contas_contabeis(data_inicial_sql,data_final_sql):
    conexao = ConexaoBD()
    sql = f"SELECT `id`,`referencia_mes_transacao`,`referencia_ano_transacao`,`data_lancamento`,`valor_lancamento`,`conta_creditada_id`,`conta_debitada_id` FROM financeiro.fin_transacoes WHERE `data_lancamento` <= '{data_final_sql}' and `transacao_realizada` = '1';"
    result = conexao.executa_DQL(sql)

    lista_id = []
    lista_referencia_mes = []
    lista_referencia_ano = []
    lista_data_lancamento = []
    lista_valor_lancamento = []
    lista_conta_creditada_id = []
    lista_conta_debitada_id = []

    for item in result:
        id = item[0]
        referencia_mes = item[1]
        referencia_ano = item[2]
        data_lancamento = item[3]
        valor_lancamento = item[4]
        conta_creditada_id = item[5]
        conta_debitada_id = item[6]

        lista_id.append(id)
        lista_referencia_mes.append(referencia_mes)
        lista_referencia_ano.append(referencia_ano)
        lista_data_lancamento.append(data_lancamento)
        lista_valor_lancamento.append(valor_lancamento)
        lista_conta_creditada_id.append(conta_creditada_id)
        lista_conta_debitada_id.append(conta_debitada_id)

    df_financeiro = pd.DataFrame(data=[lista_id,lista_referencia_mes,lista_referencia_ano,lista_data_lancamento,lista_valor_lancamento,lista_conta_creditada_id,lista_conta_debitada_id]).transpose()
    df_financeiro.columns=['id','ref_mes','ref_ano','data','valor','cta_credito_id','cta_debito_id']
    df_financeiro.set_index('id', inplace=True, drop=True)

    # contas_nivel_5
    sql ='SELECT `id`,`nome_conta_contabilidade_nv5`,`natureza_da_conta`,`conta_nivel_4_id` FROM financeiro.fin_contas_contabilidade_nv5;'
    result = conexao.executa_DQL(sql)

    lista_ids = []
    lista_nomes= []
    lista_natureza = []
    lista_conta_mae = []

    for item in result:
        lista_ids.append(item[0])
        lista_nomes.append(item[1])
        lista_natureza.append(item[2])
        lista_conta_mae.append(item[3])

    df_contas_nivel_5 = pd.DataFrame(data=[lista_ids,lista_nomes,lista_natureza,lista_conta_mae]).transpose()
    df_contas_nivel_5.columns=['id','nome','natureza','id_conta_mae']
    # contas_nivel_4
    sql ='SELECT `id`,`nome_conta_nv_4`,`natureza_da_conta`,`conta_mae_nivel_3_id` FROM financeiro.fin_contas_niv_4;'
    result = conexao.executa_DQL(sql)
    lista_ids = []
    lista_nomes= []
    lista_natureza = []
    lista_conta_mae = []

    for item in result:
        lista_ids.append(item[0])
        lista_nomes.append(item[1])
        lista_natureza.append(item[2])
        lista_conta_mae.append(item[3])

    df_contas_nivel_4 = pd.DataFrame(data=[lista_ids,lista_nomes,lista_natureza,lista_conta_mae]).transpose()
    df_contas_nivel_4.columns=['id','nome','natureza','id_conta_mae']
    # contas_nivel_3
    sql ='SELECT `id`,`nome_conta_nv_3`,`natureza_da_conta`,`conta_mae_nivel_2_id` FROM financeiro.fin_contas_niv_3;'
    result = conexao.executa_DQL(sql)
    lista_ids = []
    lista_nomes= []
    lista_natureza = []
    lista_conta_mae = []

    for item in result:
        lista_ids.append(item[0])
        lista_nomes.append(item[1])
        lista_natureza.append(item[2])
        lista_conta_mae.append(item[3])

    df_contas_nivel_3 = pd.DataFrame(data=[lista_ids,lista_nomes,lista_natureza,lista_conta_mae]).transpose()
    df_contas_nivel_3.columns=['id','nome','natureza','id_conta_mae']
    # contas_nivel_2
    sql ='SELECT `id`,`nome_conta_nv_2`,`natureza_da_conta`,`conta_mae_nivel_1_id` FROM financeiro.fin_contas_niv_2;'
    result = conexao.executa_DQL(sql)
    lista_ids = []
    lista_nomes= []
    lista_natureza = []
    lista_conta_mae = []

    for item in result:
        lista_ids.append(item[0])
        lista_nomes.append(item[1])
        lista_natureza.append(item[2])
        lista_conta_mae.append(item[3])

    df_contas_nivel_2 = pd.DataFrame(data=[lista_ids,lista_nomes,lista_natureza,lista_conta_mae]).transpose()
    df_contas_nivel_2.columns=['id','nome','natureza','id_conta_mae']
    # contas_nivel_1
    sql = "SELECT `id`,`nome_conta_nv_1`,`natureza_da_conta` FROM financeiro.fin_contas_niv_1;"
    result = conexao.executa_DQL(sql)
    lista_ids = []
    lista_nomes= []
    lista_natureza = []

    for item in result:
        lista_ids.append(item[0])
        lista_nomes.append(item[1])
        lista_natureza.append(item[2])

    df_contas_nivel_1 = pd.DataFrame(data=[lista_ids,lista_nomes,lista_natureza]).transpose()
    df_contas_nivel_1.columns=['id','nome','natureza']
    df_contas_completas = pd.merge(left=df_contas_nivel_5,right=df_contas_nivel_4,left_on='id_conta_mae',right_on='id',suffixes=['_5','_4'])
    df_contas_completas = pd.merge(left=df_contas_completas,right=df_contas_nivel_3,left_on='id_conta_mae_4',right_on='id',suffixes=['_4','_3'])
    df_contas_completas = pd.merge(left=df_contas_completas,right=df_contas_nivel_2,left_on='id_conta_mae',right_on='id',suffixes=['_3','_2'])
    df_contas_completas = pd.merge(left=df_contas_completas,right=df_contas_nivel_1,left_on='id_conta_mae_2',right_on='id',suffixes=['_2','_1'])
    df_contas_completas.drop(['natureza_5', 'id_conta_mae_5', 'id_4', 'natureza_4', 'id_conta_mae_4', 'id_3', 'natureza_3', 'id_conta_mae_3', 'id_2', 'natureza_2', 'id_conta_mae_2'], inplace=True, axis=1)
    df_contas_completas.set_index('id_5',drop=True,inplace=True)
    df_contas_completas.sort_values('nome_5', inplace=True, axis=0, ascending=True)

    df_contas_completas['saldo_devedor'] = 0
    df_contas_completas['saldo_credor'] = 0
    df_contas_completas['saldo_conta'] = 0
    df_contas_completas['saldo_devedor'] = df_contas_completas['saldo_devedor'].astype('float')
    df_contas_completas['saldo_credor'] = df_contas_completas['saldo_credor'].astype('float')
    df_contas_completas['saldo_conta'] = df_contas_completas['saldo_conta'].astype('float')
  
    # df_contas_completas[[df_contas_completas['natureza'] == 'C']].saldo_conta = df_contas_completas['saldo_credor'] - df_contas_completas['saldo_devedor']
    # df_contas_completas[[df_contas_completas['natureza'] == 'D']].saldo_conta = df_contas_completas['saldo_devedor'] - df_contas_completas['saldo_credor']

    print('adicionando valores de débito e crédito às contas')
    for linha in df_financeiro.itertuples():
        #'id','ref_mes','ref_ano','data','valor','cta_credito_id','cta_debito_id'
        df_contas_completas.loc[linha.cta_credito_id,'saldo_credor'] += linha.valor
        df_contas_completas.loc[linha.cta_debito_id,'saldo_devedor'] += linha.valor        

    for linha in df_contas_completas.itertuples(index=True):
        if linha.natureza == 'C':
            df_contas_completas.loc[linha.Index,'saldo_conta'] = df_contas_completas.loc[linha.Index,'saldo_credor'] - df_contas_completas.loc[linha.Index,'saldo_devedor']
        if linha.natureza == 'D':
            df_contas_completas.loc[linha.Index,'saldo_conta'] = df_contas_completas.loc[linha.Index,'saldo_devedor'] - df_contas_completas.loc[linha.Index,'saldo_credor']   

    # print('gravando os dados em excel')
    # # gravacao do arquivo com as pastas
    # caminho = fr"c:\dados para analise\dados\contas_contabilidade.xlsx"
    # with pd.ExcelWriter(caminho, engine="openpyxl") as writer:
    #     df_contas_completas.to_excel(writer, sheet_name="contas")
    return(df_contas_completas)
