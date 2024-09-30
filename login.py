import tkinter as tk #Importa o módulo tkinter, que é a biblioteca padrão para criar interfaces gráficas em Python
from tkinter import messagebox
import datetime as dt
import hashlib

import inicio

def voltar_para_tela_principal(frame_interno, janela_login, janela_principal):
    botao_voltar = tk.Label(frame_interno, text="voltar", font=("Helvetica", 12, "bold"), fg="#f9e653", bg="#90c7e8",cursor="hand2")
    botao_voltar.bind("<Button-1>", lambda e: [janela_login.withdraw(), janela_principal.deiconify()])
    # Ajuste para garantir que o botão "voltar" fique na linha abaixo do botão "login"
    botao_voltar.grid(row=5, column=0, pady=(10, 10))  # linha

def fazer_login(janela_principal):
    email = entry_email_login.get()
    senha = entry_senha_login.get()
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    from config import lista_cadastros

    for cadastro in lista_cadastros:
        if cadastro[2] == email and cadastro[3] == senha_hash:
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            janela_login.withdraw()
            inicio.criar_janela_inicial(janela_principal)
            return

    messagebox.showerror("Erro", "Email ou senha incorretos")

def criar_janela_login(janela_principal):
    global entry_email_login, entry_senha_login, janela_login

    janela_login = tk.Toplevel()
    janela_login.title('Login')
    janela_login.geometry('400x400')#tamanho da janela
    janela_login.configure(bg='#a2d8f1') #cor de fundo

    frame_centralizar = tk.Frame(janela_login, bg='#a2d8f1')
    frame_centralizar.pack(expand=True, fill='both')

    fundo_quadro = tk.Frame(frame_centralizar, bg='#90c7e8', padx=10,pady=10)  # Adiciona preenchimento interno (padding)
    fundo_quadro.pack(expand=True)

    frame_internal = tk.Frame(fundo_quadro, bg='#90c7e8')
    frame_internal.pack(expand=True)

    label_email = tk.Label(frame_internal, text="Email", font = ("Helvetica", 14, "bold"), bg = '#90c7e8', fg = '#f9e653')
    label_email.grid(row=0, column=0, pady=(10, 2))
    entry_email_login = tk.Entry(frame_internal,font=("Helvetica", 12),bg='#539AFF',fg="white")
    entry_email_login.grid(row=1, column=0, pady=10)

    label_senha = tk.Label(frame_internal, text="Senha", font = ("Helvetica", 14, "bold"), bg = '#90c7e8', fg = '#f9e653')
    label_senha.grid(row=2, column=0, pady=(10, 2))
    entry_senha_login = tk.Entry(frame_internal,font=("Helvetica", 12),bg='#539AFF',fg="white", show='*')
    entry_senha_login.grid(row=3, column=0, pady=10)

    botao_login = tk.Button(frame_internal, text="Fazer login",font=("Helvetica", 12,"bold"), bg="#5fa3f1", fg='#f9e653', width=10,
                                                    height=1,  command=lambda: fazer_login(janela_principal))
    botao_login.grid(row=4, column=0, pady=(10, 0))  # Removi o padding inferior para evitar muito espaço

    voltar_para_tela_principal(frame_internal, janela_login, janela_principal)

    janela_login.mainloop()

    from inicio import janela_inicial
    janela_login.transient(janela_inicial) # deixar o login sempre em cima da principal
    janela_login.grab_set() # bloquear interações com a janela principal até o login ser fechado
    janela_inicial.wait_window(janela_login)

#Fabi não deu cntl+v, eu só botei oq eu fiz, n mudou quase nada, só o grid msm, e umas funções ai