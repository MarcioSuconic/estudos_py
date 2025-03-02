from selenium import webdriver
import time
from datetime import datetime, timedelta

def verificar_precos_passagens(data_inicial, n_dias_verificacao, origem_ida, destino_ida, origem_volta, destino_volta, dias_ficar_viagem,segundos_espera):
    # abrir o navegador
    navegador = webdriver.Chrome()

    classe_ida = "koxMWe"
    classe_volta = "koxMWe"

    lista_datas_ida = []
    lista_valores_ida = []
    #lista_horario_saida_ida = []
    #lista_horario_chegada_ida = []

    lista_datas_volta = []
    lista_valores_volta = []
    #lista_horario_saida_volta = []
    #lista_horario_chegada_volta = []

    preco_menor_ida = 5000
    preco_menor_volta = 5000

    soma_ida_e_volta_menor = 10000

    tempo_espera_segundos = segundos_espera

    for dias in range(1,n_dias_verificacao):
        tempo_delta_ida = timedelta(days=dias)

        data_leitura_ida = (data_inicial + tempo_delta_ida).date()

        dia_leitura = str(data_leitura_ida.day)
        mes_leitura = str(data_leitura_ida.month)
        ano_leitura = str(data_leitura_ida.year)

        if len(dia_leitura) == 1:
            dia_leitura = f'0{dia_leitura}'

        if len(mes_leitura) == 1:
            mes_leitura = f'0{mes_leitura}'

        # URL do produto
        url_ida = f"https://www.latamairlines.com/br/pt/oferta-voos?origin={origem_ida}&outbound={ano_leitura}-{mes_leitura}-{dia_leitura}T12%3A00%3A00.000Z&destination={destino_ida}&inbound=null&adt=1&chd=0&inf=0&trip=OW&cabin=Economy&redemption=false&sort=PRICE%2Casc"

        # acessar um site
        navegador.get(url_ida)

        time.sleep(tempo_espera_segundos)

        # pegar preço
        preco_ida = navegador.find_element("class name",classe_ida).text


    #<span font-weight="normal" color="#10004F" class="sc-aXZVg dxSNap latam-typography latam-typography--heading-04 sc-gEvEer flightInfostyles__TextHourFlight-sc__sc-edlvrg-4 fteAEG lcVysi">7:25</span>
        #horario_saida_ida = navegador.find_element("class name","lcVysi").text
    #<span font-weight="normal" color="#10004F" class="sc-aXZVg dxSNap latam-typography latam-typography--heading-04 sc-gEvEer flightInfostyles__TextHourFlight-sc__sc-edlvrg-4 fteAEG lcVysi">9:45<span font-weight="normal" color="#10004F" class="sc-aXZVg dxSNap latam-typography latam-typography--paragraph-medium sc-gEvEer flightInfostyles__TextDaysDifference-sc__sc-edlvrg-6 fteAEG jrxwkA"></span></span>
        #horario_chegada_ida = navegador.find_element("class name","flightInfostyles__TextHourFlight-sc__sc-edlvrg-4").text

        #print(horario_saida_ida)
        #print(horario_chegada_ida)

        #ida_saindo_de = navegador.find_element("class name","kgsfDI").text

        preco_ida = preco_ida[4:]

        preco_ida = preco_ida.replace(",",".")
        preco_ida = float(preco_ida)

        if preco_ida < preco_menor_ida:
            preco_menor_ida = preco_ida
            data_preco_menor_ida = data_leitura_ida

        print('----------------')
        print(data_leitura_ida)
        print(preco_ida)
        #print(horario_saida_ida)
        #print(horario_chegada_ida)
        # print(f'{ida_saindo_de=}')
        print(f'o preço menor até agora para a ida é: {preco_menor_ida} de {data_preco_menor_ida}')




        tempo_delta_volta = timedelta(days=dias_ficar_viagem)

        data_leitura_volta = (data_inicial + tempo_delta_ida + tempo_delta_volta).date()  

        dia_leitura = str(data_leitura_volta.day)
        mes_leitura = str(data_leitura_volta.month)
        ano_leitura = str(data_leitura_volta.year)

        if len(dia_leitura) == 1:
            dia_leitura = f'0{dia_leitura}'

        if len(mes_leitura) == 1:
            mes_leitura = f'0{mes_leitura}'

        # URL do produto
        url_volta = f"https://www.latamairlines.com/br/pt/oferta-voos?origin={origem_volta}&outbound={ano_leitura}-{mes_leitura}-{dia_leitura}T12%3A00%3A00.000Z&destination={destino_volta}&inbound=null&adt=1&chd=0&inf=0&trip=OW&cabin=Economy&redemption=false&sort=PRICE%2Casc"

        # acessar um site
        navegador.get(url_volta)

        time.sleep(tempo_espera_segundos)

        # pegar preço
        preco_volta = navegador.find_element("class name",classe_volta).text
        preco_volta = preco_volta[4:]

        preco_volta = preco_volta.replace(",",".")
        preco_volta = float(preco_volta)

        if preco_volta < preco_menor_volta:
            preco_menor_volta = preco_volta
            data_preco_menor_volta = data_leitura_volta
    
        print('----------------------------------------------------')
        print(data_leitura_volta)
        print(preco_volta)
        # print(horario_saida_volta)
        # print(horario_chegada_volta)
        print(f'o preço menor até agora para a volta é: {preco_menor_volta} de {data_preco_menor_volta}')
        print()

        soma_ida_e_volta = preco_ida + preco_volta

        if soma_ida_e_volta < soma_ida_e_volta_menor:
            soma_ida_e_volta_menor = soma_ida_e_volta
            data_menor_ida_e_volta = [data_leitura_ida,data_leitura_volta]
            print(f'data de ida: {data_leitura_ida} e data de volta {data_leitura_volta} total: {soma_ida_e_volta}')
    
        lista_datas_ida.append(data_leitura_ida)
        lista_valores_ida.append(preco_ida)

        lista_datas_volta.append(data_leitura_volta)
        lista_valores_volta.append(preco_volta)

        print(f'até agora o mais barato ida e volta é: {soma_ida_e_volta_menor} de {data_menor_ida_e_volta}')
        print('--------------------------------------------------')
        print()

    print(f'a passagem mais barata de ida é {preco_menor_ida} de {data_preco_menor_ida}')
    print(f'a passagem mais barata de volta é {preco_menor_volta} de {data_preco_menor_volta}')
    print(f'ida e volta mais barata é de R$ {soma_ida_e_volta_menor} de ida em {data_menor_ida_e_volta[0]} e volta em {data_menor_ida_e_volta[0]}')

    return(lista_datas_ida,lista_valores_ida,lista_datas_volta,lista_valores_volta)

data_inicial = datetime(day=30,month=4,year=2025)
n_dias_verificacao = 31
origem_ida = "SAO"
destino_ida = "PMW"
origem_volta = "PMW"
destino_volta = "SAO"
dias_ficar_viagem = 8
segundos_espera = 20 

resultado = verificar_precos_passagens(data_inicial,n_dias_verificacao,origem_ida,destino_ida,origem_volta,destino_volta,dias_ficar_viagem, segundos_espera)
print(resultado[0])
print(resultado[1])
print(resultado[2])
print(resultado[3])
