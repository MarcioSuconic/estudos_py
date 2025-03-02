from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from utilitarios import executa_DML, executa_DQL
import tkinter as tk
from datetime import datetime
import os
#from criar_dados import criar_dados
#from verificacao_geral import verificar

verificar()

class Cervejaria():

    def __init__(self):
        self.janela = Tk()
        self.janela.title('Cervejaria MVB')
        self.janela.geometry('1043x640+10+10')

        self.cor_fundo_frame_2 = "#ea526f"
        self.cor_fundo_frame_1 = "#6e44ff"
        self.cor_fundo_frame_3 = "#d2f1e4"

        self.cor_texto_frame_1 = "#252323"

        self.cor_fundo_botao_principal = "#f6f7eb"
        self.cor_texto_botao_principal = "#6e44ff"

        self.cor_fundo_label = "#d2f1e4"
        self.cor_texto_label = "black"

        self.cor_fundo_entry = "#9ec1a3"
        self.cor_texto_entry = "black"

        self.altura_campos = 0.03
        self.espaco_interno = 0.005
        self.espaco_externo = 0.02

        self.espaco_para_botoes = 0.2

        self.altura_listbox = 0.12
        self.fonte_listbox = ("Morgana",9)
        
        #frames
        self.frame_1 = Frame(self.janela, bg=self.cor_fundo_frame_1)
        self.frame_1.place(relx=0, rely=0.00, relheight=0.06, relwidth=1)

        self.frame_2 = Frame(self.janela, bg=self.cor_fundo_frame_2)
        self.frame_2.place(relx=0, rely=0.06, relheight=0.94, relwidth=0.55)

        self.frame_3 = Frame(self.janela, bg=self.cor_fundo_frame_3)
        self.frame_3.place(relx=0.55, rely=0.06, relheight=0.94, relwidth=0.45)

        #widgtes frame_1
        self.label_frame_1 = Label(self.frame_1, text="HOME", bg=self.cor_fundo_frame_1, fg=self.cor_texto_frame_1, justify="center", font=("Morgana",16))
        self.label_frame_1.place(relx=0.5, rely=0.5, anchor="center")

        # menu
        barraMenu = Menu(self.janela)

        menuCaminhos_outros = Menu(barraMenu)        
        menuCaminhos_outros.add_command(label="Grandezas Físicas", command=self.grandezas_fisicas)
        menuCaminhos_outros.add_command(label="Relacionamentos Unidades", command=self.relacionamento_unidades)        
        menuCaminhos_outros.add_cascade(label="Harmonização", command=self.harmonizacao)
        menuCaminhos_outros.add_cascade(label="Pareceres", command=self.pareceres)

        menuCaminhos_basicos = Menu(barraMenu)
        menuCaminhos_basicos.add_command(label="Unidades", command=self.unidades)
        menuCaminhos_basicos.add_command(label="Insumos", command=self.insumos)
        menuCaminhos_basicos.add_command(label="Tipos Sub Produtos", command=self.tipos_sub_produtos)
        menuCaminhos_basicos.add_command(label="Sub Produtos", command=self.sub_produtos)
        menuCaminhos_basicos.add_command(label="Tipos Produtos", command=self.tipos_produtos)
        menuCaminhos_basicos.add_command(label="Produtos", command=self.produtos)
        
        menuCaminhos_relacionamentos = Menu(barraMenu)
        menuCaminhos_relacionamentos.add_command(label="Sub Produtos x Insumos", command=self.sub_produtos_x_insumos)        
        menuCaminhos_relacionamentos.add_command(label="Produtos x Sub Produtos", command=self.produtos_x_sub_produtos)
        menuCaminhos_relacionamentos.add_command(label="Tempo de m.o. de Produtos", command=self.produtos_mao_obra)
        menuCaminhos_relacionamentos.add_command(label="Processo de Feitura de Produtos - Energia", command=self.processo_feitura_produto_energia)
        menuCaminhos_relacionamentos.add_command(label="Processo de Feitura de Produtos - Insumos", command=self.processo_feitura_produto_insumos)
        menuCaminhos_relacionamentos.add_command(label="Finalizações de Produtos", command=self.finalizacao_produtos)        

        barraMenu.add_cascade(label="Básicos", menu=menuCaminhos_basicos)
        barraMenu.add_cascade(label="Relações", menu=menuCaminhos_relacionamentos)
        barraMenu.add_cascade(label="Outros", menu=menuCaminhos_outros)      
        self.janela.config(menu=barraMenu)
        self.pastaApp = os.path.dirname(__file__)
        self.tela_inicial()
    
    def tela_inicial(self):
        self.label_frame_1.configure(text="HOME")        
        # widgets frame_2
        botoes = [
            'Unidades',
            'Insumos',
            'Tipos de\nSub Produtos',
            'Sub Produtos',
            'Sub Produtos\nx Insumos',
            'Tipos de Produtos',
            'Produtos',
            'Produtos x\nSub_Produtos',
            'Processo de Feitura\ndos Produtos - Energia',
            'Processo de Feitura\ndos Produtos - Insumos',
            'Finalização\ndos Produtos',
            'Tempo de Mão-de-Obra\nde produto',
            'Harmonização',
            'Pareceres',
            'Centro de Custos\nde Produtos',
        ]

        qtde_botoes_por_linha = 3

        qtde_botoes = len(botoes)

        qtde_linhas_completas = int(qtde_botoes/qtde_botoes_por_linha)
        qtde_botoes_linha_ultima = int(qtde_botoes%qtde_botoes_por_linha)

        margem_vertical_interna = 0.1
        margem_horizontal = 0.04

        altura_botao = 0.10
        largura_botao = round((1-margem_horizontal*(qtde_botoes_por_linha+1))/qtde_botoes_por_linha,2)

        if qtde_botoes_linha_ultima >= 1:
            qtde_linhas = qtde_linhas_completas + 1
        else:
            qtde_linhas = qtde_linhas_completas

        margem_superior = (1-(qtde_linhas*altura_botao+(margem_vertical_interna*(qtde_linhas-1))))/2

        def entrou_btn_1(Event):
            btn_1.configure(bg="blue", fg="white")
        def saiu_btn_1(Event):
            btn_1.configure(bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal)
        btn_1 = Button(self.frame_2, bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal, text=botoes[0], command = self.unidades)
        btn_1.place(relx=margem_horizontal/2, rely=margem_superior, relheight=altura_botao, relwidth=largura_botao)
        btn_1.bind('<Enter>',entrou_btn_1)
        btn_1.bind('<Leave>',saiu_btn_1)

        def entrou_btn_2(Event):
            btn_2.configure(bg="blue", fg="white")
        def saiu_btn_2(Event):
            btn_2.configure(bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal)
        btn_2 = Button(self.frame_2, bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal, text=botoes[1], command = self.insumos)
        btn_2.place(relx=1.5*margem_horizontal + largura_botao, rely=margem_superior, relheight=altura_botao, relwidth=largura_botao)
        btn_2.bind('<Enter>',entrou_btn_2)
        btn_2.bind('<Leave>',saiu_btn_2)

        def entrou_btn_3(Event):
            btn_3.configure(bg="blue", fg="white")
        def saiu_btn_3(Event):
            btn_3.configure(bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal)
        btn_3 = Button(self.frame_2, bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal, text=botoes[2], command = self.tipos_sub_produtos)
        btn_3.place(relx=2.5*margem_horizontal + 2*largura_botao, rely=margem_superior, relheight=altura_botao, relwidth=largura_botao)        
        btn_3.bind('<Enter>',entrou_btn_3)
        btn_3.bind('<Leave>',saiu_btn_3)

        def entrou_btn_4(Event):
            btn_4.configure(bg="blue", fg="white")
        def saiu_btn_4(Event):
            btn_4.configure(bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal)
        btn_4 = Button(self.frame_2, bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal, text=botoes[3], command = self.sub_produtos)
        btn_4.place(relx=margem_horizontal/2, rely=margem_superior + altura_botao + margem_vertical_interna, relheight=altura_botao, relwidth=largura_botao)
        btn_4.bind('<Enter>',entrou_btn_4)
        btn_4.bind('<Leave>',saiu_btn_4)

        def entrou_btn_5(Event):
            btn_5.configure(bg="blue", fg="white")
        def saiu_btn_5(Event):
            btn_5.configure(bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal)
        btn_5 = Button(self.frame_2, bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal, text=botoes[4], command = self.sub_produtos_x_insumos)
        btn_5.place(relx=1.5*margem_horizontal + largura_botao, rely=margem_superior + altura_botao + margem_vertical_interna, relheight=altura_botao, relwidth=largura_botao)
        btn_5.bind('<Enter>',entrou_btn_5)
        btn_5.bind('<Leave>',saiu_btn_5)

        def entrou_btn_6(Event):
            btn_6.configure(bg="blue", fg="white")
        def saiu_btn_6(Event):
            btn_6.configure(bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal)
        btn_6 = Button(self.frame_2, bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal, text=botoes[5], command = self.tipos_produtos)
        btn_6.place(relx=2.5*margem_horizontal + 2*largura_botao, rely=margem_superior + altura_botao + margem_vertical_interna, relheight=altura_botao, relwidth=largura_botao)
        btn_6.bind('<Enter>',entrou_btn_6)
        btn_6.bind('<Leave>',saiu_btn_6)

        def entrou_btn_7(Event):
            btn_7.configure(bg="blue", fg="white")
        def saiu_btn_7(Event):
            btn_7.configure(bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal)
        btn_7 = Button(self.frame_2, bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal, text=botoes[6], command = self.produtos)
        btn_7.place(relx=margem_horizontal/2, rely=margem_superior + 2*altura_botao + 2*margem_vertical_interna, relheight=altura_botao, relwidth=largura_botao)
        btn_7.bind('<Enter>',entrou_btn_7)
        btn_7.bind('<Leave>',saiu_btn_7)

        def entrou_btn_8(Event):
            btn_8.configure(bg="blue", fg="white")
        def saiu_btn_8(Event):
            btn_8.configure(bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal)
        btn_8 = Button(self.frame_2, bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal, text=botoes[7], command = self.produtos_x_sub_produtos)
        btn_8.place(relx=1.5*margem_horizontal + largura_botao, rely=margem_superior + 2*altura_botao + 2*margem_vertical_interna, relheight=altura_botao, relwidth=largura_botao)
        btn_8.bind('<Enter>',entrou_btn_8)
        btn_8.bind('<Leave>',saiu_btn_8)

        def entrou_btn_9(Event):
            btn_9.configure(bg="blue", fg="white")
        def saiu_btn_9(Event):
            btn_9.configure(bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal)
        btn_9 = Button(self.frame_2, bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal, text=botoes[8], command = self.processo_feitura_produto_energia)
        btn_9.place(relx=2.5*margem_horizontal + 2*largura_botao, rely=margem_superior + 2*altura_botao + 2*margem_vertical_interna, relheight=altura_botao, relwidth=largura_botao)
        btn_9.bind('<Enter>',entrou_btn_9)
        btn_9.bind('<Leave>',saiu_btn_9)

        def entrou_btn_10(Event):
            btn_10.configure(bg="blue", fg="white")
        def saiu_btn_10(Event):
            btn_10.configure(bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal)
        btn_10 = Button(self.frame_2, bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal, text=botoes[9], command = self.processo_feitura_produto_insumos)
        btn_10.place(relx=margem_horizontal/2, rely=margem_superior + 3*altura_botao + 3*margem_vertical_interna, relheight=altura_botao, relwidth=largura_botao)
        btn_10.bind('<Enter>',entrou_btn_10)
        btn_10.bind('<Leave>',saiu_btn_10)

        def entrou_btn_11(Event):
            btn_11.configure(bg="blue", fg="white")
        def saiu_btn_11(Event):
            btn_11.configure(bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal)
        btn_11 = Button(self.frame_2, bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal, text=botoes[10], command= self.finalizacao_produtos)
        btn_11.place(relx=1.5*margem_horizontal + largura_botao, rely=margem_superior + 3*altura_botao + 3*margem_vertical_interna, relheight=altura_botao, relwidth=largura_botao)
        btn_11.bind('<Enter>',entrou_btn_11)
        btn_11.bind('<Leave>',saiu_btn_11)

        def entrou_btn_12(Event):
            btn_12.configure(bg="blue", fg="white")
        def saiu_btn_12(Event):
            btn_12.configure(bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal)
        btn_12 = Button(self.frame_2, bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal, text=botoes[11], command = self.produtos_mao_obra)
        btn_12.place(relx=2.5*margem_horizontal + 2*largura_botao, rely=margem_superior + 3*altura_botao + 3*margem_vertical_interna, relheight=altura_botao, relwidth=largura_botao)
        btn_12.bind('<Enter>',entrou_btn_12)
        btn_12.bind('<Leave>',saiu_btn_12)

        def entrou_btn_13(Event):
            btn_13.configure(bg="blue", fg="white")
        def saiu_btn_13(Event):
            btn_13.configure(bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal)
        btn_13 = Button(self.frame_2, bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal, text=botoes[12], command = self.harmonizacao)
        btn_13.place(relx=margem_horizontal/2, rely=margem_superior + 4*altura_botao + 4*margem_vertical_interna, relheight=altura_botao, relwidth=largura_botao)
        btn_13.bind('<Enter>',entrou_btn_13)
        btn_13.bind('<Leave>',saiu_btn_13)

        def entrou_btn_14(Event):
            btn_14.configure(bg="blue", fg="white")
        def saiu_btn_14(Event):
            btn_14.configure(bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal)
        btn_14 = Button(self.frame_2, bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal, text=botoes[13], command = self.pareceres)
        btn_14.place(relx=1.5*margem_horizontal + largura_botao, rely=margem_superior + 4*altura_botao + 4*margem_vertical_interna, relheight=altura_botao, relwidth=largura_botao)
        btn_14.bind('<Enter>',entrou_btn_14)
        btn_14.bind('<Leave>',saiu_btn_14)

        def entrou_btn_15(Event):
            btn_15.configure(bg="blue", fg="white")
        def saiu_btn_15(Event):
            btn_15.configure(bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal)
        btn_15 = Button(self.frame_2, bg=self.cor_fundo_botao_principal, fg=self.cor_texto_botao_principal, text=botoes[14], command = self.ccp)
        btn_15.place(relx=2.5*margem_horizontal + 2*largura_botao, rely=margem_superior + 4*altura_botao + 4*margem_vertical_interna, relheight=altura_botao, relwidth=largura_botao)
        btn_15.bind('<Enter>',entrou_btn_15)
        btn_15.bind('<Leave>',saiu_btn_15)

        img_Tocantins = PhotoImage(file=self.pastaApp+"\\tocantins.png")
        label_Tocantins = Label(self.frame_3, image=img_Tocantins)
        label_Tocantins.place(relx=0.25, rely=0.15, relwidth=.50, relheight=0.30)

        img_Palmas = PhotoImage(file=self.pastaApp+"\\palmas.png")
        label_Palmas = Label(self.frame_3, image=img_Palmas)
        label_Palmas.place(relx=0.25, rely=0.50, relwidth=.50, relheight=0.30)

        self.janela.mainloop()
