import os #usado para construir caminhos para os arquivos de imagem
import tkinter as tk #Importa o módulo tkinter, que é a biblioteca padrão para criar interfaces gráficas em Python
from tkinter import PhotoImage #Importa a classe PhotoImage do tkinter, usada para exibir imagens em janelas gráficas
from PIL import Image, ImageTk #Importa as classes Image e ImageTk da biblioteca Pillow (PIL), que é usada para manipulação avançada de imagens
import datetime as dt
import hashlib

#amarelo: '#f9e653'
#azul claro: '#a2d8f1'
#azul escuro: "#5fa3f1"

#janela.deiconify() //reexibe uma janela
#janela_principal.withdraw()
def criar_janela_interface(): #Criação da janela principal
    global janela_principal, img_tk
    janela_principal = tk.Tk() #primeira janela criada(janela inteira)
    janela_principal.title('Koala Helper')
    janela_principal.geometry('400x600')#tamanho da janela
    janela_principal.configure(bg='#a2d8f1') #Cor de fundo semelhante à da imagem

    # Frame para centralizar o conteúdo
    frame = tk.Frame(janela_principal, bg='#a2d8f1')
    frame.pack(expand=True)

    caminho_imagem = os.path.join("assets", "logo.png")# Caminho relativo para a imagem na pasta assets

    # Carregar a imagem do koala
    img = Image.open(caminho_imagem)
    img = img.resize((150, 150), Image.Resampling.LANCZOS)  # Redimensionar a imagem
    img_tk = ImageTk.PhotoImage(img)#converte a imagem para o tkinter exibir

    # Label para exibir a imagem
    label_img = tk.Label(frame, image=img_tk, bg='#a2d8f1')
    label_img.pack(padx=0,pady=0)

    # Label para o título
    label_titulo = tk.Label(frame, text="KOALA HELPER", font=("Franklin Gothic Medium", 26, "bold"), bg='#a2d8f1', fg='#f9e653')
    label_titulo.pack(pady=5)

    from login import criar_janela_login
    # Botão de Entrar
    botao_entrar = tk.Button(frame, text="ENTRAR", font=("Helvetica", 16, "bold"), bg="#5fa3f1", fg="#f9e653", width=15, height=1,
                             command=lambda: [janela_principal.withdraw(),criar_janela_login(janela_principal)])
    botao_entrar.pack(pady=5)

    from cadastro import criar_janela_cadastro
    # Botão de Criar Conta
    botao_criar = tk.Button(frame, text="CRIAR CONTA", font=("Helvetica", 16, "bold"), bg="#5fa3f1", fg="#f9e653", width=15, height=1,
                            command=lambda: [janela_principal.withdraw(),criar_janela_cadastro(janela_principal)])
    botao_criar.pack(pady=5)

    from inicio import criar_janela_inicial
    '''botao_continuar = tk.Button(frame, text="continuar", font=("Helvetica", 9,"bold"), bg="#5fa3f1", fg="#f9e653", width=15, height=1,  command=lambda: [janela_principal.withdraw(), criar_janela_inicial(janela_principal)])
    botao_continuar.pack(pady=5)
    '''
    botao_continuar = tk.Label(frame, text="continuar", font=("Helvetica", 12,"bold"), fg="#f9e653", bg="#a2d8f1", cursor="hand2")
    botao_continuar.bind("<Button-1>", lambda e: [janela_principal.withdraw(), criar_janela_inicial(janela_principal)])
    botao_continuar.pack(pady=5)

    janela_principal.mainloop()

criar_janela_interface()
