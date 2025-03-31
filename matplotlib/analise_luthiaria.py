from conexao import ConexaoBD
import matplotlib.pyplot as plt

conexao = ConexaoBD()

class AnaliseLuthiaria:

    def __init__(self, data_inicial: str, data_final: str):
        self.ano_inicial = data_inicial[0:4]
        self.mes_inicial = data_inicial[5:7]
        self.dia_inicial = data_inicial[8:10]

        self.ano_final = data_final[0:4]
        self.mes_final = data_final[5:7]
        self.dia_final = data_final[8:10]

        self.lista_final_ref = []
        self.lista_final_valores_bruto = []
        self.lista_final_valores_liquidos = []

        self.lista_refs_datas_meses_anos = self.devolve_lista_datas_meses_ref()
        self.lista_ids_fechamentos_caixas = self.devolve_ids_fechamentos_caixas()
        self.lista_ids_boletos = self.devolve_lista_ids_boletos()        
        self.listas_valores_brutos = self.devolve_valores_brutos_boletos()
        self.listas_valores_liquidos = self.devolve_valores_brutos_liquidos()
        self.lista_soma_valores_brutos = self.devolve_soma_valor_bruto_por_ref()
        self.lista_soma_valores_liquidos = self.devolve_soma_valor_liquido_por_ref()       
        self.lista_refs = self.devolve_lista_refs()

        fig = plt.figure()
        ax = fig.add_subplot()

        lista_meses = self.lista_refs
        lista_valores = self.lista_soma_valores_brutos
        ax.plot(lista_meses,lista_valores)

        lista_meses = self.lista_refs
        lista_valores = self.lista_soma_valores_liquidos
        ax.plot(lista_meses,lista_valores)

        plt.show()


    def devolve_lista_datas_meses_ref(self):
        vai = True
        lista_refs = []

        mes_inicial = int(self.mes_inicial)
        ano_inicial = int(self.ano_inicial)

        mes_final = int(self.mes_final)
        ano_final = int(self.ano_final)

        ano = ano_inicial
        mes = mes_inicial

        while (vai==True):

            lista_temp = []
            lista_temp.append(mes)
            lista_temp.append(ano)
            lista_refs.append(lista_temp)

            if mes == mes_final and ano == ano_final:
                vai = False

            if mes == 12:
                mes = 1
                ano += 1
            else:
                mes += 1

        return(lista_refs)
    
    def devolve_ids_fechamentos_caixas_datas(self):
        sql = sql = f"SELECT `id` FROM `marsoft`.`msf_slj_fechamentos_caixas` WHERE `mes` = '{self.mes_leitura}' and `ano`='{self.ano_leitura}';"
        result = conexao.executa_DQL(sql)

        lista_temp = []

        for item in result:            
            lista_temp.append(item[0])

        return(lista_temp)

    def devolve_ids_fechamentos_caixas(self):
        
        lista_ids_fechamentos_caixas = []

        for item in self.lista_refs_datas_meses_anos:
            self.mes_leitura = item[0]
            self.ano_leitura = item[1]
            lista = self.devolve_ids_fechamentos_caixas_datas()
            lista_ids_fechamentos_caixas.append(lista)

        return(lista_ids_fechamentos_caixas)
        
    def devolve_lista_ids_boletos(self):

        lista_ids_boletos_geral = []

        for item_sup in self.lista_ids_fechamentos_caixas:
            lista_temp = []

            for item in item_sup:
                sql = f"SELECT `id` FROM marsoft.msf_slj_boletos WHERE `fechamento_caixa_id` = '{item}' and `eh_luthiaria` = '1' ORDER BY `id`;"
                result = conexao.executa_DQL(sql)

                for id_boleto in result:
                    lista_temp.append(id_boleto[0])

            lista_ids_boletos_geral.append(lista_temp)

        return(lista_ids_boletos_geral)   
    
    def devolve_valores_brutos_boletos(self):

        lista_valores_bruto = []

        for ref in self.lista_ids_boletos:

            lista_temp = []

            for boleto_id in ref:
                sql = f"SELECT sum(`preco_total`) FROM `marsoft`.`msf_slj_boletos_x_produtos` WHERE `boleto_id` = '{boleto_id}';"
                result = conexao.executa_DQL(sql)
                valor_bruto = result[0][0]
                valor_bruto = round(valor_bruto,2)
                lista_temp.append(valor_bruto)

            lista_valores_bruto.append(lista_temp)

        return(lista_valores_bruto)

    
    def devolve_valores_brutos_liquidos(self):

        lista_valores_liq = []

        for ref in self.lista_ids_boletos:

            lista_temp = []

            for boleto_id in ref:
                sql = f"SELECT sum(`preco_total`) FROM `marsoft`.`msf_slj_boletos_x_produtos` WHERE `boleto_id` = '{boleto_id}' and `produto_id` = '4857';"
                result = conexao.executa_DQL(sql)
                valor_bruto = result[0][0]
                valor_bruto = round(valor_bruto,2)
                lista_temp.append(valor_bruto)
            
            lista_valores_liq.append(lista_temp)

        return(lista_valores_liq)

    def devolve_soma_valor_bruto_por_ref(self):
        
        lista = []

        for ref in self.listas_valores_brutos:
            soma = 0

            for venda in ref:
                soma += venda

            soma = round(soma,2)
            lista.append(soma)

        return(lista)

    def devolve_soma_valor_liquido_por_ref(self):
        
        lista = []

        for ref in self.listas_valores_liquidos:
            soma = 0

            for venda in ref:
                soma += venda

            soma = round(soma,2)
            lista.append(soma)

        return(lista)

    def devolve_lista_refs(self):

        lista = []

        for item in self.lista_refs_datas_meses_anos:
            mes = str(item[0])
            ano = str(item[1])
            ref =f'{mes}/{ano}'
            lista.append(ref)

        return(lista)

AnaliseLuthiaria('2024-08-01','2025-03-31')
