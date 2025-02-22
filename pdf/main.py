from tkinter import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os
from tkinter import ttk, messagebox

pastaApp = os.path.dirname(__file__)

def mm_p_pts(milimetros):
    pontos = milimetros/0.352777
    return(pontos)

def criar_pdf():
    cnv = canvas.Canvas(pastaApp + "\\marcio.pdf", pagesize=A4)

    for n in range(0,200,6):
        cnv.drawString(mm_p_pts(100),mm_p_pts(n),"Marcio")
    try:
        cnv.save()
        messagebox.showinfo("OK","O arquivo foi salvo .")
    except:
        messagebox.showinfo("ERRO","O arquivo está aberto.")

app = Tk()
app.title("PDF")
app.geometry("600x450")

frame1 = Frame(app)
frame1.pack()

btn_criarPDF = Button(frame1, text="criar PDF", command=criar_pdf)
btn_criarPDF.pack()

app.mainloop()
