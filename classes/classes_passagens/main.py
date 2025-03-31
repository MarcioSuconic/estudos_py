from selenium import webdriver
import time
from datetime import datetime, timedelta
from conexao import executa_DML
import pywhatkit

class Passagens:
    
    def __init__(self,dia:int ,mes:int ,ano: int, n_dias_pesquisa: int ,valor_abaixo_a_informar: float, dias_livres_na_viagem:int, lista_operadoras: list, tempo_espera_segundos: int, origem: str, destino: str, ida_e_volta: bool, lista_numeros_whattsapp: list, apagar_todo_o_banco_de_dados: bool = False) -> None:
        print('construino a classe')
        
        self.dia_inicial = dia
        self.mes_inicial = mes
        self.ano_inicial = ano
        self.dias_a_pesquisar = n_dias_pesquisa
        self.valor_abaixo_a_informar = valor_abaixo_a_informar
        self.lista_operadoras = lista_operadoras
        self.dias_para_ficar_tirando_os_dias_de_viagem = dias_livres_na_viagem
        self.tempo_espera_segundos = tempo_espera_segundos
        self.ida_e_volta = ida_e_volta
        self.lista_numeros_whattsapp = lista_numeros_whattsapp

        self.origem_ida = origem
        self.destino_ida = destino
        self.destino_volta = self.origem_ida
        self.origem_volta = self.destino_ida        

        self.apagar_todo_o_banco_de_dados = apagar_todo_o_banco_de_dados

        if self.apagar_todo_o_banco_de_dados == True:
            
            sql = "DELETE FROM `passagens` WHERE `id` >= '1'"
            executa_DML(sql)

            sql = "UPDATE FROM `sqlite_sequence` (`seq`) VALUES ('0');"
            executa_DML(sql)

        self.data_inicial = datetime(day=self.dia_inicial, month=self.mes_inicial, year=self.ano_inicial)              

        self.define_lista_datas_a_procurar()

        msg_3 = ''

        for comp in self.lista_operadoras:
            msg_3 += f'{comp} '

        if self.ida_e_volta == True:
            msg_1 = 'ida e volta'
            data_inicial_ida = self.lista_datas_ida[0]
            data_final_ida = self.lista_datas_ida[-1]
            data_inicial_volta = self.lista_datas_volta[0]
            data_final_volta = self.lista_datas_volta[-1]            
            msg_2 = f'{msg_3} entre as datas de ida de {data_inicial_ida} e {data_final_ida} e volta entre as datas {data_inicial_volta} e {data_final_volta}'
        else:
            msg_1 = 'ida'
            data_inicial_ida = self.lista_datas_ida[0]
            data_final_ida = self.lista_datas_ida[-1]
            msg_2 = f'{msg_3} entre as datas de {data_inicial_ida} e {data_final_ida}'

        self.mensagem_para_zap = f'Só serão avisadas as passagens de {msg_1} entre {self.origem_ida} e {self.destino_ida} com valores abaixo de {self.valor_abaixo_a_informar} {msg_2}:\n\n'

        self.prepara_busca_passagem()

    def prepara_busca_passagem(self):

        for operadora in self.lista_operadoras:

            self.compania = operadora
            self.tipo_chave = self.retorna_tipo_chave(operadora)
            self.chave = self.retorna_chave(operadora)

            # ida
            indice_ida = 0
            for item in self.lista_datas_ida:                
                self.msg_inicial = f'ida de {operadora} em {item} de {self.origem_ida} para {self.destino_ida}: '
                
                self.dia_viagem = self.lista_dias_ida[indice_ida]
                self.mes_viagem = self.lista_meses_ida[indice_ida]
                self.ano_viagem = self.lista_anos_ida[indice_ida]

                self.url = self.retorna_url(self.compania, self.dia_viagem, self.mes_viagem, self.ano_viagem, self.origem_ida, self.destino_ida)
                
                self.origem = self.origem_ida
                self.destino = self.destino_ida

                self.procura_valor_passagem()
                indice_ida += 1

            # volta            
            if self.ida_e_volta == True:

                indice_volta = 0
                for item in self.lista_datas_volta:                   
                    self.msg_inicial = f'volta de {operadora} em {item} de {self.origem_volta} para {self.destino_volta}: '
                    
                    self.dia_viagem = self.lista_dias_volta[indice_volta]
                    self.mes_viagem = self.lista_meses_volta[indice_volta]
                    self.ano_viagem = self.lista_anos_volta[indice_volta]

                    self.url = self.retorna_url(self.compania, self.dia_viagem, self.mes_viagem, self.ano_viagem, self.origem_volta, self.destino_volta)

                    self.origem = self.origem_volta
                    self.destino = self.destino_volta

                    self.procura_valor_passagem()
                    indice_volta += 1

        print('mensagem para o Zap:')
        print(self.mensagem_para_zap)
        
        for numero in self.lista_numeros_whattsapp:            
            
            self.agora = datetime.now()

            self.hora = self.agora.hour
            self.minutos = self.agora.minute

            if self.minutos >= 57:
                self.minutos = 1

                if self.hora == 23:
                    self.hora = 00
                else:
                    self.hora = self.hora + 1

            else:
                self.minutos += 2

            print('enviando a mensagem.....')
            pywhatkit.sendwhatmsg(numero, self.mensagem_para_zap, self.hora, self.minutos, 90)

    def retorna_preco(self, compania, valor_str) -> float:
        if self.compania == "LATAM":
            valor_float = self.entra_valor_str_sai_float_brl(valor_str)
        if self.compania == "GOL":
            valor_float = self.entra_valor_str_sai_float_reais(valor_str)
        return(valor_float)

    def retorna_dois_digitos_str(self,valor:str) -> None:
        valor = str(valor)
        tamanho = len(valor)
        if tamanho == 1:
            valor = f"0{valor}"
        return(valor)

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
        origem = self.origem_achada
        destino = self.destino_achado

        sql = f"INSERT INTO `passagens` (`origem`,`destino`,`data_pesquisa`,`data_passagem`,`valor`,`compania`) VALUES ('{origem}','{destino}','{hoje}','{dia}/{mes}/{ano}','{preco}','{compania}')"
        executa_DML(sql)

    def define_lista_datas_a_procurar(self):        

        print('fazendo a lista de datas ......')
        
        dif = timedelta(days=(self.dias_a_pesquisar))
        dif_int = int(dif.days)
        
        self.lista_datas_ida = []    
        self.lista_dias_ida = []
        self.lista_meses_ida = []
        self.lista_anos_ida = []

        self.lista_datas_volta = []
        self.lista_dias_volta = []
        self.lista_meses_volta = []
        self.lista_anos_volta = []

        for num in range(0,dif_int):
            # ida
            delta_dias_ida = timedelta(days=num)
            data_leitura_ida = self.data_inicial + delta_dias_ida
            dia_ida = data_leitura_ida.day
            mes_ida = data_leitura_ida.month
            ano_leitura_ida = data_leitura_ida.year
            
            dia_leitura_ida = self.retorna_dois_digitos_str(dia_ida)
            mes_leitura_ida = self.retorna_dois_digitos_str(mes_ida)

            self.lista_dias_ida.append(dia_leitura_ida)
            self.lista_meses_ida.append(mes_leitura_ida)
            self.lista_anos_ida.append(ano_leitura_ida)
            self.lista_datas_ida.append(f'{dia_leitura_ida}/{mes_leitura_ida}/{ano_leitura_ida}')

            if self.ida_e_volta == True:
                # volta
                delta_dias_volta = timedelta(days=( num + self.dias_para_ficar_tirando_os_dias_de_viagem + 1 ))
                data_leitura_volta = self.data_inicial + delta_dias_volta
                dia_volta = data_leitura_volta.day
                mes_volta = data_leitura_volta.month
                ano_leitura_volta = data_leitura_volta.year
                
                dia_leitura_volta = self.retorna_dois_digitos_str(dia_volta)
                mes_leitura_volta = self.retorna_dois_digitos_str(mes_volta)

                self.lista_dias_volta.append(dia_leitura_volta)
                self.lista_meses_volta.append(mes_leitura_volta)
                self.lista_anos_volta.append(ano_leitura_volta)
                self.lista_datas_volta.append(f'{dia_leitura_volta}/{mes_leitura_volta}/{ano_leitura_volta}')

        return(self.lista_datas_ida, self.lista_dias_ida, self.lista_meses_ida, self.lista_anos_ida, self.lista_datas_volta, self.lista_dias_volta, self.lista_meses_volta, self.lista_anos_volta)   

    def procura_valor_passagem(self):

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
                self.origem_achada = navegador.find_element(self.tipo_chave, "lbl_origin_1_emission").text
                self.destino_achado = navegador.find_element(self.tipo_chave, "lbl_destination_1_emission").text
            except:
                self.origem_achada = self.origem
                self.destino_achado = self.destino

        if self.compania == "LATAM":

            try:
                sup_origem_1 = navegador.find_element(self.tipo_chave, "lcVysi").text
                sup_origem_2 = navegador.find_element(self.tipo_chave, "kgsfDI").text            
                sup_destino_1 = navegador.find_element(self.tipo_chave, "jrxwkA").text
                sup_destino_2 = navegador.find_element(self.tipo_chave, "kgsfDI").text
                self.origem_achada = f'{sup_origem_2} - {sup_origem_1}'
                self.destino_achado = '' #f'{sup_destino_2} - {sup_destino_1}'
            except:
                self.origem_achada = self.origem
                self.destino_achado = self.destino        

        self.preco_float = self.retorna_preco(self.compania,preco_str)
        msg = f"{self.msg_inicial}\n {self.compania}, {self.origem_achada}-{self.destino_achado}, {self.dia_viagem}/{self.mes_viagem}/{self.ano_viagem}, R$ {self.preco_float}\n\n"
        print(msg)

        if self.preco_float <= self.valor_abaixo_a_informar:
            self.mensagem_para_zap += msg 
        
        self.inserir_no_banco_de_dados()        
        navegador.close()

    #def cria_mensagem_para_whattsapp(self):

apagar_todo_o_banco_de_dados = True
tempo_espera_segundos = 18
dia_inicial = 16
mes_inicial = 5
ano_inicial= 2025
dias_para_pesquisar = 14
valor_abaixo_de_para_avisar = 2000
dias_livres_na_viagem = 7
lista_operadoras = ["LATAM","GOL"] #["LATAM","GOL"]
origem = "SAO"
destino = "PMW"
ida_e_volta = True
lista_numeros_whattsapp = ["+5511962996562","+5511967169420"] # ["+5511962996562","+5511967169420"] "+5511982841612"

viagem = Passagens(dia_inicial, mes_inicial, ano_inicial, dias_para_pesquisar, valor_abaixo_de_para_avisar, dias_livres_na_viagem, lista_operadoras, tempo_espera_segundos, origem, destino, ida_e_volta, lista_numeros_whattsapp, apagar_todo_o_banco_de_dados)
