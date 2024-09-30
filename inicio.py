import os
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

import materia
import temporizador
import ia

def criar_janela_inicial(janela_principal):
    global janela_inicial, img_cronometro_tk, img_IA_tk, img_materia_tk, img_acessar_tk  # Para manter a referência das imagens
    janela_inicial = tk.Toplevel()
    janela_inicial.title('Bem-vindo(a)')
    janela_inicial.geometry('400x600')
    janela_inicial.configure(bg='#a2d8f1')

    # Carregar e redimensionar as imagens
    caminho_imagem_cronometro = os.path.join("assets", "cronometro.png")
    caminho_imagem_IA = os.path.join("assets", "IA.png")
    caminho_imagem_materia = os.path.join("assets", "criarmateria.png")
    caminho_imagem_acessar_materia = os.path.join("assets", "acessarmateria.png")

    img_cronometro = Image.open(caminho_imagem_cronometro)
    img_cronometro = img_cronometro.resize((100, 100), Image.Resampling.LANCZOS)
    img_cronometro_tk = ImageTk.PhotoImage(img_cronometro)

    img_IA = Image.open(caminho_imagem_IA)
    img_IA = img_IA.resize((100, 100), Image.Resampling.LANCZOS)
    img_IA_tk = ImageTk.PhotoImage(img_IA)

    img_materia = Image.open(caminho_imagem_materia)
    img_materia = img_materia.resize((100, 100), Image.Resampling.LANCZOS)
    img_materia_tk = ImageTk.PhotoImage(img_materia)

    img_acessar_materia = Image.open(caminho_imagem_acessar_materia)
    img_acessar_materia = img_acessar_materia.resize((100, 100), Image.Resampling.LANCZOS)#redimencionar imagem e garante a qualidade
    img_acessar_materia_tk = ImageTk.PhotoImage(img_acessar_materia)

    # Título centralizado
    titulo_centralizado = tk.Label(janela_inicial, text="TELA INICIAL", font=("Helvetica", 16, "bold"), bg='#a2d8f1',fg='#f9e653')
    titulo_centralizado.grid(row=1, column=1, pady=(20, 0), sticky='n')

    # Linha abaixo do título
    canvas = tk.Canvas(janela_inicial, width=400, height=2, bg='#a2d8f1', highlightthickness=0) #remover a borda
    canvas.grid(row=2, column=1, pady=(0, 10), sticky='n')
    canvas.create_line(0, 1, 400, 1, fill="#539aff", width=2)

    # Frame para os botões "Criar matéria" e "Acessar matérias"
    frame_botao1e2 = tk.Frame(janela_inicial, bg='#a2d8f1')
    frame_botao1e2.grid(row=3, column=1, pady=(20, 20))

    # Exibir a imagem acima do botão "Criar matéria"
    label_img_materia = tk.Label(frame_botao1e2, image=img_materia_tk, bg='#a2d8f1')
    label_img_materia.grid(row=0, column=0, pady=(0, 5))

    botao_criar_materia = tk.Button(frame_botao1e2, text="Criar matéria", font=("Helvetica", 12, "bold"), bg="#5fa3f1",
                                    fg="#f9f58a", width=15, height=1, command=materia.criar_janela_materia)

    botao_acessar_materia = tk.Button(frame_botao1e2, text="Acessar matérias", font=("Helvetica", 12, "bold"),
                                      bg="#5fa3f1", fg="#f9f58a", width=15, height=1, command=materia.acessar_materia)

    # Exibir a imagem acima do botão "Acessar matérias"
    label_img_acessar = tk.Label(frame_botao1e2, image=img_acessar_materia_tk, bg='#a2d8f1')
    label_img_acessar.grid(row=0, column=1, pady=(0, 5))

    # Posicionando os botões "Criar matéria" e "Acessar matérias"
    botao_criar_materia.grid(row=1, column=0, padx=10, pady=10)
    botao_acessar_materia.grid(row=1, column=1, padx=10, pady=10)

    # Frame para os botões "IA" e "Cronômetro"
    frame_botao3e4 = tk.Frame(janela_inicial, bg='#a2d8f1')
    frame_botao3e4.grid(row=4, column=1, pady=(20, 20))

    # Exibir a imagem acima do botão "Cronômetro"
    label_img_cronometro = tk.Label(frame_botao3e4, image=img_cronometro_tk, bg='#a2d8f1')
    label_img_cronometro.grid(row=0, column=1, pady=(0, 5))

    botao_IA = tk.Button(frame_botao3e4, text="IA", font=("Helvetica", 12, "bold"), bg="#5fa3f1", fg="#f9f58a", width=15, height=1,
                         command=lambda: ia.criar_janela_ia())

    botao_cronometro = tk.Button(frame_botao3e4, text="Cronômetro", font=("Helvetica", 12, "bold"), bg="#5fa3f1",
                                 fg="#f9f58a", width=15, height=1, command=lambda: temporizador.criar_janela_temporizador())

    # Exibir a imagem acima do botão "IA"
    label_img_ia = tk.Label(frame_botao3e4, image=img_IA_tk, bg='#a2d8f1')
    label_img_ia.grid(row=0, column=0, pady=(0, 5))

    # Posicionando os botões "IA" e "Cronômetro"
    botao_IA.grid(row=1, column=0, padx=10, pady=10)

    botao_cronometro.grid(row=1, column=1, padx=10, pady=10)

    # Botão "Sair" no canto inferior direito
    botao_sair = tk.Button(janela_inicial, text="Sair", font=("Helvetica", 12, "bold"), bg="#5fa3f1", fg="#f9f58a",
                width=10, height=1, command=lambda: [janela_principal.deiconify(), janela_inicial.withdraw()])
    botao_sair.grid(row=5, column=1, padx=10, pady=10, sticky='se')  # Centralizado na coluna 1, alinhado à direita

    # Fazendo as colunas laterais expandirem para centralizar o título e os botões superiores
    janela_inicial.grid_columnconfigure(0, weight=1)  # Expande a coluna da esquerda
    janela_inicial.grid_columnconfigure(1, weight=1)  # Expande a coluna do meio (onde estão os botões)
    janela_inicial.grid_columnconfigure(2, weight=1)  # Expande a coluna da direita

    # Garantindo que o título e a linha estejam centralizados
    janela_inicial.grid_rowconfigure(0, weight=0)
    janela_inicial.grid_rowconfigure(1, weight=0)

    # Garantindo que os botões superiores estejam centralizados
    janela_inicial.grid_rowconfigure(2, weight=0)

    # Preenchendo o espaço vazio nas linhas inferiores
    janela_inicial.grid_rowconfigure(3, weight=1)
    janela_inicial.grid_rowconfigure(4, weight=1)
    janela_inicial.grid_rowconfigure(5, weight=1)

    janela_inicial.mainloop()
