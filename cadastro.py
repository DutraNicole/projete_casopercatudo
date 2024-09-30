import tkinter as tk #Importa o módulo tkinter, que é a biblioteca padrão para criar interfaces gráficas em Python
from tkinter import messagebox
import datetime as dt #fornece classes para a manipulação de datas e horários
import hashlib #proteger informações sensíveis

def voltar_para_tela_principal2(frame_interno, janela_cadastro, janela_principal):
    botao_voltar = tk.Label(frame_interno, text="voltar", font=("Helvetica", 12, "bold"), fg="#f9e653", bg="#90c7e8",cursor="hand2")
    botao_voltar.bind("<Button-1>", lambda e: [janela_cadastro.withdraw(), janela_principal.deiconify()])
    botao_voltar.grid(row=9, column=0, pady=(10, 10)) # grid para controlar melhor o posicionamento

def criar_cadastro(janela_principal):
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()
    confirmar_senha = entry_confirmar_senha.get()

    if not nome or not email or not senha or not confirmar_senha:
        messagebox.showerror("Erro", "Preencha todos os campos")
        return

    if senha != confirmar_senha:
        messagebox.showerror("Erro", "As senhas são diferentes")
        return

    # Hash da senha
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    # Colocando data e hora no cadastro
    data_criacao = dt.datetime.now().strftime("%d/%m/%y %H:%M")

    from config import lista_cadastros

    # Adicionando cadastro à lista
    cadastros = len(lista_cadastros) + 1
    cadastros_str = f"cadastro-{cadastros}"
    lista_cadastros.append((cadastros_str, nome, email, senha_hash, data_criacao))

    # Salvar informações no arquivo
    salvar_cadastro_no_arquivo(nome, email, senha_hash, data_criacao)

    # Limpar tudo depois de cadastrar
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_senha.delete(0, tk.END)
    entry_confirmar_senha.delete(0, tk.END)

    # Mensagem de sucesso
    messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

    # Fecha a janela de cadastro e abre a janela inicial
    janela_cadastro.destroy()
    from inicio import criar_janela_inicial
    criar_janela_inicial(janela_principal)

def salvar_cadastro_no_arquivo(nome, email, senha_hash, tempo):
    # Salvar informações no arquivo
    with open('arquivos_salvos.txt', 'a') as arquivo:  # Mudar para 'a' para adicionar ao final
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Email: {email}\n")
        arquivo.write(f"Senha (hash): {senha_hash}\n")
        arquivo.write(f"Data e Hora: {tempo}\n")
        arquivo.write("="*40 + "\n")  # Linha separadora para melhor leitura

def criar_janela_cadastro(janela_principal):
    global entry_nome, entry_email, entry_senha, entry_confirmar_senha, janela_cadastro

    janela_cadastro = tk.Toplevel()  #janela criada
    janela_cadastro.title('Cadastro')
    janela_cadastro.geometry('400x600')  # tamanho da janela
    janela_cadastro.configure(bg='#a2d8f1')  # Cor de fundo semelhante à da imagem

    frame_central = tk.Frame(janela_cadastro, bg='#a2d8f1')
    frame_central.pack(expand=True, fill='both')

    quadro_fundo = tk.Frame(frame_central, bg='#90c7e8', padx=20, pady=20)  # Adiciona preenchimento interno (padding)
    quadro_fundo.pack(expand=True)

    frame_interno = tk.Frame(quadro_fundo, bg='#90c7e8')
    frame_interno.pack(expand=True)

    label_nome = tk.Label(frame_interno, text="Nome de usuário", font = ("Helvetica", 14, "bold"), bg = '#90c7e8', fg = '#f9e653')
    label_nome.grid(row=0, column=0, pady=(10, 2))  # Usar grid
    entry_nome = tk.Entry(frame_interno,font=("Helvetica", 12),bg='#539AFF',fg="white")
    entry_nome.grid(row=1, column=0, pady=10)

    label_email = tk.Label(frame_interno, text="Email", font = ("Helvetica", 14, "bold"), bg = '#90c7e8', fg = '#f9e653')
    label_email.grid(row=2, column=0, pady=(10, 2))
    entry_email = tk.Entry(frame_interno,font=("Helvetica", 12),bg='#539AFF',fg="white")
    entry_email.grid(row=3, column=0, pady=10)

    label_senha = tk.Label(frame_interno, text="Senha", font = ("Helvetica", 14, "bold"), bg = '#90c7e8', fg = '#f9e653')
    label_senha.grid(row=4, column=0, pady=(10, 2))
    entry_senha = tk.Entry(frame_interno,font=("Helvetica", 12),bg='#539AFF',fg="white", show='*')
    entry_senha.grid(row=5, column=0, pady=10)

    label_confirmar_senha = tk.Label(frame_interno, text="Confirmar senha", font = ("Helvetica", 14, "bold"), bg = '#90c7e8', fg = '#f9e653')
    label_confirmar_senha.grid(row=6, column=0, pady=10)
    entry_confirmar_senha = tk.Entry(frame_interno,font=("Helvetica", 12),bg='#539AFF',fg="white",show='*')
    entry_confirmar_senha.grid(row=7, column=0, pady=10)

    # correção: botão de cadastro deve chama a função diretamente
    botao_cadastrar = tk.Button(frame_interno, text="cadastrar", font=("Helvetica", 12, "bold"), bg="#5fa3f1", fg='#f9e653', width=10, height=1, command=lambda: criar_cadastro(janela_principal))
    botao_cadastrar.grid(row=8, column=0, pady=10)  # Posicionar com grid

    voltar_para_tela_principal2(frame_interno, janela_cadastro, janela_principal)

    janela_cadastro.mainloop()

    # Fabi não deu cntl+v, eu só botei oq eu fiz, n musou quase nada, só o grid msm, e umas funções ai