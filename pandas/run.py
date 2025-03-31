import pandas as pd

caminho_arquivo = r"c:\\lixo\\notas.xlsx"
pasta = "sala_1"
df_professor = pd.read_excel(caminho_arquivo, sheet_name = pasta)
