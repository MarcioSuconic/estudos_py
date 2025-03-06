import pandas as pd

lista_produtos = ['a','b','c','d']
lista_cmv = [10,10,10,10]
lista_vendas = [10,15,20,25]

df_vds = pd.DataFrame(data=[lista_produtos,lista_cmv,lista_vendas]).transpose()
df_vds.columns = ['produto','cmv','venda']

df_vds['markup'] = 1+ (df_vds['venda'] - df_vds['cmv'])/df_vds['cmv']

caminho=r"c:\dados_marsoft\teste.xlsx"
df_vds.to_excel(caminho)
print(df_vds)
