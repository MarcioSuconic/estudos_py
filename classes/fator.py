from utilitarios import executa_DML, executa_DQL

def volta_valor_insumo(insumo_id, mensuracao, unidade_id, rendimento=100):

    sql = f"SELECT `unidade_id`,`qtde_ref`,`peso_uma_unidade_ref`,`preco_ref` FROM `insumos` WHERE `id_insumo` = '{insumo_id}' and `ativo` = '1';"
    result = executa_DQL(sql)

    unidade_id_insumo = int(result[0][0])
    qtde_ref_insumo = result[0][1]
    peso_uma_unidade_ref_insumo = result[0][2]
    preco_ref_insumo = result[0][3]

    sql = f"SELECT `grandeza_id` FROM `unidades` WHERE `id_unidade`='{unidade_id}'"
    result = executa_DQL(sql)
    id_grandeza_insumo_id = int(result[0][0])

    sql = f"SELECT `grandeza_id` FROM `unidades` WHERE `id_unidade`='{unidade_id_insumo}'"
    result = executa_DQL(sql)
    id_grandeza_unidade_insumo_id = result[0][0]

    if id_grandeza_insumo_id == id_grandeza_unidade_insumo_id:
        if int(unidade_id) == int(unidade_id_insumo):
            fator = 1
        else:
            sql = f"SELECT `fator_multiplicador_de_1_p_2` FROM `relacionamento_unidades` where `unidade_2` = '{int(unidade_id)}' and `unidade_1` = '{int(unidade_id_insumo)}'"
            result = executa_DQL(sql)
            try:    
                fator = result[0][0]
            except:
                fator =1
        valor = (preco_ref_insumo*fator*mensuracao)/qtde_ref_insumo

    else:
        if int(unidade_id) == 2:
            fator = mensuracao/peso_uma_unidade_ref_insumo
        else:
            sql = f"SELECT `fator_multiplicador_de_1_p_2` FROM `relacionamento_unidades` where `unidade_2` = '{int(unidade_id)}' and `unidade_1` = '2'"
            result = executa_DQL(sql)
            valor_achado = result[0][0]
            fator = valor_achado / peso_uma_unidade_ref_insumo          

        valor = fator * preco_ref_insumo
    
    valor = valor * (100/rendimento)
    return([valor])
