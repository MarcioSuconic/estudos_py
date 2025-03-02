from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from utilitarios import executa_DML, executa_DQL
import tkinter as tk
from datetime import datetime
import os
from criar_dados import criar_dados
from verificacao_geral import verificar

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

    def unidades(self):
        self.tabela="unidades"

        abc = self.listagem_grandezas()

        self.lista_ids_grandezas = abc[0]
        self.lista_grandezas = abc[1]

        if len(self.lista_ids_grandezas) == 0:
            messagebox.showinfo("Faltam dados","Grandezas Físicas necessitam de algu(ns) dado(s).")
            self.home()

        # frame_1
        self.label_frame_1.configure(text="Unidades")

        # frame 2
        self.apagar_widgets_frame_2()        

        qtde_labels_e_entrys = 5
        adicional_tamanhos_listbox = 3
        margem_superior = ((1-self.espaco_para_botoes)-((qtde_labels_e_entrys*2+adicional_tamanhos_listbox)*self.altura_campos)-(qtde_labels_e_entrys*self.espaco_interno)-((qtde_labels_e_entrys-1)*self.espaco_externo))/2

        self.label_id_uni = Label(self.frame_2, text="ID", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_id_uni.place(relx=0.05, rely=margem_superior, relwidth=0.90, relheight=self.altura_campos)

        self.entry_id_uni = Label(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, text="novo")
        self.entry_id_uni.place(relx=0.05, rely=margem_superior + self.altura_campos + self.espaco_interno, relwidth=0.90, relheight=self.altura_campos)
        
        self.label_uni = Label(self.frame_2, text="unidade", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_uni.place(relx=0.05, rely=margem_superior + 2*self.altura_campos + self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_uni = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_uni.place(relx=0.05, rely=margem_superior + 3*self.altura_campos + 2*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_sim = Label(self.frame_2, text="simbolo (max 3 carac.)", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_sim.place(relx=0.05, rely=margem_superior + 4*self.altura_campos + 2*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_sim = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_sim.place(relx=0.05, rely=margem_superior + 5*self.altura_campos + 3*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_uni_grandeza = Label(self.frame_2, text="grandeza física da unidade", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_uni_grandeza.place(relx=0.05, rely=margem_superior + 6*self.altura_campos + 3*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_uni_grandeza = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox, selectmode=SINGLE)

        indice = 0       
        for id in self.lista_ids_grandezas:
            unidade = self.lista_grandezas[indice]
            self.entry_uni_grandeza.insert(id,unidade)
            indice += 1
        
        self.scbar_uni_grandeza = Scrollbar(self.entry_uni_grandeza, orient=VERTICAL)
        self.scbar_uni_grandeza.config(command=self.entry_uni_grandeza.yview)
        self.scbar_uni_grandeza.pack(side=RIGHT, fill=Y)       

        self.entry_uni_grandeza.configure(yscrollcommand=self.scbar_uni_grandeza.set)
        self.entry_uni_grandeza.place(relx=0.05, rely=margem_superior + 7*self.altura_campos + 4*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.escolha_uni_grandeza = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_uni_grandeza.place(relx=0.05, rely=margem_superior + 11*self.altura_campos + 5*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_uni_grandeza.bind('<<ListboxSelect>>', self.on_select_uni_grandeza)

        def btn_incluir_entrar(event):
            botao_incluir.configure(bg="blue", fg="white")
        def btn_incluir_sair(event):
            botao_incluir.configure(bg="white", fg="black")
        botao_incluir = Button(self.frame_2, text="Incluir", bg="white", fg="black", command=self.incluir_uni)
        botao_incluir.place(relx=0.10, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_incluir.bind('<Enter>',btn_incluir_entrar)
        botao_incluir.bind('<Leave>',btn_incluir_sair)

        def btn_atualizar_entrar(event):
            botao_atualizar.configure(bg="yellow", fg="black")
        def btn_atualizar_sair(event):
            botao_atualizar.configure(bg="white", fg="black")
        botao_atualizar = Button(self.frame_2, text="Atualizar", bg="white", fg="black", command=self.atualizar_uni)
        botao_atualizar.place(relx=0.40, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_atualizar.bind('<Enter>',btn_atualizar_entrar)
        botao_atualizar.bind('<Leave>',btn_atualizar_sair)

        def btn_deletar_entrar(event):
            botao_deletar.configure(bg="red", fg="white")
        def btn_deletar_sair(event):
            botao_deletar.configure(bg="white", fg="black")
        botao_deletar = Button(self.frame_2, text="Deletar", bg="white", fg="black", command=self.deletar_uni)
        botao_deletar.place(relx=0.70, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_deletar.bind('<Enter>',btn_deletar_entrar)
        botao_deletar.bind('<Leave>',btn_deletar_sair)

        def btn_limpar_entrar(event):
            botao_limpar.configure(bg="orange", fg="black")
        def btn_limpar_sair(event):
            botao_limpar.configure(bg="white", fg="black")
        botao_limpar = Button(self.frame_2, text="Limpar", bg="white", fg="black", command=self.limpar_uni)
        botao_limpar.place(relx=0.10, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_limpar.bind('<Enter>',btn_limpar_entrar)
        botao_limpar.bind('<Leave>',btn_limpar_sair)

        def btn_home_entrar(event):
            botao_home.configure(bg="green", fg="white")
        def btn_home_sair(event):
            botao_home.configure(bg="white", fg="black")
        botao_home = Button(self.frame_2, text="HOME", bg="white", fg="black", command=self.home)
        botao_home.place(relx=0.40, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_home.bind('<Enter>',btn_home_entrar)
        botao_home.bind('<Leave>',btn_home_sair)

        def btn_ativar_entrar(event):
            botao_ativar.configure(bg="purple", fg="white")
        def btn_ativar_sair(event):
            botao_ativar.configure(bg="white", fg="black")
        botao_ativar = Button(self.frame_2, text="Ativar", bg="white", fg="black", command=self.ativar_uni)
        botao_ativar.place(relx=0.70, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_ativar.bind('<Enter>',btn_ativar_entrar)
        botao_ativar.bind('<Leave>',btn_ativar_sair)

        # frame 3
        self.apagar_widgets_frame_3()
        self.criar_tv_uni()

        def btn_capturar_entrar(event):
            botao_capturar.configure(bg="pink", fg="black")
        def btn_capturar_sair(event):
            botao_capturar.configure(bg="white", fg="black")
        botao_capturar = Button(self.frame_3, text="Capturar", bg="black", fg="white", command=self.capturar_uni)
        botao_capturar.place(relx=0.30, rely=0.90, relheight=0.05, relwidth=0.40)
        botao_capturar.bind('<Enter>',btn_capturar_entrar)
        botao_capturar.bind('<Leave>',btn_capturar_sair)

    def on_select_uni_grandeza(self, event):
        try:
            self.escolha_uni_grandeza.configure(text=self.entry_uni_grandeza.get(self.entry_uni_grandeza.curselection()), bg=self.cor_fundo_entry, fg="black")
        except:
            pass

    def capturar_uni(self):
        
        try:
            Item_Selecionado = self.tv_uni.selection()[0]
        except:
            messagebox.showinfo("ERRO","Precisa Selecionar um item.")
            return()
        
        valores_selecionados = self.tv_uni.item(Item_Selecionado,"values")

        id_capturado = valores_selecionados[0]
        unidade_capturada = valores_selecionados[1]
        simbolo_capturado = valores_selecionados[2]
        grandeza_capturada = valores_selecionados[3] 

        self.entry_id_uni.configure(text=id_capturado)

        self.entry_uni.delete(0,END)
        self.entry_uni.insert(0,unidade_capturada)

        self.entry_sim.delete(0,END)
        self.entry_sim.insert(0,simbolo_capturado)

        indice = 0
        for item in self.lista_grandezas:
            if grandeza_capturada == item:
                indice_grandeza = self.lista_ids_grandezas[indice]
            indice += 1

        self.entry_uni_grandeza.selection_clear(0,tk.END)
        self.entry_uni_grandeza.selection_set(indice_grandeza)
        self.escolha_uni_grandeza.configure(text=self.entry_uni_grandeza.get(self.entry_uni_grandeza.curselection()), bg=self.cor_fundo_entry, fg="black")

        return()

    def criar_tv_uni(self):

        self.tv_uni = ttk.Treeview(self.frame_3, columns=('id','unidade','simbolo','grandeza','ativo'), show='headings')
        
        self.tv_uni.column('id', minwidth=0, width=10)
        self.tv_uni.column('unidade', minwidth=0, width=100)
        self.tv_uni.column('simbolo', minwidth=0, width=10)
        self.tv_uni.column('grandeza', minwidth=0, width=10)
        self.tv_uni.column('ativo', minwidth=0, width=10)
        
        self.tv_uni.heading('id', text="ID")
        self.tv_uni.heading('unidade', text="Unidade")
        self.tv_uni.heading('simbolo', text="Símbolo")
        self.tv_uni.heading('grandeza', text="Grandeza")
        self.tv_uni.heading('ativo', text="Ativo")        

        sql = "SELECT `id_unidade`,`unidade`,`simbolo`,`grandeza_id`,`ativo` FROM unidades"
        result = executa_DQL(sql)

        for item_result in result:
            grandeza_id = item_result[3]
            sql = f"SELECT grandeza FROM grandezas_fisicas WHERE id = '{grandeza_id}'"
            result = executa_DQL(sql)
            item_grandeza = result[0][0]
            self.tv_uni.insert("", END, values=(item_result[0], item_result[1], item_result[2], item_grandeza, item_result[4]))                    

        self.tv_uni.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

    def deletar_uni(self):
        id_entry = self.entry_id_uni.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        sql = f"UPDATE `unidades` SET `ativo` = 0 WHERE id_unidade = {id_entry};"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo("ERRO","Algo deu errado na inclusão de itens no banco de dados.")

        self.criar_tv_uni()
        self.limpar_uni()
        return()        

    def atualizar_uni(self):
        id_entry = self.entry_id_uni.cget("text")

        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        
        id_entry = int(id_entry)
        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID tipo: {type(id_entry)}.")
            return()

        unidade_entry = self.entry_uni.get()

        if len(unidade_entry) == 0:
            messagebox.showinfo("ERRO",f"Unidade precisa ser preenchida.")
            return()

        simbolo_entry = self.entry_sim.get()
        if len(simbolo_entry) == 0:
            messagebox.showinfo("ERRO",f"Símbolo precisa ser preenchida.")
            return()      

        grandeza_entry = self.escolha_uni_grandeza.cget("text")

        if len(grandeza_entry)==0 or grandeza_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Grandeza precisa ser escolhida.")
            return() 

        sql = f"SELECT id FROM grandezas_fisicas WHERE `grandeza`='{grandeza_entry}'"
        result = executa_DQL(sql)
        grandeza_id_entry = result[0][0]

        if grandeza_id_entry == 0:
            messagebox.showinfo("ERRO","algo está errado com a grandeza, não foi feita a atualização.")
            return()

        sql = f"UPDATE `unidades` SET unidade = '{unidade_entry}', simbolo = '{simbolo_entry}', grandeza_id = '{grandeza_id_entry}' WHERE id_unidade = {id_entry};"
        print(sql)
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo("ERRO","O registro não foi atualizado.")
            print(sql)
            return()
        
        self.criar_tv_uni()
        self.limpar_uni()
        return()

    def incluir_uni(self):
        entry_unidade = self.entry_uni.get()
        entry_simbolo = self.entry_sim.get()

        if len(entry_unidade) == 0:
            messagebox.showinfo("Em branco","Campo unidade precisa ser preenchido.")
            return()

        if len(entry_simbolo) == 0:
            messagebox.showinfo("Em branco","Campo simbolo precisa ser preenchido.")
            return

        grandeza_entry = self.escolha_uni_grandeza.cget("text")
        if len(grandeza_entry)==0 or grandeza_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Grandeza precisa ser escolhida.")
            return() 
        
        sql = f"SELECT id FROM grandezas_fisicas WHERE `grandeza`='{grandeza_entry}'"
        result = executa_DQL(sql)
        grandeza_id_entry = result[0][0]

        if grandeza_id_entry == 0:
            messagebox.showinfo("EERO","algo está errado com a grandeza, não foi feita a atualização.")
            return()

        sql = f"INSERT INTO {self.tabela} (unidade,simbolo,grandeza_id,ativo) VALUES ('{entry_unidade}','{entry_simbolo}','{grandeza_id_entry}','1')"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo(title="ERRO", message="Algo deu errado com o banco de dados.")
            return()
                                
        self.criar_tv_uni()
        self.limpar_uni()
        return()

    def limpar_uni(self):
        self.entry_sim.delete(0,END)
        self.entry_uni.delete(0,END)
        self.entry_id_uni.configure(text="novo")
        self.entry_uni_grandeza.selection_clear(0,tk.END)
        self.escolha_uni_grandeza.configure(text="escolher", bg="white", fg="red")
        self.on_select_uni_grandeza(Event)
        self.entry_uni.focus()

    def ativar_uni(self):
        id_entry = self.entry_id_uni.cget("text")

        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        sql = f"UPDATE `unidades` SET `ativo` = 1 WHERE id_unidade = {id_entry};"
        result = executa_DML(sql)
        self.criar_tv_uni()
        self.limpar_uni()
        return()


    def insumos(self):
        self.tabela = "insumos"

        abc = self.listagem_unidades_insumos()

        self.lista_ids_unidades = abc[0]
        self.lista_unidades = abc[1]

        if len(self.lista_ids_unidades) == 0:
            messagebox.showinfo("Faltam dados","Unidades necessitam de algu(ns) dado(s).")
            self.home()
        
        self.apagar_widgets_frame_2()
        self.apagar_widgets_frame_3()

        # frame_1
        self.label_frame_1.configure(text="Insumos")

        # frame 2
        self.apagar_widgets_frame_2()
        
        qtde_labels_e_entrys = 7
        adicional_tamanhos_listbox = 3
        margem_superior = ((1-self.espaco_para_botoes)-((qtde_labels_e_entrys*2+adicional_tamanhos_listbox)*self.altura_campos)-(qtde_labels_e_entrys*self.espaco_interno)-((qtde_labels_e_entrys-1)*self.espaco_externo))/2

        self.label_id_ins = Label(self.frame_2, text="ID", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_id_ins.place(relx=0.05, rely=margem_superior, relwidth=0.90, relheight=self.altura_campos)

        self.entry_id_ins = Label(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, text="novo")
        self.entry_id_ins.place(relx=0.05, rely=margem_superior + self.altura_campos + self.espaco_interno, relwidth=0.90, relheight=self.altura_campos)
        
        self.label_ins = Label(self.frame_2, text="insumo", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_ins.place(relx=0.05, rely=margem_superior + 2*self.altura_campos + self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_ins = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_ins.place(relx=0.05, rely=margem_superior + 3*self.altura_campos + 2*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_qtde_ref = Label(self.frame_2, text="qtde ref.", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_qtde_ref.place(relx=0.05, rely=margem_superior + 4*self.altura_campos + 2*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_qtde_ref = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_qtde_ref.place(relx=0.05, rely=margem_superior + 5*self.altura_campos + 3*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_qtde_ref.insert(0,'1')        

        self.label_ins_unidade = Label(self.frame_2, text="unidade", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_ins_unidade.place(relx=0.05, rely=margem_superior + 6*self.altura_campos + 3*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_ins_unidade = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox, selectmode=SINGLE)

        indice = 0        
        for id in self.lista_ids_unidades:
            unidade = self.lista_unidades[indice]
            self.entry_ins_unidade.insert(id,unidade)
            indice += 1

        self.scbar_ins_unidade = Scrollbar(self.entry_ins_unidade, orient=VERTICAL)
        self.scbar_ins_unidade.config(command=self.entry_ins_unidade.yview)
        self.scbar_ins_unidade.pack(side=RIGHT, fill=Y)

        self.entry_ins_unidade.configure(yscrollcommand=self.scbar_ins_unidade.set)
        self.entry_ins_unidade.place(relx=0.05, rely=margem_superior + 7*self.altura_campos + 4*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_ins_unidade.bind('<<ListboxSelect>>',self.on_select_ins_unidade)

        self.escolha_ins_unidade = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_ins_unidade.place(relx=0.05, rely=margem_superior + 11*self.altura_campos + 5*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_preco_ref = Label(self.frame_2, text="preço referencial por unidade escolhida", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_preco_ref.place(relx=0.05, rely=margem_superior + 12*self.altura_campos + 5*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_preco_ref = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_preco_ref.place(relx=0.05, rely=margem_superior + 13*self.altura_campos + 6*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_peso_uma_unidade_ref = Label(self.frame_2, text="peso em gramas de 1 litro do insumo", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_peso_uma_unidade_ref.place(relx=0.05, rely=margem_superior + 14*self.altura_campos + 7*self.espaco_interno + 5*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_peso_uma_unidade_ref = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_peso_uma_unidade_ref.place(relx=0.05, rely=margem_superior + 15*self.altura_campos + 8*self.espaco_interno + 5*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
 
        def btn_incluir_entrar(event):
            botao_incluir.configure(bg="blue", fg="white")
        def btn_incluir_sair(event):
            botao_incluir.configure(bg="white", fg="black")
        botao_incluir = Button(self.frame_2, text="Incluir", bg="white", fg="black", command=self.incluir_ins)
        botao_incluir.place(relx=0.10, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_incluir.bind('<Enter>',btn_incluir_entrar)
        botao_incluir.bind('<Leave>',btn_incluir_sair)

        def btn_atualizar_entrar(event):
            botao_atualizar.configure(bg="yellow", fg="black")
        def btn_atualizar_sair(event):
            botao_atualizar.configure(bg="white", fg="black")
        botao_atualizar = Button(self.frame_2, text="Atualizar", bg="white", fg="black", command=self.atualizar_ins)
        botao_atualizar.place(relx=0.40, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_atualizar.bind('<Enter>',btn_atualizar_entrar)
        botao_atualizar.bind('<Leave>',btn_atualizar_sair)

        def btn_deletar_entrar(event):
            botao_deletar.configure(bg="red", fg="white")
        def btn_deletar_sair(event):
            botao_deletar.configure(bg="white", fg="black")
        botao_deletar = Button(self.frame_2, text="Deletar", bg="white", fg="black", command=self.deletar_ins)
        botao_deletar.place(relx=0.70, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_deletar.bind('<Enter>',btn_deletar_entrar)
        botao_deletar.bind('<Leave>',btn_deletar_sair)

        def btn_limpar_entrar(event):
            botao_limpar.configure(bg="orange", fg="black")
        def btn_limpar_sair(event):
            botao_limpar.configure(bg="white", fg="black")
        botao_limpar = Button(self.frame_2, text="Limpar", bg="white", fg="black", command=self.limpar_ins)
        botao_limpar.place(relx=0.10, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_limpar.bind('<Enter>',btn_limpar_entrar)
        botao_limpar.bind('<Leave>',btn_limpar_sair)

        def btn_home_entrar(event):
            botao_home.configure(bg="green", fg="white")
        def btn_home_sair(event):
            botao_home.configure(bg="white", fg="black")
        botao_home = Button(self.frame_2, text="HOME", bg="white", fg="black", command=self.home)
        botao_home.place(relx=0.40, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_home.bind('<Enter>',btn_home_entrar)
        botao_home.bind('<Leave>',btn_home_sair)

        def btn_ativar_entrar(event):
            botao_ativar.configure(bg="purple", fg="white")
        def btn_ativar_sair(event):
            botao_ativar.configure(bg="white", fg="black")
        botao_ativar = Button(self.frame_2, text="Ativar", bg="white", fg="black", command=self.ativar_ins)
        botao_ativar.place(relx=0.70, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_ativar.bind('<Enter>',btn_ativar_entrar)
        botao_ativar.bind('<Leave>',btn_ativar_sair)

        # frame 3
        self.apagar_widgets_frame_3()
        self.criar_tv_ins()

        def btn_capturar_entrar(event):
            botao_capturar.configure(bg="pink", fg="black")
        def btn_capturar_sair(event):
            botao_capturar.configure(bg="white", fg="black")
        botao_capturar = Button(self.frame_3, text="Capturar", bg="black", fg="white", command=self.capturar_ins)
        botao_capturar.place(relx=0.30, rely=0.90, relheight=0.05, relwidth=0.40)
        botao_capturar.bind('<Enter>',btn_capturar_entrar)
        botao_capturar.bind('<Leave>',btn_capturar_sair)

    def on_select_ins_unidade(self, event):
        try:
            self.escolha_ins_unidade.configure(text=self.entry_ins_unidade.get(self.entry_ins_unidade.curselection()), bg=self.cor_fundo_entry, fg="black")
        except:
            pass

    def capturar_ins(self):

        try:
            Item_Selecionado = self.tv_ins.selection()[0]
        except:
            messagebox.showinfo("ERRO","Precisa Selecionar um item.")
            return()
        
        valores_selecionados = self.tv_ins.item(Item_Selecionado,"values")
        
        id_capturado = valores_selecionados[0]
        insumo_capturado = valores_selecionados[1]
        qtde_capturada = valores_selecionados[2]
        unidade_capturada = valores_selecionados[3]
        preco_ref_capturado = valores_selecionados[4]
        peso_uma_unidade_ref = valores_selecionados[5]

        self.entry_id_ins.configure(text=id_capturado)

        self.entry_ins.delete(0,END)
        self.entry_ins.insert(0, insumo_capturado)        

        self.entry_preco_ref.delete(0,END)
        self.entry_preco_ref.insert(0, preco_ref_capturado)

        self.entry_qtde_ref.delete(0,END)
        self.entry_qtde_ref.insert(0, qtde_capturada)

        self.entry_peso_uma_unidade_ref.delete(0,END)
        self.entry_peso_uma_unidade_ref.insert(0, peso_uma_unidade_ref)

        indice = 0
        for item in self.lista_unidades:
            if unidade_capturada == item:
                indice_unidade = self.lista_ids_unidades[indice]
            indice += 1

        self.entry_ins_unidade.selection_clear(0,tk.END)
        self.entry_ins_unidade.selection_set(indice_unidade)
        self.entry_ins_unidade.activate(indice_unidade)
        self.entry_ins_unidade.see(indice_unidade)
        self.escolha_ins_unidade.configure(text=unidade_capturada,background=self.cor_fundo_entry, fg='black')

        self.on_select_uni_grandeza(Event)

    def criar_tv_ins(self):

        self.tv_ins = ttk.Treeview(self.frame_3, columns=('id','insumo','qtde_ref','unidade','preco_ref','peso','ativo'), show='headings')
        self.tv_ins.column('id', minwidth=0, width=10)
        self.tv_ins.column('insumo', minwidth=0, width=75)
        self.tv_ins.column('qtde_ref', minwidth=0, width=10)
        self.tv_ins.column('unidade', minwidth=0, width=10)
        self.tv_ins.column('preco_ref', minwidth=0, width=10)
        self.tv_ins.column('peso', minwidth=0, width=10)
        self.tv_ins.column('ativo', minwidth=0, width=10)
        
        self.tv_ins.heading('id', text="ID")
        self.tv_ins.heading('insumo', text="Insumo")
        self.tv_ins.heading('qtde_ref', text="Qtde Ref.")
        self.tv_ins.heading('unidade', text="Unidade")
        self.tv_ins.heading('preco_ref', text="Preço Referencial")
        self.tv_ins.heading('peso', text="Peso 1 unid ref")
        self.tv_ins.heading('ativo', text="Ativo")

        sql = f"SELECT `id_insumo`,`insumo`,`qtde_ref`,`unidade_id`,`preco_ref`,`peso_uma_unidade_ref`,`ativo` FROM {self.tabela}"
        result = executa_DQL(sql)

        for item_result in result:
            sql = f"SELECT unidade FROM `unidades` WHERE `id_unidade` = '{item_result[3]}'"
            result = executa_DQL(sql)
            unidade = result[0][0]
            self.tv_ins.insert("", END, values=(item_result[0], item_result[1], item_result[2], unidade, item_result[4], item_result[5], item_result[6]))

        self.tv_ins.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

    def deletar_ins(self):
        id_entry = self.entry_id_ins.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        
        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '0' WHERE id_insumo = {id_entry};"
        result = executa_DML(sql)
        self.criar_tv_ins()
        self.limpar_ins()
        return()        

    def atualizar_ins(self):
        id_entry = self.entry_id_ins.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        
        id_entry = int(id_entry)
        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID tipo: {type(id_entry)}.")
            return()

        insumo_entry = self.entry_ins.get()
        
        if len(insumo_entry) == 0:
            messagebox.showinfo("ERRO",f"Insumo precisa ser preenchido.")
            return()

        preco_ref = self.entry_preco_ref.get()
        preco_ref = preco_ref.replace(',','.')

        try:
            preco_ref = float(preco_ref)
        except:
            messagebox.showinfo("Não válido",f"Campo preço referencial não é válido. {preco_ref}")
            return()

        if preco_ref == 0:
            messagebox.showinfo("Em branco","Campo preço referencial precisa ser preenchido.")
            return()  

        qtde_ref = self.entry_qtde_ref.get()
        qtde_ref = qtde_ref.replace(',','.')

        try:
            qtde_ref = float(qtde_ref)
        except:
            messagebox.showinfo("Não válido",f"Campo quantidade referencial não é válido. {qtde_ref}")
            return()

        if qtde_ref == 0:
            messagebox.showinfo("Em branco","Campo quantidade referencial precisa ser preenchido.")
            return()

        unidade_entry = self.escolha_ins_unidade.cget("text")

        if len(unidade_entry) == 0 or unidade_entry == 'escolher':
            messagebox.showinfo("Em branco","Campo unidade precisa ser preenchida.")
            return()

        sql = f"SELECT id_unidade FROM unidades WHERE `unidade` = '{unidade_entry}'"
        result = executa_DQL(sql)
        unidade_id = result[0][0]

        peso_ref = self.entry_peso_uma_unidade_ref.get()
        peso_ref = peso_ref.replace(",",".")

        try:
            peso_ref = float(peso_ref)
        except:
            messagebox.showinfo("ERRO","Peso ref da unidade informada precisa ser preenchida")
            return()

        if peso_ref == 0:
            messagebox.showinfo("ERRO","Peso ref da unidade informada precisa ser preenchida")
            return()
           
        sql = f"UPDATE `{self.tabela}` SET insumo = '{insumo_entry}', unidade_id = '{unidade_id}', preco_ref = '{preco_ref}', qtde_ref = '{qtde_ref}', peso_uma_unidade_ref = '{peso_ref}'  WHERE id_insumo = {id_entry};"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo("ERRO","O registro não foi atualizado.")
            print(sql)
            return()          
        
        self.criar_tv_ins()
        self.limpar_ins()
        return()

    def incluir_ins(self):
        
        entry_insumo = self.entry_ins.get()

        unidade_entry = self.escolha_ins_unidade.cget("text")

        if len(unidade_entry) == 0 or unidade_entry == 'escolher':
            messagebox.showinfo("Em branco","Campo unidade precisa ser preenchida.")
            return()

        sql = f"SELECT id_unidade FROM unidades WHERE `unidade` = '{unidade_entry}'"
        result = executa_DQL(sql)
        unidade_id = result[0][0]

        if len(entry_insumo) == 0:
            messagebox.showinfo("Em branco","Campo insumo precisa ser preenchido.")
            return()

        preco_ref = self.entry_preco_ref.get()
        preco_ref = preco_ref.replace(',','.')

        try:
            preco_ref = float(preco_ref)
        except:
            messagebox.showinfo("Não válido",f"Campo preço referencial não é válido. {preco_ref}")
            return()

        if preco_ref == 0:
            messagebox.showinfo("Em branco","Campo preço referencial precisa ser preenchido.")
            return()

        qtde_ref = self.entry_qtde_ref.get()
        qtde_ref = qtde_ref.replace(',','.')

        try:
            qtde_ref = float(qtde_ref)
        except:
            messagebox.showinfo("Não válido",f"Campo quantidade referencial não é válido. {qtde_ref}")
            return()

        if qtde_ref == 0:
            messagebox.showinfo("Em branco","Campo quantidade referencial precisa ser preenchido.")
            return()

        peso_ref = self.entry_peso_uma_unidade_ref.get()
        peso_ref = peso_ref.replace(',','.')

        try:
            peso_ref = float(peso_ref)
        except:
            messagebox.showinfo("ERRO","Peso ref da unidade informada precisa ser preenchida")
            return()

        if peso_ref == 0:
            messagebox.showinfo("ERRO","Peso ref da unidade informada precisa ser preenchida")
            return()

        sql = f"INSERT INTO {self.tabela} (insumo, unidade_id, preco_ref, qtde_ref, peso_uma_unidade_ref, ativo) VALUES ('{entry_insumo}','{unidade_id}','{preco_ref}','{qtde_ref}','{peso_ref}','1')"
        result = executa_DML(sql)

        if result == False:
            print(sql)
            messagebox.showinfo(title="ERRO", message="Algo deu errado com o banco de dados.")
            return()

        self.criar_tv_ins()
        self.limpar_ins()
        return()

    def limpar_ins(self):
        self.entry_ins.delete(0,END)
        self.entry_id_ins.configure(text="novo")
        self.entry_preco_ref.delete(0,END)
        self.entry_qtde_ref.delete(0,END)
        self.entry_qtde_ref.insert(0,1)
        self.entry_peso_uma_unidade_ref.delete(0,END)
        self.entry_peso_uma_unidade_ref.insert(0,1)
        self.entry_ins_unidade.selection_clear(0,tk.END)
        self.escolha_ins_unidade.configure(text="escolher", bg="white", fg="red")
        self.on_select_ins_unidade(Event)

        self.entry_ins.focus()

    def ativar_ins(self):
        id_entry = self.entry_id_ins.cget("text")

        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '1' WHERE id_insumo = {id_entry};"
        result = executa_DML(sql)
        self.criar_tv_ins()
        self.limpar_ins()
        return()


    def tipos_produtos(self):
        self.tabela = "tipos_produtos"
        # frame_1
        self.label_frame_1.configure(text="Tipos de Produtos")

        # frame 2
        self.apagar_widgets_frame_2()
        
        qtde_labels_e_entrys = 4
        adicional_tamanhos_listbox = 3
        margem_superior = ((1-self.espaco_para_botoes)-((qtde_labels_e_entrys*2+adicional_tamanhos_listbox)*self.altura_campos)-(qtde_labels_e_entrys*self.espaco_interno)-((qtde_labels_e_entrys-1)*self.espaco_externo))/2

        self.label_id_tpr = Label(self.frame_2, text="ID", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_id_tpr.place(relx=0.05, rely=margem_superior, relwidth=0.90, relheight=self.altura_campos)

        self.entry_id_tpr = Label(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, text="novo")
        self.entry_id_tpr.place(relx=0.05, rely=margem_superior + self.altura_campos + self.espaco_interno, relwidth=0.90, relheight=self.altura_campos)
        
        self.label_tpr = Label(self.frame_2, text="tipo de produtos", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_tpr.place(relx=0.05, rely=margem_superior + 2*self.altura_campos + self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_tpr = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_tpr.place(relx=0.05, rely=margem_superior + 3*self.altura_campos + 2*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        #self.label_tpr_markup = Label(self.frame_2, text="markup", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        #self.label_tpr_markup.place(relx=0.05, rely=margem_superior + 4*self.altura_campos + 2*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        #self.entry_tpr_markup = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        #self.entry_tpr_markup.place(relx=0.05, rely=margem_superior + 5*self.altura_campos + 3*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_tpr_descricao = Label(self.frame_2, text="descrição do tipo do produto", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_tpr_descricao.place(relx=0.05, rely=margem_superior + 4*self.altura_campos + 2*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_tpr_descricao = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_tpr_descricao.place(relx=0.05, rely=margem_superior + 5*self.altura_campos + 3*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_tpr_posicao = Label(self.frame_2, text="posição no menu do tipo do produto", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_tpr_posicao.place(relx=0.05, rely=margem_superior + 6*self.altura_campos + 3*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_tpr_posicao = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_tpr_posicao.place(relx=0.05, rely=margem_superior + 7*self.altura_campos + 4*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)


        def btn_incluir_entrar(event):
            botao_incluir.configure(bg="blue", fg="white")
        def btn_incluir_sair(event):
            botao_incluir.configure(bg="white", fg="black")
        botao_incluir = Button(self.frame_2, text="Incluir", bg="white", fg="black", command=self.incluir_tpr)
        botao_incluir.place(relx=0.10, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_incluir.bind('<Enter>',btn_incluir_entrar)
        botao_incluir.bind('<Leave>',btn_incluir_sair)


        def btn_atualizar_entrar(event):
            botao_atualizar.configure(bg="yellow", fg="black")
        def btn_atualizar_sair(event):
            botao_atualizar.configure(bg="white", fg="black")
        botao_atualizar = Button(self.frame_2, text="Atualizar", bg="white", fg="black", command=self.atualizar_tpr)
        botao_atualizar.place(relx=0.40, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_atualizar.bind('<Enter>',btn_atualizar_entrar)
        botao_atualizar.bind('<Leave>',btn_atualizar_sair)

        def btn_deletar_entrar(event):
            botao_deletar.configure(bg="red", fg="white")
        def btn_deletar_sair(event):
            botao_deletar.configure(bg="white", fg="black")
        botao_deletar = Button(self.frame_2, text="Deletar", bg="white", fg="black", command=self.deletar_tpr)
        botao_deletar.place(relx=0.70, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_deletar.bind('<Enter>',btn_deletar_entrar)
        botao_deletar.bind('<Leave>',btn_deletar_sair)

        def btn_limpar_entrar(event):
            botao_limpar.configure(bg="orange", fg="black")
        def btn_limpar_sair(event):
            botao_limpar.configure(bg="white", fg="black")
        botao_limpar = Button(self.frame_2, text="Limpar", bg="white", fg="black", command=self.limpar_tpr)
        botao_limpar.place(relx=0.10, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_limpar.bind('<Enter>',btn_limpar_entrar)
        botao_limpar.bind('<Leave>',btn_limpar_sair)

        def btn_home_entrar(event):
            botao_home.configure(bg="green", fg="white")
        def btn_home_sair(event):
            botao_home.configure(bg="white", fg="black")
        botao_home = Button(self.frame_2, text="HOME", bg="white", fg="black", command=self.home)
        botao_home.place(relx=0.40, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_home.bind('<Enter>',btn_home_entrar)
        botao_home.bind('<Leave>',btn_home_sair)

        def btn_ativar_entrar(event):
            botao_ativar.configure(bg="purple", fg="white")
        def btn_ativar_sair(event):
            botao_ativar.configure(bg="white", fg="black")
        botao_ativar = Button(self.frame_2, text="Ativar", bg="white", fg="black", command=self.ativar_tpr)
        botao_ativar.place(relx=0.70, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_ativar.bind('<Enter>',btn_ativar_entrar)
        botao_ativar.bind('<Leave>',btn_ativar_sair)

        # frame 3
        self.apagar_widgets_frame_3()
        self.criar_tv_tpr()

        def btn_capturar_entrar(event):
            botao_capturar.configure(bg="pink", fg="black")
        def btn_capturar_sair(event):
            botao_capturar.configure(bg="white", fg="black")
        botao_capturar = Button(self.frame_3, text="Capturar", bg="black", fg="white", command=self.capturar_tpr)
        botao_capturar.place(relx=0.30, rely=0.90, relheight=0.05, relwidth=0.40)
        botao_capturar.bind('<Enter>',btn_capturar_entrar)
        botao_capturar.bind('<Leave>',btn_capturar_sair)

    def capturar_tpr(self):

        try:
            Item_Selecionado = self.tv_tpr.selection()[0]
        except:
            messagebox.showinfo("ERRO","Precisa Selecionar um item.")
            return()
        
        valores_selecionados = self.tv_tpr.item(Item_Selecionado,"values")

        id_capturado = valores_selecionados[0]
        tipo_produto_capturado = valores_selecionados[1]
        #markup_capturado = valores_selecionados[2]
        descricao_capturada = valores_selecionados[2]
        posicao_capturada = valores_selecionados[3]
            

        self.entry_id_tpr.configure(text=id_capturado)

        self.entry_tpr.delete(0,END)
        self.entry_tpr.insert(0,tipo_produto_capturado)        

        # self.entry_tpr_markup.delete(0,END)
        # self.entry_tpr_markup.insert(0,markup_capturado)

        self.entry_tpr_descricao.delete(0,END)
        self.entry_tpr_descricao.insert(0,descricao_capturada)

        self.entry_tpr_posicao.delete(0,END)
        self.entry_tpr_posicao.insert(0,posicao_capturada)

    def criar_tv_tpr(self):
        self.tv_tpr = ttk.Treeview(self.frame_3, columns=('id','tipo_produto','descricao','posicao','ativo'), show='headings')
        self.tv_tpr.column('id', minwidth=0, width=5)
        self.tv_tpr.column('tipo_produto', minwidth=0, width=100)
        self.tv_tpr.column('descricao', minwidth=0, width=100)
        self.tv_tpr.column('posicao', minwidth=0, width=10)
        self.tv_tpr.column('ativo', minwidth=0, width=5)
        
        self.tv_tpr.heading('id', text="ID")
        self.tv_tpr.heading('tipo_produto', text="Tipo de Produto")
        self.tv_tpr.heading('descricao', text="Descrição")
        self.tv_tpr.heading('posicao', text="Posição")
        self.tv_tpr.heading('ativo', text="Ativo")        

        sql = f"SELECT `id_tipo_produto`,`tipo_produto`,`descricao_tipo_produto`,`posicao`,`ativo` FROM {self.tabela} order by `tipo_produto`"
        result = executa_DQL(sql)

        if len(result) >= 1:
            for item in result:
                self.tv_tpr.insert("", item[0], values=(item[0], item[1], item[2], item[3], item[4]))

        self.tv_tpr.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

    def deletar_tpr(self):
        id_entry = self.entry_id_tpr.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            
        
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '0' WHERE id_tipo_produto = {id_entry};"
        result = executa_DML(sql)
        self.criar_tv_tpr()
        self.limpar_tpr()
        return()        

    def ativar_tpr(self):
        id_entry = self.entry_id_tpr.cget("text")
        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            
        
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '1' WHERE id_tipo_produto = {id_entry};"
        result = executa_DML(sql)
        self.criar_tv_tpr()
        self.limpar_tpr()
        return()

    def atualizar_tpr(self):
        
        id_entry = self.entry_id_tpr.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        
        id_entry = int(id_entry)
        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID tipo: {type(id_entry)}.")
            return()

        tipo_produto_entry = self.entry_tpr.get()
        
        if len(tipo_produto_entry) == 0:
            messagebox.showinfo("ERRO",f"Tipo de Produto precisa ser preenchido.")
            return()

        descricao_tipo = self.entry_tpr_descricao.get()

        if len(descricao_tipo) == 0:
            messagebox.showinfo("ERRO",f"Descrição do tipo de produto precisa ser preenchido.")
            return()
        
        posicao = self.entry_tpr_posicao.get()

        if len(posicao) >= 6 or len(posicao) == 0:
            messagebox.showinfo("ERRO",f"Posição do tipo de produto precisa ser preenchido corretamente.")
            return()

        sql = f"UPDATE `{self.tabela}` SET tipo_produto = '{tipo_produto_entry}', descricao_tipo_produto = '{descricao_tipo}', posicao = '{posicao}' WHERE id_tipo_produto = {id_entry};"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo("ERRO","O registro não foi atualizado.")
            print(sql)
            return()
        
        self.criar_tv_tpr()
        self.limpar_tpr()
        return()

    def incluir_tpr(self):
        entry_tipo_produto = self.entry_tpr.get()

        if len(entry_tipo_produto) == 0:
            messagebox.showinfo("Em branco","Campo unidade precisa ser preenchido.")
            return()

        descricao_tipo = self.entry_tpr_descricao.get()

        if len(descricao_tipo) == 0:
            messagebox.showinfo("ERRO",f"Descrição do tipo de produto precisa ser preenchido.")
            return()

        # markup = self.entry_tpr_markup.get()

        # if markup == 0 or len(markup) == 0:
        #     messagebox.showinfo("ERRO",f"Markup precisa ser preenchido.")
        #     return()

        # markup = markup.replace(",",".")
        # try:
        #     markup = float(markup)
        # except:
        #     messagebox.showinfo("ERRO",f"Markup precisa ser preenchido corretamente.")
        #     return()
        
        posicao = self.entry_tpr_posicao.get()

        if len(posicao) >= 6 or len(posicao) == 0:
            messagebox.showinfo("ERRO",f"Posição do tipo de produto precisa ser preenchido corretamente.")
            return()

        sql = f"INSERT INTO {self.tabela} (tipo_produto, descricao_tipo_produto, posicao, ativo) VALUES ('{entry_tipo_produto}', '{descricao_tipo}', '{posicao}', '1');"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo(title="ERRO", message="Algo deu errado com o banco de dados.")
            return()

        self.criar_tv_tpr()
        self.limpar_tpr()
        return()

    def limpar_tpr(self):
        self.entry_tpr.delete(0,END)
        self.entry_id_tpr.configure(text="novo")
        # self.entry_tpr_markup.delete(0,END)
        self.entry_tpr_descricao.delete(0,END)
        self.entry_tpr_posicao.delete(0,END)
        self.entry_tpr.focus()


    def sub_produtos(self):
        self.tabela = "sub_produtos"

        abc = self.listagem_tipos_sub_produtos()

        self.lista_ids_tipos_sub_produtos = abc[0]
        self.lista_tipos_sub_produtos = abc[1]

        if len(self.lista_ids_tipos_sub_produtos) == 0:
            messagebox.showinfo("Faltam dados","Tipos de Sub Produtos necessita(m) de algu(ns) dado(s).")
            self.home()
        
        self.apagar_widgets_frame_3()
        # frame_1
        self.label_frame_1.configure(text="Sub Produtos")

        # frame 2
        self.apagar_widgets_frame_2()
        
        qtde_labels_e_entrys = 4     
        adicional_tamanhos_listbox = 0
        margem_superior = ((1-self.espaco_para_botoes)-((qtde_labels_e_entrys*2+adicional_tamanhos_listbox)*self.altura_campos)-(qtde_labels_e_entrys*self.espaco_interno)-((qtde_labels_e_entrys-1)*self.espaco_externo))/2

        self.label_id_spr = Label(self.frame_2, text="ID", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_id_spr.place(relx=0.05, rely=margem_superior, relwidth=0.90, relheight=self.altura_campos)

        self.entry_id_spr = Label(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, text="novo")
        self.entry_id_spr.place(relx=0.05, rely=margem_superior + self.altura_campos + self.espaco_interno, relwidth=0.90, relheight=self.altura_campos)
        
        self.label_spr = Label(self.frame_2, text="sub produto", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_spr.place(relx=0.05, rely=margem_superior + 2*self.altura_campos + self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_spr = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_spr.place(relx=0.05, rely=margem_superior + 3*self.altura_campos + 2*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_spr_tipo_sub_produto = Label(self.frame_2, text="tipo de sub produto", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_spr_tipo_sub_produto.place(relx=0.05, rely=margem_superior + 4*self.altura_campos + 2*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_spr_tipo_sub_produto = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, height=1)

        indice = 0        
        for id in self.lista_ids_tipos_sub_produtos:
            tipo_sub_produto = self.lista_tipos_sub_produtos[indice]
            self.entry_spr_tipo_sub_produto.insert(id, tipo_sub_produto)
            indice += 1

        self.scbar_spr_tipo_sub_produto = Scrollbar(self.entry_spr_tipo_sub_produto, orient=VERTICAL)
        self.scbar_spr_tipo_sub_produto.config(command=self.entry_spr_tipo_sub_produto.yview)
        self.scbar_spr_tipo_sub_produto.pack(side=RIGHT, fill=Y)

        self.entry_spr_tipo_sub_produto.configure(yscrollcommand=self.scbar_spr_tipo_sub_produto.set)
        self.entry_spr_tipo_sub_produto.place(relx=0.05, rely=margem_superior + 5*self.altura_campos + 3*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_spr_tipo_sub_produto.bind('<<ListboxSelect>>',self.on_select_spr_tipo_sub_produto)

        self.escolha_spr_tipo_sub_produto = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_spr_tipo_sub_produto.place(relx=0.05, rely=margem_superior + 9*self.altura_campos + 4*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        # def mudando_spr_revenda_somente():
        #     if self.revenda_spr.get() == 1:
        #         self.label_spr_markup_revenda = Label(self.frame_2, text="markup: ", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        #         self.label_spr_markup_revenda.place(relx=0.35, rely=margem_superior + 10*self.altura_campos + 4*self.espaco_interno + 3*self.espaco_externo, relheight=self.altura_campos)
        #         self.entry_spr_markup_revenda = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        #         self.entry_spr_markup_revenda.place(relx=0.48, rely=margem_superior + 10*self.altura_campos + 4*self.espaco_interno + 3*self.espaco_externo, relwidth=0.30, relheight=self.altura_campos)
        #     else:
        #         self.label_spr_markup_revenda.destroy()
        #         self.entry_spr_markup_revenda.destroy()
        #     return()

        # self.revenda_spr = tk.IntVar()
        # self.checkbox_spr_revenda_somente = tk.Checkbutton(self.frame_2, text='apenas revenda', variable=self.revenda_spr, onvalue=1, offvalue=0, command=mudando_spr_revenda_somente)
        # self.checkbox_spr_revenda_somente.place(relx=0.05, rely=margem_superior + 10*self.altura_campos + 4*self.espaco_interno + 3*self.espaco_externo, relheight=self.altura_campos)
       

        self.label_spr_markup = Label(self.frame_2, text="markup para o Sub produto", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_spr_markup.place(relx=0.05, rely=margem_superior + 10*self.altura_campos + 4*self.espaco_interno + 3*self.espaco_externo, relheight=self.altura_campos, relwidth=0.90)
        self.entry_spr_markup = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_spr_markup.place(relx=0.05, rely=margem_superior + 11*self.altura_campos + 5*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        def btn_incluir_entrar(event):
            botao_incluir.configure(bg="blue", fg="white")
        def btn_incluir_sair(event):
            botao_incluir.configure(bg="white", fg="black")
        botao_incluir = Button(self.frame_2, text="Incluir", bg="white", fg="black", command=self.incluir_spr)
        botao_incluir.place(relx=0.10, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_incluir.bind('<Enter>',btn_incluir_entrar)
        botao_incluir.bind('<Leave>',btn_incluir_sair)

        def btn_atualizar_entrar(event):
            botao_atualizar.configure(bg="yellow", fg="black")
        def btn_atualizar_sair(event):
            botao_atualizar.configure(bg="white", fg="black")
        botao_atualizar = Button(self.frame_2, text="Atualizar", bg="white", fg="black", command=self.atualizar_spr)
        botao_atualizar.place(relx=0.40, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_atualizar.bind('<Enter>',btn_atualizar_entrar)
        botao_atualizar.bind('<Leave>',btn_atualizar_sair)

        def btn_deletar_entrar(event):
            botao_deletar.configure(bg="red", fg="white")
        def btn_deletar_sair(event):
            botao_deletar.configure(bg="white", fg="black")
        botao_deletar = Button(self.frame_2, text="Deletar", bg="white", fg="black", command=self.deletar_spr)
        botao_deletar.place(relx=0.70, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_deletar.bind('<Enter>',btn_deletar_entrar)
        botao_deletar.bind('<Leave>',btn_deletar_sair)

        def btn_limpar_entrar(event):
            botao_limpar.configure(bg="orange", fg="black")
        def btn_limpar_sair(event):
            botao_limpar.configure(bg="white", fg="black")
        botao_limpar = Button(self.frame_2, text="Limpar", bg="white", fg="black", command=self.limpar_spr)
        botao_limpar.place(relx=0.10, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_limpar.bind('<Enter>',btn_limpar_entrar)
        botao_limpar.bind('<Leave>',btn_limpar_sair)

        def btn_home_entrar(event):
            botao_home.configure(bg="green", fg="white")
        def btn_home_sair(event):
            botao_home.configure(bg="white", fg="black")
        botao_home = Button(self.frame_2, text="HOME", bg="white", fg="black", command=self.home)
        botao_home.place(relx=0.40, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_home.bind('<Enter>',btn_home_entrar)
        botao_home.bind('<Leave>',btn_home_sair)

        def btn_ativar_entrar(event):
            botao_ativar.configure(bg="purple", fg="white")
        def btn_ativar_sair(event):
            botao_ativar.configure(bg="white", fg="black")
        botao_ativar = Button(self.frame_2, text="Ativar", bg="white", fg="black", command=self.ativar_spr)
        botao_ativar.place(relx=0.70, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_ativar.bind('<Enter>',btn_ativar_entrar)
        botao_ativar.bind('<Leave>',btn_ativar_sair)

        # frame 3
        self.apagar_widgets_frame_3()
        self.criar_tv_spr()

        def btn_capturar_entrar(event):
            botao_capturar.configure(bg="pink", fg="black")
        def btn_capturar_sair(event):
            botao_capturar.configure(bg="white", fg="black")
        botao_capturar = Button(self.frame_3, text="Capturar", bg="black", fg="white", command=self.capturar_spr)
        botao_capturar.place(relx=0.30, rely=0.90, relheight=0.05, relwidth=0.40)
        botao_capturar.bind('<Enter>',btn_capturar_entrar)
        botao_capturar.bind('<Leave>',btn_capturar_sair)

    def on_select_spr_tipo_sub_produto(self, event):
        try:
            self.escolha_spr_tipo_sub_produto.configure(text=self.entry_spr_tipo_sub_produto.get(self.entry_spr_tipo_sub_produto.curselection()), bg=self.cor_fundo_entry, fg="black")
            tipo_sub_produto = self.entry_spr_tipo_sub_produto.get(self.entry_spr_tipo_sub_produto.curselection())
            sql = f"SELECT `markup_minimo` from `tipos_sub_produtos` WHERE `tipo_sub_produto` = '{tipo_sub_produto}'"
            result = executa_DQL(sql)
            markup_min = result[0][0]
            self.label_spr_markup.configure(text=f"markup para o Sub produto. Lembrando, markup mínimo: {markup_min}")
        except:
            pass

    def capturar_spr(self):
        try:
            Item_Selecionado = self.tv_spr.selection()[0]
        except:
            messagebox.showinfo("ERRO","Precisa Selecionar um item.")
            return()
        valores_selecionados = self.tv_spr.item(Item_Selecionado,"values")
        
        id_capturado = valores_selecionados[0]
        sub_produto_capturado = valores_selecionados[1]
        tipo_sub_produto_capturado = valores_selecionados[2]
        markup_capturado = valores_selecionados[3]

        self.entry_id_spr.configure(text=id_capturado)

        self.entry_spr.delete(0,END)
        self.entry_spr.insert(0, sub_produto_capturado)        

        sql = f"SELECT `id_tipo_sub_produto` FROM `tipos_sub_produtos` WHERE `tipo_sub_produto` = '{tipo_sub_produto_capturado}'"
        result = executa_DQL(sql)
        id_tipo_sub_produto = result[0][0]

        self.entry_spr_tipo_sub_produto.selection_clear(0,tk.END)
        self.entry_spr_tipo_sub_produto.selection_set(id_tipo_sub_produto)
        self.escolha_spr_tipo_sub_produto.configure(text=tipo_sub_produto_capturado, bg=self.cor_fundo_entry, fg="black")

        self.entry_spr_markup.delete(0,END)
        self.entry_spr_markup.insert(0,markup_capturado)

    def criar_tv_spr(self):
        self.tv_spr = ttk.Treeview(self.frame_3, columns=('id','sub_produto','tipo_sub_produto','markup','ativo'), show='headings')
        self.tv_spr.column('id', minwidth=0, width=10)
        self.tv_spr.column('sub_produto', minwidth=0, width=100)
        self.tv_spr.column('tipo_sub_produto', minwidth=0, width=10)
        self.tv_spr.column('markup', minwidth=0, width=10)        
        self.tv_spr.column('ativo', minwidth=0, width=10)
        
        self.tv_spr.heading('id', text="ID")
        self.tv_spr.heading('sub_produto', text="Produto")
        self.tv_spr.heading('tipo_sub_produto', text="Tipo Produto")
        self.tv_spr.heading('markup', text="markup")        
        self.tv_spr.heading('ativo', text="Ativo")      

        sql = f"SELECT `id_sub_produto`,`sub_produto`,`tipo_sub_produto_id`,`markup`,`ativo` FROM {self.tabela} ORDER BY `sub_produto`"
        result = executa_DQL(sql)

        for item_result in result:
            id_tipo_sub_produto = item_result[2]
            sql = f"SELECT `tipo_sub_produto` FROM `tipos_sub_produtos` WHERE `id_tipo_sub_produto` = '{id_tipo_sub_produto}'"
            result = executa_DQL(sql)
            tipo_sub_produto = result[0][0]
            self.tv_spr.insert("", id_tipo_sub_produto, values=(item_result[0], item_result[1], tipo_sub_produto, item_result[3], item_result[4]))

        self.tv_spr.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

    def deletar_spr(self):
        id_entry = self.entry_id_spr.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        
        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '0' WHERE id_sub_produto = {id_entry};"
        result = executa_DML(sql)
        self.criar_tv_spr()
        self.limpar_spr()
        return()        

    def atualizar_spr(self):
        id_entry = self.entry_id_spr.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        
        id_entry = int(id_entry)
        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID tipo: {type(id_entry)}.")
            return()

        sub_produto_entry = self.entry_spr.get()
        
        if len(sub_produto_entry) == 0:
            messagebox.showinfo("ERRO",f"Produto precisa ser preenchido.")
            return()
        
        entry_tipo_sub_produto = self.escolha_spr_tipo_sub_produto.cget("text")
        
        if len(entry_tipo_sub_produto) == 0:
            messagebox.showinfo("Em branco","Campo Tipo de Sub Produto precisa ser escolhido.")
            return()            

        sql = f"SELECT `id_tipo_sub_produto` FROM `tipos_sub_produtos` WHERE `tipo_sub_produto` = '{entry_tipo_sub_produto}'"
        result = executa_DQL(sql)
        id_tipo_sub_produto = result[0][0]   

        # apenas_revenda = self.revenda_spr.get()

        # if apenas_revenda == 1:
        #     markup_entry = self.entry_spr_markup.get()
            
        #     if len(markup_entry) == 0 or len(markup_entry) == 0:
        #         messagebox.showinfo("ERRO",f"Markup precisa ser preenchido.")
        #         return()

        #     markup_entry = markup_entry.replace(",",".")

        #     try:
        #         markup_entry = float(markup_entry)
        #     except:                
        #         messagebox.showinfo("ERRO",f"Markup não está correto.")
        #         return()
        # else:
        #     markup_entry = 0

        markup_entry = self.entry_spr_markup.get()
        
        if len(markup_entry) == 0 or len(markup_entry) == 0:
            messagebox.showinfo("ERRO",f"Markup precisa ser preenchido.")
            return()

        markup_entry = markup_entry.replace(",",".")

        try:
            markup_entry = float(markup_entry)
        except:                
            messagebox.showinfo("ERRO",f"Markup não está correto.")
            return()

        sql = f"UPDATE `{self.tabela}` SET sub_produto = '{sub_produto_entry}', tipo_sub_produto_id = '{id_tipo_sub_produto}', markup = '{markup_entry}' WHERE id_sub_produto = {id_entry};"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo("ERRO","O registro não foi atualizado.")
            print(sql)
            return()          
        
        self.criar_tv_spr()
        self.limpar_spr()
        return()

    def incluir_spr(self):
        entry_sub_produto = self.entry_spr.get()
        entry_tipo_sub_produto = self.escolha_spr_tipo_sub_produto.cget("text")
        print('tipo sub produto: ' + entry_tipo_sub_produto)

        if len(entry_tipo_sub_produto) == 0 or entry_tipo_sub_produto == 'escolher':
            messagebox.showinfo("Em branco","Campo Tipo de Sub Produto precisa ser escolhido.")
            return()            

        sql = f"SELECT `id_tipo_sub_produto` FROM `tipos_sub_produtos` WHERE `tipo_sub_produto` = '{entry_tipo_sub_produto}'"
        result = executa_DQL(sql)
        id_tipo_sub_produto = result[0][0]

        if len(entry_sub_produto) == 0:
            messagebox.showinfo("Em branco","Campo Sub Produto precisa ser preenchido.")
            return()
       
        # apenas_revenda = self.revenda_spr.get()

        # if apenas_revenda == 1:
        #     markup_entry = self.entry_spr_markup.get()
            
        #     if len(markup_entry) == 0 or len(markup_entry) == 0:
        #         messagebox.showinfo("ERRO",f"Markup precisa ser preenchido.")
        #         return()

        #     markup_entry = markup_entry.replace(",",".")

        #     try:
        #         markup_entry = float(markup_entry)
        #     except:                
        #         messagebox.showinfo("ERRO",f"Markup não está correto.")
        #         return()
        # else:
        #     markup_entry = 0

        markup_entry = self.entry_spr_markup.get()
        
        if len(markup_entry) == 0 or len(markup_entry) == 0:
            messagebox.showinfo("ERRO",f"Markup precisa ser preenchido.")
            return()

        markup_entry = markup_entry.replace(",",".")

        try:
            markup_entry = float(markup_entry)
        except:                
            messagebox.showinfo("ERRO",f"Markup não está correto.")
            return()

        sql = f"INSERT INTO {self.tabela} (sub_produto, tipo_sub_produto_id, markup, ativo) VALUES ('{entry_sub_produto}','{id_tipo_sub_produto}', '{markup_entry}','1');"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo(title="ERRO", message=f"Algo deu errado com o banco de dados. {sql}")
            print(sql)
            return()

        self.criar_tv_spr()
        self.limpar_spr()
        return()

    def limpar_spr(self):
        self.entry_spr.delete(0,END)
        self.entry_id_spr.configure(text="novo")
        self.entry_spr_tipo_sub_produto.selection_clear(0,tk.END)
        self.escolha_spr_tipo_sub_produto.configure(text="escolher", bg="white", fg="red")
        self.on_select_spr_tipo_sub_produto(Event)
        
        try:
            self.entry_spr_markup.delete(0,END)
        except:
            pass

        self.entry_spr.focus()

    def ativar_spr(self):
        id_entry = self.entry_id_spr.cget("text")

        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()
        
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '1' WHERE id_sub_produto = {id_entry};"
        result = executa_DML(sql)
        self.criar_tv_spr()
        self.limpar_spr()
        return()



    def aviso_spi(self, sub_produto, id_sub_produto):
        sql = f"SELECT sum(`percentual`) FROM {self.tabela} WHERE `sub_produto_id` = '{id_sub_produto}' and `ativo` = '1'"
        result = executa_DQL(sql)
        total = result[0][0]
        if total == None or total == 0:
            total = 0
            texto = f'{sub_produto} com 0,0 %'
        else:
            total = round(total,1)
            total = str(total)
            total = total.replace(".",",")
            texto = f'{sub_produto} com {total} %'

        self.percentual_sub_produto_spi.configure(text=texto)
        #messagebox.showinfo("Aviso",f"{sub_produto} está com {total}% ")
        return()

    def sub_produtos_x_insumos(self):
        self.tabela = "sub_produtos_x_insumos"
        abc = self.listagem_sub_produtos()

        self.lista_ids_sub_produtos = abc[0]
        self.lista_sub_produtos = abc[1]

        if len(self.lista_ids_sub_produtos) == 0:
            messagebox.showinfo("Faltam dados","Sub Produtos necessita(m) de algu(ns) dado(s).")
            self.home()

        abc = self.listagem_insumos()

        self.lista_ids_insumos = abc[0]
        self.lista_insumos = abc[1]

        if len(self.lista_ids_insumos) == 0:
            messagebox.showinfo("Faltam dados","Insumos necessita(m) de algu(ns) dado(s).")
            self.home()
        
        self.apagar_widgets_frame_3()

        # frame_1
        self.label_frame_1.configure(text="Sub Produtos x Insumos")

        # frame 2
        self.apagar_widgets_frame_2()
        
        qtde_labels_e_entrys = 5.50
        adicional_tamanhos_listbox = 6
        margem_superior = ((1-self.espaco_para_botoes)-((qtde_labels_e_entrys*2+adicional_tamanhos_listbox)*self.altura_campos)-(qtde_labels_e_entrys*self.espaco_interno)-((qtde_labels_e_entrys-1)*self.espaco_externo))/2

        self.percentual_sub_produto_spi = Label(self.frame_2, bg=self.cor_fundo_label, fg=self.cor_texto_label)
        self.percentual_sub_produto_spi.place(relx=0.45,rely=0,relheight=0.05,relwidth=0.54)
        self.percentual_sub_produto_spi.configure(text="0,0 %")

        self.label_id_spi = Label(self.frame_2, text="ID", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_id_spi.place(relx=0.05, rely=margem_superior, relwidth=0.90, relheight=self.altura_campos)

        self.entry_id_spi = Label(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, text="novo")
        self.entry_id_spi.place(relx=0.05, rely=margem_superior + self.altura_campos + self.espaco_interno, relwidth=0.90, relheight=self.altura_campos)

        self.label_spi = Label(self.frame_2, text="selecione o sub produto", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_spi.place(relx=0.05, rely=margem_superior + 2*self.altura_campos + self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_spi_sub_produto = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox)      
       
        indice = 0
        for id in self.lista_ids_sub_produtos:
            sub_produto = self.lista_sub_produtos[indice]
            self.entry_spi_sub_produto.insert(id, sub_produto)
            indice += 1

        self.scbar_spi_sub_produto = Scrollbar(self.entry_spi_sub_produto, orient=VERTICAL)
        self.scbar_spi_sub_produto.config(command=self.entry_spi_sub_produto.yview)
        self.scbar_spi_sub_produto.pack(side=RIGHT, fill=Y)

        self.entry_spi_sub_produto.configure(yscrollcommand=self.scbar_spi_sub_produto.set)
        self.entry_spi_sub_produto.place(relx=0.05, rely=margem_superior + 3*self.altura_campos + 2*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_spi_sub_produto.bind('<<ListboxSelect>>',self.on_select_spi_sub_produto)

        self.escolha_spi_sub_produto = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_spi_sub_produto.place(relx=0.05, rely=margem_superior + 7*self.altura_campos + 3*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_spi_insumo = Label(self.frame_2, text="selecione o insumo", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_spi_insumo.place(relx=0.05, rely=margem_superior + 8*self.altura_campos + 3*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_spi_insumo = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox)

        indice = 0        
        for id in self.lista_ids_insumos:
            insumo = self.lista_insumos[indice]
            self.entry_spi_insumo.insert(id, insumo)
            indice += 1

        self.scbar_spi_insumo = Scrollbar(self.entry_spi_insumo, orient=VERTICAL)
        self.scbar_spi_insumo.config(command=self.entry_spi_insumo.yview)
        self.scbar_spi_insumo.pack(side=RIGHT, fill=Y)       

        self.entry_spi_insumo.configure(yscrollcommand=self.scbar_spi_insumo.set)
        self.entry_spi_insumo.place(relx=0.05, rely=margem_superior + 9*self.altura_campos + 4*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_spi_insumo.bind('<<ListboxSelect>>',self.on_select_spi_insumo)

        self.escolha_spi_insumo = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_spi_insumo.place(relx=0.05, rely=margem_superior + 13*self.altura_campos + 5*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_spi_percentual = Label(self.frame_2, text="percentual peso (ex.: 10% digite 10)", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_spi_percentual.place(relx=0.05, rely=margem_superior + 14*self.altura_campos + 5*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_spi_percentual = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_spi_percentual.place(relx=0.05, rely=margem_superior + 15*self.altura_campos + 6*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)    

        self.label_spi_rendimento = Label(self.frame_2, text="rendimento peso (ex.: 80% digite 80)", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_spi_rendimento.place(relx=0.05, rely=margem_superior + 16*self.altura_campos + 6*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_spi_rendimento = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_spi_rendimento.place(relx=0.05, rely=margem_superior + 17*self.altura_campos + 7*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        self.entry_spi_rendimento.insert(0,100)

        def btn_incluir_entrar(event):
            botao_incluir.configure(bg="blue", fg="white")
        def btn_incluir_sair(event):
            botao_incluir.configure(bg="white", fg="black")
        botao_incluir = Button(self.frame_2, text="Incluir", bg="white", fg="black", command=self.incluir_spi)
        botao_incluir.place(relx=0.10, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_incluir.bind('<Enter>',btn_incluir_entrar)
        botao_incluir.bind('<Leave>',btn_incluir_sair)

        def btn_atualizar_entrar(event):
            botao_atualizar.configure(bg="yellow", fg="black")
        def btn_atualizar_sair(event):
            botao_atualizar.configure(bg="white", fg="black")
        botao_atualizar = Button(self.frame_2, text="Atualizar", bg="white", fg="black", command=self.atualizar_spi)
        botao_atualizar.place(relx=0.40, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_atualizar.bind('<Enter>',btn_atualizar_entrar)
        botao_atualizar.bind('<Leave>',btn_atualizar_sair)

        def btn_deletar_entrar(event):
            botao_deletar.configure(bg="red", fg="white")
        def btn_deletar_sair(event):
            botao_deletar.configure(bg="white", fg="black")
        botao_deletar = Button(self.frame_2, text="Deletar", bg="white", fg="black", command=self.deletar_spi)
        botao_deletar.place(relx=0.70, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_deletar.bind('<Enter>',btn_deletar_entrar)
        botao_deletar.bind('<Leave>',btn_deletar_sair)

        def btn_limpar_entrar(event):
            botao_limpar.configure(bg="orange", fg="black")
        def btn_limpar_sair(event):
            botao_limpar.configure(bg="white", fg="black")
        botao_limpar = Button(self.frame_2, text="Limpar", bg="white", fg="black", command=self.limpar_spi)
        botao_limpar.place(relx=0.10, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_limpar.bind('<Enter>',btn_limpar_entrar)
        botao_limpar.bind('<Leave>',btn_limpar_sair)

        def btn_home_entrar(event):
            botao_home.configure(bg="green", fg="white")
        def btn_home_sair(event):
            botao_home.configure(bg="white", fg="black")
        botao_home = Button(self.frame_2, text="HOME", bg="white", fg="black", command=self.home)
        botao_home.place(relx=0.40, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_home.bind('<Enter>',btn_home_entrar)
        botao_home.bind('<Leave>',btn_home_sair)

        def btn_ativar_entrar(event):
            botao_ativar.configure(bg="purple", fg="white")
        def btn_ativar_sair(event):
            botao_ativar.configure(bg="white", fg="black")
        botao_ativar = Button(self.frame_2, text="Ativar", bg="white", fg="black", command=self.ativar_spi)
        botao_ativar.place(relx=0.70, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_ativar.bind('<Enter>',btn_ativar_entrar)
        botao_ativar.bind('<Leave>',btn_ativar_sair)

        # frame 3
        self.criar_tv_spi()

        def btn_capturar_entrar(event):
            botao_capturar.configure(bg="pink", fg="black")
        def btn_capturar_sair(event):
            botao_capturar.configure(bg="white", fg="black")
        botao_capturar = Button(self.frame_3, text="Capturar", bg="black", fg="white", command=self.capturar_spi)
        botao_capturar.place(relx=0.30, rely=0.90, relheight=0.05, relwidth=0.40)
        botao_capturar.bind('<Enter>',btn_capturar_entrar)
        botao_capturar.bind('<Leave>',btn_capturar_sair)

    def on_select_spi_sub_produto(self, event):
        try:
            sub_produto = self.entry_spi_sub_produto.get(self.entry_spi_sub_produto.curselection())
            self.escolha_spi_sub_produto.configure(text=sub_produto, bg=self.cor_fundo_entry, fg="black")           
            sql = f"SELECT `id_sub_produto` FROM `sub_produtos` WHERE `sub_produto` = '{sub_produto}'"
            result = executa_DQL(sql)
            id_sub_produto = result[0][0]
            self.aviso_spi(sub_produto,id_sub_produto)
            self.criar_tv_spi()
        except:
            print(sql)
            messagebox.showinfo("erro",sql)

    def on_select_spi_sub_produto_origin(self, event):
        try:
            sub_produto = self.entry_spi_sub_produto.get(self.entry_spi_sub_produto.curselection())
            self.escolha_spi_sub_produto.configure(text=sub_produto, bg=self.cor_fundo_entry, fg="black")           
        except:
            pass

    def on_select_spi_insumo(self, event):
        try:
            self.escolha_spi_insumo.configure(text=self.entry_spi_insumo.get(self.entry_spi_insumo.curselection()), bg=self.cor_fundo_entry, fg="black")
        except:
            pass

    def capturar_spi(self):

        try:
            Item_Selecionado = self.tv_spi.selection()[0]
        except:
            messagebox.showinfo("ERRO","Precisa Selecionar um item.")
            return()
                                
        valores_selecionados = self.tv_spi.item(Item_Selecionado,"values")
        
        id_capturado = valores_selecionados[0]
        sub_produto_capturado = valores_selecionados[1]
        insumo_capturado = valores_selecionados[2]
        percentual_capturado = valores_selecionados[3]
        rendimento_capturado = valores_selecionados[3]

        self.entry_id_spi.configure(text=id_capturado)
        
        self.entry_spi_percentual.delete(0,END)
        self.entry_spi_percentual.insert(0,percentual_capturado)
        
        self.entry_spi_rendimento.delete(0,END)
        self.entry_spi_rendimento.insert(0,rendimento_capturado)

        sql = f"SELECT `id_insumo` FROM insumos WHERE `insumo` = '{insumo_capturado}'"
        result = executa_DQL(sql)
        id_insumo = result[0][0]
        
        sql = f"SELECT `id_sub_produto` FROM sub_produtos WHERE `sub_produto` = '{sub_produto_capturado}'"
        result = executa_DQL(sql)
        id_sub_produto = result[0][0]

        self.entry_spi_sub_produto.selection_clear(0,tk.END)
        self.entry_spi_sub_produto.selection_set(id_sub_produto)
        self.escolha_spi_sub_produto.configure(text=sub_produto_capturado, bg=self.cor_fundo_entry, fg="black")

        self.entry_spi_insumo.selection_clear(0,tk.END)
        self.entry_spi_insumo.selection_set(id_insumo)
        self.escolha_spi_insumo.configure(text=insumo_capturado, bg=self.cor_fundo_entry, fg="black")

        self.aviso_spi(sub_produto_capturado,id_sub_produto)

        return()

    def criar_tv_spi(self):
        self.tv_spi = ttk.Treeview(self.frame_3, columns=('id','sub_produto','insumo','percentual','rendimento','ativo'), show='headings')
        
        self.tv_spi.column('id', minwidth=0, width=4)
        self.tv_spi.column('sub_produto', minwidth=0, width=50)
        self.tv_spi.column('insumo', minwidth=0, width=150)
        self.tv_spi.column('percentual', minwidth=0, width=4)
        self.tv_spi.column('rendimento', minwidth=0, width=4)
        self.tv_spi.column('ativo', minwidth=0, width=4)
        
        self.tv_spi.heading('id', text="ID")
        self.tv_spi.heading('sub_produto', text="Sub Produto")
        self.tv_spi.heading('insumo', text="Insumo")
        self.tv_spi.heading('percentual', text="Percentual")
        self.tv_spi.heading('rendimento', text="Rendimento")
        self.tv_spi.heading('ativo', text="Ativo")      

        sub_produto_entry = self.escolha_spi_sub_produto.cget("text")

        if sub_produto_entry == 'escolher':
            sql = f"SELECT `id_sub_produto_x_insumo`,`sub_produto_id`,`insumo_id`,`percentual`,`rendimento`,`ativo` FROM `{self.tabela}`"
        else:
            sql = f"SELECT `id_sub_produto` FROM sub_produtos WHERE `sub_produto` = '{sub_produto_entry}'"
            result = executa_DQL(sql)
            id_sub_produto = result[0][0]            
            sql = f"SELECT `id_sub_produto_x_insumo`,`sub_produto_id`,`insumo_id`,`percentual`,`rendimento`,`ativo` FROM `{self.tabela}` WHERE `sub_produto_id` = '{id_sub_produto}'"

        result = executa_DQL(sql)

        for item_result in result:
            sql = f"SELECT `sub_produto` FROM `sub_produtos` WHERE `id_sub_produto` = '{item_result[1]}'"
            result = executa_DQL(sql)
            item_sub_produto = result[0][0]

            sql = f"SELECT `insumo` FROM `insumos` WHERE `id_insumo` = '{item_result[2]}'"
            result = executa_DQL(sql)
            item_insumo = result[0][0]

            self.tv_spi.insert("", item_result[0], values=(item_result[0], item_sub_produto, item_insumo, item_result[3], item_result[4], item_result[5]))

        self.tv_spi.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)
      
    def deletar_spi(self):
        id_entry = self.entry_id_spi.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        sub_produto_entry = self.escolha_spi_sub_produto.cget("text")
        if len(sub_produto_entry)==0 or sub_produto_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Sub Produto precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_sub_produto` FROM sub_produtos WHERE `sub_produto` = '{sub_produto_entry}'"
        result = executa_DQL(sql)
        id_sub_produto = result[0][0]

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '0' WHERE id_sub_produto_x_insumo = {id_entry};"
        result = executa_DML(sql)

        self.aviso_spi(sub_produto_entry,id_sub_produto)
        self.criar_tv_spi()
        self.limpar_spi()
        return()        

    def atualizar_spi(self):
        id_entry = self.entry_id_spi.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()

        insumo_entry = self.escolha_spi_insumo.cget("text")
        if len(insumo_entry) == 0 or insumo_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Insumos precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_insumo` FROM insumos WHERE `insumo` = '{insumo_entry}'"
        result = executa_DQL(sql)
        id_insumo = result[0][0]

        sub_produto_entry = self.escolha_spi_sub_produto.cget("text")
        if len(sub_produto_entry)==0 or sub_produto_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Sub Produto precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_sub_produto` FROM sub_produtos WHERE `sub_produto` = '{sub_produto_entry}'"
        result = executa_DQL(sql)
        id_sub_produto = result[0][0]

        percentual = self.entry_spi_percentual.get()
        percentual = percentual.replace(",",".")
        
        if len(self.entry_spi_percentual.get()) == 0:
            messagebox.showinfo("Em branco","Campo percentual precisa ser preenchido.")
            return()

        try:
            percentual = float(percentual)
        except:
            messagebox.showinfo("ERRO","Campo percentual não válido.")
            return()

        rendimento = self.entry_spi_rendimento.get()
        rendimento = rendimento.replace(",",".")
        
        if len(self.entry_spi_rendimento.get()) == 0:
            messagebox.showinfo("Em branco","Campo rendimento precisa ser preenchido.")
            return()

        try:
            rendimento = float(rendimento)
        except:
            messagebox.showinfo("ERRO","Campo rendimento não válido.")
            return()

        sql = f"UPDATE `{self.tabela}` SET `sub_produto_id` = '{id_sub_produto}', `insumo_id` = '{id_insumo}', `percentual`='{percentual}', `rendimento`='{rendimento}'  WHERE `id_sub_produto_x_insumo` = {id_entry};"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo("ERRO","O registro não foi atualizado.")
            print(sql)
            return()          

        self.aviso_spi(sub_produto_entry,id_sub_produto)
        self.criar_tv_spi()
        self.limpar_spi()
        return()

    def incluir_spi(self):
   
        insumo_entry = self.escolha_spi_insumo.cget("text")
        if len(insumo_entry) == 0 or insumo_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Insumos precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_insumo` FROM insumos WHERE `insumo` = '{insumo_entry}'"
        result = executa_DQL(sql)
        id_insumo = result[0][0]

        sub_produto_entry = self.escolha_spi_sub_produto.cget("text")
        if len(sub_produto_entry)==0 or sub_produto_entry == 'escolher':
            messagebox.showinfo("ERRO",f"sub produtos precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_sub_produto` FROM sub_produtos WHERE `sub_produto` = '{sub_produto_entry}'"
        result = executa_DQL(sql)
        id_sub_produto = result[0][0]

        percentual = self.entry_spi_percentual.get()
        percentual = percentual.replace(",",".")
        
        if len(self.entry_spi_percentual.get()) == 0:
            messagebox.showinfo("Em branco","Campo percentual precisa ser preenchido.")
            return()

        try:
            percentual = float(percentual)
        except:
            messagebox.showinfo("ERRO","Campo percentual não válido.")
            return()

        rendimento = self.entry_spi_rendimento.get()
        rendimento = rendimento.replace(",",".")
        
        if len(self.entry_spi_rendimento.get()) == 0:
            messagebox.showinfo("Em branco","Campo rendimento precisa ser preenchido.")
            return()

        try:
            rendimento = float(rendimento)
        except:
            messagebox.showinfo("ERRO","Campo rendimento não válido.")
            return()

        sql = f"INSERT INTO {self.tabela} (sub_produto_id, insumo_id, percentual, rendimento, ativo) VALUES ('{id_sub_produto}','{id_insumo}','{percentual}','{rendimento}','1');"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo(title="ERRO", message=f"Algo deu errado com o banco de dados. {sql}")
            return()

        self.aviso_spi(sub_produto_entry,id_sub_produto)
        self.criar_tv_spi()
        self.limpar_spi()
        return()

    def limpar_spi(self):
        print('chegou em limpar')        

        self.entry_spi_rendimento.delete(0,END)
        self.entry_spi_rendimento.insert(0,100)

        self.entry_id_spi.configure(text="novo")

        self.entry_spi_sub_produto.selection_clear(0,tk.END)
        self.escolha_spi_sub_produto.configure(text="escolher", bg="white", fg="red")
        self.on_select_spi_sub_produto_origin(Event)

        self.entry_spi_insumo.selection_clear(0,tk.END)
        self.escolha_spi_insumo.configure(text="escolher", bg="white", fg="red")
        self.on_select_spi_insumo(Event)

        self.entry_spi_percentual.delete(0,END)
        self.entry_spi_percentual.focus()

    def ativar_spi(self):
        id_entry = self.entry_id_spi.cget("text")

        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        sub_produto_entry = self.escolha_spi_sub_produto.cget("text")
        if len(sub_produto_entry)==0 or sub_produto_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Insumos precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_sub_produto` FROM sub_produtos WHERE `sub_produto` = '{sub_produto_entry}'"
        result = executa_DQL(sql)
        id_sub_produto = result[0][0]

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '1' WHERE id_sub_produto_x_insumo = {id_entry};"
        result = executa_DML(sql)

        self.aviso_spi(sub_produto_entry,id_sub_produto)
        self.criar_tv_spi()
        self.limpar_spi()
        return()


    def produtos(self):
        self.tabela = "produtos"
        abc = self.listagem_tipos_produtos()

        self.lista_ids_tipos_produtos = abc[0]
        self.lista_tipos_produtos = abc[1]

        if len(self.lista_ids_tipos_produtos) == 0:
            messagebox.showinfo("Faltam dados","Tipos de Produtos necessita(m) de algu(ns) dado(s).")
            self.home()
        
        self.apagar_widgets_frame_3()

        # frame_1
        self.label_frame_1.configure(text="Produtos")

        # frame 2
        self.apagar_widgets_frame_2()
        
        qtde_labels_e_entrys = 5
        adicional_tamanhos_listbox = 3
        margem_superior = ((1-self.espaco_para_botoes)-((qtde_labels_e_entrys*2+adicional_tamanhos_listbox)*self.altura_campos)-(qtde_labels_e_entrys*self.espaco_interno)-((qtde_labels_e_entrys-1)*self.espaco_externo))/2

        self.label_id_pro = Label(self.frame_2, text="ID", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_id_pro.place(relx=0.05, rely=margem_superior, relwidth=0.90, relheight=self.altura_campos)

        self.entry_id_pro = Label(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, text="novo")
        self.entry_id_pro.place(relx=0.05, rely=margem_superior + self.altura_campos + self.espaco_interno, relwidth=0.90, relheight=self.altura_campos)
        
        self.label_pro = Label(self.frame_2, text="produto", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_pro.place(relx=0.05, rely=margem_superior + 2*self.altura_campos + self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_pro = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_pro.place(relx=0.05, rely=margem_superior + 3*self.altura_campos + 2*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_pro_tipo_produto = Label(self.frame_2, text="tipo de produto", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_pro_tipo_produto.place(relx=0.05, rely=margem_superior + 4*self.altura_campos + 2*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_pro_tipo_produto = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox)

        indice = 0        
        for id in self.lista_ids_tipos_produtos:
            tipo_produto = self.lista_tipos_produtos[indice]
            self.entry_pro_tipo_produto.insert(id,tipo_produto)
            indice += 1

        self.scbar_pro_tipo_produto = Scrollbar(self.entry_pro_tipo_produto, orient=VERTICAL)
        self.scbar_pro_tipo_produto.config(command=self.entry_pro_tipo_produto.yview)
        self.scbar_pro_tipo_produto.pack(side=RIGHT, fill=Y)       

        self.entry_pro_tipo_produto.configure(yscrollcommand=self.scbar_pro_tipo_produto.set)
        self.entry_pro_tipo_produto.place(relx=0.05, rely=margem_superior + 5*self.altura_campos + 3*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_pro_tipo_produto.bind('<<ListboxSelect>>',self.on_select_pro_tipo_produto)

        self.escolha_pro_tipo_produto = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_pro_tipo_produto.place(relx=0.05, rely=margem_superior + 9*self.altura_campos + 4*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_pro_nome_cardapio = Label(self.frame_2, text="nome para o cardápio", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_pro_nome_cardapio.place(relx=0.05, rely=margem_superior + 10*self.altura_campos + 4*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_pro_nome_cardapio = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_pro_nome_cardapio.place(relx=0.05, rely=margem_superior + 11*self.altura_campos + 5*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_pro_descricao_cardapio = Label(self.frame_2, text="descrição do produto no cardápio", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_pro_descricao_cardapio.place(relx=0.05, rely=margem_superior + 12*self.altura_campos + 5*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_pro_descricao_cardapio = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_pro_descricao_cardapio.place(relx=0.05, rely=margem_superior + 13*self.altura_campos + 6*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        def btn_incluir_entrar(event):
            botao_incluir.configure(bg="blue", fg="white")
        def btn_incluir_sair(event):
            botao_incluir.configure(bg="white", fg="black")
        botao_incluir = Button(self.frame_2, text="Incluir", bg="white", fg="black", command=self.incluir_pro)
        botao_incluir.place(relx=0.10, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_incluir.bind('<Enter>',btn_incluir_entrar)
        botao_incluir.bind('<Leave>',btn_incluir_sair)

        def btn_atualizar_entrar(event):
            botao_atualizar.configure(bg="yellow", fg="black")
        def btn_atualizar_sair(event):
            botao_atualizar.configure(bg="white", fg="black")
        botao_atualizar = Button(self.frame_2, text="Atualizar", bg="white", fg="black", command=self.atualizar_pro)
        botao_atualizar.place(relx=0.40, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_atualizar.bind('<Enter>',btn_atualizar_entrar)
        botao_atualizar.bind('<Leave>',btn_atualizar_sair)

        def btn_deletar_entrar(event):
            botao_deletar.configure(bg="red", fg="white")
        def btn_deletar_sair(event):
            botao_deletar.configure(bg="white", fg="black")
        botao_deletar = Button(self.frame_2, text="Deletar", bg="white", fg="black", command=self.deletar_pro)
        botao_deletar.place(relx=0.70, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_deletar.bind('<Enter>',btn_deletar_entrar)
        botao_deletar.bind('<Leave>',btn_deletar_sair)

        def btn_limpar_entrar(event):
            botao_limpar.configure(bg="orange", fg="black")
        def btn_limpar_sair(event):
            botao_limpar.configure(bg="white", fg="black")
        botao_limpar = Button(self.frame_2, text="Limpar", bg="white", fg="black", command=self.limpar_pro)
        botao_limpar.place(relx=0.10, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_limpar.bind('<Enter>',btn_limpar_entrar)
        botao_limpar.bind('<Leave>',btn_limpar_sair)

        def btn_home_entrar(event):
            botao_home.configure(bg="green", fg="white")
        def btn_home_sair(event):
            botao_home.configure(bg="white", fg="black")
        botao_home = Button(self.frame_2, text="HOME", bg="white", fg="black", command=self.home)
        botao_home.place(relx=0.40, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_home.bind('<Enter>',btn_home_entrar)
        botao_home.bind('<Leave>',btn_home_sair)

        def btn_ativar_entrar(event):
            botao_ativar.configure(bg="purple", fg="white")
        def btn_ativar_sair(event):
            botao_ativar.configure(bg="white", fg="black")
        botao_ativar = Button(self.frame_2, text="Ativar", bg="white", fg="black", command=self.ativar_pro)
        botao_ativar.place(relx=0.70, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_ativar.bind('<Enter>',btn_ativar_entrar)
        botao_ativar.bind('<Leave>',btn_ativar_sair)

        # frame 3
        self.apagar_widgets_frame_3()
        self.criar_tv_pro()

        def btn_capturar_entrar(event):
            botao_capturar.configure(bg="pink", fg="black")
        def btn_capturar_sair(event):
            botao_capturar.configure(bg="white", fg="black")
        botao_capturar = Button(self.frame_3, text="Capturar", bg="black", fg="white", command=self.capturar_pro)
        botao_capturar.place(relx=0.30, rely=0.90, relheight=0.05, relwidth=0.40)
        botao_capturar.bind('<Enter>',btn_capturar_entrar)
        botao_capturar.bind('<Leave>',btn_capturar_sair)

    def on_select_pro_tipo_produto(self, event):
        try:
            self.escolha_pro_tipo_produto.configure(text=self.entry_pro_tipo_produto.get(self.entry_pro_tipo_produto.curselection()), bg=self.cor_fundo_entry, fg="black")
        except:
            pass

    def capturar_pro(self):
        
        try:
            Item_Selecionado = self.tv_pro.selection()[0]
        except:
            messagebox.showinfo("ERRO","Precisa Selecionar um item.")
            return()
        
        valores_selecionados = self.tv_pro.item(Item_Selecionado,"values")
        
        id_capturado = valores_selecionados[0]
        produto_capturado = valores_selecionados[1]
        tipo_produto_capturado = valores_selecionados[2]
        nome_cardapio_capturado = valores_selecionados[3]
        descricao_cardapio_capturado = valores_selecionados[4]

        self.entry_pro_descricao_cardapio.delete(0,END)
        self.entry_pro_descricao_cardapio.insert(0,descricao_cardapio_capturado)

        self.entry_pro_nome_cardapio.delete(0,END)
        self.entry_pro_nome_cardapio.insert(0,nome_cardapio_capturado)

        self.entry_id_pro.configure(text=id_capturado)

        self.entry_pro.delete(0,END)
        self.entry_pro.insert(0, produto_capturado)

        indice = 0
        for item in self.lista_tipos_produtos:
            if tipo_produto_capturado == item:
                indice_tipo_produto = self.lista_ids_tipos_produtos[indice]
            indice += 1

        self.entry_pro_tipo_produto.selection_clear(0,tk.END)
        self.entry_pro_tipo_produto.selection_set(indice_tipo_produto)
        self.escolha_pro_tipo_produto.configure(text=tipo_produto_capturado, bg=self.cor_fundo_entry, fg="black")
       
    def criar_tv_pro(self):
        self.tv_pro = ttk.Treeview(self.frame_3, columns=('id','produto','tipo_produto','nome_cardapio','descricao_cardapio','ativo'), show='headings')
        self.tv_pro.column('id', minwidth=0, width=5)
        self.tv_pro.column('produto', minwidth=0, width=50)
        self.tv_pro.column('tipo_produto', minwidth=0, width=50)
        self.tv_pro.column('nome_cardapio', minwidth=0, width=100)
        self.tv_pro.column('descricao_cardapio', minwidth=0, width=100)
        self.tv_pro.column('ativo', minwidth=0, width=4)
        
        self.tv_pro.heading('id', text="ID")
        self.tv_pro.heading('produto', text="Produto")
        self.tv_pro.heading('tipo_produto', text="Tipo Produto")
        self.tv_pro.heading('nome_cardapio', text="Nome no Cardápio")
        self.tv_pro.heading('descricao_cardapio', text="Descrição Cardápio")
        self.tv_pro.heading('ativo', text="Ativo")      

        sql = f"SELECT `id_produto`,`produto`,`tipo_produto_id`,`nome_cardapio`,`descricao_cardapio`,`ativo` FROM {self.tabela}"
        result = executa_DQL(sql)
        
        for item in result:
            sql = F"SELECT tipo_produto FROM tipos_produtos WHERE id_tipo_produto = '{item[2]}'"
            rslt = executa_DQL(sql)
            tipo_produto = rslt[0][0]
            self.tv_pro.insert("", END, values=(item[0], item[1], tipo_produto, item[3], item[4], item[5]))
          
        self.tv_pro.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

    def deletar_pro(self):
        id_entry = self.entry_id_pro.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '0' WHERE id_produto = {id_entry};"
        #sql = f"DELETE FROM `{self.tabela}` WHERE (`id_proumo` = '{id_entry}');"
        result = executa_DML(sql)
        self.criar_tv_pro()
        self.limpar_pro()
        return()        

    def atualizar_pro(self):
        id_entry = self.entry_id_pro.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        
        id_entry = int(id_entry)
        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID tipo: {type(id_entry)}.")
            return()

        produto_entry = self.entry_pro.get()
        
        if len(produto_entry) == 0:
            messagebox.showinfo("ERRO",f"Produto precisa ser preenchido.")
            return()

        nome_cardapio_entry = self.entry_pro_nome_cardapio.get()
        if len(nome_cardapio_entry) == 0:
            messagebox.showinfo("ERRO",f"Nome do Cardápio precisa ser preenchido.")
            return()

        descricao_cardapio_entry = self.entry_pro_descricao_cardapio.get()
        if len(descricao_cardapio_entry) == 0:
            messagebox.showinfo("ERRO",f"Descrição do Cardápio precisa ser preenchido.")
            return()

        tipo_produto_entry = self.escolha_pro_tipo_produto.cget("text")
        if len(tipo_produto_entry) == 0:
            messagebox.showinfo("ERRO",f"Precisa escolher um tipo de produto para o produto.")
            return()

        sql = f"SELECT `id_tipo_produto` FROM tipos_produtos WHERE `tipo_produto` = '{tipo_produto_entry}'"
        result = executa_DQL(sql)
        id_tipo_produto = result[0][0]

        sql = f"UPDATE `{self.tabela}` SET produto = '{produto_entry}', tipo_produto_id = '{id_tipo_produto}', nome_cardapio = '{nome_cardapio_entry}', descricao_cardapio = '{descricao_cardapio_entry}' WHERE id_produto = {id_entry};"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo("ERRO","O registro não foi atualizado.")
            return()          
        
        self.criar_tv_pro()
        self.limpar_pro()
        return()

    def incluir_pro(self):
        
        entry_produto = self.entry_pro.get()
        nome_cardapio_entry = self.entry_pro_nome_cardapio.get()
        if len(nome_cardapio_entry) == 0:
            messagebox.showinfo("ERRO",f"Nome do Cardápio precisa ser preenchido.")
            return()

        descricao_cardapio_entry = self.entry_pro_descricao_cardapio.get()
        if len(descricao_cardapio_entry) == 0:
            messagebox.showinfo("ERRO",f"Descrição do Cardápio precisa ser preenchido.")
            return()

        tipo_produto_entry = self.escolha_pro_tipo_produto.cget("text")
        if len(tipo_produto_entry) == 0 or tipo_produto_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Precisa escolher um tipo de produto para o produto.")
            return()

        sql = f"SELECT `id_tipo_produto` FROM tipos_produtos WHERE `tipo_produto` = '{tipo_produto_entry}'"
        result = executa_DQL(sql)
        id_tipo_produto = result[0][0]

        if len(entry_produto) == 0:
            messagebox.showinfo("Em branco","Campo produto precisa ser preenchido.")
            return()

        sql = f"INSERT INTO {self.tabela} (produto, tipo_produto_id, nome_cardapio, descricao_cardapio, ativo) VALUES ('{entry_produto}','{id_tipo_produto}','{nome_cardapio_entry}','{descricao_cardapio_entry}','1');"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo(title="ERRO", message=f"Algo deu errado com o banco de dados. {sql}")
            print(sql)
            return()

        sql = f"INSERT INTO {self.tabela} (produto, tipo_produto_id, nome_cardapio, descricao_cardapio, ativo) VALUES ('{entry_produto}','{id_tipo_produto}','{nome_cardapio_entry}','{descricao_cardapio_entry}','1');"
        result = executa_DML(sql)

        sql = f"SELECT `id_produto` FROM `produtos` WHERE `produto` = '{entry_produto}'"
        result = executa_DQL(sql)
        produto_id = result[0][0]

        sql = f"INSERT INTO `produtos_mo` ('produto_id','tempo_min_grau_1_mo','tempo_min_grau_2_mo','tempo_min_grau_3_mo','cpmo','ativo') VALUES ('{produto_id}','0.0','0.0','0.0','0.0','1');"
        result = executa_DML(sql)

        sql = f"INSERT INTO `centro_custos_produto` ('produto_id','total_cip','total_cfpr','total_cpfp','total_cpmo','total_cel','pv') VALUES ('{produto_id}','0.0','0.0','0.0','0.0','0.0','0.0');"
        result = executa_DML(sql)

        self.criar_tv_pro()
        self.limpar_pro()
        return()

    def limpar_pro(self):
        self.entry_pro.delete(0,END)
        self.entry_id_pro.configure(text="novo")

        self.entry_pro_tipo_produto.selection_clear(0,tk.END)
        self.escolha_pro_tipo_produto.configure(text="escolher", bg="white", fg="red")
        self.on_select_pro_tipo_produto(Event)

        self.entry_pro_nome_cardapio.delete(0,END)
        self.entry_pro_descricao_cardapio.delete(0,END)

        self.entry_pro.focus()

    def ativar_pro(self):
        id_entry = self.entry_id_pro.cget("text")

        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '1' WHERE id_produto = {id_entry};"
        result = executa_DML(sql)
        self.criar_tv_pro()
        self.limpar_pro()
        return()


    def harmonizacao(self):
        self.tabela = "harmonizacoes"
        abc = self.listagem_produtos()

        self.lista_ids_produtos = abc[0]
        self.lista_produtos = abc[1]

        if len(self.lista_ids_produtos) == 0:
            messagebox.showinfo("Faltam dados","Produtos necessitam de algu(ns) dado(s).")
            self.home()
        
        self.apagar_widgets_frame_2()
        self.apagar_widgets_frame_3()

        # frame_1
        self.label_frame_1.configure(text="Harmonizações")

        # frame 2
        self.apagar_widgets_frame_2()
        
        qtde_labels_e_entrys = 3
        
        adicional_tamanhos_listbox = 6
        margem_superior = ((1-self.espaco_para_botoes)-((qtde_labels_e_entrys*2+adicional_tamanhos_listbox)*self.altura_campos)-(qtde_labels_e_entrys*self.espaco_interno)-((qtde_labels_e_entrys-1)*self.espaco_externo))/2

        self.label_id_har = Label(self.frame_2, text="ID", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_id_har.place(relx=0.05, rely=margem_superior, relwidth=0.90, relheight=self.altura_campos)

        self.entry_id_har = Label(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, text="novo")
        self.entry_id_har.place(relx=0.05, rely=margem_superior + self.altura_campos + self.espaco_interno, relwidth=0.90, relheight=self.altura_campos)

        self.label_har_produto_1 = Label(self.frame_2, text="produto 1", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_har_produto_1.place(relx=0.05, rely=margem_superior + 2*self.altura_campos + 1*self.espaco_interno + 1*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_har_produto_1 = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox)

        indice = 0
        
        for id in self.lista_ids_produtos:
            produto = self.lista_produtos[indice]
            self.entry_har_produto_1.insert(id,produto)
            indice += 1

        self.scbar_har_produto_1 = Scrollbar(self.entry_har_produto_1, orient=VERTICAL)
        self.scbar_har_produto_1.config(command=self.entry_har_produto_1.yview)
        self.scbar_har_produto_1.pack(side=RIGHT, fill=Y)       

        self.entry_har_produto_1.configure(yscrollcommand=self.scbar_har_produto_1.set)
        self.entry_har_produto_1.place(relx=0.05, rely=margem_superior + 3*self.altura_campos + 2*self.espaco_interno + 1*self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_har_produto_1.bind('<<ListboxSelect>>',self.on_select_har_produto_1)

        self.escolha_har_produto_1 = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_har_produto_1.place(relx=0.05, rely=margem_superior + 7*self.altura_campos + 3*self.espaco_interno + 1*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_har_produto_2 = Label(self.frame_2, text="produto 1", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_har_produto_2.place(relx=0.05, rely=margem_superior + 8*self.altura_campos + 3*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_har_produto_2 = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox)

        indice = 0
        
        for id in self.lista_ids_produtos:
            produto = self.lista_produtos[indice]
            self.entry_har_produto_2.insert(id,produto)
            indice += 1

        self.scbar_har_produto_2 = Scrollbar(self.entry_har_produto_2, orient=VERTICAL)
        self.scbar_har_produto_2.config(command=self.entry_har_produto_2.yview)
        self.scbar_har_produto_2.pack(side=RIGHT, fill=Y)       

        self.entry_har_produto_2.configure(yscrollcommand=self.scbar_har_produto_2.set)
        self.entry_har_produto_2.place(relx=0.05, rely=margem_superior + 9*self.altura_campos + 2*self.espaco_interno + 1*self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_har_produto_2.bind('<<ListboxSelect>>',self.on_select_har_produto_2)

        self.escolha_har_produto_2 = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_har_produto_2.place(relx=0.05, rely=margem_superior + 13*self.altura_campos + 3*self.espaco_interno + 1*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
       
        def btn_incluir_entrar(event):
            botao_incluir.configure(bg="blue", fg="white")
        def btn_incluir_sair(event):
            botao_incluir.configure(bg="white", fg="black")
        botao_incluir = Button(self.frame_2, text="Incluir", bg="white", fg="black", command=self.incluir_har)
        botao_incluir.place(relx=0.10, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_incluir.bind('<Enter>',btn_incluir_entrar)
        botao_incluir.bind('<Leave>',btn_incluir_sair)

        def btn_atualizar_entrar(event):
            botao_atualizar.configure(bg="yellow", fg="black")
        def btn_atualizar_sair(event):
            botao_atualizar.configure(bg="white", fg="black")
        botao_atualizar = Button(self.frame_2, text="Atualizar", bg="white", fg="black", command=self.atualizar_har)
        botao_atualizar.place(relx=0.40, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_atualizar.bind('<Enter>',btn_atualizar_entrar)
        botao_atualizar.bind('<Leave>',btn_atualizar_sair)

        def btn_deletar_entrar(event):
            botao_deletar.configure(bg="red", fg="white")
        def btn_deletar_sair(event):
            botao_deletar.configure(bg="white", fg="black")
        botao_deletar = Button(self.frame_2, text="Deletar", bg="white", fg="black", command=self.deletar_har)
        botao_deletar.place(relx=0.70, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_deletar.bind('<Enter>',btn_deletar_entrar)
        botao_deletar.bind('<Leave>',btn_deletar_sair)

        def btn_limpar_entrar(event):
            botao_limpar.configure(bg="orange", fg="black")
        def btn_limpar_sair(event):
            botao_limpar.configure(bg="white", fg="black")
        botao_limpar = Button(self.frame_2, text="Limpar", bg="white", fg="black", command=self.limpar_har)
        botao_limpar.place(relx=0.10, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_limpar.bind('<Enter>',btn_limpar_entrar)
        botao_limpar.bind('<Leave>',btn_limpar_sair)

        def btn_home_entrar(event):
            botao_home.configure(bg="green", fg="white")
        def btn_home_sair(event):
            botao_home.configure(bg="white", fg="black")
        botao_home = Button(self.frame_2, text="HOME", bg="white", fg="black", command=self.home)
        botao_home.place(relx=0.40, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_home.bind('<Enter>',btn_home_entrar)
        botao_home.bind('<Leave>',btn_home_sair)

        def btn_ativar_entrar(event):
            botao_ativar.configure(bg="purple", fg="white")
        def btn_ativar_sair(event):
            botao_ativar.configure(bg="white", fg="black")
        botao_ativar = Button(self.frame_2, text="Ativar", bg="white", fg="black", command=self.ativar_har)
        botao_ativar.place(relx=0.70, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_ativar.bind('<Enter>',btn_ativar_entrar)
        botao_ativar.bind('<Leave>',btn_ativar_sair)

        # frame 3
        self.apagar_widgets_frame_3()
        self.criar_tv_har()

        def btn_capturar_entrar(event):
            botao_capturar.configure(bg="pink", fg="black")
        def btn_capturar_sair(event):
            botao_capturar.configure(bg="white", fg="black")
        botao_capturar = Button(self.frame_3, text="Capturar", bg="black", fg="white", command=self.capturar_har)
        botao_capturar.place(relx=0.30, rely=0.90, relheight=0.05, relwidth=0.40)
        botao_capturar.bind('<Enter>',btn_capturar_entrar)
        botao_capturar.bind('<Leave>',btn_capturar_sair)

    def on_select_har_produto_1(self, event):
        try:
            self.escolha_har_produto_1.configure(text=self.entry_har_produto_1.get(self.entry_har_produto_1.curselection()), bg=self.cor_fundo_entry, fg="black")
        except:
            pass

    def on_select_har_produto_2(self, event):
        try:
            self.escolha_har_produto_2.configure(text=self.entry_har_produto_2.get(self.entry_har_produto_2.curselection()), bg=self.cor_fundo_entry, fg="black")
        except:
            pass

    def capturar_har(self):
        try:
            Item_Selecionado = self.tv_har.selection()[0]
        except:
            messagebox.showinfo("ERRO","Precisa Selecionar um item.")
            return()
        
        valores_selecionados = self.tv_har.item(Item_Selecionado,"values")

        id_capturado = valores_selecionados[0]
        produto_1_capturado = valores_selecionados[1]
        produto_2_capturado = valores_selecionados[2]        

        self.entry_id_har.configure(text=id_capturado)

        indice = 0
        for item in self.lista_produtos:
            if produto_1_capturado == item:
                indice_produto_1 = self.lista_ids_produtos[indice]
            indice += 1

        self.entry_har_produto_1.selection_clear(0,tk.END)
        self.entry_har_produto_1.selection_set(indice_produto_1)
        self.escolha_har_produto_1.configure(text=self.entry_har_produto_1.get(self.entry_har_produto_1.curselection()), bg=self.cor_fundo_entry, fg="black")

        indice = 0
        for item in self.lista_produtos:
            if produto_2_capturado == item:
                indice_produto_2 = self.lista_ids_produtos[indice]
            indice += 1

        self.entry_har_produto_2.selection_clear(0,tk.END)
        self.entry_har_produto_2.selection_set(indice_produto_2)
        self.escolha_har_produto_2.configure(text=self.entry_har_produto_2.get(self.entry_har_produto_2.curselection()), bg=self.cor_fundo_entry, fg="black")

    def criar_tv_har(self):

        self.tv_har = ttk.Treeview(self.frame_3, columns=('id','produto_1','produto_2','ativo'), show='headings')
        self.tv_har.column('id', minwidth=0, width=10)
        self.tv_har.column('produto_1', minwidth=0, width=50)
        self.tv_har.column('produto_2', minwidth=0, width=50)
        self.tv_har.column('ativo', minwidth=0, width=10)
        
        self.tv_har.heading('id', text="ID")
        self.tv_har.heading('produto_1', text="Produto 1")
        self.tv_har.heading('produto_2', text="Produto 2")
        self.tv_har.heading('ativo', text="ativo")

        sql = f"SELECT `id_harmonizacao`,`produto_id_1`,`produto_id_2`,`ativo` FROM {self.tabela}"
        result = executa_DQL(sql)

        for item_result in result:
            
            sql = f"SELECT `produto` FROM `produtos` WHERE `id_produto` = '{item_result[1]}'"
            result = executa_DQL(sql)
            produto_1 = result[0][0]

            sql = f"SELECT `produto` FROM `produtos` WHERE `id_produto` = '{item_result[2]}'"
            result = executa_DQL(sql)
            produto_2 = result[0][0]

            self.tv_har.insert("", item_result[0], values=(item_result[0], produto_1, produto_2, item_result[3]))                  

        self.tv_har.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

    def deletar_har(self):

        id_entry = self.entry_id_har.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        
        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()
  
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '0' WHERE id_harmonizacao = {id_entry};"
        result = executa_DML(sql)
        self.criar_tv_har()
        self.limpar_har()
        return()        

    def atualizar_har(self):
        id_entry = self.entry_id_har.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()

        id_entry = int(id_entry)

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID tipo: {type(id_entry)}.")
            return()

        produto_1_entry = self.escolha_har_produto_1.cget("text")
        if len(produto_1_entry) == 0:
            messagebox.showinfo("ERRO",f"Produto 1 precisa ser escolhido.")
            return()

        produto_2_entry = self.escolha_har_produto_2.cget("text")
        if len(produto_2_entry) == 0:
            messagebox.showinfo("ERRO",f"Produto 2 precisa ser escolhido.")
            return()

        if produto_1_entry == produto_2_entry:
            messagebox.showinfo("ERRO",f"Produtos precisam ser diferentes para harmonizarem.")
            return()
        
        sql = f"SELECT id_produto FROM produtos WHERE produto = '{produto_1_entry}'"
        result = executa_DQL(sql)
        prod_1_id = result[0][0]

        sql = f"SELECT id_produto FROM produtos WHERE produto = '{produto_2_entry}'"
        result = executa_DQL(sql)
        prod_2_id = result[0][0]
         
        sql = f"UPDATE `{self.tabela}` SET produto_id_1 = '{prod_1_id}', produto_id_2 = '{prod_2_id}' WHERE id_harmonizacao = {id_entry};"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo("ERRO","O registro não foi atualizado.")
            print(sql)
            return()          
        
        self.criar_tv_har()
        self.limpar_har()
        return()

    def incluir_har(self):
        produto_1_entry = self.escolha_har_produto_1.cget("text")
        if len(produto_1_entry) == 0:
            messagebox.showinfo("ERRO",f"Produto 1 precisa ser escolhido.")
            return()

        produto_2_entry = self.escolha_har_produto_2.cget("text")
        if len(produto_2_entry) == 0:
            messagebox.showinfo("ERRO",f"Produto 2 precisa ser escolhido.")
            return()

        if produto_1_entry == produto_2_entry:
            messagebox.showinfo("ERRO",f"Produtos precisam ser diferentes para harmonizarem.")
            return()
        
        sql = f"SELECT id_produto FROM produtos WHERE produto = '{produto_1_entry}'"
        result = executa_DQL(sql)
        prod_1_id = result[0][0]

        sql = f"SELECT id_produto FROM produtos WHERE produto = '{produto_2_entry}'"
        result = executa_DQL(sql)
        prod_2_id = result[0][0]

        sql = f"INSERT INTO {self.tabela} (produto_id_1, produto_id_2, ativo) VALUES ('{prod_1_id}','{prod_2_id}','1')"
        result = executa_DML(sql)

        if result == False:
            print(sql)
            messagebox.showinfo(title="ERRO", message="Algo deu errado com o banco de dados.")
            return()

        self.criar_tv_har()
        self.limpar_har()
        return()

    def limpar_har(self):
        
        self.entry_har_produto_1.selection_clear(0,tk.END)
        self.escolha_har_produto_1.configure(text="escolher", bg="white", fg="red")
        self.on_select_har_produto_1(Event)

        self.entry_har_produto_2.selection_clear(0,tk.END)
        self.escolha_har_produto_2.configure(text="escolher", bg="white", fg="red")
        self.on_select_har_produto_2(Event)

    def ativar_har(self):
        id_entry = self.entry_id_har.cget("text")

        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()
        
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '1' WHERE id_harmonizacao = {id_entry};"
        result = executa_DML(sql)
        self.criar_tv_har()
        self.limpar_har()
        return()


    def tipos_sub_produtos(self):
        self.tabela = "tipos_sub_produtos"
        
        # frame_1
        self.label_frame_1.configure(text="Tipos de Sub Produtos")

        # frame 2
        self.apagar_widgets_frame_2()
        
        qtde_labels_e_entrys = 2
       
        adicional_tamanhos_listbox = 0
        margem_superior = ((1-self.espaco_para_botoes)-((qtde_labels_e_entrys*2+adicional_tamanhos_listbox)*self.altura_campos)-(qtde_labels_e_entrys*self.espaco_interno)-((qtde_labels_e_entrys-1)*self.espaco_externo))/2

        self.label_id_tsp = Label(self.frame_2, text="ID", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_id_tsp.place(relx=0.05, rely=margem_superior, relwidth=0.90, relheight=self.altura_campos)

        self.entry_id_tsp = Label(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, text="novo")
        self.entry_id_tsp.place(relx=0.05, rely=margem_superior + self.altura_campos + self.espaco_interno, relwidth=0.90, relheight=self.altura_campos)
        
        self.label_tsp = Label(self.frame_2, text="tipo de sub produtos", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_tsp.place(relx=0.05, rely=margem_superior + 2*self.altura_campos + self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_tsp = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_tsp.place(relx=0.05, rely=margem_superior + 3*self.altura_campos + 2*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_tsp_markup = Label(self.frame_2, text="markup mínimo do Tipo de Sub Produto", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_tsp_markup.place(relx=0.05, rely=margem_superior + 4*self.altura_campos + 2*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_tsp_markup = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_tsp_markup.place(relx=0.05, rely=margem_superior + 5*self.altura_campos + 3*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        def btn_incluir_entrar(event):
            botao_incluir.configure(bg="blue", fg="white")
        def btn_incluir_sair(event):
            botao_incluir.configure(bg="white", fg="black")
        botao_incluir = Button(self.frame_2, text="Incluir", bg="white", fg="black", command=self.incluir_tsp)
        botao_incluir.place(relx=0.10, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_incluir.bind('<Enter>',btn_incluir_entrar)
        botao_incluir.bind('<Leave>',btn_incluir_sair)

        def btn_atualizar_entrar(event):
            botao_atualizar.configure(bg="yellow", fg="black")
        def btn_atualizar_sair(event):
            botao_atualizar.configure(bg="white", fg="black")
        botao_atualizar = Button(self.frame_2, text="Atualizar", bg="white", fg="black", command=self.atualizar_tsp)
        botao_atualizar.place(relx=0.40, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_atualizar.bind('<Enter>',btn_atualizar_entrar)
        botao_atualizar.bind('<Leave>',btn_atualizar_sair)

        def btn_deletar_entrar(event):
            botao_deletar.configure(bg="red", fg="white")
        def btn_deletar_sair(event):
            botao_deletar.configure(bg="white", fg="black")
        botao_deletar = Button(self.frame_2, text="Deletar", bg="white", fg="black", command=self.deletar_tsp)
        botao_deletar.place(relx=0.70, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_deletar.bind('<Enter>',btn_deletar_entrar)
        botao_deletar.bind('<Leave>',btn_deletar_sair)

        def btn_limpar_entrar(event):
            botao_limpar.configure(bg="orange", fg="black")
        def btn_limpar_sair(event):
            botao_limpar.configure(bg="white", fg="black")
        botao_limpar = Button(self.frame_2, text="Limpar", bg="white", fg="black", command=self.limpar_tsp)
        botao_limpar.place(relx=0.10, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_limpar.bind('<Enter>',btn_limpar_entrar)
        botao_limpar.bind('<Leave>',btn_limpar_sair)

        def btn_home_entrar(event):
            botao_home.configure(bg="green", fg="white")
        def btn_home_sair(event):
            botao_home.configure(bg="white", fg="black")
        botao_home = Button(self.frame_2, text="HOME", bg="white", fg="black", command=self.home)
        botao_home.place(relx=0.40, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_home.bind('<Enter>',btn_home_entrar)
        botao_home.bind('<Leave>',btn_home_sair)

        def btn_ativar_entrar(event):
            botao_ativar.configure(bg="purple", fg="white")
        def btn_ativar_sair(event):
            botao_ativar.configure(bg="white", fg="black")
        botao_ativar = Button(self.frame_2, text="Ativar", bg="white", fg="black", command=self.ativar_tsp)
        botao_ativar.place(relx=0.70, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_ativar.bind('<Enter>',btn_ativar_entrar)
        botao_ativar.bind('<Leave>',btn_ativar_sair)

        # frame 3
        self.apagar_widgets_frame_3()
        self.criar_tv_tsp()

        def btn_capturar_entrar(event):
            botao_capturar.configure(bg="pink", fg="black")
        def btn_capturar_sair(event):
            botao_capturar.configure(bg="white", fg="black")
        botao_capturar = Button(self.frame_3, text="Capturar", bg="black", fg="white", command=self.capturar_tsp)
        botao_capturar.place(relx=0.30, rely=0.90, relheight=0.05, relwidth=0.40)
        botao_capturar.bind('<Enter>',btn_capturar_entrar)
        botao_capturar.bind('<Leave>',btn_capturar_sair)

    def capturar_tsp(self):
        
        try:
            Item_Selecionado = self.tv_tsp.selection()[0]
        except:
            messagebox.showinfo("ERRO","Precisa Selecionar um item.")
            return()
        valores_selecionados = self.tv_tsp.item(Item_Selecionado,"values")
        id_capturado = valores_selecionados[0]
        tipo_sub_produto_capturado = valores_selecionados[1]
        markup_capturado = valores_selecionados[2]

        self.entry_id_tsp.configure(text=id_capturado)
        self.entry_tsp.delete(0,END)
        self.entry_tsp.insert(0,tipo_sub_produto_capturado)

        self.entry_tsp_markup.delete(0,END)
        self.entry_tsp_markup.insert(0,markup_capturado)

    def criar_tv_tsp(self):        
        self.tv_tsp = ttk.Treeview(self.frame_3, columns=('id','tipo_sub_produto','markup','ativo'), show='headings')
        self.tv_tsp.column('id', minwidth=0, width=10)
        self.tv_tsp.column('tipo_sub_produto', minwidth=0, width=150)
        self.tv_tsp.column('markup', minwidth=0, width=10)
        self.tv_tsp.column('ativo', minwidth=0, width=10)
        
        self.tv_tsp.heading('id', text="ID")
        self.tv_tsp.heading('tipo_sub_produto', text="Tipo de Sub Produto")
        self.tv_tsp.heading('markup', text="markup")
        self.tv_tsp.heading('ativo', text="Ativo")
        
        sql = f"SELECT `id_tipo_sub_produto`,`tipo_sub_produto`,`markup_minimo`,`ativo` FROM {self.tabela}"
        result = executa_DQL(sql)

        for item in result:
            self.tv_tsp.insert("", END, values=(item[0], item[1], item[2], item[3]))

        self.tv_tsp.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

    def deletar_tsp(self):
        id_entry = self.entry_id_tsp.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        
        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            
        
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '0' WHERE id_tipo_sub_produto = {id_entry};"
        result = executa_DML(sql)
        self.criar_tv_tsp()
        self.limpar_tsp()
        return()        

    def ativar_tsp(self):
        id_entry = self.entry_id_tsp.cget("text")
        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            
        
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '1' WHERE id_tipo_sub_produto = {id_entry};"
        result = executa_DML(sql)
        self.criar_tv_tsp()
        self.limpar_tsp()
        return()

    def atualizar_tsp(self):
        
        id_entry = self.entry_id_tsp.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        
        id_entry = int(id_entry)
        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID tipo: {type(id_entry)}.")
            return()

        tipo_sub_produto_entry = self.entry_tsp.get()
        
        if len(tipo_sub_produto_entry) == 0:
            messagebox.showinfo("ERRO",f"Tipo de Produto precisa ser preenchido.")
            return()

        markup_entry = self.entry_tsp_markup.get()

        if len(markup_entry) == 0 or markup_entry == '0' or markup_entry == 0:
            messagebox.showinfo("ERRO",f"Markup precisa ser preenchido.")
            return()

        markup_entry = markup_entry.replace(",",".")

        try:
            markup_entry = float(markup_entry)
        except:
            messagebox.showinfo("ERRO",f"Markup não está correto.")
            return()

        sql = f"UPDATE `{self.tabela}` SET tipo_sub_produto = '{tipo_sub_produto_entry}', `markup_minimo` = '{markup_entry}' WHERE id_tipo_sub_produto = {id_entry};"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo("ERRO","O registro não foi atualizado.")
            print(sql)
            return()
        
        self.criar_tv_tsp()
        self.limpar_tsp()
        return()

    def incluir_tsp(self):

        entry_tipo_sub_produto = self.entry_tsp.get()

        if len(entry_tipo_sub_produto) == 0:
            messagebox.showinfo("Em branco","Campo unidade precisa ser preenchido.")
            return()

        markup_entry = self.entry_tsp_markup.get()

        if len(markup_entry) == 0 or markup_entry == '0' or markup_entry == 0:
            messagebox.showinfo("ERRO",f"Markup precisa ser preenchido.")
            return()

        markup_entry = markup_entry.replace(",",".")

        try:
            markup_entry = float(markup_entry)
        except:
            messagebox.showinfo("ERRO",f"Markup não está correto.")
            return()

        sql = f"INSERT INTO {self.tabela} (tipo_sub_produto, markup_minimo) VALUES ('{entry_tipo_sub_produto}','{markup_entry}')"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo(title="ERRO", message="Algo deu errado com o banco de dados.")
            print(sql)
            return()

        self.criar_tv_tsp()
        self.limpar_tsp()
        return()

    def limpar_tsp(self):
        self.entry_tsp.delete(0,END)
        self.entry_tsp_markup.delete(0,END)
        self.entry_id_tsp.configure(text="novo")
        self.entry_tsp.focus()


    def produtos_x_sub_produtos(self):

        self.tabela = "produtos_x_sub_produtos"

        abc = self.listagem_unidades()

        self.lista_ids_unidades = abc[0]
        self.lista_unidades = abc[1]

        if len(self.lista_ids_unidades) == 0:
            messagebox.showinfo("Faltam dados","Unidades necessita(m) de algu(ns) dado(s).")
            self.home()            
        
        abc = self.listagem_sub_produtos()

        self.lista_ids_sub_produtos = abc[0]
        self.lista_sub_produtos = abc[1]

        if len(self.lista_ids_sub_produtos) == 0:
            messagebox.showinfo("Faltam dados","Sub Produtos necessita(m) de algu(ns) dado(s).")
            self.home()            

        abc = self.listagem_produtos()

        self.lista_ids_produtos = abc[0]
        self.lista_produtos = abc[1]

        if len(self.lista_ids_produtos) == 0:
            messagebox.showinfo("Faltam dados","Produtos necessita(m) de algu(ns) dado(s).")
            self.home()
        
        # frame 2
        self.apagar_widgets_frame_2()
        self.apagar_widgets_frame_3()

        # frame_1
        self.label_frame_1.configure(text="Produtos x Sub Produtos")
        
        # qtde_labels_e_entrys = 5
        # adicional_tamanhos_listbox = 9

        # margem_superior = ((1-self.espaco_para_botoes)-((qtde_labels_e_entrys*2+adicional_tamanhos_listbox)*self.altura_campos)-(qtde_labels_e_entrys*self.espaco_interno)-((qtde_labels_e_entrys-1)*self.espaco_externo))/2

        margem_superior = 0

        self.label_id_psp = Label(self.frame_2, text="ID", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_id_psp.place(relx=0.05, rely=margem_superior, relwidth=0.90, relheight=self.altura_campos)

        self.entry_id_psp = Label(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, text="novo")
        self.entry_id_psp.place(relx=0.05, rely=margem_superior + self.altura_campos + self.espaco_interno, relwidth=0.90, relheight=self.altura_campos)

        self.label_psp_sub_produto = Label(self.frame_2, text="selecione o sub produto", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_psp_sub_produto.place(relx=0.05, rely=margem_superior + 2*self.altura_campos + self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_psp_sub_produto = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox, selectmode=SINGLE)
        
        indice = 0
        for id in self.lista_ids_sub_produtos:
            sub_produto = self.lista_sub_produtos[indice]
            self.entry_psp_sub_produto.insert(id, sub_produto)
            indice += 1

        self.scbar_psp_sub_produto = Scrollbar(self.entry_psp_sub_produto, orient=VERTICAL)
        self.scbar_psp_sub_produto.config(command=self.entry_psp_sub_produto.yview)
        self.scbar_psp_sub_produto.pack(side=RIGHT, fill=Y)       

        self.entry_psp_sub_produto.configure(yscrollcommand=self.scbar_psp_sub_produto.set)
        self.entry_psp_sub_produto.place(relx=0.05, rely=margem_superior + 3*self.altura_campos + 2*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_psp_sub_produto.bind('<<ListboxSelect>>',self.on_select_psp_sub_produto)

        self.escolha_psp_sub_produto = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_psp_sub_produto.place(relx=0.05, rely=margem_superior + 7*self.altura_campos + 3*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_psp_produto = Label(self.frame_2, text="selecione o produto", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_psp_produto.place(relx=0.05, rely=margem_superior + 8*self.altura_campos + 3*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_psp_produto = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, height=1, selectmode=SINGLE)

        indice = 0        
        for id in self.lista_ids_produtos:
            produto = self.lista_produtos[indice]
            self.entry_psp_produto.insert(id, produto)
            indice += 1

        self.entry_psp_produto.place(relx=0.05, rely=margem_superior + 9*self.altura_campos + 4*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_psp_produto.bind('<<ListboxSelect>>',self.on_select_psp_produto)

        self.escolha_psp_produto = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_psp_produto.place(relx=0.05, rely=margem_superior + 13*self.altura_campos + 5*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_psp_peso = Label(self.frame_2, text="mensuração", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_psp_peso.place(relx=0.05, rely=margem_superior + 14*self.altura_campos + 5*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_psp_peso = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_psp_peso.place(relx=0.05, rely=margem_superior + 15*self.altura_campos + 6*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)    

        self.label_psp_unidade = Label(self.frame_2, text="unidade", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_psp_unidade.place(relx=0.05, rely=margem_superior + 16*self.altura_campos + 6*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_psp_unidade = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, height=1, selectmode=SINGLE)

        indice = 0
        
        for id in self.lista_ids_unidades:
            unidade = self.lista_unidades[indice]
            self.entry_psp_unidade.insert(id,unidade)
            indice += 1

        self.scbar_psp_unidade = Scrollbar(self.entry_psp_unidade, orient=VERTICAL)
        self.scbar_psp_unidade.config(command=self.entry_psp_unidade.yview)
        self.scbar_psp_unidade.pack(side=RIGHT, fill=Y)       

        self.entry_psp_unidade.configure(yscrollcommand=self.scbar_psp_unidade.set)
        self.entry_psp_unidade.place(relx=0.05, rely=margem_superior + 17*self.altura_campos + 7*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_psp_unidade.bind('<<ListboxSelect>>',self.on_select_psp_unidade)

        self.escolha_psp_unidade = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_psp_unidade.place(relx=0.05, rely=margem_superior + 21*self.altura_campos + 8*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        def btn_incluir_entrar(event):
            botao_incluir.configure(bg="blue", fg="white")
        def btn_incluir_sair(event):
            botao_incluir.configure(bg="white", fg="black")
        botao_incluir = Button(self.frame_2, text="Incluir", bg="white", fg="black", command=self.incluir_psp)
        botao_incluir.place(relx=0.10, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_incluir.bind('<Enter>',btn_incluir_entrar)
        botao_incluir.bind('<Leave>',btn_incluir_sair)


        def btn_atualizar_entrar(event):
            botao_atualizar.configure(bg="yellow", fg="black")
        def btn_atualizar_sair(event):
            botao_atualizar.configure(bg="white", fg="black")
        botao_atualizar = Button(self.frame_2, text="Atualizar", bg="white", fg="black", command=self.atualizar_psp)
        botao_atualizar.place(relx=0.40, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_atualizar.bind('<Enter>',btn_atualizar_entrar)
        botao_atualizar.bind('<Leave>',btn_atualizar_sair)

        def btn_deletar_entrar(event):
            botao_deletar.configure(bg="red", fg="white")
        def btn_deletar_sair(event):
            botao_deletar.configure(bg="white", fg="black")
        botao_deletar = Button(self.frame_2, text="Deletar", bg="white", fg="black", command=self.deletar_psp)
        botao_deletar.place(relx=0.70, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_deletar.bind('<Enter>',btn_deletar_entrar)
        botao_deletar.bind('<Leave>',btn_deletar_sair)

        def btn_limpar_entrar(event):
            botao_limpar.configure(bg="orange", fg="black")
        def btn_limpar_sair(event):
            botao_limpar.configure(bg="white", fg="black")
        botao_limpar = Button(self.frame_2, text="Limpar", bg="white", fg="black", command=self.limpar_psp)
        botao_limpar.place(relx=0.10, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_limpar.bind('<Enter>',btn_limpar_entrar)
        botao_limpar.bind('<Leave>',btn_limpar_sair)

        def btn_home_entrar(event):
            botao_home.configure(bg="green", fg="white")
        def btn_home_sair(event):
            botao_home.configure(bg="white", fg="black")
        botao_home = Button(self.frame_2, text="HOME", bg="white", fg="black", command=self.home)
        botao_home.place(relx=0.40, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_home.bind('<Enter>',btn_home_entrar)
        botao_home.bind('<Leave>',btn_home_sair)

        def btn_ativar_entrar(event):
            botao_ativar.configure(bg="purple", fg="white")
        def btn_ativar_sair(event):
            botao_ativar.configure(bg="white", fg="black")
        botao_ativar = Button(self.frame_2, text="Ativar", bg="white", fg="black", command=self.ativar_psp)
        botao_ativar.place(relx=0.70, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_ativar.bind('<Enter>',btn_ativar_entrar)
        botao_ativar.bind('<Leave>',btn_ativar_sair)

        def btn_capturar_entrar(event):
            botao_capturar.configure(bg="pink", fg="black")
        def btn_capturar_sair(event):
            botao_capturar.configure(bg="white", fg="black")
        botao_capturar = Button(self.frame_3, text="Capturar", bg="black", fg="white", command=self.capturar_psp)
        botao_capturar.place(relx=0.30, rely=0.90, relheight=0.05, relwidth=0.40)
        botao_capturar.bind('<Enter>',btn_capturar_entrar)
        botao_capturar.bind('<Leave>',btn_capturar_sair)

        # frame 3
        self.criar_tv_psp()

    def on_select_psp_produto(self, event):
        try:
            self.escolha_psp_produto.configure(text=self.entry_psp_produto.get(self.entry_psp_produto.curselection()), bg=self.cor_fundo_entry, fg="black")
            self.criar_tv_psp()
        except:
            pass

    def on_select_psp_sub_produto(self, event):
        try:
            self.escolha_psp_sub_produto.configure(text=self.entry_psp_sub_produto.get(self.entry_psp_sub_produto.curselection()), bg=self.cor_fundo_entry, fg="black")
        except:
            pass

    def on_select_psp_unidade(self, event):
        try:
            self.escolha_psp_unidade.configure(text=self.entry_psp_unidade.get(self.entry_psp_unidade.curselection()), bg=self.cor_fundo_entry, fg="black")
        except:
            pass

    def capturar_psp(self):
        
        try:
            Item_Selecionado = self.tv_psp.selection()[0]
        except:
            messagebox.showinfo("ERRO","Precisa Selecionar um item.")
            return()
                                
        valores_selecionados = self.tv_psp.item(Item_Selecionado,"values")
        
        id_capturado = valores_selecionados[0]
        sub_produto_capturado = valores_selecionados[1]
        produto_capturado = valores_selecionados[2]
        peso_capturado = valores_selecionados[3]
        unidade_capturada = valores_selecionados[4]

        self.entry_id_psp.configure(text=id_capturado)
        
        self.entry_psp_peso.delete(0,END)
        self.entry_psp_peso.insert(0,peso_capturado)

        indice = 0
        for item in self.lista_sub_produtos:
            if sub_produto_capturado == item:
                indice_sub_produto_capturado = self.lista_ids_sub_produtos[indice]
            indice += 1

        self.entry_psp_sub_produto.selection_clear(0,tk.END)
        self.entry_psp_sub_produto.selection_set(indice_sub_produto_capturado)
        self.escolha_psp_sub_produto.configure(text=sub_produto_capturado, bg=self.cor_fundo_entry, fg="black")

        indice = 0
        for item in self.lista_produtos:
            if produto_capturado == item:
                indice_produto = self.lista_ids_produtos[indice]
            indice += 1

        self.entry_psp_produto.selection_clear(0,tk.END)
        self.entry_psp_produto.selection_set(indice_produto)
        self.escolha_psp_produto.configure(text=produto_capturado, bg=self.cor_fundo_entry, fg="black")

        indice = 0
        for item in self.lista_unidades:
            if unidade_capturada == item:
                indice_unidade = self.lista_ids_unidades[indice]
            indice += 1

        self.entry_psp_unidade.selection_clear(0,tk.END)
        self.entry_psp_unidade.selection_set(indice_unidade)
        self.escolha_psp_unidade.configure(text=unidade_capturada, bg=self.cor_fundo_entry, fg="black")

    def criar_tv_psp(self):
        self.tv_psp = ttk.Treeview(self.frame_3, columns=('id','sub_produto','produto','peso','unidade','ativo'), show='headings')
        
        self.tv_psp.column('id', minwidth=0, width=10)
        self.tv_psp.column('sub_produto', minwidth=0, width=100)
        self.tv_psp.column('produto', minwidth=0, width=10)
        self.tv_psp.column('peso', minwidth=0, width=10)
        self.tv_psp.column('unidade', minwidth=0, width=10)
        self.tv_psp.column('ativo', minwidth=0, width=10)
        
        self.tv_psp.heading('id', text="ID")
        self.tv_psp.heading('sub_produto', text="Sub Produto")
        self.tv_psp.heading('produto', text="produto")
        self.tv_psp.heading('peso', text="peso")
        self.tv_psp.heading('unidade', text="peso")
        self.tv_psp.heading('ativo', text="ativo")      

        produto_entry = self.escolha_psp_produto.cget("text")

        if produto_entry == 'escolher':
            sql = f"SELECT `id_produtos_x_sub_produtos`,`sub_produto_id`,`produto_id`,`peso`,`unidade_id`,`ativo` FROM {self.tabela}"
        else:
            sql = f"SELECT `id_produto` FROM `produtos` WHERE `produto` = '{produto_entry}'"
            result = executa_DQL(sql)
            id_produto = result[0][0]
            sql = f"SELECT `id_produtos_x_sub_produtos`,`sub_produto_id`,`produto_id`,`peso`,`unidade_id`,`ativo` FROM {self.tabela} WHERE `produto_id` = '{id_produto}'"

        result = executa_DQL(sql)

        for item_result in result:           
            sql = f"SELECT `sub_produto` FROM `sub_produtos` WHERE `id_sub_produto` = '{item_result[1]}'"
            result = executa_DQL(sql)
            item_sub_produto = result[0][0]

            sql = f"SELECT `produto` FROM `produtos` WHERE `id_produto` = '{item_result[2]}'"
            result = executa_DQL(sql)
            item_produto = result[0][0]

            sql = f"SELECT `unidade` FROM `unidades` WHERE `id_unidade` = '{item_result[4]}'"
            result = executa_DQL(sql)
            item_unidade = result[0][0]

            self.tv_psp.insert("", item_result[0], values=(item_result[0], item_sub_produto, item_produto, item_result[3], item_unidade, item_result[5]))

        self.tv_psp.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

    def deletar_psp(self):
        id_entry = self.entry_id_psp.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '0' WHERE id_produtos_x_sub_produtos = {id_entry};"
       
        result = executa_DML(sql)
        self.criar_tv_psp()
        self.limpar_psp()
        return()        

    def atualizar_psp(self):

        id_entry = self.entry_id_psp.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()

        produto_entry = self.escolha_psp_produto.cget("text")
        sub_produto_entry = self.escolha_psp_sub_produto.cget("text")
        unidade_entry = self.escolha_psp_unidade.cget("text")

        if len(produto_entry) == 0 or produto_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Precisa selecionar o Produto.")
            return()
            
        if len(sub_produto_entry) == 0 or sub_produto_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Precisa selecionar o Sub Produto.")
            return()

        if len(unidade_entry ) == 0 or unidade_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Precisa selecionar a Unidade.")
            return()

        sql = f"SELECT id_sub_produto FROM sub_produtos WHERE sub_produto = '{sub_produto_entry}'"
        result = executa_DQL(sql)
        id_sub_produto = result[0][0]

        sql = f"SELECT id_produto FROM produtos WHERE produto = '{produto_entry}'"
        result = executa_DQL(sql)
        id_produto = result[0][0]

        sql = f"SELECT id_unidade FROM unidades WHERE unidade = '{unidade_entry}'"
        result = executa_DQL(sql)
        id_unidade = result[0][0]

        qtde = self.entry_psp_peso.get()
        qtde = qtde.replace(',','.')

        if qtde == 0 or qtde == '0':
            messagebox.showinfo("Não válido",f"Campo peso não é válido. {qtde}")
            return()            

        try:
            qtde = float(qtde)
        except:
            messagebox.showinfo("Não válido",f"Campo peso não é válido. {qtde}")
            return()

        if qtde == 0:
            messagebox.showinfo("Em branco","Campo quantidade referencial precisa ser preenchido.")
            return()
        
        sql = f"UPDATE `{self.tabela}` SET `sub_produto_id` = '{id_sub_produto}', `produto_id` = '{id_produto}', `peso`='{qtde}', `unidade_id` = '{id_unidade}' WHERE `id_produtos_x_sub_produtos` = {id_entry};"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo("ERRO","O registro não foi atualizado.")
            print(sql)
            return()          
        
        self.criar_tv_psp()
        self.limpar_psp()
        return()

    def incluir_psp(self):
        produto_entry = self.escolha_psp_produto.cget("text")
        sub_produto_entry = self.escolha_psp_sub_produto.cget("text")
        unidade_entry = self.escolha_psp_unidade.cget("text")

        if len(produto_entry) == 0 or produto_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Precisa selecionar o Produto.")
            return()
            
        if len(sub_produto_entry) == 0 or sub_produto_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Precisa selecionar o Sub Produto.")
            return()

        if len(unidade_entry ) == 0 or unidade_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Precisa selecionar a Unidade.")
            return()

        sql = f"SELECT id_sub_produto FROM sub_produtos WHERE sub_produto = '{sub_produto_entry}'"
        result = executa_DQL(sql)
        sub_produto_id = result[0][0]

        sql = f"SELECT id_produto FROM produtos WHERE produto = '{produto_entry}'"
        result = executa_DQL(sql)
        produto_id = result[0][0]

        sql = f"SELECT id_unidade FROM unidades WHERE unidade = '{unidade_entry}'"
        result = executa_DQL(sql)
        unidade_id = result[0][0]
                   
        if produto_id == 0:
            messagebox.showinfo("EERO","algo está errado com o produto, não foi feita a atualização.")
            return()

        if sub_produto_id == 0:
            messagebox.showinfo("EERO","algo está errado com o sub_produto, não foi feita a atualização.")
            return()
      
        if unidade_id == 0:
            messagebox.showinfo("EERO","algo está errado com a unidade, não foi feita a atualização.")
            return()

        # sql = f"SELECT count(`id_produtos_x_sub_produtos`) FROM `produtos_x_sub_produtos` WHERE `sub_produto_id` = '{sub_produto_id}' `and produto_id` <> '{produto_id}'"
        # result = executa_DQL(sql)
        # contagem = result[0][0]

        # contagem = int(contagem)

        # if contagem >= 1:
        #     messagebox.showinfo("EERO","Sub produto já usado em outro Produto. Usar outro.")
        #     return()

        peso = self.entry_psp_peso.get()
        peso = peso.replace(",",".")
        
        if len(self.entry_psp_peso.get()) == 0:
            messagebox.showinfo("Em branco","Campo peso precisa ser preenchido.")
            return()

        try:
            peso = float(peso)
        except:
            messagebox.showinfo("ERRO","Campo peso não válido.")
            return()       

        sql = f"INSERT INTO {self.tabela} (sub_produto_id, produto_id, peso, unidade_id, ativo) VALUES ('{sub_produto_id}','{produto_id}','{peso}','{unidade_id}','1');"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo(title="ERRO", message=f"Algo deu errado com o banco de dados. {sql}")
            print(sql)
            return()

        self.criar_tv_psp()
        self.limpar_psp()
        return()

    def limpar_psp(self):

        self.entry_psp_peso.delete(0,END)
        self.entry_id_psp.configure(text="novo")

        self.entry_psp_produto.selection_clear(0,tk.END)
        self.escolha_psp_produto.configure(text="escolher", bg="white", fg="red")
        self.on_select_psp_produto(Event)

        self.entry_psp_sub_produto.selection_clear(0,tk.END)
        self.escolha_psp_sub_produto.configure(text="escolher", bg="white", fg="red")
        self.on_select_psp_sub_produto(Event)

        self.entry_psp_unidade.selection_clear(0,tk.END)
        self.escolha_psp_unidade.configure(text="escolher", bg="white", fg="red")
        self.on_select_psp_unidade(Event)

        self.criar_tv_psp()

    def ativar_psp(self):
        id_entry = self.entry_id_psp.cget("text")
        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()
        
        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()
        
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '1' WHERE id_produtos_x_sub_produtos = {id_entry};"
        result = executa_DML(sql)
        self.criar_tv_psp()
        self.limpar_psp()
        return()


    def pareceres(self):
        self.tabela = "pareceres"
        abc = self.listagem_produtos()

        self.lista_ids_produtos = abc[0]
        self.lista_produtos = abc[1]

        if len(self.lista_ids_produtos) == 0:
            messagebox.showinfo("Faltam dados","Produtos necessitam de algu(ns) dado(s).")
            self.home()
        
        self.apagar_widgets_frame_2()
        self.apagar_widgets_frame_3()

        # frame_1
        self.label_frame_1.configure(text="pareceres")

        # frame 2
        self.apagar_widgets_frame_2()
        
        qtde_labels_e_entrys = 5
        
        adicional_tamanhos_listbox = 3
        margem_superior = ((1-self.espaco_para_botoes)-((qtde_labels_e_entrys*2+adicional_tamanhos_listbox)*self.altura_campos)-(qtde_labels_e_entrys*self.espaco_interno)-((qtde_labels_e_entrys-1)*self.espaco_externo))/2

        self.label_id_par = Label(self.frame_2, text="ID", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_id_par.place(relx=0.05, rely=margem_superior, relwidth=0.90, relheight=self.altura_campos)

        self.entry_id_par = Label(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, text="novo")
        self.entry_id_par.place(relx=0.05, rely=margem_superior + self.altura_campos + self.espaco_interno, relwidth=0.90, relheight=self.altura_campos)

        self.label_par_produto = Label(self.frame_2, text="produto", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_par_produto.place(relx=0.05, rely=margem_superior + 2*self.altura_campos + 1*self.espaco_interno + 1*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_par_produto = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox)

        indice = 0
        
        for id in self.lista_ids_produtos:
            produto = self.lista_produtos[indice]
            self.entry_par_produto.insert(id,produto)
            indice += 1

        self.scbar_par_produto = Scrollbar(self.entry_par_produto, orient=VERTICAL)
        self.scbar_par_produto.config(command=self.entry_par_produto.yview)
        self.scbar_par_produto.pack(side=RIGHT, fill=Y)       

        self.entry_par_produto.configure(yscrollcommand=self.scbar_par_produto.set)

        self.entry_par_produto.place(relx=0.05, rely=margem_superior + 3*self.altura_campos + 2*self.espaco_interno + 1*self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_par_produto.bind('<<ListboxSelect>>',self.on_select_par_produto)

        self.escolha_par_produto = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_par_produto.place(relx=0.05, rely=margem_superior + 7*self.altura_campos + 3*self.espaco_interno + 1*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_par_pessoa = Label(self.frame_2, text="pessoa", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_par_pessoa.place(relx=0.05, rely=margem_superior + 8*self.altura_campos + 3*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_par_pessoa = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_par_pessoa.place(relx=0.05, rely=margem_superior + 9*self.altura_campos + 4*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_par = Label(self.frame_2, text="parecer", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_par.place(relx=0.05, rely=margem_superior + 10*self.altura_campos + 4*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_par = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_par.place(relx=0.05, rely=margem_superior + 11*self.altura_campos + 5*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_par_data = Label(self.frame_2, text="data", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_par_data.place(relx=0.05, rely=margem_superior + 12*self.altura_campos + 5*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_par_data = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_par_data.place(relx=0.05, rely=margem_superior + 13*self.altura_campos + 6*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        hoje = datetime.now().date()
        self.entry_par_data.insert(0,hoje)


        def btn_incluir_entrar(event):
            botao_incluir.configure(bg="blue", fg="white")
        def btn_incluir_sair(event):
            botao_incluir.configure(bg="white", fg="black")
        botao_incluir = Button(self.frame_2, text="Incluir", bg="white", fg="black", command=self.incluir_par)
        botao_incluir.place(relx=0.10, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_incluir.bind('<Enter>',btn_incluir_entrar)
        botao_incluir.bind('<Leave>',btn_incluir_sair)

        def btn_atualizar_entrar(event):
            botao_atualizar.configure(bg="yellow", fg="black")
        def btn_atualizar_sair(event):
            botao_atualizar.configure(bg="white", fg="black")
        botao_atualizar = Button(self.frame_2, text="Atualizar", bg="white", fg="black", command=self.atualizar_par)
        botao_atualizar.place(relx=0.40, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_atualizar.bind('<Enter>',btn_atualizar_entrar)
        botao_atualizar.bind('<Leave>',btn_atualizar_sair)

        def btn_deletar_entrar(event):
            botao_deletar.configure(bg="red", fg="white")
        def btn_deletar_sair(event):
            botao_deletar.configure(bg="white", fg="black")
        botao_deletar = Button(self.frame_2, text="Deletar", bg="white", fg="black", command=self.deletar_par)
        botao_deletar.place(relx=0.70, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_deletar.bind('<Enter>',btn_deletar_entrar)
        botao_deletar.bind('<Leave>',btn_deletar_sair)

        def btn_limpar_entrar(event):
            botao_limpar.configure(bg="orange", fg="black")
        def btn_limpar_sair(event):
            botao_limpar.configure(bg="white", fg="black")
        botao_limpar = Button(self.frame_2, text="Limpar", bg="white", fg="black", command=self.limpar_par)
        botao_limpar.place(relx=0.10, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_limpar.bind('<Enter>',btn_limpar_entrar)
        botao_limpar.bind('<Leave>',btn_limpar_sair)

        def btn_home_entrar(event):
            botao_home.configure(bg="green", fg="white")
        def btn_home_sair(event):
            botao_home.configure(bg="white", fg="black")
        botao_home = Button(self.frame_2, text="HOME", bg="white", fg="black", command=self.home)
        botao_home.place(relx=0.40, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_home.bind('<Enter>',btn_home_entrar)
        botao_home.bind('<Leave>',btn_home_sair)

        # frame 3
        self.apagar_widgets_frame_3()
        self.criar_tv_par()

        def btn_capturar_entrar(event):
            botao_capturar.configure(bg="pink", fg="black")
        def btn_capturar_sair(event):
            botao_capturar.configure(bg="white", fg="black")
        botao_capturar = Button(self.frame_3, text="Capturar", bg="black", fg="white", command=self.capturar_par)
        botao_capturar.place(relx=0.30, rely=0.90, relheight=0.05, relwidth=0.40)
        botao_capturar.bind('<Enter>',btn_capturar_entrar)
        botao_capturar.bind('<Leave>',btn_capturar_sair)

    def on_select_par_produto(self, event):
        try:
            self.escolha_par_produto.configure(text=self.entry_par_produto.get(self.entry_par_produto.curselection()), bg=self.cor_fundo_entry, fg="black")
        except:
            pass

    def capturar_par(self):
        try:
            Item_Selecionado = self.tv_par.selection()[0]
        except:
            messagebox.showinfo("ERRO","Precisa Selecionar um item.")
            return()
        
        valores_selecionados = self.tv_par.item(Item_Selecionado,"values")

        id_capturado = valores_selecionados[0]
        pessoa_capturada = valores_selecionados[1]
        data_capturada = valores_selecionados[2]
        produto_capturado = valores_selecionados[3]
        parecer_capturado = valores_selecionados[4]

        self.entry_id_par.configure(text=id_capturado)

        self.entry_par.delete(0,END)
        self.entry_par.insert(0, parecer_capturado)        

        self.entry_par_data.delete(0,END)
        self.entry_par_data.insert(0, data_capturada)

        self.entry_par_pessoa.delete(0,END)
        self.entry_par_pessoa.insert(0, pessoa_capturada)

        indice = 0
        for item in self.lista_produtos:
            if produto_capturado == item:
                indice_produto = self.lista_ids_produtos[indice]
            indice += 1

        self.entry_par_produto.selection_clear(0,tk.END)
        self.entry_par_produto.selection_set(indice_produto)
        self.escolha_par_produto.configure(text=self.entry_par_produto.get(self.entry_par_produto.curselection()), bg=self.cor_fundo_entry, fg="black")

    def criar_tv_par(self):

        self.tv_par = ttk.Treeview(self.frame_3, columns=('id','pessoa','data','produto','parecer'), show='headings')
        self.tv_par.column('id', minwidth=0, width=10)
        self.tv_par.column('pessoa', minwidth=0, width=75)
        self.tv_par.column('data', minwidth=0, width=10)
        self.tv_par.column('produto', minwidth=0, width=10)
        self.tv_par.column('parecer', minwidth=0, width=10)
        
        self.tv_par.heading('id', text="ID")
        self.tv_par.heading('pessoa', text="Pessoa")
        self.tv_par.heading('data', text="Data")
        self.tv_par.heading('produto', text="Produto")
        self.tv_par.heading('parecer', text="parecer")

        sql = f"SELECT `id_parecer`,`pessoa`,`data`,`produto_id`,`parecer` FROM {self.tabela}"
        result = executa_DQL(sql)

        for item_result in result:
            indice = 0
            
            for item in self.lista_ids_produtos:
                item_produto = self.lista_produtos[indice]
                
                if int(item) == item_result[3]:
                    self.tv_par.insert("", END, values=(item_result[0], item_result[1], item_result[2], item_produto, item_result[4]))
                    
                indice += 1

        self.tv_par.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

    def deletar_par(self):

        id_entry = self.entry_id_par.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        
        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()
               
        sql = f"DELETE FROM `{self.tabela}` WHERE id_parecer = {id_entry};"
        result = executa_DML(sql)
        self.criar_tv_par()
        self.limpar_par()
        return()        

    def atualizar_par(self):
        
        id_entry = self.entry_id_par.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        
        id_entry = int(id_entry)
        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID tipo: {type(id_entry)}.")
            return()

        parecer_entry = self.entry_par.get()
        data_entry = self.entry_par_data.get()
        pessoa_entry = self.entry_par_pessoa.get()
        
        if len(parecer_entry) == 0:
            messagebox.showinfo("ERRO",f"parecer precisa ser preenchido.")
            return()

        produto_entry = self.escolha_par_produto.cget("text")

        if len(produto_entry) == 0:
            messagebox.showinfo("ERRO",f"Prouto precisa ser preenchido.")
            return()

        sql = f"SELECT `id_prodduto` FROM produtos WHERE `produto` = '{produto_entry}'"
        result = executa_DQL(sql)
        produto_id = result[0][0]

        sql = f"UPDATE `{self.tabela}` SET parecer = '{parecer_entry}', produto_id = '{produto_id}', data = '{data_entry}', pessoa = '{pessoa_entry}' WHERE id_parecer = {id_entry};"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo("ERRO","O registro não foi atualizado.")
            print(sql)
            return()          
        
        self.criar_tv_par()
        self.limpar_par()
        return()

    def incluir_par(self):
        
        entry_parecer = self.entry_par.get()
        entry_pessoa = self.entry_par_pessoa.get()
        entry_data = self.entry_par_data.get()

        produto_entry = self.escolha_par_produto.cget("text")

        if len(produto_entry) == 0:
            messagebox.showinfo("ERRO",f"Prouto precisa ser preenchido.")
            return()

        sql = f"SELECT `id_prodduto` FROM produtos WHERE `produto` = '{produto_entry}'"
        result = executa_DQL(sql)
        produto_id = result[0][0]

        if len(entry_parecer) == 0:
            messagebox.showinfo("Em branco","Campo parecer precisa ser preenchido.")
            return()

        if len(entry_pessoa) == 0:
            messagebox.showinfo("Em branco","Campo parecer precisa ser preenchido.")
            return()

        sql = f"INSERT INTO {self.tabela} (parecer, produto_id, pessoa, data) VALUES ('{entry_parecer}','{produto_id}','{entry_pessoa}','{entry_data}')"
        result = executa_DML(sql)

        if result == False:
            print(sql)
            messagebox.showinfo(title="ERRO", message="Algo deu errado com o banco de dados.")
            return()

        self.criar_tv_par()
        self.limpar_par()
        return()

    def limpar_par(self):
        self.entry_par.delete(0,END)
        self.entry_id_par.configure(text="novo")        
        self.entry_par_pessoa.delete(0,END)
        self.entry_par_data.delete(0,END)
        hoje = datetime.now().date()
        self.entry_par_data.insert(0,hoje)

        self.entry_par_produto.selection_clear(0,tk.END)
        self.escolha_par_produto.configure(text="escolher", bg="white", fg="red")
        self.on_select_par_produto(Event)

        self.entry_par.focus()


    def grandezas_fisicas(self):
        self.tabela = "grandezas_fisicas"
        # frame_1
        self.label_frame_1.configure(text="Grandezas Físicas")

        # frame 2
        self.apagar_widgets_frame_2()
        
        qtde_labels_e_entrys = 2 
        adicional_tamanhos_listbox = 0
        margem_superior = ((1-self.espaco_para_botoes)-((qtde_labels_e_entrys*2+adicional_tamanhos_listbox)*self.altura_campos)-(qtde_labels_e_entrys*self.espaco_interno)-((qtde_labels_e_entrys-1)*self.espaco_externo))/2

        self.label_id_grf = Label(self.frame_2, text="ID", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_id_grf.place(relx=0.05, rely=margem_superior, relwidth=0.90, relheight=self.altura_campos)

        self.entry_id_grf = Label(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, text="novo")
        self.entry_id_grf.place(relx=0.05, rely=margem_superior + self.altura_campos + self.espaco_interno, relwidth=0.90, relheight=self.altura_campos)
        
        self.label_grf = Label(self.frame_2, text="grandeza física", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_grf.place(relx=0.05, rely=margem_superior + 2*self.altura_campos + self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_grf = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_grf.place(relx=0.05, rely=margem_superior + 3*self.altura_campos + 2*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        def btn_incluir_entrar(event):
            botao_incluir.configure(bg="blue", fg="white")
        def btn_incluir_sair(event):
            botao_incluir.configure(bg="white", fg="black")
        botao_incluir = Button(self.frame_2, text="Incluir", bg="white", fg="black", command=self.incluir_grf)
        botao_incluir.place(relx=0.10, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_incluir.bind('<Enter>',btn_incluir_entrar)
        botao_incluir.bind('<Leave>',btn_incluir_sair)


        def btn_atualizar_entrar(event):
            botao_atualizar.configure(bg="yellow", fg="black")
        def btn_atualizar_sair(event):
            botao_atualizar.configure(bg="white", fg="black")
        botao_atualizar = Button(self.frame_2, text="Atualizar", bg="white", fg="black", command=self.atualizar_grf)
        botao_atualizar.place(relx=0.40, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_atualizar.bind('<Enter>',btn_atualizar_entrar)
        botao_atualizar.bind('<Leave>',btn_atualizar_sair)

        def btn_deletar_entrar(event):
            botao_deletar.configure(bg="red", fg="white")
        def btn_deletar_sair(event):
            botao_deletar.configure(bg="white", fg="black")
        botao_deletar = Button(self.frame_2, text="Deletar", bg="white", fg="black", command=self.deletar_grf)
        botao_deletar.place(relx=0.70, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_deletar.bind('<Enter>',btn_deletar_entrar)
        botao_deletar.bind('<Leave>',btn_deletar_sair)

        def btn_limpar_entrar(event):
            botao_limpar.configure(bg="orange", fg="black")
        def btn_limpar_sair(event):
            botao_limpar.configure(bg="white", fg="black")
        botao_limpar = Button(self.frame_2, text="Limpar", bg="white", fg="black", command=self.limpar_grf)
        botao_limpar.place(relx=0.10, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_limpar.bind('<Enter>',btn_limpar_entrar)
        botao_limpar.bind('<Leave>',btn_limpar_sair)

        def btn_home_entrar(event):
            botao_home.configure(bg="green", fg="white")
        def btn_home_sair(event):
            botao_home.configure(bg="white", fg="black")
        botao_home = Button(self.frame_2, text="HOME", bg="white", fg="black", command=self.home)
        botao_home.place(relx=0.40, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_home.bind('<Enter>',btn_home_entrar)
        botao_home.bind('<Leave>',btn_home_sair)

        # frame 3
        self.apagar_widgets_frame_3()
        self.criar_tv_grf()

        def btn_capturar_entrar(event):
            botao_capturar.configure(bg="pink", fg="black")
        def btn_capturar_sair(event):
            botao_capturar.configure(bg="white", fg="black")
        botao_capturar = Button(self.frame_3, text="Capturar", bg="black", fg="white", command=self.capturar_grf)
        botao_capturar.place(relx=0.30, rely=0.90, relheight=0.05, relwidth=0.40)
        botao_capturar.bind('<Enter>',btn_capturar_entrar)
        botao_capturar.bind('<Leave>',btn_capturar_sair)

    def capturar_grf(self):

        try:
            Item_Selecionado = self.tv_grf.selection()[0]
        except:
            messagebox.showinfo("ERRO","Precisa Selecionar um item.")
            return()
        
        valores_selecionados = self.tv_grf.item(Item_Selecionado,"values")

        id_capturado = valores_selecionados[0]
        grandeza_fisica_capturada = valores_selecionados[1]    

        self.entry_id_grf.configure(text=id_capturado)

        self.entry_grf.delete(0,END)
        self.entry_grf.insert(0,grandeza_fisica_capturada)

    def criar_tv_grf(self):
        self.tv_grf = ttk.Treeview(self.frame_3, columns=('id','grandeza_fisica'), show='headings')
        self.tv_grf.column('id', minwidth=0, width=10)
        self.tv_grf.column('grandeza_fisica', minwidth=0, width=150)
        
        self.tv_grf.heading('id', text="ID")
        self.tv_grf.heading('grandeza_fisica', text="Grandeza Física")   

        sql = f"SELECT `id`,`grandeza` FROM {self.tabela}"
        result = executa_DQL(sql)

        for item in result:
            self.tv_grf.insert("", END, values=(item[0], item[1]))

        self.tv_grf.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

    def deletar_grf(self):
        id_entry = self.entry_id_grf.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            
        
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '0' WHERE id_grandeza_fisica = {id_entry};"
        result = executa_DML(sql)
        self.criar_tv_grf()
        self.limpar_grf()
        return()        

    def atualizar_grf(self):
        
        id_entry = self.entry_id_grf.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        
        id_entry = int(id_entry)
        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID tipo: {type(id_entry)}.")
            return()

        grandeza_fisica_entry = self.entry_grf.get()
        
        if len(grandeza_fisica_entry) == 0:
            messagebox.showinfo("ERRO",f"Grandeza Física precisa ser preenchida.")
            return()
                            
        sql = f"UPDATE `{self.tabela}` SET grandeza = '{grandeza_fisica_entry}' WHERE id = {id_entry};"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo("ERRO","O registro não foi atualizado.")
            print(sql)
            return()
        
        self.criar_tv_grf()
        self.limpar_grf()
        return()

    def incluir_grf(self):
        entry_grandeza_fisica = self.entry_grf.get()

        if len(entry_grandeza_fisica) == 0:
            messagebox.showinfo("Em branco","Campo unidade precisa ser preenchido.")
            return()

        sql = f"INSERT INTO {self.tabela} (grandeza) VALUES ('{entry_grandeza_fisica}')"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo(title="ERRO", message="Algo deu errado com o banco de dados.")
            return()

        self.criar_tv_grf()
        self.limpar_grf()
        return()

    def limpar_grf(self):
        self.entry_grf.delete(0,END)
        self.entry_id_grf.configure(text="novo")
        self.entry_grf.focus()


    def relacionamento_unidades(self):
        self.tabela = "relacionamento_unidades"
        abc = self.listagem_unidades()

        self.lista_ids_unidades = abc[0]
        self.lista_unidades = abc[1]

        if len(self.lista_ids_unidades) == 0:
            messagebox.showinfo("Faltam dados","Unidades necessitam de algu(ns) dado(s).")
            self.home()
        
        self.apagar_widgets_frame_2()
        self.apagar_widgets_frame_3()

        # frame_1
        self.label_frame_1.configure(text="Relacionamentos entre Unidades")

        # frame 2
        self.apagar_widgets_frame_2()
        
        qtde_labels_e_entrys = 3
        
        adicional_tamanhos_listbox = 6
        margem_superior = ((1-self.espaco_para_botoes)-((qtde_labels_e_entrys*2+adicional_tamanhos_listbox)*self.altura_campos)-(qtde_labels_e_entrys*self.espaco_interno)-((qtde_labels_e_entrys-1)*self.espaco_externo))/2

        self.label_id_run = Label(self.frame_2, text="ID", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_id_run.place(relx=0.05, rely=margem_superior, relwidth=0.90, relheight=self.altura_campos)

        self.entry_id_run = Label(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, text="novo")
        self.entry_id_run.place(relx=0.05, rely=margem_superior + self.altura_campos + self.espaco_interno, relwidth=0.90, relheight=self.altura_campos)

        self.label_run_unidade_1 = Label(self.frame_2, text="unidade 1", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_run_unidade_1.place(relx=0.05, rely=margem_superior + 2*self.altura_campos + 1*self.espaco_interno + 1*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_run_unidade_1 = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox)

        indice = 0
        
        for id in self.lista_ids_unidades:
            unidade = self.lista_unidades[indice]
            self.entry_run_unidade_1.insert(id,unidade)
            indice += 1

        self.scbar_run_unidade_1 = Scrollbar(self.entry_run_unidade_1, orient=VERTICAL)
        self.scbar_run_unidade_1.config(command=self.entry_run_unidade_1.yview)
        self.scbar_run_unidade_1.pack(side=RIGHT, fill=Y)       

        self.entry_run_unidade_1.configure(yscrollcommand=self.scbar_run_unidade_1.set)
        self.entry_run_unidade_1.place(relx=0.05, rely=margem_superior + 3*self.altura_campos + 2*self.espaco_interno + 1*self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_run_unidade_1.bind('<<ListboxSelect>>',self.on_select_run_unidade_1)

        self.escolha_run_unidade_1 = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_run_unidade_1.place(relx=0.05, rely=margem_superior + 7*self.altura_campos + 3*self.espaco_interno + 1*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_run_unidade_2 = Label(self.frame_2, text="unidade 2", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_run_unidade_2.place(relx=0.05, rely=margem_superior + 8*self.altura_campos + 3*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_run_unidade_2 = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox)

        indice = 0
        
        for id in self.lista_ids_unidades:
            unidade = self.lista_unidades[indice]
            self.entry_run_unidade_2.insert(id,unidade)
            indice += 1

        self.scbar_run_unidade_2 = Scrollbar(self.entry_run_unidade_2, orient=VERTICAL)
        self.scbar_run_unidade_2.config(command=self.entry_run_unidade_2.yview)
        self.scbar_run_unidade_2.pack(side=RIGHT, fill=Y)       

        self.entry_run_unidade_2.configure(yscrollcommand=self.scbar_run_unidade_2.set)
        self.entry_run_unidade_2.place(relx=0.05, rely=margem_superior + 9*self.altura_campos + 2*self.espaco_interno + 1*self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_run_unidade_2.bind('<<ListboxSelect>>',self.on_select_run_unidade_2)

        self.escolha_run_unidade_2 = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_run_unidade_2.place(relx=0.05, rely=margem_superior + 13*self.altura_campos + 3*self.espaco_interno + 1*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_run_fator = Label(self.frame_2, text="Fator de unidade 1 para unidade 2", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_run_fator.place(relx=0.05, rely=margem_superior + 14*self.altura_campos + 3*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_run_fator = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_run_fator.place(relx=0.05, rely=margem_superior + 15*self.altura_campos + 4*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)


        def btn_incluir_entrar(event):
            botao_incluir.configure(bg="blue", fg="white")
        def btn_incluir_sair(event):
            botao_incluir.configure(bg="white", fg="black")
        botao_incluir = Button(self.frame_2, text="Incluir", bg="white", fg="black", command=self.incluir_run)
        botao_incluir.place(relx=0.10, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_incluir.bind('<Enter>',btn_incluir_entrar)
        botao_incluir.bind('<Leave>',btn_incluir_sair)

        def btn_atualizar_entrar(event):
            botao_atualizar.configure(bg="yellow", fg="black")
        def btn_atualizar_sair(event):
            botao_atualizar.configure(bg="white", fg="black")
        botao_atualizar = Button(self.frame_2, text="Atualizar", bg="white", fg="black", command=self.atualizar_run)
        botao_atualizar.place(relx=0.40, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_atualizar.bind('<Enter>',btn_atualizar_entrar)
        botao_atualizar.bind('<Leave>',btn_atualizar_sair)

        def btn_deletar_entrar(event):
            botao_deletar.configure(bg="red", fg="white")
        def btn_deletar_sair(event):
            botao_deletar.configure(bg="white", fg="black")
        botao_deletar = Button(self.frame_2, text="Deletar", bg="white", fg="black", command=self.deletar_run)
        botao_deletar.place(relx=0.70, rely=0.80, relheight=0.05, relwidth=0.20)
        botao_deletar.bind('<Enter>',btn_deletar_entrar)
        botao_deletar.bind('<Leave>',btn_deletar_sair)

        def btn_limpar_entrar(event):
            botao_limpar.configure(bg="orange", fg="black")
        def btn_limpar_sair(event):
            botao_limpar.configure(bg="white", fg="black")
        botao_limpar = Button(self.frame_2, text="Limpar", bg="white", fg="black", command=self.limpar_run)
        botao_limpar.place(relx=0.10, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_limpar.bind('<Enter>',btn_limpar_entrar)
        botao_limpar.bind('<Leave>',btn_limpar_sair)

        def btn_home_entrar(event):
            botao_home.configure(bg="green", fg="white")
        def btn_home_sair(event):
            botao_home.configure(bg="white", fg="black")
        botao_home = Button(self.frame_2, text="HOME", bg="white", fg="black", command=self.home)
        botao_home.place(relx=0.40, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_home.bind('<Enter>',btn_home_entrar)
        botao_home.bind('<Leave>',btn_home_sair)

        # frame 3
        self.apagar_widgets_frame_3()
        self.criar_tv_run()

        def btn_capturar_entrar(event):
            botao_capturar.configure(bg="pink", fg="black")
        def btn_capturar_sair(event):
            botao_capturar.configure(bg="white", fg="black")
        botao_capturar = Button(self.frame_3, text="Capturar", bg="black", fg="white", command=self.capturar_run)
        botao_capturar.place(relx=0.30, rely=0.90, relheight=0.05, relwidth=0.40)
        botao_capturar.bind('<Enter>',btn_capturar_entrar)
        botao_capturar.bind('<Leave>',btn_capturar_sair)

    def on_select_run_unidade_1(self, event):
        try:
            self.escolha_run_unidade_1.configure(text=self.entry_run_unidade_1.get(self.entry_run_unidade_1.curselection()), bg=self.cor_fundo_entry, fg="black")
        except:
            pass

    def on_select_run_unidade_2(self, event):
        try:
            self.escolha_run_unidade_2.configure(text=self.entry_run_unidade_2.get(self.entry_run_unidade_2.curselection()), bg=self.cor_fundo_entry, fg="black")
        except:
            pass

    def capturar_run(self):
        try:
            Item_Selecionado = self.tv_run.selection()[0]
        except:
            messagebox.showinfo("ERRO","Precisa Selecionar um item.")
            return()
        
        valores_selecionados = self.tv_run.item(Item_Selecionado,"values")

        id_capturado = valores_selecionados[0]
        unidade_1_capturado = valores_selecionados[1]
        unidade_2_capturado = valores_selecionados[2]
        fator_capturado = valores_selecionados[3]

        self.entry_id_run.configure(text=id_capturado)

        self.entry_run_fator.delete(0,END)
        self.entry_run_fator.insert(0,fator_capturado)

        indice = 0
        for item in self.lista_unidades:
            if unidade_1_capturado == item:
                indice_unidade_1 = self.lista_ids_unidades[indice]
            indice += 1

        self.entry_run_unidade_1.selection_clear(0,tk.END)
        self.entry_run_unidade_1.selection_set(indice_unidade_1)
        self.escolha_run_unidade_1.configure(text=self.entry_run_unidade_1.get(self.entry_run_unidade_1.curselection()), bg=self.cor_fundo_entry, fg="black")

        indice = 0
        for item in self.lista_unidades:
            if unidade_2_capturado == item:
                indice_unidade_2 = self.lista_ids_unidades[indice]
            indice += 1

        self.entry_run_unidade_2.selection_clear(0,tk.END)
        self.entry_run_unidade_2.selection_set(indice_unidade_2)
        self.escolha_run_unidade_2.configure(text=self.entry_run_unidade_2.get(self.entry_run_unidade_2.curselection()), bg=self.cor_fundo_entry, fg="black")

    def criar_tv_run(self):

        self.tv_run = ttk.Treeview(self.frame_3, columns=('id','unidade_1','unidade_2','fator'), show='headings')
        self.tv_run.column('id', minwidth=0, width=10)
        self.tv_run.column('unidade_1', minwidth=0, width=50)
        self.tv_run.column('unidade_2', minwidth=0, width=50)
        self.tv_run.column('fator', minwidth=0, width=10)
        
        self.tv_run.heading('id', text="ID")
        self.tv_run.heading('unidade_1', text="Unidade 1")
        self.tv_run.heading('unidade_2', text="Unidade 2")
        self.tv_run.heading('fator', text="Fator de 1 p 2")

        sql = f"SELECT `id`,`unidade_1`,`unidade_2`,`fator_multiplicador_de_1_p_2` FROM {self.tabela}"
        result = executa_DQL(sql)

        for item_result in result:
            indice = 0
            
            for item in self.lista_ids_unidades:
                item_unidade = self.lista_unidades[indice]
                
                if int(item) == item_result[1]:
                    unidade_1 = item_unidade

                if int(item) == item_result[2]:
                    unidade_2 = item_unidade
                
                indice += 1

            self.tv_run.insert("", END, values=(item_result[0], unidade_1, unidade_2, item_result[3]))                  

        self.tv_run.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

    def deletar_run(self):

        id_entry = self.entry_id_run.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        
        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()
               
        sql = f"DELETE FROM `{self.tabela}` WHERE id = {id_entry};"
        result = executa_DML(sql)
        self.criar_tv_run()
        self.limpar_run()
        return()        

    def atualizar_run(self):
        id_entry = self.entry_id_run.cget("text")

        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()

        id_entry = int(id_entry)

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID tipo: {type(id_entry)}.")
            return()

        unidade_1_entry = self.escolha_run_unidade_1.cget("text")
        unidade_2_entry = self.escolha_run_unidade_2.cget("text")

        if len(unidade_1_entry) == 0:
            messagebox.showinfo("ERRO",f"Unidade 1 precisa ser selecionada.")
            return()

        if len(unidade_2_entry) == 0:
            messagebox.showinfo("ERRO",f"Unidade 2 precisa ser selecionada.")
            return()

        if unidade_1_entry == unidade_2_entry:
            messagebox.showinfo("ERRO",f"Unidades precisam ser diferentes para harmonizarem.")
            return()
        
        sql = f"SELECT id_unidade FROM unidades WHERE unidade = '{unidade_1_entry}'"
        result = executa_DQL(sql)
        unid_1_id = result[0][0]

        sql = f"SELECT id_unidade FROM unidades WHERE unidade = '{unidade_2_entry}'"
        result = executa_DQL(sql)
        unid_2_id = result[0][0]

        fator = self.entry_run_fator.get()

        if len(fator) == 0:
            messagebox.showinfo("ERRO",f"Fator precisa ser preenchido.")
            return()

        fator = fator.replace(",",".")

        try:
            fator = float(fator)
        except:
            messagebox.showinfo("ERRO",f"Fator precisa ter valor válido.")
            return()

        sql = f"UPDATE `{self.tabela}` SET unidade_1 = '{unid_1_id}', unidade_2 = '{unid_2_id}', fator_multiplicador_de_1_p_2 = '{fator}' WHERE id = {id_entry};"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo("ERRO","O registro não foi atualizado.")
            print(sql)
            return()          
        
        self.criar_tv_run()
        self.limpar_run()
        return()

    def incluir_run(self):
        unidade_1_entry = self.escolha_run_unidade_1.cget("text")
        unidade_2_entry = self.escolha_run_unidade_2.cget("text")

        if len(unidade_1_entry) == 0:
            messagebox.showinfo("ERRO",f"Unidade 1 precisa ser selecionada.")
            return()

        if len(unidade_2_entry) == 0:
            messagebox.showinfo("ERRO",f"Unidade 2 precisa ser selecionada.")
            return()

        if unidade_1_entry == unidade_2_entry:
            messagebox.showinfo("ERRO",f"Unidades precisam ser diferentes para harmonizarem.")
            return()

        sql = f"SELECT id_unidade FROM unidades WHERE unidade = '{unidade_1_entry}'"
        result = executa_DQL(sql)
        unid_1_id = result[0][0]

        sql = f"SELECT id_unidade FROM unidades WHERE unidade = '{unidade_2_entry}'"
        result = executa_DQL(sql)
        unid_2_id = result[0][0]

        fator = self.entry_run_fator.get()

        if len(fator) == 0:
            messagebox.showinfo("ERRO",f"Fator precisa ser preenchido.")
            return()

        fator = fator.replace(",",".")

        try:
            fator = float(fator)
        except:
            messagebox.showinfo("ERRO",f"Fator precisa ter valor válido.")
            return()

        sql = f"INSERT INTO {self.tabela} (unidade_1, unidade_2, fator_multiplicador_de_1_p_2) VALUES ('{unid_1_id}','{unid_2_id}','{fator}')"
        result = executa_DML(sql)

        if result == False:
            print(sql)
            messagebox.showinfo(title="ERRO", message="Algo deu errado com o banco de dados.")
            return()

        self.criar_tv_run()
        self.limpar_run()
        return()

    def limpar_run(self):
        
        self.entry_run_unidade_1.selection_clear(0,tk.END)
        self.escolha_run_unidade_1.configure(text="escolher", bg="white", fg="red")
        self.on_select_run_unidade_1(Event)

        self.entry_run_unidade_2.selection_clear(0,tk.END)
        self.escolha_run_unidade_2.configure(text="escolher", bg="white", fg="red")
        self.on_select_run_unidade_2(Event)


    def processo_feitura_produto_energia(self):
        self.tabela = "processo_feitura_produtos_energia"

        abc = self.listagem_produtos()

        self.lista_ids_produtos = abc[0]
        self.lista_produtos = abc[1]

        if len(self.lista_ids_produtos) == 0:
            messagebox.showinfo("Faltam dados","Produtos necessita(m) de algu(ns) dado(s).")
            self.home()

       
        self.apagar_widgets_frame_3()

        # frame_1
        self.label_frame_1.configure(text="Insumos Secundários para o Processo de Feitura de Produtos.")

        # frame 2
        self.apagar_widgets_frame_2()
        
        qtde_labels_e_entrys = 3
        adicional_tamanhos_listbox = 3

        self.altura_campos = 0.03
        self.espaco_interno = 0.004
        self.espaco_externo = 0.01

        margem_superior = ((1-self.espaco_para_botoes)-((qtde_labels_e_entrys*2+adicional_tamanhos_listbox)*self.altura_campos)-(qtde_labels_e_entrys*self.espaco_interno)-((qtde_labels_e_entrys-1)*self.espaco_externo))/2

        self.label_id_pfe = Label(self.frame_2, text="ID", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_id_pfe.place(relx=0.05, rely=margem_superior, relwidth=0.90, relheight=self.altura_campos)

        self.entry_id_pfe = Label(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, text="novo")
        self.entry_id_pfe.place(relx=0.05, rely=margem_superior + self.altura_campos + self.espaco_interno, relwidth=0.90, relheight=self.altura_campos)

        self.label_pfe = Label(self.frame_2, text="selecione o Produto", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_pfe.place(relx=0.05, rely=margem_superior + 2*self.altura_campos + self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_pfe_produto = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox)      
       
        indice = 0
        for id in self.lista_ids_produtos:
            produto = self.lista_produtos[indice]
            self.entry_pfe_produto.insert(id, produto)
            indice += 1

        self.scbar_pfe_produto = Scrollbar(self.entry_pfe_produto, orient=VERTICAL)
        self.scbar_pfe_produto.config(command=self.entry_pfe_produto.yview)
        self.scbar_pfe_produto.pack(side=RIGHT, fill=Y)

        self.entry_pfe_produto.configure(yscrollcommand=self.scbar_pfe_produto.set)
        self.entry_pfe_produto.place(relx=0.05, rely=margem_superior + 3*self.altura_campos + 2*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_pfe_produto.bind('<<ListboxSelect>>',self.on_select_pfe_produto)

        self.escolha_pfe_produto = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_pfe_produto.place(relx=0.05, rely=margem_superior + 7*self.altura_campos + 3*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_pfe_potencia_w = Label(self.frame_2, text="potencia_w", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_pfe_potencia_w.place(relx=0.375, rely=margem_superior + 22*self.altura_campos + 7*self.espaco_interno + 5*self.espaco_externo, relwidth=0.25, relheight=self.altura_campos)

        self.entry_pfe_potencia_w = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_pfe_potencia_w.place(relx=0.375, rely=margem_superior + 23*self.altura_campos + 8*self.espaco_interno + 5*self.espaco_externo, relwidth=0.25, relheight=self.altura_campos)
        self.entry_pfe_potencia_w.insert(0,0)

        self.label_pfe_tempo_energia_eletrica = Label(self.frame_2, text="tempo energia (min)", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_pfe_tempo_energia_eletrica.place(relx=0.70, rely=margem_superior + 22*self.altura_campos + 7*self.espaco_interno + 5*self.espaco_externo, relwidth=0.25, relheight=self.altura_campos)

        self.entry_pfe_tempo_energia_eletrica = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_pfe_tempo_energia_eletrica.place(relx=0.70, rely=margem_superior + 23*self.altura_campos + 8*self.espaco_interno + 5*self.espaco_externo, relwidth=0.25, relheight=self.altura_campos)
        self.entry_pfe_tempo_energia_eletrica.insert(0,0)

        def btn_incluir_entrar(event):
            botao_incluir.configure(bg="blue", fg="white")
        def btn_incluir_sair(event):
            botao_incluir.configure(bg="white", fg="black")
        botao_incluir = Button(self.frame_2, text="Incluir", bg="white", fg="black", command=self.incluir_pfe)
        botao_incluir.place(relx=0.10, rely=0.90, relheight=0.035, relwidth=0.20)
        botao_incluir.bind('<Enter>',btn_incluir_entrar)
        botao_incluir.bind('<Leave>',btn_incluir_sair)

        def btn_atualizar_entrar(event):
            botao_atualizar.configure(bg="yellow", fg="black")
        def btn_atualizar_sair(event):
            botao_atualizar.configure(bg="white", fg="black")
        botao_atualizar = Button(self.frame_2, text="Atualizar", bg="white", fg="black", command=self.atualizar_pfe)
        botao_atualizar.place(relx=0.40, rely=0.90, relheight=0.035, relwidth=0.20)
        botao_atualizar.bind('<Enter>',btn_atualizar_entrar)
        botao_atualizar.bind('<Leave>',btn_atualizar_sair)

        def btn_deletar_entrar(event):
            botao_deletar.configure(bg="red", fg="white")
        def btn_deletar_sair(event):
            botao_deletar.configure(bg="white", fg="black")
        botao_deletar = Button(self.frame_2, text="Deletar", bg="white", fg="black", command=self.deletar_pfe)
        botao_deletar.place(relx=0.70, rely=0.90, relheight=0.035, relwidth=0.20)
        botao_deletar.bind('<Enter>',btn_deletar_entrar)
        botao_deletar.bind('<Leave>',btn_deletar_sair)

        def btn_limpar_entrar(event):
            botao_limpar.configure(bg="orange", fg="black")
        def btn_limpar_sair(event):
            botao_limpar.configure(bg="white", fg="black")
        botao_limpar = Button(self.frame_2, text="Limpar", bg="white", fg="black", command=self.limpar_pfe)
        botao_limpar.place(relx=0.10, rely=0.95, relheight=0.035, relwidth=0.20)
        botao_limpar.bind('<Enter>',btn_limpar_entrar)
        botao_limpar.bind('<Leave>',btn_limpar_sair)

        def btn_home_entrar(event):
            botao_home.configure(bg="green", fg="white")
        def btn_home_sair(event):
            botao_home.configure(bg="white", fg="black")
        botao_home = Button(self.frame_2, text="HOME", bg="white", fg="black", command=self.home)
        botao_home.place(relx=0.40, rely=0.95, relheight=0.035, relwidth=0.20)
        botao_home.bind('<Enter>',btn_home_entrar)
        botao_home.bind('<Leave>',btn_home_sair)

        def btn_ativar_entrar(event):
            botao_ativar.configure(bg="purple", fg="white")
        def btn_ativar_sair(event):
            botao_ativar.configure(bg="white", fg="black")
        botao_ativar = Button(self.frame_2, text="Ativar", bg="white", fg="black", command=self.ativar_pfe)
        botao_ativar.place(relx=0.70, rely=0.95, relheight=0.035, relwidth=0.20)
        botao_ativar.bind('<Enter>',btn_ativar_entrar)
        botao_ativar.bind('<Leave>',btn_ativar_sair)

        # frame 3
        self.criar_tv_pfe()

        def btn_capturar_entrar(event):
            botao_capturar.configure(bg="pink", fg="black")
        def btn_capturar_sair(event):
            botao_capturar.configure(bg="white", fg="black")
        botao_capturar = Button(self.frame_3, text="Capturar", bg="black", fg="white", command=self.capturar_pfe)
        botao_capturar.place(relx=0.30, rely=0.90, relheight=0.05, relwidth=0.40)
        botao_capturar.bind('<Enter>',btn_capturar_entrar)
        botao_capturar.bind('<Leave>',btn_capturar_sair)

    def on_select_pfe_produto(self, event):
        try:
            produto = self.entry_pfe_produto.get(self.entry_pfe_produto.curselection())
            self.escolha_pfe_produto.configure(text=produto, bg=self.cor_fundo_entry, fg="black")           
            sql = f"SELECT `id_produto` FROM `produtos` WHERE `produto` = '{produto}'"
            result = executa_DQL(sql)
            id_produto = result[0][0]
            #self.aviso_pfe(produto,id_produto)
            self.criar_tv_pfe()
        except:
            print(sql)
            messagebox.showinfo("erro",sql)

    def on_select_pfe_produto_origin(self, event):
        try:
            produto = self.entry_pfe_produto.get(self.entry_pfe_produto.curselection())
            self.escolha_pfe_produto.configure(text=produto, bg=self.cor_fundo_entry, fg="black")           
        except:
            pass

    def capturar_pfe(self):

        try:
            Item_Selecionado = self.tv_pfe.selection()[0]
        except:
            messagebox.showinfo("ERRO","Precisa Selecionar um item.")
            return()
                                
        valores_selecionados = self.tv_pfe.item(Item_Selecionado,"values")
        
        id_capturado = valores_selecionados[0]
        produto_capturado = valores_selecionados[1]
        potencia_w_capturado = valores_selecionados[2]
        tempo_energia_eletrica_capturado = valores_selecionados[3]

        self.entry_id_pfe.configure(text=id_capturado)

        self.entry_pfe_potencia_w.delete(0,END)
        self.entry_pfe_potencia_w.insert(0,potencia_w_capturado)

        self.entry_pfe_tempo_energia_eletrica.delete(0,END)
        self.entry_pfe_tempo_energia_eletrica.insert(0,tempo_energia_eletrica_capturado)
        
        sql = f"SELECT `id_produto` FROM produtos WHERE `produto` = '{produto_capturado}'"
        result = executa_DQL(sql)
        id_produto = result[0][0]

        self.entry_pfe_produto.selection_clear(0,tk.END)
        self.entry_pfe_produto.selection_set(id_produto)
        self.escolha_pfe_produto.configure(text=produto_capturado, bg=self.cor_fundo_entry, fg="black")

        return()

    def criar_tv_pfe(self):
        self.tv_pfe = ttk.Treeview(self.frame_3, columns=('id','produto','potencia_w','tempo_energia_eletrica','ativo'), show='headings')
        
        self.tv_pfe.column('id', minwidth=0, width=4)
        self.tv_pfe.column('produto', minwidth=0, width=50)
        self.tv_pfe.column('potencia_w', minwidth=0, width=4)
        self.tv_pfe.column('tempo_energia_eletrica', minwidth=0, width=4)
        self.tv_pfe.column('ativo', minwidth=0, width=4)
        
        self.tv_pfe.heading('id', text="ID")
        self.tv_pfe.heading('unidade', text="Unidade")
        self.tv_pfe.heading('potencia_w', text="Potência")
        self.tv_pfe.heading('tempo_energia_eletrica', text="Tempo(min)")
        self.tv_pfe.heading('ativo', text="Ativo")      

        produto_entry = self.escolha_pfe_produto.cget("text")

        if produto_entry == 'escolher':
            sql = f"SELECT `id_pfe`,`produto_id`,`potencia_w`,`tempo_energia_eletrica`,`ativo` FROM `{self.tabela}`"            
        else:
            sql = f"SELECT `id_produto` FROM `produtos` WHERE `produto` = '{produto_entry}'"
            result = executa_DQL(sql)
            id_produto = result[0][0]

            sql = f"SELECT `id_pfe`,`produto_id`,`potencia_w`,`tempo_energia_eletrica`,`ativo` FROM `{self.tabela}` WHERE `produto_id` = '{id_produto}'"
        result = executa_DQL(sql)

        for item_result in result:
            sql = f"SELECT `produto` FROM `produtos` WHERE `id_produto` = '{item_result[1]}'"
            result = executa_DQL(sql)
            item_produto = result[0][0]

            self.tv_pfe.insert("", item_result[0], values=(item_result[0], item_produto, item_result[2], item_result[3], item_result[4]))

        self.tv_pfe.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)
      
    def deletar_pfe(self):
        id_entry = self.entry_id_pfe.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        
        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()
                    
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '0' WHERE id_pfe = {id_entry};"
        result = executa_DML(sql)

        self.criar_tv_pfe()
        self.limpar_pfe()
        return()        

    def atualizar_pfe(self):

        id_entry = self.entry_id_pfe.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()

        produto_entry = self.escolha_pfe_produto.cget("text")
        if len(produto_entry)==0 or produto_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Produto precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_produto` FROM produtos WHERE `produto` = '{produto_entry}'"
        result = executa_DQL(sql)
        id_produto = result[0][0]

        potencia_w = self.entry_pfe_potencia_w.get()
        potencia_w = potencia_w.replace(",",".")
        
        if len(potencia_w) == 0:
            messagebox.showinfo("Em branco","Campo potencia_w precisa ser preenchido.")
            return()

        try:
            potencia_w = float(potencia_w)
        except:
            messagebox.showinfo("ERRO","Campo potencia_w não válido.")
            return()

        tempo_energia_eletrica = self.entry_pfe_tempo_energia_eletrica.get()
        tempo_energia_eletrica = tempo_energia_eletrica.replace(",",".")
        
        if len(tempo_energia_eletrica) == 0:
            messagebox.showinfo("Em branco","Campo tempo de potencia_w precisa ser preenchido.")
            return()

        try:
            tempo_energia_eletrica = float(tempo_energia_eletrica)
        except:
            messagebox.showinfo("ERRO","Campo tempo de potencia_w não válido.")
            return()

        sql = f"UPDATE `{self.tabela}` SET `produto_id` = '{id_produto}', `potencia_w` = '{potencia_w}', `tempo_energia_eletrica` = '{tempo_energia_eletrica}' WHERE `id_pfe` = {id_entry};"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo("ERRO","O registro não foi atualizado.")
            print(sql)
            return()          

        self.criar_tv_pfe()
        self.limpar_pfe()
        return()

    def incluir_pfe(self):
   
        id_entry = self.entry_id_pfe.cget("text")
        if id_entry != 'novo':
            messagebox.showinfo("ERRO",f"Incluir precisa de ID como `novo`.")
            return()

        produto_entry = self.escolha_pfe_produto.cget("text")
        if len(produto_entry)==0 or produto_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Produto precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_produto` FROM produtos WHERE `produto` = '{produto_entry}'"
        result = executa_DQL(sql)
        id_produto = result[0][0]

        potencia_w = self.entry_pfe_potencia_w.get()
        potencia_w = potencia_w.replace(",",".")
        
        if len(potencia_w) == 0:
            messagebox.showinfo("Em branco","Campo potencia_w precisa ser preenchido.")
            return()

        try:
            potencia_w = float(potencia_w)
        except:
            messagebox.showinfo("ERRO","Campo potencia_w não válido.")
            return()

        tempo_energia_eletrica = self.entry_pfe_tempo_energia_eletrica.get()
        tempo_energia_eletrica = tempo_energia_eletrica.replace(",",".")
        
        if len(tempo_energia_eletrica) == 0:
            messagebox.showinfo("Em branco","Campo tempo de potencia_w precisa ser preenchido.")
            return()
        try:
            tempo_energia_eletrica = float(tempo_energia_eletrica)
        except:
            messagebox.showinfo("ERRO","Campo tempo de potencia_w não válido.")
            return()

        sql = f"INSERT INTO {self.tabela} (`produto_id`, `potencia_w`, `tempo_energia_eletrica`, `ativo`) VALUES ('{id_produto}','{potencia_w}','{tempo_energia_eletrica}','1');"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo(title="ERRO", message=f"Algo deu errado com o banco de dados. {sql}")
            return()

        self.criar_tv_pfe()
        self.limpar_pfe()
        return()

    def limpar_pfe(self):

        self.entry_pfe_potencia_w.delete(0,END)
        self.entry_pfe_potencia_w.insert(0,0)

        self.entry_pfe_tempo_energia_eletrica.delete(0,END)
        self.entry_pfe_tempo_energia_eletrica.insert(0,0)

        self.entry_id_pfe.configure(text="novo")

        self.entry_pfe_produto.selection_clear(0,tk.END)
        self.escolha_pfe_produto.configure(text="escolher", bg="white", fg="red")
        self.on_select_pfe_produto_origin(Event)

    def ativar_pfe(self):
        id_entry = self.entry_id_pfe.cget("text")

        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()     
               
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '1' WHERE id_pfe = {id_entry};"
        result = executa_DML(sql)

        #self.aviso_pfe(produto_entry,id_produto)
        self.criar_tv_pfe()
        self.limpar_pfe()
        return()





    def processo_feitura_produto_insumos(self):
        self.tabela = "processo_feitura_produtos_insumos"

        abc = self.listagem_unidades()

        self.lista_ids_unidades = abc[0]
        self.lista_unidades = abc[1]

        if len(self.lista_ids_unidades) == 0:
            messagebox.showinfo("Faltam dados","Unidades necessitam de algu(ns) dado(s).")
            self.home()

        abc = self.listagem_produtos()

        self.lista_ids_produtos = abc[0]
        self.lista_produtos = abc[1]

        if len(self.lista_ids_produtos) == 0:
            messagebox.showinfo("Faltam dados","Produtos necessita(m) de algu(ns) dado(s).")
            self.home()

        abc = self.listagem_insumos()

        self.lista_ids_insumos = abc[0]
        self.lista_insumos = abc[1]

        if len(self.lista_ids_insumos) == 0:
            messagebox.showinfo("Faltam dados","Insumos necessita(m) de algu(ns) dado(s).")
            self.home()
        
        self.apagar_widgets_frame_3()

        # frame_1
        self.label_frame_1.configure(text="Insumos Secundários para o Processo de Feitura de Produtos.")

        # frame 2
        self.apagar_widgets_frame_2()
        
        qtde_labels_e_entrys = 4
        adicional_tamanhos_listbox = 9

        self.altura_campos = 0.03
        self.espaco_interno = 0.004
        self.espaco_externo = 0.01

        margem_superior = ((1-self.espaco_para_botoes)-((qtde_labels_e_entrys*2+adicional_tamanhos_listbox)*self.altura_campos)-(qtde_labels_e_entrys*self.espaco_interno)-((qtde_labels_e_entrys-1)*self.espaco_externo))/2

        self.label_id_pfi = Label(self.frame_2, text="ID", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_id_pfi.place(relx=0.05, rely=margem_superior, relwidth=0.90, relheight=self.altura_campos)

        self.entry_id_pfi = Label(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, text="novo")
        self.entry_id_pfi.place(relx=0.05, rely=margem_superior + self.altura_campos + self.espaco_interno, relwidth=0.90, relheight=self.altura_campos)

        self.label_pfi = Label(self.frame_2, text="selecione o Produto", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_pfi.place(relx=0.05, rely=margem_superior + 2*self.altura_campos + self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_pfi_produto = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox)      
       
        indice = 0
        for id in self.lista_ids_produtos:
            produto = self.lista_produtos[indice]
            self.entry_pfi_produto.insert(id, produto)
            indice += 1

        self.scbar_pfi_produto = Scrollbar(self.entry_pfi_produto, orient=VERTICAL)
        self.scbar_pfi_produto.config(command=self.entry_pfi_produto.yview)
        self.scbar_pfi_produto.pack(side=RIGHT, fill=Y)

        self.entry_pfi_produto.configure(yscrollcommand=self.scbar_pfi_produto.set)
        self.entry_pfi_produto.place(relx=0.05, rely=margem_superior + 3*self.altura_campos + 2*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_pfi_produto.bind('<<ListboxSelect>>',self.on_select_pfi_produto)

        self.escolha_pfi_produto = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_pfi_produto.place(relx=0.05, rely=margem_superior + 7*self.altura_campos + 3*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_pfi_insumo = Label(self.frame_2, text="selecione o insumo", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_pfi_insumo.place(relx=0.05, rely=margem_superior + 8*self.altura_campos + 3*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_pfi_insumo = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox)

        indice = 0        
        for id in self.lista_ids_insumos:
            insumo = self.lista_insumos[indice]
            self.entry_pfi_insumo.insert(id, insumo)
            indice += 1

        self.scbar_pfi_insumo = Scrollbar(self.entry_pfi_insumo, orient=VERTICAL)
        self.scbar_pfi_insumo.config(command=self.entry_pfi_insumo.yview)
        self.scbar_pfi_insumo.pack(side=RIGHT, fill=Y)       

        self.entry_pfi_insumo.configure(yscrollcommand=self.scbar_pfi_insumo.set)
        self.entry_pfi_insumo.place(relx=0.05, rely=margem_superior + 9*self.altura_campos + 4*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_pfi_insumo.bind('<<ListboxSelect>>',self.on_select_pfi_insumo)

        self.escolha_pfi_insumo = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_pfi_insumo.place(relx=0.05, rely=margem_superior + 13*self.altura_campos + 5*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_pfi_mensuracao = Label(self.frame_2, text="mensuração", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_pfi_mensuracao.place(relx=0.05, rely=margem_superior + 14*self.altura_campos + 5*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_pfi_mensuracao = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_pfi_mensuracao.place(relx=0.05, rely=margem_superior + 15*self.altura_campos + 5*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_pfi_unidade = Label(self.frame_2, text="unidade", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_pfi_unidade.place(relx=0.05, rely=margem_superior + 16*self.altura_campos + 5*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_pfi_unidade = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox, selectmode=SINGLE)

        indice = 0        
        for id in self.lista_ids_unidades:
            unidade = self.lista_unidades[indice]
            self.entry_pfi_unidade.insert(id,unidade)
            indice += 1

        self.scbar_pfi_unidade = Scrollbar(self.entry_pfi_unidade, orient=VERTICAL)
        self.scbar_pfi_unidade.config(command=self.entry_pfi_unidade.yview)
        self.scbar_pfi_unidade.pack(side=RIGHT, fill=Y)

        self.entry_pfi_unidade.configure(yscrollcommand=self.scbar_pfi_unidade.set)
        self.entry_pfi_unidade.place(relx=0.05, rely=margem_superior + 17*self.altura_campos + 6*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_pfi_unidade.bind('<<ListboxSelect>>',self.on_select_pfi_unidade)

        self.escolha_pfi_unidade = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_pfi_unidade.place(relx=0.05, rely=margem_superior + 21*self.altura_campos + 7*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        def btn_incluir_entrar(event):
            botao_incluir.configure(bg="blue", fg="white")
        def btn_incluir_sair(event):
            botao_incluir.configure(bg="white", fg="black")
        botao_incluir = Button(self.frame_2, text="Incluir", bg="white", fg="black", command=self.incluir_pfi)
        botao_incluir.place(relx=0.10, rely=0.90, relheight=0.035, relwidth=0.20)
        botao_incluir.bind('<Enter>',btn_incluir_entrar)
        botao_incluir.bind('<Leave>',btn_incluir_sair)

        def btn_atualizar_entrar(event):
            botao_atualizar.configure(bg="yellow", fg="black")
        def btn_atualizar_sair(event):
            botao_atualizar.configure(bg="white", fg="black")
        botao_atualizar = Button(self.frame_2, text="Atualizar", bg="white", fg="black", command=self.atualizar_pfi)
        botao_atualizar.place(relx=0.40, rely=0.90, relheight=0.035, relwidth=0.20)
        botao_atualizar.bind('<Enter>',btn_atualizar_entrar)
        botao_atualizar.bind('<Leave>',btn_atualizar_sair)

        def btn_deletar_entrar(event):
            botao_deletar.configure(bg="red", fg="white")
        def btn_deletar_sair(event):
            botao_deletar.configure(bg="white", fg="black")
        botao_deletar = Button(self.frame_2, text="Deletar", bg="white", fg="black", command=self.deletar_pfi)
        botao_deletar.place(relx=0.70, rely=0.90, relheight=0.035, relwidth=0.20)
        botao_deletar.bind('<Enter>',btn_deletar_entrar)
        botao_deletar.bind('<Leave>',btn_deletar_sair)

        def btn_limpar_entrar(event):
            botao_limpar.configure(bg="orange", fg="black")
        def btn_limpar_sair(event):
            botao_limpar.configure(bg="white", fg="black")
        botao_limpar = Button(self.frame_2, text="Limpar", bg="white", fg="black", command=self.limpar_pfi)
        botao_limpar.place(relx=0.10, rely=0.95, relheight=0.035, relwidth=0.20)
        botao_limpar.bind('<Enter>',btn_limpar_entrar)
        botao_limpar.bind('<Leave>',btn_limpar_sair)

        def btn_home_entrar(event):
            botao_home.configure(bg="green", fg="white")
        def btn_home_sair(event):
            botao_home.configure(bg="white", fg="black")
        botao_home = Button(self.frame_2, text="HOME", bg="white", fg="black", command=self.home)
        botao_home.place(relx=0.40, rely=0.95, relheight=0.035, relwidth=0.20)
        botao_home.bind('<Enter>',btn_home_entrar)
        botao_home.bind('<Leave>',btn_home_sair)

        def btn_ativar_entrar(event):
            botao_ativar.configure(bg="purple", fg="white")
        def btn_ativar_sair(event):
            botao_ativar.configure(bg="white", fg="black")
        botao_ativar = Button(self.frame_2, text="Ativar", bg="white", fg="black", command=self.ativar_pfi)
        botao_ativar.place(relx=0.70, rely=0.95, relheight=0.035, relwidth=0.20)
        botao_ativar.bind('<Enter>',btn_ativar_entrar)
        botao_ativar.bind('<Leave>',btn_ativar_sair)

        # frame 3
        self.criar_tv_pfi()

        def btn_capturar_entrar(event):
            botao_capturar.configure(bg="pink", fg="black")
        def btn_capturar_sair(event):
            botao_capturar.configure(bg="white", fg="black")
        botao_capturar = Button(self.frame_3, text="Capturar", bg="black", fg="white", command=self.capturar_pfi)
        botao_capturar.place(relx=0.30, rely=0.90, relheight=0.05, relwidth=0.40)
        botao_capturar.bind('<Enter>',btn_capturar_entrar)
        botao_capturar.bind('<Leave>',btn_capturar_sair)

    def on_select_pfi_produto(self, event):
        try:
            produto = self.entry_pfi_produto.get(self.entry_pfi_produto.curselection())
            self.escolha_pfi_produto.configure(text=produto, bg=self.cor_fundo_entry, fg="black")           
            sql = f"SELECT `id_produto` FROM `produtos` WHERE `produto` = '{produto}'"
            result = executa_DQL(sql)
            id_produto = result[0][0]
            #self.aviso_pfi(produto,id_produto)
            self.criar_tv_pfi()
        except:
            print(sql)
            messagebox.showinfo("erro",sql)

    def on_select_pfi_produto_origin(self, event):
        try:
            produto = self.entry_pfi_produto.get(self.entry_pfi_produto.curselection())
            self.escolha_pfi_produto.configure(text=produto, bg=self.cor_fundo_entry, fg="black")           
        except:
            pass

    def on_select_pfi_insumo(self, event):
        try:
            self.escolha_pfi_insumo.configure(text=self.entry_pfi_insumo.get(self.entry_pfi_insumo.curselection()), bg=self.cor_fundo_entry, fg="black")
        except:
            pass

    def on_select_pfi_unidade(self, event):
        try:
            self.escolha_pfi_unidade.configure(text=self.entry_pfi_unidade.get(self.entry_pfi_unidade.curselection()), bg=self.cor_fundo_entry, fg="black")
        except:
            pass

    def capturar_pfi(self):

        try:
            Item_Selecionado = self.tv_pfi.selection()[0]
        except:
            messagebox.showinfo("ERRO","Precisa Selecionar um item.")
            return()
                                
        valores_selecionados = self.tv_pfi.item(Item_Selecionado,"values")
        
        id_capturado = valores_selecionados[0]
        produto_capturado = valores_selecionados[1]
        insumo_capturado = valores_selecionados[2]
        mensuracao_capturada = valores_selecionados[3]
        unidade_capturada = valores_selecionados[4]

        self.entry_id_pfi.configure(text=id_capturado)
        
        self.entry_pfi_mensuracao.delete(0,END)
        self.entry_pfi_mensuracao.insert(0,mensuracao_capturada)

        sql = f"SELECT `id_insumo` FROM insumos WHERE `insumo` = '{insumo_capturado}'"
        result = executa_DQL(sql)
        id_insumo = result[0][0]

        sql = f"SELECT `id_unidade` FROM unidades WHERE `unidade` = '{unidade_capturada}'"
        result = executa_DQL(sql)
        id_unidade = result[0][0]
        
        sql = f"SELECT `id_produto` FROM produtos WHERE `produto` = '{produto_capturado}'"
        result = executa_DQL(sql)
        id_produto = result[0][0]

        self.entry_pfi_produto.selection_clear(0,tk.END)
        self.entry_pfi_produto.selection_set(id_produto)
        self.escolha_pfi_produto.configure(text=produto_capturado, bg=self.cor_fundo_entry, fg="black")

        self.entry_pfi_insumo.selection_clear(0,tk.END)
        self.entry_pfi_insumo.selection_set(id_insumo)
        self.escolha_pfi_insumo.configure(text=insumo_capturado, bg=self.cor_fundo_entry, fg="black")

        self.entry_pfi_unidade.selection_clear(0,tk.END)
        self.entry_pfi_unidade.selection_set(id_unidade)
        self.escolha_pfi_unidade.configure(text=unidade_capturada, bg=self.cor_fundo_entry, fg="black")

        return()

    def criar_tv_pfi(self):
        self.tv_pfi = ttk.Treeview(self.frame_3, columns=('id','produto','insumo','mensuracao','unidade','ativo'), show='headings')
        
        self.tv_pfi.column('id', minwidth=0, width=4)
        self.tv_pfi.column('produto', minwidth=0, width=50)
        self.tv_pfi.column('insumo', minwidth=0, width=150)
        self.tv_pfi.column('mensuracao', minwidth=0, width=4)
        self.tv_pfi.column('unidade', minwidth=0, width=4)
        self.tv_pfi.column('ativo', minwidth=0, width=4)
        
        self.tv_pfi.heading('id', text="ID")
        self.tv_pfi.heading('produto', text="Produto")
        self.tv_pfi.heading('insumo', text="Insumo")
        self.tv_pfi.heading('mensuracao', text="Mensuração")
        self.tv_pfi.heading('unidade', text="Unidade")
        self.tv_pfi.heading('ativo', text="Ativo")      

        produto_entry = self.escolha_pfi_produto.cget("text")

        if produto_entry == 'escolher':
            sql = f"SELECT `id_pfi`,`produto_id`,`insumo_id`,`mensuracao`,`unidade_id`,`ativo` FROM `{self.tabela}`"            
        else:
            sql = f"SELECT `id_produto` FROM `produtos` WHERE `produto` = '{produto_entry}'"
            result = executa_DQL(sql)
            id_produto = result[0][0]
            sql = f"SELECT `id_pfi`,`produto_id`,`insumo_id`,`mensuracao`,`unidade_id`,`ativo` FROM `{self.tabela}` WHERE `produto_id` = '{id_produto}'"
        result = executa_DQL(sql)

        for item_result in result:
            sql = f"SELECT `produto` FROM `produtos` WHERE `id_produto` = '{item_result[1]}'"
            result = executa_DQL(sql)
            item_produto = result[0][0]

            sql = f"SELECT `insumo` FROM `insumos` WHERE `id_insumo` = '{item_result[2]}'"
            result = executa_DQL(sql)
            item_insumo = result[0][0]

            sql = f"SELECT `unidade` FROM `unidades` WHERE `id_unidade` = '{item_result[4]}'"
            result = executa_DQL(sql)
            item_unidade = result[0][0]

            self.tv_pfi.insert("", item_result[0], values=(item_result[0], item_produto, item_insumo, item_result[3], item_unidade, item_result[5]))

        self.tv_pfi.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)
      
    def deletar_pfi(self):
        id_entry = self.entry_id_pfi.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        
        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()
                    
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '0' WHERE id_pfi = {id_entry};"
        result = executa_DML(sql)

        self.criar_tv_pfi()
        self.limpar_pfi()
        return()        

    def atualizar_pfi(self):

        id_entry = self.entry_id_pfi.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()

        insumo_entry = self.escolha_pfi_insumo.cget("text")
        if len(insumo_entry) == 0 or insumo_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Insumos precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_insumo` FROM insumos WHERE `insumo` = '{insumo_entry}'"
        result = executa_DQL(sql)
        id_insumo = result[0][0]

        
        unidade_entry = self.escolha_pfi_unidade.cget("text")
        if len(unidade_entry) == 0 or unidade_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Unidade precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_unidade` FROM unidades WHERE `unidade` = '{unidade_entry}'"
        result = executa_DQL(sql)
        id_unidade = result[0][0]

        produto_entry = self.escolha_pfi_produto.cget("text")
        if len(produto_entry)==0 or produto_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Produto precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_produto` FROM produtos WHERE `produto` = '{produto_entry}'"
        result = executa_DQL(sql)
        id_produto = result[0][0]

        mensuracao = self.entry_pfi_mensuracao.get()
        mensuracao = mensuracao.replace(",",".")
        
        if len(self.entry_pfi_mensuracao.get()) == 0:
            messagebox.showinfo("Em branco","Campo mensuracao precisa ser preenchido.")
            return()

        try:
            mensuracao = float(mensuracao)
        except:
            messagebox.showinfo("ERRO","Campo mensuracao não válido.")
            return()

        sql = f"UPDATE `{self.tabela}` SET `produto_id` = '{id_produto}', `insumo_id` = '{id_insumo}', `mensuracao`='{mensuracao}', `unidade_id` = '{id_unidade}' WHERE `id_pfi` = {id_entry};"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo("ERRO","O registro não foi atualizado.")
            print(sql)
            return()          

        self.criar_tv_pfi()
        self.limpar_pfi()
        return()

    def incluir_pfi(self):
   
        id_entry = self.entry_id_pfi.cget("text")
        if id_entry != 'novo':
            messagebox.showinfo("ERRO",f"Incluir precisa de ID como `novo`.")
            return()

        insumo_entry = self.escolha_pfi_insumo.cget("text")
        if len(insumo_entry) == 0 or insumo_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Insumos precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_insumo` FROM insumos WHERE `insumo` = '{insumo_entry}'"
        result = executa_DQL(sql)
        id_insumo = result[0][0]

        
        unidade_entry = self.escolha_pfi_unidade.cget("text")
        if len(unidade_entry) == 0 or unidade_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Unidade precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_unidade` FROM unidades WHERE `unidade` = '{unidade_entry}'"
        result = executa_DQL(sql)
        id_unidade = result[0][0]
        print(id_unidade, unidade_entry)

        produto_entry = self.escolha_pfi_produto.cget("text")
        if len(produto_entry)==0 or produto_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Produto precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_produto` FROM produtos WHERE `produto` = '{produto_entry}'"
        result = executa_DQL(sql)
        id_produto = result[0][0]

        mensuracao = self.entry_pfi_mensuracao.get()
        mensuracao = mensuracao.replace(",",".")
        
        if len(self.entry_pfi_mensuracao.get()) == 0:
            messagebox.showinfo("Em branco","Campo mensuracao precisa ser preenchido.")
            return()

        try:
            mensuracao = float(mensuracao)
        except:
            messagebox.showinfo("ERRO","Campo mensuracao não válido.")
            return()

        sql = f"INSERT INTO {self.tabela} (`produto_id`, `insumo_id`, `mensuracao`, `unidade_id`, `ativo`) VALUES ('{id_produto}','{id_insumo}','{mensuracao}','{id_unidade}','1');"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo(title="ERRO", message=f"Algo deu errado com o banco de dados. {sql}")
            return()

        #self.aviso_pfi(produto_entry,id_produto)
        self.criar_tv_pfi()
        self.limpar_pfi()
        return()

    def limpar_pfi(self):

        self.entry_pfi_mensuracao.delete(0,END)

        self.entry_id_pfi.configure(text="novo")

        self.entry_pfi_produto.selection_clear(0,tk.END)
        self.escolha_pfi_produto.configure(text="escolher", bg="white", fg="red")
        self.on_select_pfi_produto_origin(Event)

        self.entry_pfi_insumo.selection_clear(0,tk.END)
        self.escolha_pfi_insumo.configure(text="escolher", bg="white", fg="red")
        self.on_select_pfi_insumo(Event)

        self.entry_pfi_unidade.selection_clear(0,tk.END)
        self.escolha_pfi_unidade.configure(text="escolher", bg="white", fg="red")
        self.on_select_pfi_unidade(Event)

    def ativar_pfi(self):
        id_entry = self.entry_id_pfi.cget("text")

        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()     
               
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '1' WHERE id_pfi = {id_entry};"
        result = executa_DML(sql)

        #self.aviso_pfi(produto_entry,id_produto)
        self.criar_tv_pfi()
        self.limpar_pfi()
        return()



    def finalizacao_produtos(self):
        self.tabela = "finalizacao_produtos"

        abc = self.listagem_unidades()

        self.lista_ids_unidades = abc[0]
        self.lista_unidades = abc[1]

        if len(self.lista_ids_unidades) == 0:
            messagebox.showinfo("Faltam dados","Unidades necessitam de algu(ns) dado(s).")
            self.home()

        abc = self.listagem_produtos()

        self.lista_ids_produtos = abc[0]
        self.lista_produtos = abc[1]

        if len(self.lista_ids_produtos) == 0:
            messagebox.showinfo("Faltam dados","Produtos necessita(m) de algu(ns) dado(s).")
            self.home()

        abc = self.listagem_insumos()

        self.lista_ids_insumos = abc[0]
        self.lista_insumos = abc[1]

        if len(self.lista_ids_insumos) == 0:
            messagebox.showinfo("Faltam dados","Insumos necessita(m) de algu(ns) dado(s).")
            self.home()
        
        self.apagar_widgets_frame_3()

        # frame_1
        self.label_frame_1.configure(text="Insumos na Finalização do Produtos")

        # frame 2
        self.apagar_widgets_frame_2()
        
        qtde_labels_e_entrys = 6
        adicional_tamanhos_listbox = 9

        self.altura_campos = 0.03
        self.espaco_interno = 0.004
        self.espaco_externo = 0.01

        margem_superior = ((1-self.espaco_para_botoes)-((qtde_labels_e_entrys*2+adicional_tamanhos_listbox)*self.altura_campos)-(qtde_labels_e_entrys*self.espaco_interno)-((qtde_labels_e_entrys-1)*self.espaco_externo))/2

        self.label_id_fpr = Label(self.frame_2, text="ID", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_id_fpr.place(relx=0.05, rely=margem_superior, relwidth=0.90, relheight=self.altura_campos)

        self.entry_id_fpr = Label(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, text="novo")
        self.entry_id_fpr.place(relx=0.05, rely=margem_superior + self.altura_campos + self.espaco_interno, relwidth=0.90, relheight=self.altura_campos)

        self.label_fpr = Label(self.frame_2, text="selecione o Produto", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_fpr.place(relx=0.05, rely=margem_superior + 2*self.altura_campos + self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_fpr_produto = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox)      
       
        indice = 0
        for id in self.lista_ids_produtos:
            produto = self.lista_produtos[indice]
            self.entry_fpr_produto.insert(id, produto)
            indice += 1

        self.scbar_fpr_produto = Scrollbar(self.entry_fpr_produto, orient=VERTICAL)
        self.scbar_fpr_produto.config(command=self.entry_fpr_produto.yview)
        self.scbar_fpr_produto.pack(side=RIGHT, fill=Y)

        self.entry_fpr_produto.configure(yscrollcommand=self.scbar_fpr_produto.set)
        self.entry_fpr_produto.place(relx=0.05, rely=margem_superior + 3*self.altura_campos + 2*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_fpr_produto.bind('<<ListboxSelect>>',self.on_select_fpr_produto)

        self.escolha_fpr_produto = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_fpr_produto.place(relx=0.05, rely=margem_superior + 7*self.altura_campos + 3*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_fpr_insumo = Label(self.frame_2, text="selecione o insumo", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_fpr_insumo.place(relx=0.05, rely=margem_superior + 8*self.altura_campos + 3*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_fpr_insumo = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox)

        indice = 0        
        for id in self.lista_ids_insumos:
            insumo = self.lista_insumos[indice]
            self.entry_fpr_insumo.insert(id, insumo)
            indice += 1

        self.scbar_fpr_insumo = Scrollbar(self.entry_fpr_insumo, orient=VERTICAL)
        self.scbar_fpr_insumo.config(command=self.entry_fpr_insumo.yview)
        self.scbar_fpr_insumo.pack(side=RIGHT, fill=Y)       

        self.entry_fpr_insumo.configure(yscrollcommand=self.scbar_fpr_insumo.set)
        self.entry_fpr_insumo.place(relx=0.05, rely=margem_superior + 9*self.altura_campos + 4*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_fpr_insumo.bind('<<ListboxSelect>>',self.on_select_fpr_insumo)

        self.escolha_fpr_insumo = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_fpr_insumo.place(relx=0.05, rely=margem_superior + 13*self.altura_campos + 5*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_fpr_mensuracao = Label(self.frame_2, text="mensuração da unidade", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_fpr_mensuracao.place(relx=0.05, rely=margem_superior + 14*self.altura_campos + 5*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_fpr_mensuracao = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_fpr_mensuracao.place(relx=0.05, rely=margem_superior + 15*self.altura_campos + 5*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_fpr_unidade = Label(self.frame_2, text="unidade", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_fpr_unidade.place(relx=0.05, rely=margem_superior + 16*self.altura_campos + 5*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_fpr_unidade = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox, selectmode=SINGLE)

        indice = 0        
        for id in self.lista_ids_unidades:
            unidade = self.lista_unidades[indice]
            self.entry_fpr_unidade.insert(id,unidade)
            indice += 1

        self.scbar_fpr_unidade = Scrollbar(self.entry_fpr_unidade, orient=VERTICAL)
        self.scbar_fpr_unidade.config(command=self.entry_fpr_unidade.yview)
        self.scbar_fpr_unidade.pack(side=RIGHT, fill=Y)

        self.entry_fpr_unidade.configure(yscrollcommand=self.scbar_fpr_unidade.set)
        self.entry_fpr_unidade.place(relx=0.05, rely=margem_superior + 17*self.altura_campos + 6*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_fpr_unidade.bind('<<ListboxSelect>>',self.on_select_fpr_unidade)

        self.escolha_fpr_unidade = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_fpr_unidade.place(relx=0.05, rely=margem_superior + 21*self.altura_campos + 7*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_fpr_rendimento = Label(self.frame_2, text="rendimento peso (ex.: 80% digite 80)", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_fpr_rendimento.place(relx=0.05, rely=margem_superior + 22*self.altura_campos + 7*self.espaco_interno + 5*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_fpr_rendimento = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_fpr_rendimento.place(relx=0.05, rely=margem_superior + 23*self.altura_campos + 8*self.espaco_interno + 5*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        self.entry_fpr_rendimento.insert(0,100)

        def btn_incluir_entrar(event):
            botao_incluir.configure(bg="blue", fg="white")
        def btn_incluir_sair(event):
            botao_incluir.configure(bg="white", fg="black")
        botao_incluir = Button(self.frame_2, text="Incluir", bg="white", fg="black", command=self.incluir_fpr)
        botao_incluir.place(relx=0.10, rely=0.90, relheight=0.035, relwidth=0.20)
        botao_incluir.bind('<Enter>',btn_incluir_entrar)
        botao_incluir.bind('<Leave>',btn_incluir_sair)

        def btn_atualizar_entrar(event):
            botao_atualizar.configure(bg="yellow", fg="black")
        def btn_atualizar_sair(event):
            botao_atualizar.configure(bg="white", fg="black")
        botao_atualizar = Button(self.frame_2, text="Atualizar", bg="white", fg="black", command=self.atualizar_fpr)
        botao_atualizar.place(relx=0.40, rely=0.90, relheight=0.035, relwidth=0.20)
        botao_atualizar.bind('<Enter>',btn_atualizar_entrar)
        botao_atualizar.bind('<Leave>',btn_atualizar_sair)

        def btn_deletar_entrar(event):
            botao_deletar.configure(bg="red", fg="white")
        def btn_deletar_sair(event):
            botao_deletar.configure(bg="white", fg="black")
        botao_deletar = Button(self.frame_2, text="Deletar", bg="white", fg="black", command=self.deletar_fpr)
        botao_deletar.place(relx=0.70, rely=0.90, relheight=0.035, relwidth=0.20)
        botao_deletar.bind('<Enter>',btn_deletar_entrar)
        botao_deletar.bind('<Leave>',btn_deletar_sair)

        def btn_limpar_entrar(event):
            botao_limpar.configure(bg="orange", fg="black")
        def btn_limpar_sair(event):
            botao_limpar.configure(bg="white", fg="black")
        botao_limpar = Button(self.frame_2, text="Limpar", bg="white", fg="black", command=self.limpar_fpr)
        botao_limpar.place(relx=0.10, rely=0.95, relheight=0.035, relwidth=0.20)
        botao_limpar.bind('<Enter>',btn_limpar_entrar)
        botao_limpar.bind('<Leave>',btn_limpar_sair)

        def btn_home_entrar(event):
            botao_home.configure(bg="green", fg="white")
        def btn_home_sair(event):
            botao_home.configure(bg="white", fg="black")
        botao_home = Button(self.frame_2, text="HOME", bg="white", fg="black", command=self.home)
        botao_home.place(relx=0.40, rely=0.95, relheight=0.035, relwidth=0.20)
        botao_home.bind('<Enter>',btn_home_entrar)
        botao_home.bind('<Leave>',btn_home_sair)

        def btn_ativar_entrar(event):
            botao_ativar.configure(bg="purple", fg="white")
        def btn_ativar_sair(event):
            botao_ativar.configure(bg="white", fg="black")
        botao_ativar = Button(self.frame_2, text="Ativar", bg="white", fg="black", command=self.ativar_fpr)
        botao_ativar.place(relx=0.70, rely=0.95, relheight=0.035, relwidth=0.20)
        botao_ativar.bind('<Enter>',btn_ativar_entrar)
        botao_ativar.bind('<Leave>',btn_ativar_sair)

        # frame 3
        self.criar_tv_fpr()

        def btn_capturar_entrar(event):
            botao_capturar.configure(bg="pink", fg="black")
        def btn_capturar_sair(event):
            botao_capturar.configure(bg="white", fg="black")
        botao_capturar = Button(self.frame_3, text="Capturar", bg="black", fg="white", command=self.capturar_fpr)
        botao_capturar.place(relx=0.30, rely=0.90, relheight=0.05, relwidth=0.40)
        botao_capturar.bind('<Enter>',btn_capturar_entrar)
        botao_capturar.bind('<Leave>',btn_capturar_sair)

    def on_select_fpr_produto(self, event):
        try:
            produto = self.entry_fpr_produto.get(self.entry_fpr_produto.curselection())
            self.escolha_fpr_produto.configure(text=produto, bg=self.cor_fundo_entry, fg="black")           
            sql = f"SELECT `id_produto` FROM `produtos` WHERE `produto` = '{produto}'"
            result = executa_DQL(sql)
            id_produto = result[0][0]
            #self.aviso_fpr(produto,id_produto)
            self.criar_tv_fpr()
        except:
            try:
                print(sql)
                messagebox.showinfo("erro",sql)
            except:
                pass

    def on_select_fpr_produto_origin(self, event):
        try:
            produto = self.entry_fpr_produto.get(self.entry_fpr_produto.curselection())
            self.escolha_fpr_produto.configure(text=produto, bg=self.cor_fundo_entry, fg="black")           
        except:
            pass

    def on_select_fpr_insumo(self, event):
        try:
            self.escolha_fpr_insumo.configure(text=self.entry_fpr_insumo.get(self.entry_fpr_insumo.curselection()), bg=self.cor_fundo_entry, fg="black")
        except:
            pass

    def on_select_fpr_unidade(self, event):
        try:
            self.escolha_fpr_unidade.configure(text=self.entry_fpr_unidade.get(self.entry_fpr_unidade.curselection()), bg=self.cor_fundo_entry, fg="black")
        except:
            pass

    def capturar_fpr(self):

        try:
            Item_Selecionado = self.tv_fpr.selection()[0]
        except:
            messagebox.showinfo("ERRO","Precisa Selecionar um item.")
            return()
                                
        valores_selecionados = self.tv_fpr.item(Item_Selecionado,"values")
        
        id_capturado = valores_selecionados[0]
        produto_capturado = valores_selecionados[1]
        insumo_capturado = valores_selecionados[2]
        mensuracao_capturada = valores_selecionados[3]
        unidade_capturada = valores_selecionados[4]

        self.entry_id_fpr.configure(text=id_capturado)
        
        self.entry_fpr_mensuracao.delete(0,END)
        self.entry_fpr_mensuracao.insert(0,mensuracao_capturada)
        
        sql = f"SELECT `id_insumo` FROM insumos WHERE `insumo` = '{insumo_capturado}'"
        result = executa_DQL(sql)
        id_insumo = result[0][0]

        sql = f"SELECT `id_unidade` FROM unidades WHERE `unidade` = '{unidade_capturada}'"
        result = executa_DQL(sql)
        id_unidade = result[0][0]
        
        sql = f"SELECT `id_produto` FROM produtos WHERE `produto` = '{produto_capturado}'"
        result = executa_DQL(sql)
        id_produto = result[0][0]

        self.entry_fpr_produto.selection_clear(0,tk.END)
        self.entry_fpr_produto.selection_set(id_produto)
        self.escolha_fpr_produto.configure(text=produto_capturado, bg=self.cor_fundo_entry, fg="black")

        self.entry_fpr_insumo.selection_clear(0,tk.END)
        self.entry_fpr_insumo.selection_set(id_insumo)
        self.escolha_fpr_insumo.configure(text=insumo_capturado, bg=self.cor_fundo_entry, fg="black")

        self.entry_fpr_unidade.selection_clear(0,tk.END)
        self.entry_fpr_unidade.selection_set(id_unidade)
        self.escolha_fpr_unidade.configure(text=unidade_capturada, bg=self.cor_fundo_entry, fg="black")

        #self.aviso_fpr(produto_capturado,id_produto)

        return()

    def criar_tv_fpr(self):
        self.tv_fpr = ttk.Treeview(self.frame_3, columns=('id','produto','insumo','mensuracao','unidade','ativo'), show='headings')
        
        self.tv_fpr.column('id', minwidth=0, width=4)
        self.tv_fpr.column('produto', minwidth=0, width=50)
        self.tv_fpr.column('insumo', minwidth=0, width=150)
        self.tv_fpr.column('mensuracao', minwidth=0, width=4)
        self.tv_fpr.column('unidade', minwidth=0, width=4)
        self.tv_fpr.column('ativo', minwidth=0, width=4)
        
        self.tv_fpr.heading('id', text="ID")
        self.tv_fpr.heading('produto', text="Produto")
        self.tv_fpr.heading('insumo', text="Insumo")
        self.tv_fpr.heading('mensuracao', text="Mensuração")
        self.tv_fpr.heading('unidade', text="Unidade")
        self.tv_fpr.heading('ativo', text="Ativo")      

        produto_entry = self.escolha_fpr_produto.cget("text")

        if produto_entry == 'escolher':
            sql = f"SELECT `id_fpr`,`produto_id`,`insumo_id`,`mensuracao`,`unidade_id`,`ativo` FROM `{self.tabela}`"
        else:
            sql = f"SELECT `id_produto` FROM `produtos` WHERE `produto` = '{produto_entry}'"
            result = executa_DQL(sql)
            id_produto = result[0][0]

            sql = f"SELECT `id_fpr`,`produto_id`,`insumo_id`,`mensuracao`,`unidade_id`,`ativo` FROM `{self.tabela}` WHERE `produto_id` = '{id_produto}'"

        result = executa_DQL(sql)

        for item_result in result:
            sql = f"SELECT `produto` FROM `produtos` WHERE `id_produto` = '{item_result[1]}'"
            result = executa_DQL(sql)
            item_produto = result[0][0]

            sql = f"SELECT `insumo` FROM `insumos` WHERE `id_insumo` = '{item_result[2]}'"
            result = executa_DQL(sql)
            item_insumo = result[0][0]

            sql = f"SELECT `unidade` FROM `unidades` WHERE `id_unidade` = '{item_result[4]}'"
            result = executa_DQL(sql)
            item_unidade = result[0][0]

            self.tv_fpr.insert("", item_result[0], values=(item_result[0], item_produto, item_insumo, item_result[3], item_unidade, item_result[5]))

        self.tv_fpr.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)
      
    def deletar_fpr(self):
        id_entry = self.entry_id_fpr.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        
        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()
                    
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '0' WHERE id_fpr = {id_entry};"
        result = executa_DML(sql)

        self.criar_tv_fpr()
        self.limpar_fpr()
        return()        

    def atualizar_fpr(self):
        id_entry = self.entry_id_fpr.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()

        insumo_entry = self.escolha_fpr_insumo.cget("text")
        if len(insumo_entry) == 0 or insumo_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Insumos precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_insumo` FROM insumos WHERE `insumo` = '{insumo_entry}'"
        result = executa_DQL(sql)
        id_insumo = result[0][0]
        
        unidade_entry = self.escolha_fpr_unidade.cget("text")
        if len(unidade_entry) == 0 or unidade_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Unidade precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_unidade` FROM unidades WHERE `unidade` = '{unidade_entry}'"
        result = executa_DQL(sql)
        id_unidade = result[0][0]

        produto_entry = self.escolha_fpr_produto.cget("text")
        if len(produto_entry)==0 or produto_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Produto precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_produto` FROM produtos WHERE `produto` = '{produto_entry}'"
        result = executa_DQL(sql)
        id_produto = result[0][0]

        mensuracao = self.entry_fpr_mensuracao.get()
        mensuracao = mensuracao.replace(",",".")
        
        if len(self.entry_fpr_mensuracao.get()) == 0:
            messagebox.showinfo("Em branco","Campo mensuracao precisa ser preenchido.")
            return()

        try:
            mensuracao = float(mensuracao)
        except:
            messagebox.showinfo("ERRO","Campo mensuracao não válido.")
            return()

        sql = f"UPDATE `{self.tabela}` SET `produto_id` = '{id_produto}', `insumo_id` = '{id_insumo}', `mensuracao`='{mensuracao}', `unidade_id` = '{id_unidade}', `cfpr` = '0'   WHERE `id_fpr` = {id_entry};"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo("ERRO","O registro não foi atualizado.")
            print(sql)
            return()          

        #self.aviso_fpr(produto_entry,id_produto)
        self.criar_tv_fpr()
        self.limpar_fpr()
        return()

    def incluir_fpr(self):
   
        id_entry = self.entry_id_fpr.cget("text")
        if id_entry != 'novo':
            messagebox.showinfo("ERRO",f"Incluir precisa de ID como `novo`.")
            return()

        insumo_entry = self.escolha_fpr_insumo.cget("text")
        if len(insumo_entry) == 0 or insumo_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Insumos precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_insumo` FROM insumos WHERE `insumo` = '{insumo_entry}'"
        result = executa_DQL(sql)
        id_insumo = result[0][0]

        
        unidade_entry = self.escolha_fpr_unidade.cget("text")
        if len(unidade_entry) == 0 or unidade_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Unidade precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_unidade` FROM unidades WHERE `unidade` = '{unidade_entry}'"
        result = executa_DQL(sql)
        id_unidade = result[0][0]

        produto_entry = self.escolha_fpr_produto.cget("text")
        if len(produto_entry)==0 or produto_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Produto precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_produto` FROM produtos WHERE `produto` = '{produto_entry}'"
        result = executa_DQL(sql)
        id_produto = result[0][0]

        mensuracao = self.entry_fpr_mensuracao.get()
        mensuracao = mensuracao.replace(",",".")
        
        if len(self.entry_fpr_mensuracao.get()) == 0:
            messagebox.showinfo("Em branco","Campo mensuracao precisa ser preenchido.")
            return()

        try:
            mensuracao = float(mensuracao)
        except:
            messagebox.showinfo("ERRO","Campo mensuracao não válido.")
            return()

        sql = f"INSERT INTO {self.tabela} (produto_id, insumo_id, mensuracao, unidade_id, cfpr, ativo) VALUES ('{id_produto}','{id_insumo}','{mensuracao}','{id_unidade}','0','1');"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo(title="ERRO", message=f"Algo deu errado com o banco de dados. {sql}")
            return()

        #self.aviso_fpr(produto_entry,id_produto)
        self.criar_tv_fpr()
        self.limpar_fpr()
        return()

    def limpar_fpr(self):
        self.entry_fpr_mensuracao.delete(0,END)
        self.entry_fpr_mensuracao.insert(0,0)

        self.entry_id_fpr.configure(text="novo")

        self.entry_fpr_produto.selection_clear(0,tk.END)
        self.escolha_fpr_produto.configure(text="escolher", bg="white", fg="red")
        self.on_select_fpr_produto_origin(Event)

        self.entry_fpr_insumo.selection_clear(0,tk.END)
        self.escolha_fpr_insumo.configure(text="escolher", bg="white", fg="red")
        self.on_select_fpr_insumo(Event)

        self.entry_fpr_unidade.selection_clear(0,tk.END)
        self.escolha_fpr_unidade.configure(text="escolher", bg="white", fg="red")
        self.on_select_fpr_unidade(Event)

    def ativar_fpr(self):
        id_entry = self.entry_id_fpr.cget("text")

        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()     
               
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '1' WHERE id_fpr = {id_entry};"
        result = executa_DML(sql)

        #self.aviso_fpr(produto_entry,id_produto)
        self.criar_tv_fpr()
        self.limpar_fpr()
        return()


    def produtos_mao_obra(self):
        self.tabela = "produtos_x_mo"

        abc = self.listagem_produtos()

        self.lista_ids_produtos = abc[0]
        self.lista_produtos = abc[1]

        if len(self.lista_ids_produtos) == 0:
            messagebox.showinfo("Faltam dados","Produtos necessita(m) de algu(ns) dado(s).")
            self.home()
        
        self.apagar_widgets_frame_3()

        # frame_1
        self.label_frame_1.configure(text="Insumos na Finalização do Produtos")

        # frame 2
        self.apagar_widgets_frame_2()
        
        qtde_labels_e_entrys = 6
        adicional_tamanhos_listbox = 9

        self.altura_campos = 0.03
        self.espaco_interno = 0.004
        self.espaco_externo = 0.01

        margem_superior = ((1-self.espaco_para_botoes)-((qtde_labels_e_entrys*2+adicional_tamanhos_listbox)*self.altura_campos)-(qtde_labels_e_entrys*self.espaco_interno)-((qtde_labels_e_entrys-1)*self.espaco_externo))/2

        self.label_id_pmo = Label(self.frame_2, text="ID", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_id_pmo.place(relx=0.05, rely=margem_superior, relwidth=0.90, relheight=self.altura_campos)

        self.entry_id_pmo = Label(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, text="novo")
        self.entry_id_pmo.place(relx=0.05, rely=margem_superior + self.altura_campos + self.espaco_interno, relwidth=0.90, relheight=self.altura_campos)

        self.label_pmo = Label(self.frame_2, text="selecione o Produto", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_pmo.place(relx=0.05, rely=margem_superior + 2*self.altura_campos + self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)
        
        self.entry_pmo_produto = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox)      
       
        indice = 0
        for id in self.lista_ids_produtos:
            produto = self.lista_produtos[indice]
            self.entry_pmo_produto.insert(id, produto)
            indice += 1

        self.scbar_pmo_produto = Scrollbar(self.entry_pmo_produto, orient=VERTICAL)
        self.scbar_pmo_produto.config(command=self.entry_pmo_produto.yview)
        self.scbar_pmo_produto.pack(side=RIGHT, fill=Y)

        self.entry_pmo_produto.configure(yscrollcommand=self.scbar_pmo_produto.set)
        self.entry_pmo_produto.place(relx=0.05, rely=margem_superior + 3*self.altura_campos + 2*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_pmo_produto.bind('<<ListboxSelect>>',self.on_select_pmo_produto)

        self.escolha_pmo_produto = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_pmo_produto.place(relx=0.05, rely=margem_superior + 7*self.altura_campos + 3*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_pmo_tempo_prof_1 = Label(self.frame_2, text="insira o tempo médio (minutos) do profissional, nível 1, do processo de m.o. do produto", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_pmo_tempo_prof_1.place(relx=0.05, rely=margem_superior + 8*self.altura_campos + 3*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_pmo_tempo_prof_1 = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_pmo_tempo_prof_1.place(relx=0.05, rely=margem_superior + 9*self.altura_campos + 4*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_pmo_tempo_prof_2 = Label(self.frame_2, text="insira o tempo médio (minutos) do profissional, nível 2, do processo de m.o. do produto", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_pmo_tempo_prof_2.place(relx=0.05, rely=margem_superior + 10*self.altura_campos + 4*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_pmo_tempo_prof_2 = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_pmo_tempo_prof_2.place(relx=0.05, rely=margem_superior + 11*self.altura_campos + 5*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.label_pmo_tempo_prof_3 = Label(self.frame_2, text="insira o tempo médio (minutos) do profissional, nível 3, do processo de m.o. do produto", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_pmo_tempo_prof_3.place(relx=0.05, rely=margem_superior + 12*self.altura_campos + 5*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_pmo_tempo_prof_3 = Entry(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry)
        self.entry_pmo_tempo_prof_3.place(relx=0.05, rely=margem_superior + 13*self.altura_campos + 6*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        self.entry_pmo_tempo_prof_1.delete(0,END)
        self.entry_pmo_tempo_prof_2.delete(0,END)
        self.entry_pmo_tempo_prof_3.delete(0,END)

        self.entry_pmo_tempo_prof_1.insert(0,0)
        self.entry_pmo_tempo_prof_2.insert(0,0)
        self.entry_pmo_tempo_prof_3.insert(0,0)

        def btn_incluir_entrar(event):
            botao_incluir.configure(bg="blue", fg="white")
        def btn_incluir_sair(event):
            botao_incluir.configure(bg="white", fg="black")
        botao_incluir = Button(self.frame_2, text="Incluir", bg="white", fg="black", command=self.incluir_pmo)
        botao_incluir.place(relx=0.10, rely=0.90, relheight=0.035, relwidth=0.20)
        botao_incluir.bind('<Enter>',btn_incluir_entrar)
        botao_incluir.bind('<Leave>',btn_incluir_sair)

        def btn_atualizar_entrar(event):
            botao_atualizar.configure(bg="yellow", fg="black")
        def btn_atualizar_sair(event):
            botao_atualizar.configure(bg="white", fg="black")
        botao_atualizar = Button(self.frame_2, text="Atualizar", bg="white", fg="black", command=self.atualizar_pmo)
        botao_atualizar.place(relx=0.40, rely=0.90, relheight=0.035, relwidth=0.20)
        botao_atualizar.bind('<Enter>',btn_atualizar_entrar)
        botao_atualizar.bind('<Leave>',btn_atualizar_sair)

        def btn_deletar_entrar(event):
            botao_deletar.configure(bg="red", fg="white")
        def btn_deletar_sair(event):
            botao_deletar.configure(bg="white", fg="black")
        botao_deletar = Button(self.frame_2, text="Deletar", bg="white", fg="black", command=self.deletar_pmo)
        botao_deletar.place(relx=0.70, rely=0.90, relheight=0.035, relwidth=0.20)
        botao_deletar.bind('<Enter>',btn_deletar_entrar)
        botao_deletar.bind('<Leave>',btn_deletar_sair)

        def btn_limpar_entrar(event):
            botao_limpar.configure(bg="orange", fg="black")
        def btn_limpar_sair(event):
            botao_limpar.configure(bg="white", fg="black")
        botao_limpar = Button(self.frame_2, text="Limpar", bg="white", fg="black", command=self.limpar_pmo)
        botao_limpar.place(relx=0.10, rely=0.95, relheight=0.035, relwidth=0.20)
        botao_limpar.bind('<Enter>',btn_limpar_entrar)
        botao_limpar.bind('<Leave>',btn_limpar_sair)

        def btn_home_entrar(event):
            botao_home.configure(bg="green", fg="white")
        def btn_home_sair(event):
            botao_home.configure(bg="white", fg="black")
        botao_home = Button(self.frame_2, text="HOME", bg="white", fg="black", command=self.home)
        botao_home.place(relx=0.40, rely=0.95, relheight=0.035, relwidth=0.20)
        botao_home.bind('<Enter>',btn_home_entrar)
        botao_home.bind('<Leave>',btn_home_sair)

        def btn_ativar_entrar(event):
            botao_ativar.configure(bg="purple", fg="white")
        def btn_ativar_sair(event):
            botao_ativar.configure(bg="white", fg="black")
        botao_ativar = Button(self.frame_2, text="Ativar", bg="white", fg="black", command=self.ativar_pmo)
        botao_ativar.place(relx=0.70, rely=0.95, relheight=0.035, relwidth=0.20)
        botao_ativar.bind('<Enter>',btn_ativar_entrar)
        botao_ativar.bind('<Leave>',btn_ativar_sair)

        # frame 3
        self.criar_tv_pmo()

        def btn_capturar_entrar(event):
            botao_capturar.configure(bg="pink", fg="black")
        def btn_capturar_sair(event):
            botao_capturar.configure(bg="white", fg="black")
        botao_capturar = Button(self.frame_3, text="Capturar", bg="black", fg="white", command=self.capturar_pmo)
        botao_capturar.place(relx=0.30, rely=0.90, relheight=0.05, relwidth=0.40)
        botao_capturar.bind('<Enter>',btn_capturar_entrar)
        botao_capturar.bind('<Leave>',btn_capturar_sair)

    def on_select_pmo_produto(self, event):
        try:
            produto = self.entry_pmo_produto.get(self.entry_pmo_produto.curselection())
            self.escolha_pmo_produto.configure(text=produto, bg=self.cor_fundo_entry, fg="black")           
        except:
            pass

    def capturar_pmo(self):

        try:
            Item_Selecionado = self.tv_pmo.selection()[0]
        except:
            messagebox.showinfo("ERRO","Precisa Selecionar um item.")
            return()
                                
        valores_selecionados = self.tv_pmo.item(Item_Selecionado,"values")
        
        id_capturado = valores_selecionados[0]
        produto_capturado = valores_selecionados[1]
        tempo_1_capturado = valores_selecionados[2]
        tempo_2_capturado = valores_selecionados[3]
        tempo_3_capturado = valores_selecionados[4]

        self.entry_id_pmo.configure(text=id_capturado)
        
        self.entry_pmo_tempo_prof_1.delete(0,END)
        self.entry_pmo_tempo_prof_1.insert(0,tempo_1_capturado)
        
        self.entry_pmo_tempo_prof_2.delete(0,END)
        self.entry_pmo_tempo_prof_2.insert(0,tempo_2_capturado)
        
        self.entry_pmo_tempo_prof_3.delete(0,END)
        self.entry_pmo_tempo_prof_3.insert(0,tempo_3_capturado)
        
        sql = f"SELECT `id_produto` FROM produtos WHERE `produto` = '{produto_capturado}'"
        result = executa_DQL(sql)
        id_produto = result[0][0]

        self.entry_pmo_produto.selection_clear(0,tk.END)
        self.entry_pmo_produto.selection_set(id_produto)
        self.escolha_pmo_produto.configure(text=produto_capturado, bg=self.cor_fundo_entry, fg="black")

        return()

    def criar_tv_pmo(self):
        self.tv_pmo = ttk.Treeview(self.frame_3, columns=('id','produto','tempo_prof_1','tempo_prof_2','tempo_prof_3','ativo'), show='headings')
        
        self.tv_pmo.column('id', minwidth=0, width=4)
        self.tv_pmo.column('produto', minwidth=0, width=50)
        self.tv_pmo.column('tempo_prof_1', minwidth=0, width=30)
        self.tv_pmo.column('tempo_prof_2', minwidth=0, width=30)
        self.tv_pmo.column('tempo_prof_3', minwidth=0, width=30)
        self.tv_pmo.column('ativo', minwidth=0, width=4)
        
        self.tv_pmo.heading('id', text="ID")
        self.tv_pmo.heading('produto', text="Produto")
        self.tv_pmo.heading('tempo_prof_1', text="Tempo prof.niv.1")
        self.tv_pmo.heading('tempo_prof_2', text="Tempo prof.niv.2")
        self.tv_pmo.heading('tempo_prof_3', text="Tempo prof.niv.3")
        self.tv_pmo.heading('ativo', text="Ativo")      

        produto_entry = self.escolha_pmo_produto.cget("text")

        if produto_entry == 'escolher':
            sql = f"SELECT `id_produto_x_mo`,`produto_id`,`tempo_min_grau_1_mo`,`tempo_min_grau_2_mo`,`tempo_min_grau_3_mo`,`ativo` FROM `{self.tabela}`"
        else:
            sql = f"SELECT `id_produto` FROM `produtos` WHERE `produto` = '{produto_entry}'"
            result = executa_DQL(sql)
            id_produto = result[0][0]

            sql = f"SELECT `id_produto_x_mo`,`produto_id`,`tempo_min_grau_1_mo`,`tempo_min_grau_2_mo`,`tempo_min_grau_3_mo`,`ativo` FROM `{self.tabela}` WHERE `produto_id` = '{id_produto}'"

        result = executa_DQL(sql)

        for item_result in result:
            sql = f"SELECT `produto` FROM `produtos` WHERE `id_produto` = '{item_result[1]}'"
            result_2 = executa_DQL(sql)
            print(result_2)

            try:
                item_produto = result_2[0][0]
                self.tv_pmo.insert("", item_result[0], values=(item_result[0], item_produto, item_result[2], item_result[3], item_result[4], item_result[5]))
            except:
                pass

        self.tv_pmo.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)
      
    def deletar_pmo(self):

        id_entry = self.entry_id_pmo.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()
        
        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()
                    
        sql = f"UPDATE `{self.tabela}` SET `ativo` = '0' WHERE `id_produto_x_mo` = {id_entry};"
        result = executa_DML(sql)
        self.criar_tv_pmo()
        self.limpar_pmo()        
        return()

    def atualizar_pmo(self):
        id_entry = self.entry_id_pmo.cget("text")
        if id_entry == 'novo':
            messagebox.showinfo("ERRO",f"Atualizar ou deletar precisa de captação.")
            return()

        produto_entry = self.escolha_pmo_produto.cget("text")
        if len(produto_entry)==0 or produto_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Produto precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_produto` FROM produtos WHERE `produto` = '{produto_entry}'"
        result = executa_DQL(sql)
        id_produto = result[0][0]

        # sql = f"SELECT count(`produto_id`) FROM {self.tabela} WHERE `produto_id` = '{id_produto}' and `ativo` = '1'"
        # result = executa_DQL(sql)
        # contagem_prod = result[0][0]
        # print(contagem_prod)

        # if contagem_prod >= 1:
        #     messagebox.showinfo("ERRO","Já existe um registro para mão de obra para este produto.\nSelecioná-lo e mudar se for o caso.")
        #     return()

        tempo_prof_1_entry = self.entry_pmo_tempo_prof_1.get()
        tempo_prof_1_entry = tempo_prof_1_entry.replace(",",".")
        
        if len(tempo_prof_1_entry) == 0:
            messagebox.showinfo("Em branco","Campo tempo do profissional 1 precisa ser preenchido.")
            return()

        try:
            tempo_prof_1_entry = float(tempo_prof_1_entry)
        except:
            messagebox.showinfo("ERRO","Campo tempo do profissional 1 não é válido.")
            return()
        

        tempo_prof_2_entry = self.entry_pmo_tempo_prof_2.get()
        tempo_prof_2_entry = tempo_prof_2_entry.replace(",",".")
        
        if len(tempo_prof_2_entry) == 0:
            messagebox.showinfo("Em branco","Campo tempo do profissional 2 precisa ser preenchido.")
            return()

        try:
            tempo_prof_2_entry = float(tempo_prof_2_entry)
        except:
            messagebox.showinfo("ERRO","Campo tempo do profissional 2 não é válido.")
            return()
        

        tempo_prof_3_entry = self.entry_pmo_tempo_prof_3.get()
        tempo_prof_3_entry = tempo_prof_3_entry.replace(",",".")
        
        if len(tempo_prof_3_entry) == 0:
            messagebox.showinfo("Em branco","Campo tempo do profissional 3 precisa ser preenchido.")
            return()

        try:
            tempo_prof_3_entry = float(tempo_prof_3_entry)
        except:
            messagebox.showinfo("ERRO","Campo tempo do profissional 3 não é válido.")
            return()

        sql = f"UPDATE `{self.tabela}` SET `produto_id` = '{id_produto}', `tempo_prof_1_entry` = '{tempo_prof_1_entry}', `tempo_prof_2_entry`='{tempo_prof_2_entry}', `tempo_prof_3_entry` = '{tempo_prof_3_entry}'   WHERE `id_produto_x_mo` = {id_entry};"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo("ERRO","O registro não foi atualizado.")
            print(sql)
            return()

        #self.aviso_pmo(produto_entry,id_produto)
        self.criar_tv_pmo()
        self.limpar_pmo()
        return()

    def incluir_pmo(self):
        id_entry = self.entry_id_pmo.cget("text")
        if id_entry != 'novo':
            messagebox.showinfo("ERRO",f"Incluir produtos precisa ser ID novo.")
            return()

        produto_entry = self.escolha_pmo_produto.cget("text")
        if len(produto_entry)==0 or produto_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Produto precisa ser escolhido.")
            return()
        
        sql = f"SELECT `id_produto` FROM produtos WHERE `produto` = '{produto_entry}'"
        result = executa_DQL(sql)
        id_produto = result[0][0]

        sql = f"SELECT count(`produto_id`) FROM {self.tabela} WHERE `produto_id` = '{id_produto}' and `ativo` = '1'"
        result = executa_DQL(sql)
        contagem_prod = result[0][0]
        print(contagem_prod)

        if contagem_prod >= 1:
            messagebox.showinfo("ERRO","Já existe um registro para mão de obra para este produto.\nSelecioná-lo e mudar se for o caso.")
            return()

        tempo_prof_1_entry = self.entry_pmo_tempo_prof_1.get()
        tempo_prof_1_entry = tempo_prof_1_entry.replace(",",".")
        
        if len(tempo_prof_1_entry) == 0:
            messagebox.showinfo("Em branco","Campo tempo do profissional 1 precisa ser preenchido.")
            return()

        try:
            tempo_prof_1_entry = float(tempo_prof_1_entry)
        except:
            messagebox.showinfo("ERRO","Campo tempo do profissional 1 não é válido.")
            return()
        

        tempo_prof_2_entry = self.entry_pmo_tempo_prof_2.get()
        tempo_prof_2_entry = tempo_prof_2_entry.replace(",",".")
        
        if len(tempo_prof_2_entry) == 0:
            messagebox.showinfo("Em branco","Campo tempo do profissional 2 precisa ser preenchido.")
            return()

        try:
            tempo_prof_2_entry = float(tempo_prof_2_entry)
        except:
            messagebox.showinfo("ERRO","Campo tempo do profissional 2 não é válido.")
            return()
        

        tempo_prof_3_entry = self.entry_pmo_tempo_prof_3.get()
        tempo_prof_3_entry = tempo_prof_3_entry.replace(",",".")
        
        if len(tempo_prof_3_entry) == 0:
            messagebox.showinfo("Em branco","Campo tempo do profissional 3 precisa ser preenchido.")
            return()

        try:
            tempo_prof_3_entry = float(tempo_prof_3_entry)
        except:
            messagebox.showinfo("ERRO","Campo tempo do profissional 3 não é válido.")
            return()
        
        sql = f"INSERT INTO {self.tabela} (produto_id, tempo_min_grau_1_mo, tempo_min_grau_2_mo, tempo_min_grau_3_mo, ativo) VALUES ('{id_produto}','{tempo_prof_1_entry}','{tempo_prof_2_entry}','{tempo_prof_3_entry}','1');"
        result = executa_DML(sql)

        if result == False:
            messagebox.showinfo(title="ERRO", message=f"Algo deu errado com o banco de dados. {sql}")
            return()

        #self.aviso_pmo(produto_entry,id_produto)
        self.criar_tv_pmo()
        self.limpar_pmo()
        return()

    def limpar_pmo(self):

        self.entry_pmo_tempo_prof_1.delete(0,END)
        self.entry_pmo_tempo_prof_2.delete(0,END)
        self.entry_pmo_tempo_prof_3.delete(0,END)

        self.entry_pmo_tempo_prof_1.insert(0,0)
        self.entry_pmo_tempo_prof_2.insert(0,0)
        self.entry_pmo_tempo_prof_3.insert(0,0)

        self.entry_id_pmo.configure(text="novo")

        self.entry_pmo_produto.selection_clear(0,tk.END)
        self.escolha_pmo_produto.configure(text="escolher", bg="white", fg="red")
        self.on_select_pmo_produto(Event)

    def ativar_pmo(self):
        id_entry = self.entry_id_pmo.cget("text")

        try:
            id_entry = int(id_entry)
        except:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()            

        if type(id_entry) != int or id_entry < 1:
            messagebox.showinfo("ERRO",f"ID necessita ser número inteiro e maior que zero. ID {id_entry} ID tipo: {type(id_entry)}.")
            return()     

        produto_entry = self.escolha_pmo_produto.cget("text")
        if len(produto_entry)==0 or produto_entry == 'escolher':
            messagebox.showinfo("ERRO",f"Produto precisa ser escolhido.")
            return()

        sql = f"SELECT `id_produto` FROM produtos WHERE `produto` = '{produto_entry}'"
        result = executa_DQL(sql)
        id_produto = result[0][0]

        # sql = f"SELECT count(`produto_id`) FROM {self.tabela} WHERE `produto_id` = '{id_produto}' and `ativo` = '1'"
        # result = executa_DQL(sql)
        # contagem_prod = result[0][0]
        # print(contagem_prod)

        # if contagem_prod >= 1:
        #     messagebox.showinfo("ERRO","Já existe um registro para mão de obra para este produto.\nSelecioná-lo e mudar se for o caso.")
        #     return()

        sql = f"UPDATE `{self.tabela}` SET `ativo` = '1' WHERE `id_produto_x_mo` = {id_entry};"
        result = executa_DML(sql)

        #self.aviso_pmo(produto_entry,id_produto)
        self.criar_tv_pmo()
        self.limpar_pmo()
        return()

    def on_select_ccp_produto(self, event):
        try:
            produto = self.entry_ccp_produto.get(self.entry_ccp_produto.curselection())
            self.escolha_ccp_produto.configure(text=produto, bg=self.cor_fundo_entry, fg="black")
        except:
            pass
            return()

        sql = f"SELECT `id_produto` FROM `produtos` WHERE `produto` = '{produto}'"
        result = executa_DQL(sql)
        id_produto =result[0][0]

        sql = f"SELECT `total_cip`,`total_cfpr`,`total_cpfp`,`total_cpmo`,`total_cel`,`pv` FROM `centro_custos_produto` WHERE `produto_id` = '{id_produto}'"
        result = executa_DQL(sql)        

        cip = result[0][0]
        cfpr = result[0][1]
        cpfp = result[0][2]
        cpmo = result[0][3]
        cel = result[0][4]
        pv = result[0][5]

        if cip == None:
            cip = 0

        if cfpr == None:
            cfpr = 0

        if cpfp == None:
            cpfp = 0

        if cpmo == None:
            cpmo = 0

        if cel == None:
            cel = 0

        if pv == None:
            pv = 0

        print(cip, cfpr, cpfp, cpmo, cel, pv)

        self.label_ccp_cip.configure(text=f"custo dos insumos do produto: R$ {cip}")
        self.label_ccp_cfpr.configure(text=f"custo dos insumos da finalização do produto: R$ {cfpr}")
        self.label_ccp_cpfp.configure(text=f"custo dos insumos para o processo de feitura do produto: R$ {cpfp}")
        self.label_ccp_cpmo.configure(text=f"custo da mão de obra do produto: R$ {cpmo}")
        self.label_ccp_cel.configure(text=f"custo da suposta energia elétrica gasta: R$ {cel}")
        self.label_ccp_pv.configure(text=f"preço de venda do produto: R$ {pv}")

    def ccp(self):
        self.tabela = "centro_custos_produto"

        abc = self.listagem_produtos()

        self.lista_ids_produtos = abc[0]
        self.lista_produtos = abc[1]

        if len(self.lista_ids_produtos) == 0:
            messagebox.showinfo("Faltam dados","Produtos necessita(m) de algu(ns) dado(s).")
            self.home()
        
        self.apagar_widgets_frame_3()

        # frame_1
        self.label_frame_1.configure(text="Centro de custos por Produto.")

        # frame 2
        self.apagar_widgets_frame_2()
        
        qtde_labels_e_entrys = 7
        adicional_tamanhos_listbox = 3

        self.altura_campos = 0.03
        self.espaco_interno = 0.004
        self.espaco_externo = 0.01

        margem_superior = ((1-self.espaco_para_botoes)-((qtde_labels_e_entrys*2+adicional_tamanhos_listbox)*self.altura_campos)-(qtde_labels_e_entrys*self.espaco_interno)-((qtde_labels_e_entrys-1)*self.espaco_externo))/2

        self.label_id_pmo = Label(self.frame_2, text="Custos por unidade de produto. Selecione o produto:", justify="center", bg=self.cor_fundo_label, fg=self.cor_texto_label, anchor="w")
        self.label_id_pmo.place(relx=0.05, rely=margem_superior, relwidth=0.90, relheight=self.altura_campos)

        self.entry_ccp_produto = Listbox(self.frame_2, justify="center", bg=self.cor_fundo_entry, fg=self.cor_texto_entry, font=self.fonte_listbox)

        indice = 0
        for id in self.lista_ids_produtos:
            produto = self.lista_produtos[indice]
            self.entry_ccp_produto.insert(id, produto)
            indice += 1

        self.scbar_ccp_produto = Scrollbar(self.entry_ccp_produto, orient=VERTICAL)
        self.scbar_ccp_produto.config(command=self.entry_ccp_produto.yview)
        self.scbar_ccp_produto.pack(side=RIGHT, fill=Y)

        self.entry_ccp_produto.configure(yscrollcommand=self.scbar_ccp_produto.set)
        self.entry_ccp_produto.place(relx=0.05, rely=margem_superior + 1*self.altura_campos + 0*self.espaco_interno + 0*self.espaco_externo, relwidth=0.90, relheight=self.altura_listbox)

        self.entry_ccp_produto.bind('<<ListboxSelect>>',self.on_select_ccp_produto)

        self.escolha_ccp_produto = Label(self.frame_2, text="escolher", justify="center", bg="white", fg="red", anchor="s")
        self.escolha_ccp_produto.place(relx=0.05, rely=margem_superior + 5*self.altura_campos + 1*self.espaco_interno + self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        def btn_home_entrar(event):
            botao_home.configure(bg="green", fg="white")
        def btn_home_sair(event):
            botao_home.configure(bg="white", fg="black")
        botao_home = Button(self.frame_2, text="HOME", bg="white", fg="black", command=self.home)
        botao_home.place(relx=0.40, rely=0.95, relheight=0.035, relwidth=0.20)
        botao_home.bind('<Enter>',btn_home_entrar)
        botao_home.bind('<Leave>',btn_home_sair)

        # `total_cip`='{cip}'
        self.label_ccp_cip = Label(self.frame_2, text="", justify="center", bg="white", fg="red", anchor="s")
        self.label_ccp_cip.place(relx=0.05, rely=margem_superior + 6*self.altura_campos + 1*self.espaco_interno + 2*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        # `total_cpmo` = '{cpmo}'
        self.label_ccp_cpmo = Label(self.frame_2, text="", justify="center", bg="white", fg="red", anchor="s")
        self.label_ccp_cpmo.place(relx=0.05, rely=margem_superior + 7*self.altura_campos + 1*self.espaco_interno + 3*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        # `total_cfpr` = '{cfpr}'
        self.label_ccp_cfpr = Label(self.frame_2, text="", justify="center", bg="white", fg="red", anchor="s")
        self.label_ccp_cfpr.place(relx=0.05, rely=margem_superior + 8*self.altura_campos + 1*self.espaco_interno + 4*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        # `total_cpfp` = '{cpfp}'
        self.label_ccp_cpfp = Label(self.frame_2, text="", justify="center", bg="white", fg="red", anchor="s")
        self.label_ccp_cpfp.place(relx=0.05, rely=margem_superior + 9*self.altura_campos + 1*self.espaco_interno + 5*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        # `total_cel` = '{cel}'
        self.label_ccp_cel = Label(self.frame_2, text="", justify="center", bg="white", fg="red", anchor="s")
        self.label_ccp_cel.place(relx=0.05, rely=margem_superior + 10*self.altura_campos + 1*self.espaco_interno + 6*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

        # `pv`='{pv}'
        self.label_ccp_pv = Label(self.frame_2, text="", justify="center", bg="white", fg="blue", anchor="s")
        self.label_ccp_pv.place(relx=0.05, rely=margem_superior + 11*self.altura_campos + 1*self.espaco_interno + 7*self.espaco_externo, relwidth=0.90, relheight=self.altura_campos)

    def listagem_unidades_insumos(self):
        sql = "SELECT `id_unidade`,`unidade` FROM `unidades` WHERE `ativo` = 1 and (`grandeza_id` = '2' or `grandeza_id` = '4') ORDER BY `unidade`"
        result = executa_DQL(sql)
        lista_ids = []
        lista_campos = []
        indice = 0

        for item in result:
            lista_ids.append(indice)
            lista_campos.append(item[1])   
            indice += 1         
        return(lista_ids, lista_campos)

    def listagem_unidades(self):
        sql = "SELECT `id_unidade`,`unidade` FROM `unidades` WHERE `ativo` = 1 ORDER BY `unidade`"
        result = executa_DQL(sql)
        lista_ids = []
        lista_campos = []
        indice = 0

        for item in result:
            lista_ids.append(indice)
            lista_campos.append(item[1])   
            indice += 1         
        return(lista_ids, lista_campos)

    def listagem_tipos_sub_produtos(self):
        sql = "SELECT `id_tipo_sub_produto`,`tipo_sub_produto` FROM `tipos_sub_produtos` WHERE `ativo` = 1 ORDER BY `tipo_sub_produto`"
        result = executa_DQL(sql)
        lista_ids = []
        lista_campos = []
        indice = 0

        for item in result:
            lista_ids.append(indice)
            lista_campos.append(item[1])            
            indice += 1 

        return(lista_ids, lista_campos)
    
    def listagem_tipos_produtos(self):
        sql = "SELECT `id_tipo_produto`,`tipo_produto` FROM `tipos_produtos` WHERE `ativo` = 1 ORDER BY `tipo_produto`"
        result = executa_DQL(sql)
        lista_ids = []
        lista_campos = []
        indice = 0
        for item in result:
            lista_ids.append(indice)
            lista_campos.append(item[1])            
            indice += 1 
        return(lista_ids, lista_campos)

    def listagem_produtos(self):
        sql = "SELECT `id_produto`,`produto` FROM `produtos` WHERE `ativo` = 1 ORDER BY `produto`"
        result = executa_DQL(sql)
        lista_ids = []
        lista_campos = []
        indice = 0
        for item in result:
            lista_ids.append(indice)
            lista_campos.append(item[1])            
            indice += 1 
        return(lista_ids, lista_campos)

    def listagem_sub_produtos(self):
        sql = "SELECT `id_sub_produto`,`sub_produto` FROM `sub_produtos` WHERE `ativo` = 1 ORDER BY `sub_produto`"
        result = executa_DQL(sql)
        lista_ids = []
        lista_campos = []
        indice = 0
        for item in result:
            lista_ids.append(indice)
            lista_campos.append(item[1])            
            indice += 1 
        return(lista_ids, lista_campos)

    def listagem_insumos(self):
        sql = "SELECT `id_insumo`,`insumo` FROM `insumos` WHERE `ativo` = 1 ORDER BY `insumo`"
        result = executa_DQL(sql)
        lista_ids = []
        lista_campos = []
        indice = 0
        for item in result:
            lista_ids.append(indice)
            lista_campos.append(item[1])            
            indice += 1 
        return(lista_ids, lista_campos)

    def listagem_grandezas(self):
        sql = "SELECT `id`,`grandeza` FROM `grandezas_fisicas` ORDER BY `grandeza`"
        result = executa_DQL(sql)
        lista_ids = []
        lista_campos = []
        indice = 0
        for item in result:
            lista_ids.append(indice)
            lista_campos.append(item[1])            
            indice += 1
        return(lista_ids, lista_campos)

    def apagar_widgets_frame_2(self):
        try:
            for widget in self.frame_2.winfo_children():
                widget.destroy()
        except:
            pass

    def apagar_widgets_frame_3(self):
        try:
            for widget in self.frame_3.winfo_children():
                widget.destroy()
        except:
            pass

    def menu(self):
        self.apagar_widgets_frame_2()
        self.apagar_widgets_frame_3()

        def btn_home_entrar(event):
            botao_home.configure(bg="green", fg="white")
        def btn_home_sair(event):
            botao_home.configure(bg="white", fg="black")

        label_1 = Label(self.frame_3, text="Aguarde, criando os arquivos a partir dos dados atualizados...", bg="black", fg="white")
        label_1.place(relx=0.10,rely=0.10,relwidth=0.80,relheight=0.10)

        criar_dados()

        label_2 = Label(self.frame_3, text=r"Arquivos criados em \dados.", bg="black", fg="white")
        label_2.place(relx=0.10,rely=0.30,relwidth=0.80,relheight=0.10)

        botao_home = Button(self.frame_2, text="HOME", bg="white", fg="black", command=self.home)
        botao_home.place(relx=0.40, rely=0.90, relheight=0.05, relwidth=0.20)
        botao_home.bind('<Enter>',btn_home_entrar)
        botao_home.bind('<Leave>',btn_home_sair)

    def home(self):
        self.apagar_widgets_frame_2()
        self.apagar_widgets_frame_3()
        self.tela_inicial()       


Cervejaria()
