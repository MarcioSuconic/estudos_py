import pandas as pd
import pandas_datareader.data as pdr
import yfinance

yfinance.pdr_override()

ativos = ['ITUB3.SA','VALE3.SA','PETR3.SA','^BVSP']

data_inicial = '2025-02-10'
data_final = '2025-02-24'

tabela_cotacoes = pdr.get_data_yahoo('^BVSP', data_inicial, data_final)
print(tabela_cotacoes)
