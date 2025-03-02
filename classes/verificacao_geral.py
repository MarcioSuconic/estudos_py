from utilitarios import executa_DML, executa_DQL
from tkinter import messagebox

def verificar():
    # sub produtos x 100 %
    lista_produtos_aptos = list()
    lista_produtos_nao_aptos = list()
    lista_sub_produtos = list()

    sql = "SELECT `id_produto`,`produto` FROM `produtos`"
    result_produtos = executa_DQL(sql)
    mensagens = ""

    if len(result_produtos) == 0:
        messagebox.showinfo("Aviso","Não há produtos para verificação.")
        return()

    for item in result_produtos:
        id_produto = item[0]
        produto = item[1]
        erros = 0

        # cel
        sql = f"SELECT sum(`potencia_w`) FROM `processo_feitura_produtos` where `produto_id` = '{id_produto}' and `ativo`='1'"
        result = executa_DQL(sql)

        try:
            pot = result[0][0]
        except:
            pot = None

        sql = f"SELECT sum(`tempo_energia_eletrica`) FROM `processo_feitura_produtos` where `produto_id` = '{id_produto}' and ativo = '1'"
        result = executa_DQL(sql)
        try:
            tempo_enel = result[0]
        except:
            tempo_enel = None

        if pot == 0 or tempo_enel == 0 or pot == None or tempo_enel == None:
            mensagens += f'Produto: {produto} de ID {id_produto} falta custo da energia elétrica.\n'    
            erros += 1

        # cpmo
        sql = f"SELECT `tempo_min_grau_1_mo`,`tempo_min_grau_2_mo`,`tempo_min_grau_3_mo` FROM `produtos_x_mo` WHERE `produto_id` = '{id_produto}' and `ativo` = '1'"
        result = executa_DQL(sql)

        try:
            tempo_1 = result[0][0]
        except:
            tempo_1 = None

        try:
            tempo_2 = result[0][1]
        except:
            tempo_2 = None

        try:
            tempo_3 = result[0][2]
        except:
            tempo_3 = None

        if ((tempo_1 == 0 and tempo_2 == 0 and tempo_3 == 0) or (tempo_1 == None and tempo_2 == None and tempo_3 == None)):
            mensagens += f'Produto: {produto} de ID {id_produto} falta custo da mão de obra.\n'    
            erros += 1

        # cpfp
        sql = f"SELECT count(`id_pfp`) FROM `processo_feitura_produtos` where `produto_id` = '{id_produto}' and `ativo`='1'"
        result = executa_DQL(sql)

        try:
            contagem = result[0][0]
        except:
            contagem = None

        if contagem == 0 or contagem == None:
            mensagens += f'Produto: {produto} de ID {id_produto} faltam insumos para a feitura do produto.\n' 
            erros += 1

        # cfpr    
        sql = f"SELECT COUNT(`id_fpr`) FROM `finalizacao_produtos` where `produto_id` = '{id_produto}' and `ativo`='1';"
        result = executa_DQL(sql)

        try:
            contagem = result[0][0]
        except:
            contagem = None

        if contagem == 0 or contagem == None:
            mensagens += f'Produto: {produto} de ID {id_produto} faltam insumos para a finalização do produto.\n' 
            erros += 1

        # cip
        lista_sub_produtos = []

        sql = f"SELECT `sub_produto_id` FROM `produtos_x_sub_produtos` where `produto_id` = '{id_produto}' and `ativo` = '1'"
        result = executa_DQL(sql)

        for item in result:
            lista_sub_produtos.append(item[0])

        for item in lista_sub_produtos:
            id_sub_produto = item

            sql = f"SELECT sum(`percentual`) from `sub_produtos_x_insumos` WHERE `sub_produto_id` = '{id_sub_produto}' and `ativo` = '1'"
            result = executa_DQL(sql)

            percentual = result[0][0]
            
            try:
                percentual = float(percentual)
            except:
                percentual = 0

            if percentual != 100:
                sql = f"select `sub_produto` FROM `sub_produtos` WHERE `id_sub_produto` = '{id_sub_produto}' and `ativo`='1'"
                result = executa_DQL(sql)
                sub_produto = result[0][0]
                mensagens += f'Sub produto: {sub_produto} com o ID {id_sub_produto} do produto: {produto} de ID {id_produto} está com {percentual} da receita.\n' 
                erros += 1

        if erros == 0:
            lista_produtos_aptos.append(id_produto)
            sql = f"UPDATE `produtos` SET menu = '1' WHERE id_produto = '{id_produto}';"
            result = executa_DML(sql)
        else:            
            lista_produtos_nao_aptos.append(id_produto)
            sql = f"UPDATE `produtos` SET menu = '0' WHERE id_produto = '{id_produto}';"
            result = executa_DML(sql)

    print(f'produtos aptos {lista_produtos_aptos}')
    print(f'produtos não aptos {lista_produtos_nao_aptos}')

    if mensagens != "":
        messagebox.showinfo("Aviso",mensagens)
    else:
        messagebox.showinfo("Tudo OK","Todos os produtos estão com os dados OK")
        