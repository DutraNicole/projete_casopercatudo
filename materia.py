import tkinter as tk  # Importa o módulo tkinter, que é a biblioteca padrão para criar interfaces gráficas em Python
from tkinter import messagebox  # Importa a classe PhotoImage do tkinter, usada para exibir imagens
import datetime as dt  # Importa a biblioteca datetime para manipulação de datas
import hashlib
from tkinter import filedialog
import shutil  # Para copiar o arquivo
import os  # Para criar diretórios e lidar com caminhos

from config import lista_materias
from materiaEditar import criar_janela_editar_materia
import inicio
global corpo
# Diretório para salvar arquivos
diretorio_arquivos = "arquivos_salvos"

# Função para enviar o arquivo e salvá-lo no diretório
def enviar_arquivo():
    # Abrir explorador de arquivos para selecionar arquivo
    caminho_arquivo = filedialog.askopenfilename(title="Selecione um arquivo para enviar")
    if caminho_arquivo:
        # Cria o diretório se ele não existir
        if not os.path.exists(diretorio_arquivos):
            os.makedirs(diretorio_arquivos)

        # Nome do arquivo
        nome_arquivo = os.path.basename(caminho_arquivo)

        # Caminho para onde o arquivo será salvo
        caminho_destino = os.path.join(diretorio_arquivos, nome_arquivo)

        # Copia o arquivo para o diretório destino
        shutil.copy(caminho_arquivo, caminho_destino)
        print(f"Arquivo {nome_arquivo} enviado e armazenado em {caminho_destino}.")

def deletar_materia(index):
    if messagebox.askyesno("Confirmar", "Você tem certeza de que deseja deletar esta matéria?"):
        lista_materias.pop(index - 1)  # Remove a matéria da lista
        messagebox.showinfo("Sucesso", "Matéria deletada com sucesso!")

        janela_acessar_materia.destroy()  # Fecha a janela atual de matérias
        acessar_materia()  # Reabre a janela atualizada

def acessar_materia():
    global janela_acessar_materia
    if not lista_materias:
        messagebox.showinfo("Informação", "Nenhuma matéria disponível")
        return

    janela_acessar_materia = tk.Toplevel()
    janela_acessar_materia.title('Acessar Matéria')
    janela_acessar_materia.geometry('400x600')  # tamanho da janela
    janela_acessar_materia.configure(bg='#a2d8f1')  # Cor de fundo semelhante à da imagem

    # titulo centralizado
    titulo_centralizado = tk.Label(janela_acessar_materia, text="MATÉRIAS", font=("Helvetica", 16, "bold"), bg='#a2d8f1',fg='#f9e653')
    titulo_centralizado.pack(pady=(20, 0))

    # linha abaixo do titulo
    canvas = tk.Canvas(janela_acessar_materia, width=400, height=2, bg='#a2d8f1', highlightthickness=0)
    canvas.pack(pady=(0, 10))
    canvas.create_line(0, 1, 400, 1, fill="#539aff", width=2)

    for i, materia in enumerate(lista_materias, start=1):
        titulo, corpo, data = materia

        tk.Label(janela_acessar_materia, text=f"{titulo}", font=("Helvetica", 15, "bold"), bg='#a2d8f1', fg="white").pack(pady=5)
        #tk.Label(janela_acessar_materia, text=f"{corpo}", font=("Helvetica", 12), bg='#a2d8f1', fg='#ffffff').pack()
        tk.Label(janela_acessar_materia, text=f"data: {data}", font=("Helvetica", 9), bg='#a2d8f1', fg='#ffffff').pack()
        #tk.Label(janela_acessar_materia, text="", bg='#a2d8f1').pack()  # Espaçamento

        # Criar um frame para os botões
        frame_botoes = tk.Frame(janela_acessar_materia, bg='#a2d8f1')
        frame_botoes.pack(pady=10)

        botao_editar = tk.Label(frame_botoes, text="editar", font=("Helvetica", 11, "bold"), fg="#0099fa", bg="#a2d8f1", cursor="hand2")
        botao_editar.bind("<Button-1>", lambda event, idx=i: [janela_acessar_materia.withdraw(), criar_janela_editar_materia(idx)])
        botao_editar.grid(row=0, column=0, padx=5)

        botao_deletar = tk.Label(frame_botoes, text="deletar", font=("Helvetica", 11, "bold"), fg="#0099fa", bg="#a2d8f1", cursor="hand2")
        botao_deletar.bind("<Button-1>", lambda e, idx=i: deletar_materia(idx))
        botao_deletar.grid(row=0, column=1, padx=5)

def criar_materia():
    titulo = entry_materia.get()
    corpo = text_corpo.get("1.0", tk.END).strip()  # Obtém o texto completo do widget Text

    if not titulo or not corpo:
        messagebox.showerror("Erro", "Preencha todos os campos")
        return

    # Salvar matéria na lista de matérias
    data_criacao = dt.datetime.now().strftime("%d/%m/%y %H:%M")
    lista_materias.append((titulo, corpo, data_criacao))

    salvar_materia_no_arquivo(titulo, corpo, data_criacao)

    messagebox.showinfo("Sucesso", "Matéria criada com sucesso!")
    janela_materia.destroy()

# Salvar informações no arquivo
def salvar_materia_no_arquivo(titulo, corpo, data_criacao):
    with open('materias_salvas.txt', 'a') as arquivo:  # Mudar para 'a' para adicionar ao final
        arquivo.write(f"Nome: {titulo}\n")
        arquivo.write(f"Email: {corpo}\n")
        arquivo.write(f"Data e Hora: {data_criacao}\n")
        arquivo.write("="*40 + "\n")  #Linha separadora para melhor leitura

def criar_janela_materia():
    global entry_materia, text_corpo , janela_materia

    janela_materia = tk.Toplevel()
    janela_materia.title('Criar Matéria')
    janela_materia.geometry('400x600')  # tamanho da janela
    janela_materia.configure(bg='#a2d8f1')  # cor de fundo semelhante à da imagem

    # Configurando o grid para centralizar
    janela_materia.grid_columnconfigure(0, weight=1)  # coluna central
    janela_materia.grid_rowconfigure(0, weight=1)  # espaço antes dos elementos
    janela_materia.grid_rowconfigure(6, weight=1)  # espaço após os elementos

    label_materia = tk.Label(janela_materia, text="Título",  font=("Helvetica", 20, "bold"), bg='#a2d8f1', fg='#f9e653')
    label_materia.grid(row=1, column=0, padx=10, pady=10, sticky='n')

    frame_entry = tk.Frame(janela_materia, bd=0.001, relief=tk.SUNKEN, background='#90c7e8')
    frame_entry.grid(row=2, column=0, padx=10, pady=10, sticky='n')

    entry_materia = tk.Entry(frame_entry, width=30, bg='white')
    entry_materia.pack(padx=10, pady=10)

    label_texto = tk.Label(janela_materia, text="Conteúdo", font=("Helvetica", 14, "bold"), bg='#a2d8f1', fg='#f9e653')
    label_texto.grid(row=3, column=0, padx=10, pady=10, sticky='n')

    # Crie um frame com uma borda
    frame_texto = tk.Frame(janela_materia, bd=0.001, relief=tk.SUNKEN, background='#90c7e8')  # 'bd' é a largura da borda
    frame_texto.grid(row=4, column=0, padx=10, pady=10, sticky='n')

    # widget Text para múltiplas linhas de entrada de texto
    text_corpo = tk.Text(frame_texto, height=15, width=40,wrap=tk.WORD, bg='white')  # 'wrap=tk.WORD' quebra o texto automaticamente
    text_corpo.pack(padx=10, pady=10)  # Margem interna da caixa de texto

    frame_botoes = tk.Frame(janela_materia, bg='#a2d8f1')
    frame_botoes.grid(row=5, column=0, padx=10, pady=10, sticky='n')  # grid utilizado ao invés de pack

    botao_materia = tk.Button(frame_botoes, text="criar", font=("Helvetica", 12, "bold"), bg="#5fa3f1", fg="#f9f58a", width=10, height=1, command=criar_materia)
    botao_materia.grid(row=0, column=0, padx=5)  # grid ao invés de pack dentro do frame_botoes

    # Cria um botão para abrir o arquivo
    botao_abrir = tk.Button(frame_botoes, text='Abrir Arquivo', font=("Helvetica", 12, "bold"), bg="#5fa3f1", fg="#f9f58a", width=10, height=1, command=enviar_arquivo)
    botao_abrir.grid(row=0, column=1, padx=5)  # grid ao invés de pack dentro do frame_botoes

    # Espaço ao redor para centralizar tudo
    janela_materia.grid_rowconfigure(0, weight=1)  # Espaço acima dos widgets
    janela_materia.grid_rowconfigure(6, weight=1)  # Espaço abaixo dos widgets

    janela_materia.transient(inicio.janela_inicial)
    janela_materia.grab_set()
    inicio.janela_inicial.wait_window(janela_materia)