#bibliotecas
import tkinter as tk
from datetime import datetime, timezone
#import teste_uso_txt_ as txt
import datetime as dt

from grafico import plotar_grafico, dados
from google.api_core.operations_v1.operations_client_config import config

# Colocando data e hora no cadastro
mes = dt.datetime.now().strftime("%m")
dia = dt.datetime.now().strftime("%d")

# Função para centralizar os widgets dentro da janela
def centralizar_widgets(root):
# Configurando as colunas para se expandirem uniformemente
    for i in range(4):
     root.grid_columnconfigure(i, weight=1)

def centralizar_widgets2(root):
    # Configurando as colunas para se expandirem uniformemente
    for i in range(3):
        root.grid_columnconfigure(i, weight=1)

def voltar_para_escolha(fcr, rootcr, root):
    bvoltar = tk.Label(fcr, text="voltar", font=("Helvetica", 12, "bold"), fg="#f9e653", bg="#90c7e8", cursor="hand2")
    bvoltar.bind("<Button-1>", lambda e: [rootcr.withdraw(), root.deiconify()])
    bvoltar.grid(row=5, column=0, columnspan=3, pady=(10, 10))

def Cronometro():
    global counter, running
    counter = 0
    running = False

    def counter_label(labelcr):
        def count():
            if running:
                global counter
                if counter == 0:
                    display = "iniciando..."
                else:
                    ttcr = datetime.fromtimestamp(counter, timezone.utc)
                    string = ttcr.strftime("%H:%M:%S")
                    display = string

                labelcr['text'] = display
                labelcr.after(1000, count)
                counter += 1
        count()

    def Start(labelcr):
        global running
        running = True
        counter_label(labelcr)
        startcr['state'] = 'disabled'
        stopcr['state'] = 'normal'
        resetcr['state'] = 'normal'

    def Stop():
        global running
        startcr['state'] = 'normal'
        stopcr['state'] = 'disabled'
        resetcr['state'] = 'normal'
        running = False

    def Reset(labelcr):
        global counter
        counter = 0
        if not running:
            resetcr['state'] = 'disabled'
            labelcr['text'] = 'Bem-vindo!'
        else:
            labelcr['text'] = 'Começando...'

    global rootcr
    rootcr = tk.Toplevel()
    rootcr.title("Temporizador")
    rootcr.geometry("400x400")
    rootcr.configure(bg="#a2d8f1")

    # Estrutura de Frames
    frame_central = tk.Frame(rootcr, bg='#a2d8f1')
    frame_central.pack(expand=True, fill='both')

    quadro_fundo = tk.Frame(frame_central, bg='#90c7e8', padx=20, pady=20)  # Adiciona preenchimento interno (padding)
    quadro_fundo.pack(expand=True)

    frame_interno = tk.Frame(quadro_fundo, bg='#90c7e8')
    frame_interno.pack(expand=True)

    labelcr = tk.Label(frame_interno, text="Iniciar!", bg="#90c7e8", fg="#f9e653", font="Verdana 17 bold")
    labelcr.grid(row=0, column=0, columnspan=3, pady=(50, 10), sticky='nsew')

    fcr = tk.Frame(frame_interno, bg='#90c7e8')
    fcr.grid(row=3, column=0, columnspan=3, pady=10)

    startcr = tk.Button(fcr, text='Começar', font="Helvetica 10 bold", width=7, bg="#5fa3f1", fg="#f9e653", command=lambda: Start(labelcr))
    stopcr = tk.Button(fcr, text='Parar', font="Helvetica 10 bold", width=7, bg="#5fa3f1", fg="#f9e653", state='disabled', command=Stop)
    resetcr = tk.Button(fcr, text='Resetar', font="Helvetica 10 bold", width=7, bg="#5fa3f1", fg="#f9e653", state='disabled', command=lambda: Reset(labelcr))

    startcr.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    stopcr.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    resetcr.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

    rootcr.grid_columnconfigure(0, weight=1)
    rootcr.grid_columnconfigure(1, weight=1)
    rootcr.grid_columnconfigure(2, weight=1)
    rootcr.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand
    rootcr.grid_columnconfigure(1, weight=1)  # Allow column 1 to expand
    rootcr.grid_columnconfigure(2, weight=1)  # Allow column 2 to expand

    # Centralizando os widgets
    centralizar_widgets2(rootcr)

    voltar_para_escolha(fcr, rootcr, root)
    rootcr.mainloop()

def Timer():
    global running, counter
    counter = 0
    running = False

    def counter_label(labelmr):
        def count():
            if running:
                global counter
                if counter <= 0:
                    display = "Fim..."
                else:
                    ttmr = datetime.fromtimestamp(counter, timezone.utc)
                    string = ttmr.strftime("%H:%M:%S")
                    display = string

                labelmr['text'] = display
                labelmr['bg'] = '#a2d8f1'
                labelmr['fg'] = 'yellow'
                labelmr.after(1000, count)
                counter -= 1

        count()

    def Start(labelmr):
        startmr.config(text='Começar')
        global running, counter
        running = True

        horas_entrada = entry_horas.get()
        minutos_entrada = entry_min.get()
        segundos_entrada = entry_segundos.get()

        if horas_entrada.isdigit() and minutos_entrada.isdigit() and segundos_entrada.isdigit():
            hours = int(horas_entrada)
            minutes = int(minutos_entrada)
            seconds = int(segundos_entrada)

            counter = (hours * 3600) + (minutes * 60) + seconds #convertendo tudo pra segundos

        else:
            labelmr['text'] = "Digite um número válido!"
            return

        counter_label(labelmr)
        startmr['state'] = 'disabled'
        stopmr['state'] = 'normal'
        resetmr['state'] = 'normal'

    def Stop():
        global running
        startmr.config(text="Continuar", command=lambda: Run(labelmr))
        startmr['state'] = 'normal'
        stopmr['state'] = 'disabled'
        resetmr['state'] = 'normal'
        running = False

    def Run(labelmr):
        global running
        running = True
        counter_label(labelmr)
        startmr['state'] = 'normal'
        stopmr['state'] = 'normal'
        resetmr['state'] = 'normal'
        startmr.config(text="Começar", font=("helvetica", 10, "bold"), command=lambda: Start(labelmr))

    def Reset(labelmr):
        global counter
        horas_entrada = entry_horas.get()
        minutos_entrada = entry_min.get()
        segundos_entrada = entry_segundos.get()

        if  horas_entrada.isdigit() and minutos_entrada.isdigit() and segundos_entrada.isdigit():
            hours = int(horas_entrada)
            minutes = int(minutos_entrada)
            seconds = int(segundos_entrada)

            counter = (hours * 3600) + (minutes * 60) + seconds #convertendo tudo pra segundos

        else:
            labelmr['text'] = "Digite um número válido!"

        if not running:
            resetmr['state'] = 'disabled'
            labelmr['text'] = 'Bem-Vindo!!'
        else:
            labelmr['text'] = 'Inicializando...'

    global rootmr
    rootmr = tk.Toplevel()
    rootmr.title("Timer")
    rootmr.geometry("400x400")
    rootmr.configure(bg="#a2d8f1")

    # Estrutura de Frames
    frame_central = tk.Frame(rootmr, bg='#a2d8f1')
    frame_central.pack(expand=True, fill='both')

    quadro_fundo = tk.Frame(frame_central, bg='#90c7e8', padx=20, pady=20)  # Adiciona preenchimento interno (padding)
    quadro_fundo.pack(expand=True)

    frame_interno = tk.Frame(quadro_fundo, bg='#90c7e8')
    frame_interno.pack(expand=True)

    # Centralizando o label
    labelmr = tk.Label(frame_interno, text="Bem-vindo!", bg='#90c7e8', fg="yellow", font="Verdana 17 bold")
    labelmr.grid(row=0, column=0, columnspan=4, pady=(50, 10), sticky='nsew')  # Centered label with more padding

    # Configurando as colunas do rootmr para centralização
    rootmr.grid_columnconfigure(0, weight=1)  # Margem esquerda
    rootmr.grid_columnconfigure(1, weight=1)  # Coluna das labels (permitir expansão)
    rootmr.grid_columnconfigure(2, weight=1)  # Coluna das entradas (permitir expansão)
    rootmr.grid_columnconfigure(3, weight=1)  # Margem direita

    # Ajustando o layout das Labels e Entries com grid e sticky
    label_horas = tk.Label(frame_interno, text="Horas", bg="#90c7e8")
    label_horas.grid(row=1, column=1, sticky='e', padx=5, pady=5)  # Alinha à direita e ajusta o padding
    entry_horas = tk.Entry(frame_interno, width=5)
    entry_horas.grid(row=1, column=2, sticky='w', padx=5, pady=5)  # Alinha à esquerda da coluna

    label_min = tk.Label(frame_interno, text="Minutos", bg="#90c7e8")
    label_min.grid(row=2, column=1, sticky='e', padx=5, pady=5)  # Alinha à direita
    entry_min = tk.Entry(frame_interno, width=5)
    entry_min.grid(row=2, column=2, sticky='w', padx=5, pady=5)  # Alinha à esquerda

    label_segundos = tk.Label(frame_interno, text="Segundos", bg="#90c7e8")
    label_segundos.grid(row=3, column=1, sticky='e', padx=5, pady=5)  # Alinha à direita
    entry_segundos = tk.Entry(frame_interno, width=5)
    entry_segundos.grid(row=3, column=2, sticky='w', padx=5, pady=5)  # Alinha à esquerda

    # Frame para os botões
    fmr = tk.Frame(frame_interno, bg='#90c7e8')
    fmr.grid(row=4, column=1, columnspan=2, pady=10)

    startmr = tk.Button(fmr, text='Start', font="Helvetica 10 bold", width=7, bg="#5fa3f1", fg="#f9e653", command=lambda: Start(labelmr))
    stopmr = tk.Button(fmr, text='Stop', font="Helvetica 10 bold", width=7, bg="#5fa3f1", fg="#f9e653", state='disabled', command=Stop)
    resetmr = tk.Button(fmr, text='Reset', font="Helvetica 10 bold", width=7, bg="#5fa3f1", fg="#f9e653", state='disabled', command=lambda: Reset(labelmr))

    # Centralizando os botões no Frame
    startmr.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    stopmr.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    resetmr.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

    # Centralizando as colunas na janela principal
    rootmr.grid_columnconfigure(0, weight=1)
    rootmr.grid_columnconfigure(1, weight=1)
    rootmr.grid_columnconfigure(2, weight=1)

    # Centralizando os widgets
    centralizar_widgets(rootmr)
    # Chama a função de voltar para escolha (caso exista)
    voltar_para_escolha(fmr, rootmr, root)
    rootmr.mainloop()


def criar_janela_temporizador():

    global root
    root = tk.Tk()
    root.title("Escolher")
    root.geometry("400x400")
    root.configure(bg="#a2d8f1")

    frame_central = tk.Frame(root, bg='#a2d8f1')
    frame_central.pack(expand=True, fill='both')

    quadro_fundo = tk.Frame(frame_central, bg='#90c7e8', padx=20, pady=20)  # Adiciona preenchimento interno (padding)
    quadro_fundo.pack(expand=True)

    frame_interno = tk.Frame(quadro_fundo, bg='#90c7e8')
    frame_interno.pack(expand=True)

    # escrever na tela
    label = tk.Label(frame_interno, text="Faça sua escolha!", fg="#f9e653", bg="#90c7e8", font="Helvetica 24 bold")
    label.grid(row=0, column=0, pady=(20, 10), sticky='nsew')

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=0)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)  # Permite expansão da coluna 0

    # botoes e suas configs
    f = tk.Frame(frame_interno, bg='#90c7e8')
    f.grid(row=1, column=0, pady=(5, 20))

    cronometro = tk.Button(f, text='Cronômetro', font=("Helvetica 12 bold"), bg="#5fa3f1", fg="#f9e653", width=15, height=1, command=lambda: [print("Botão Cronômetro pressionado"), root.withdraw(), Cronometro()])
    cronometro.grid(row=0, column=1, padx=5, pady=20, sticky='ns')

    timer = tk.Button(f, text='Timer', font=("Helvetica 12 bold"), bg="#5fa3f1", fg="#f9e653", width=15, height=1, command=lambda: [print("Botão Cronômetro pressionado"), root.withdraw(), Timer()])
    timer.grid(row=1, column=1, padx=5, pady=20, sticky='ns')

    Grafico = tk.Button(f, text='Gráfico comparativo', font=("Helvetica 12 bold"), bg="#5fa3f1", fg="#f9e653", width=15, height=1, command=lambda: (print("Botão pressionado"), plotar_grafico(dados)))
    Grafico.grid(row=2, column=1, padx=10, pady=10, sticky='ns')

    f.grid_rowconfigure(0, weight=1)
    f.grid_rowconfigure(1, weight=0)
    f.grid_rowconfigure(2, weight=1)
    f.grid_columnconfigure(0, weight=1)  # Permite expansão da coluna 0
    f.grid_columnconfigure(1, weight=0)  # Permite expansão da coluna 0
    f.grid_columnconfigure(3, weight=1)  # Permite expansão da coluna 0

    root.mainloop()
    criar.temporizador()