import pandas as pd

lista_col1 = [1,4,7,10,13,16,19,22,25]
lista_col2 = [2,5,8,11,14,17,20,23,26]
lista_col3 = [3,6,9,12,15,18,21,24,27]

df = pd.DataFrame(data=[lista_col1,lista_col2,lista_col3]).transpose()
df.index = ['lin_1','lin_2','lin_3','lin_4','lin_5','lin_6','lin_7','lin_8','lin_9',]
df.columns=['col_1','col_2','col_3']
print(df)
print(df.index)

lista_degola = []

for linha in df.itertuples(index=True):
    if linha.col_1 <= 7:
        lista_degola.append(linha.Index)

print(lista_degola)

df.drop(axis=0, inplace=True, labels=lista_degola)
print(df)

