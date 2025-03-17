import matplotlib.pyplot as plt
from dist.conexao import executa_DQL, executa_DML
from tkinter import messagebox

fig = plt.figure()
ax = fig.add_subplot()

ax.plot([1,2,3,4,5],[1,4,9,16,25])

sql = 'CREATE TABLE "passagens_new" ("id" INTEGER, "origem" TEXT,"destino" TEXT,"data_pesquisa" TEXT,"data_passagem" TEXT,"valor" REAL, "compania" TEXT, PRIMARY KEY("id" AUTOINCREMENT))'
executa_DML(sql)

sql = "SELECT * FROM passagens_new"
result=executa_DQL(sql)

messagebox.showinfo("Aviso",result)

plt.show()