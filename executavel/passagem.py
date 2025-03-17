from selenium import webdriver
import time
from datetime import datetime, timedelta
from dist.conexao import executa_DML
import pywhatkit

class Pegar_Preco_PassagemAerea:

    def __init__(self, compania, dia_viagem, mes_viagem, ano_viagem, origem, destino, tempo_espera_segundos_site, avisar_valor: float, numero_whattsapp: str) -> str:
        self.dia_viagem = dia_viagem
        self.mes_viagem = mes_viagem
        self.ano_viagem = ano_viagem
        self.compania = compania       
        self.origem = origem
        self.destino = destino
        self.tempo_espera_segundos = tempo_espera_segundos_site

        self.url = self.retorna_url(self.compania,self.dia_viagem, self.mes_viagem, self.ano_viagem, self.origem, self.destino)
        self.chave = self.retorna_chave(self.compania)
        self.tipo_chave = self.retorna_tipo_chave(self.compania)

        self.avisar_valor = avisar_valor

        self.numero_whattsapp = numero_whattsapp

        # abrir o navegador
        navegador = webdriver.Chrome()        

        # acessar um site
        navegador.get(self.url)

        # espera do site carregar
        time.sleep(self.tempo_espera_segundos)

        # pegar preço
        try:
            preco_str = navegador.find_element(self.tipo_chave, self.chave).text
        except:
            if self.compania == "GOL":
                preco_str = 'R$ 8.888,88'
            if self.compania == "LATAM":
                preco_str = 'BRL 8.888,88'

        if self.compania == "GOL":
            try:
                self.origem = navegador.find_element(self.tipo_chave, "lbl_origin_1_emission").text
                self.destino = navegador.find_element(self.tipo_chave, "lbl_destination_1_emission").text
            except:
                pass

        if self.compania == "LATAM":

            try:
                sup_origem_1 = navegador.find_element(self.tipo_chave, "lcVysi").text
                sup_origem_2 = navegador.find_element(self.tipo_chave, "kgsfDI").text            
                sup_destino_1 = navegador.find_element(self.tipo_chave, "jrxwkA").text
                sup_destino_2 = navegador.find_element(self.tipo_chave, "kgsfDI").text                
                print(f'{sup_origem_1=}')
                print(f'{sup_origem_2=}')
                print(f'{sup_destino_1=}')
                print(f'{sup_destino_2=}')

                self.origem = f'{sup_origem_2} - {sup_origem_1}'
            except:
                pass

        self.preco_float = self.retorna_preco(self.compania,preco_str)
        msg = f"{self.compania}, {self.origem}-{self.destino}, {dia_viagem}/{mes_viagem}/{ano_viagem}, {self.preco_float}"        

        if self.preco_float <= self.avisar_valor:            
            agora = datetime.now()
            hora = agora.hour
            minutos = agora.minute
            
            print(hora)
            print(minutos)

            if minutos >= 59:
                minutos = 2
                hora = hora + 1

            print(self.numero_whattsapp)            

            pywhatkit.sendwhatmsg(self.numero_whattsapp, msg, hora, minutos+2, 30)
        
        self.inserir_no_banco_de_dados()        
        navegador.close()

    def retorna_preco(self, compania, valor_str) -> float:
        if self.compania == "LATAM":
            valor_float = self.entra_valor_str_sai_float_brl(valor_str)
        if self.compania == "GOL":
            valor_float = self.entra_valor_str_sai_float_reais(valor_str)
        return(valor_float)

    def retorna_url(self, compania:str , dia_viagem:str , mes_viagem:str , ano_viagem: str, origem, destino) -> str:
        if compania == "LATAM":
            url = f"https://www.latamairlines.com/br/pt/oferta-voos?origin={origem}&outbound={ano_viagem}-{mes_viagem}-{dia_viagem}T12%3A00%3A00.000Z&destination={destino}&inbound=null&adt=1&chd=0&inf=0&trip=OW&cabin=Economy&redemption=false&sort=PRICE%2Casc"
            return(url)
        
        if compania == "GOL":
            url = f"https://b2c.voegol.com.br/compra/busca-parceiros?pv=br&tipo=DF&de={origem}&para={destino}&ida={dia_viagem}-{mes_viagem}-{ano_viagem}&ADT=1&ADL=0&CHD=0&INF=0&voebiz=0"
            return(url)

    def retorna_tipo_chave(self, compania:str) -> str:
        if compania =="LATAM":            
            tipo_chave = "class name"
        if compania =="GOL":            
            tipo_chave = "id"
        return(tipo_chave)

    def retorna_chave(self, compania:str) -> str:
        if compania =="LATAM": 
            chave = "koxMWe"
        if compania =="GOL": 
            chave = "lbl_priceValue_1_emission"
        return(chave)

    def entra_valor_str_sai_float_brl(self, vl_str: str) -> float:
        # decimal
        valor_str = vl_str[4:]
        print(valor_str)
        vl_decimais_1 = valor_str[-2]
        vl_decimais_2 = valor_str[-1]
        vl_decimal = (int(f'{vl_decimais_1}{vl_decimais_2}'))/100

        # inteiro
        tamanho = len(valor_str)
        tamanho_querido = tamanho - 3
        vl_inteiro = valor_str[:tamanho_querido]
        vl_inteiro = vl_inteiro.replace(".","")
        vl_inteiro = vl_inteiro.replace(",","")  
        
        try:
            vl_inteiro = int(vl_inteiro)
        except:
            vl_interio = 8888
            print('deu ruim em valor_passagem')

        valor_float=(vl_inteiro + vl_decimal)

        return(valor_float)

    def entra_valor_str_sai_float_reais(self, vl_str: str) -> float:
        # decimal
        valor_str = vl_str[3:]
        vl_decimais_1 = valor_str[-2]
        vl_decimais_2 = valor_str[-1]
        vl_decimal = (int(f'{vl_decimais_1}{vl_decimais_2}'))/100

        # inteiro
        tamanho = len(valor_str)
        tamanho_querido = tamanho - 3
        vl_inteiro = valor_str[:tamanho_querido]
        vl_inteiro = vl_inteiro.replace(".","")
        vl_inteiro = vl_inteiro.replace(",","")  
        
        try:
            vl_inteiro = int(vl_inteiro)
        except:
            vl_interio = 8888
            print('deu ruim em valor_passagem')

        valor_float=(vl_inteiro + vl_decimal)

        return(valor_float)
    
    def inserir_no_banco_de_dados(self):
        hoje = datetime.now()
        dia = self.dia_viagem
        mes = self.mes_viagem
        ano = self.ano_viagem
        preco = self.preco_float
        compania = self.compania
        origem = self.origem
        destino = self.destino

        sql = f"INSERT INTO `passagens` (`origem`,`destino`,`data_pesquisa`,`data_passagem`,`valor`,`compania`) VALUES ('{origem}','{destino}','{hoje}','{dia}/{mes}/{ano}','{preco}','{compania}')"
        executa_DML(sql)







    
def retorna_dois_digitos_str(valor:str) -> None:
    valor = str(valor)

    tamanho = len(valor)

    if tamanho == 1:
        valor = f"0{valor}"

    return(valor)

def lista_datas(data_inicial, dias_para_ficar_tirando_os_dias_de_viagem, dias_para_pesquisa):
    
    data_inicial = data_inicial
    dif = timedelta(days=(dias_para_pesquisa))
    dif_int = int(dif.days)
    
    lista_datas_ida = []    
    lista_dias_ida = []
    lista_meses_ida = []
    lista_anos_ida = []

    lista_datas_volta = []
    lista_dias_volta = []
    lista_meses_volta = []
    lista_anos_volta = []

    for num in range(0,dif_int):
        # ida
        delta_dias_ida = timedelta(days=num)
        data_leitura_ida = data_inicial + delta_dias_ida
        dia_ida = data_leitura_ida.day
        mes_ida = data_leitura_ida.month
        ano_leitura_ida = data_leitura_ida.year
        
        dia_leitura_ida = retorna_dois_digitos_str(dia_ida)
        mes_leitura_ida = retorna_dois_digitos_str(mes_ida)

        lista_dias_ida.append(dia_leitura_ida)
        lista_meses_ida.append(mes_leitura_ida)
        lista_anos_ida.append(ano_leitura_ida)
        lista_datas_ida.append(f'{dia_leitura_ida}/{mes_leitura_ida}/{ano_leitura_ida}')

        # volta
        delta_dias_volta = timedelta(days=( num + dias_para_ficar_tirando_os_dias_de_viagem + 1 ))
        data_leitura_volta = data_inicial + delta_dias_volta
        dia_volta = data_leitura_volta.day
        mes_volta = data_leitura_volta.month
        ano_leitura_volta = data_leitura_volta.year
        
        dia_leitura_volta = retorna_dois_digitos_str(dia_volta)
        mes_leitura_volta = retorna_dois_digitos_str(mes_volta)

        lista_dias_volta.append(dia_leitura_volta)
        lista_meses_volta.append(mes_leitura_volta)
        lista_anos_volta.append(ano_leitura_volta)
        lista_datas_volta.append(f'{dia_leitura_volta}/{mes_leitura_volta}/{ano_leitura_volta}')

    return(lista_datas_ida, lista_dias_ida, lista_meses_ida, lista_anos_ida, lista_datas_volta, lista_dias_volta, lista_meses_volta, lista_anos_volta)   
     
def start_geral(data_inicial, dias_para_ficar_tirando_os_dias_de_viagem, dias_para_pesquisar, origem, destino,tempo_espera_segundos_site, avisar_valor, numero_whattsapp, verificacoes):

    lista_datas_str = lista_datas(data_inicial, dias_para_ficar_tirando_os_dias_de_viagem, dias_para_pesquisar)
    tamanho = len(lista_datas_str[0])

    for item in range(0,tamanho):
        data_leitura_ida = lista_datas_str[0][item]
        print(data_leitura_ida)
        dia_leitura_ida = lista_datas_str[1][item]
        mes_leitura_ida = lista_datas_str[2][item]
        ano_leitura_ida = lista_datas_str[3][item]

        compania = "LATAM"
        Pegar_Preco_PassagemAerea(compania,dia_leitura_ida, mes_leitura_ida, ano_leitura_ida, origem, destino, tempo_espera_segundos_site,avisar_valor,numero_whattsapp)

        compania = "GOL"
        Pegar_Preco_PassagemAerea(compania,dia_leitura_ida, mes_leitura_ida, ano_leitura_ida, origem, destino, tempo_espera_segundos_site, avisar_valor,numero_whattsapp)

        data_leitura_volta = lista_datas_str[4][item]
        print(data_leitura_volta)
        dia_leitura_volta = lista_datas_str[5][item]
        mes_leitura_volta = lista_datas_str[6][item]
        ano_leitura_volta = lista_datas_str[7][item]

        compania = "LATAM"
        Pegar_Preco_PassagemAerea(compania,dia_leitura_volta, mes_leitura_volta, ano_leitura_volta, destino, origem, tempo_espera_segundos_site, avisar_valor,numero_whattsapp)

        compania = "GOL"
        Pegar_Preco_PassagemAerea(compania,dia_leitura_volta, mes_leitura_volta, ano_leitura_volta, destino, origem, tempo_espera_segundos_site, avisar_valor,numero_whattsapp)


data_inicial = datetime(day=16, month=5, year=2025)
dias_para_ficar_tirando_os_dias_de_viagem = 7
dias_para_pesquisar = 92
origem = "SAO"
destino = "PMW"
tempo_espera_segundos_site = 10
avisar_valor = 100
numero_whattsapp = "+5511967169420"
verificacoes = 0
start_geral(data_inicial,dias_para_ficar_tirando_os_dias_de_viagem,dias_para_pesquisar, origem, destino, tempo_espera_segundos_site, avisar_valor,numero_whattsapp, verificacoes)

