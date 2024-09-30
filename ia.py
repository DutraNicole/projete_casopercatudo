import tkinter as Tkinter
from tkinter import Canvas, Scrollbar, messagebox #scrolledtext: n permite inclusão direta de botões(contém texto apenas, por isso mudei pro canva)

def conferir_respostas():
    adicionar_respostas = []

    # se todas as perguntas foram respondidas
    for variaveis_respostas in respostas_usuario:
        resposta_atual = variaveis_respostas.get()
        if resposta_atual == "":  # Se alguma pergunta não foi respondida
            messagebox.showerror("Erro", "Por favor, responda todas as perguntas.")
            return

        adicionar_respostas.append(resposta_atual)

    print("Respostas do usuário:", adicionar_respostas)
    print("Respostas da ia:", respostas)

    #verificar as respostas com as respostas corretas
    for i in range(len(adicionar_respostas)): #loop com o n° de iterações igual a quantidade de elementos da lista
        if adicionar_respostas[i] == respostas[i]:
            print("Correto")
            #correto = Tkinter.Label(scrollable_frame, text=f"Correto!\n", font=("Arial", 10, "bold"), bg='#a2d8f1', fg='green')
            #correto.pack(anchor="e", padx=10, pady=(0, 0))
            labels_respostas[i].config(text="Correto", fg='green') #config p/ modificar o texto e a cor do Label

        else:
            #incorreto = Tkinter.Label(scrollable_frame, text=f"incorreto!\n", font=("Arial", 10, "bold"), bg='#a2d8f1', fg='red')
            #incorreto.pack(anchor="e", padx=10, pady=(0, 0))
            print("Incorreto")
            labels_respostas[i].config(text="Incorreto", fg='red')

def Gemini():
    # Import the Python SDK
    import google.generativeai as genai
    # Used to securely store your API key
    GOOGLE_API_KEY = 'AIzaSyC5ubXAp6pbZkOfeSwT2Qx7N4lSyi_Dw6Y'
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')

    # Obtenha o texto completo do widget Text
    entra = entrada.get("1.0", Tkinter.END).strip()

    # Gera o conteúdo com a API
    response = model.generate_content(
        "Me de cinco questão de verdadeiro ou falso sobre " + entra +
        " e embaixo de cada pergunta coloque sua respectiva resposta, sem necessidade de explicar. "
        "Ao gerar, lembre-se de sempre deixar, como padrão, o número da questão na frente de cada pergunta, sem nenhum elemento antes desse número "
        "e 'Resposta' na frente de cada resposta, sem a necessidade de colocar asteriscos neles"
    )

    if response and response.text: #se a api gerou
        print(response.text)
        processar_resposta_ia(response.text)
    else:
        print("Erro: Nenhuma resposta gerada pela API.")

    # nova janela para exibir a resposta
    janela_response = Tkinter.Toplevel()
    janela_response.title("Resposta Gerada")
    janela_response.geometry("400x600")
    janela_response.configure(bg="#a2d8f1")

    # configurar scroll para o frame
    global scrollable_frame
    canvas = Canvas(janela_response, bg="#a2d8f1")
    scrollbar = Scrollbar(janela_response, orient="vertical", command=canvas.yview)
    scrollable_frame = Tkinter.Frame(canvas, bg="#a2d8f1")

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    global respostas_usuario, labels_respostas
    respostas_usuario = []
    labels_respostas = []

    if perguntas:  #se a lista de perguntas foi preenchida
        for i, pergunta in enumerate(perguntas):
            text_pergunta = Tkinter.Label(scrollable_frame, text=f"{pergunta}\n", font=("Helvetica", 10, "bold"), fg="#5fa3f1",
                                                                    bg="#a2d8f1", wraplength=350, justify="left") #wraplength: limite da tela
            text_pergunta.pack(padx=10, pady=(10, 0), anchor="w")

            var = Tkinter.StringVar(value="")
            respostas_usuario.append(var)

            radio_verdadeiro = Tkinter.Radiobutton(scrollable_frame, text="Verdadeiro", variable=var, value="Verdadeiro",
                                                                    font=("Helvetica", 10, "bold"), fg="#5fa3f1", bg="#a2d8f1", selectcolor="#a2d8f1")
            radio_verdadeiro.pack(anchor="w", padx=10, pady=(0, 0))

            radio_falso = Tkinter.Radiobutton(scrollable_frame, text="Falso", variable=var, value="Falso",
                                                                font=("Helvetica", 10, "bold"), fg="#5fa3f1", bg="#a2d8f1", selectcolor="#a2d8f1")
            radio_falso.pack(anchor="w", padx=10, pady=(0, 10))

            # Label para a resposta (Correto ou Incorreto)
            label_resposta = Tkinter.Label(scrollable_frame, text="", font=("Helvetica", 10, "bold"), bg="#a2d8f1")
            label_resposta.pack(anchor="e", padx=10, pady=(0, 10))
            labels_respostas.append(label_resposta)
    else:
        text_pergunta = Tkinter.Label(scrollable_frame, text="Nenhuma pergunta foi gerada.")
        text_pergunta.pack(expand=True, fill='both')

    botao_conferir = Tkinter.Label(scrollable_frame, text="conferir", font=("Helvetica", 12, "bold"), fg="#f9e653", bg="#619df1", cursor="hand2")
    botao_conferir.bind("<Button-1>", lambda e: conferir_respostas())
    botao_conferir.pack(side="left", padx=5, pady=5)

    bvoltar = Tkinter.Label(scrollable_frame, text="voltar", font=("Helvetica", 12, "bold"), fg="#f9e653", bg="#619df1",cursor="hand2")
    bvoltar.bind("<Button-1>", lambda e: [janela_response.withdraw(), rootia.deiconify(), entrada.delete("1.0", Tkinter.END)])
    bvoltar.pack(side="right", padx=0, pady=5)

def processar_resposta_ia(response):
    global perguntas, respostas
    perguntas = []
    respostas = []

    linhas = response.splitlines()

    for i, linha in enumerate(linhas):
        if i == 0 or i == 3 or i == 6 or i == 9 or i == 12:  # detecta uma pergunta
            perguntas.append(linha.strip())

        elif "Resposta:" in linha:  # detecta uma resposta
            resposta_atual = linha.split("Resposta:")[-1].strip()
            respostas.append(resposta_atual)

    if len(perguntas) != len(respostas):
        print("Aviso: O número de perguntas e respostas não coincide!")
    else:
        print("Perguntas e respostas processadas com sucesso.")

def criar_janela_ia():
    global rootia, entrada
    rootia = Tkinter.Toplevel()
    rootia.title("Escolher")
    rootia.geometry("400x400")
    rootia.configure(bg="#a2d8f1")

    label = Tkinter.Label(rootia, text="Faça sua pergunta!", fg="#f9e653", bg="#a2d8f1", font="Verdana 20 bold")
    label.place(relx=0.5, rely=0.5, anchor='center')
    label.pack()

    entrada = Tkinter.Text(rootia, height=8, width=30, wrap=Tkinter.WORD, bg='white')
    entrada.pack(padx=10, pady=10)

    f = Tkinter.Frame(rootia)
    enviar = Tkinter.Button(f, text='Enviar', font=("Helvetica", 12, "bold"), width=8, bg="#5fa3f1", fg="#f9e653",
                                            command=lambda: [rootia.withdraw(), Gemini()])
    f.pack(padx=5, pady=5, anchor="center")
    enviar.pack()

    label = Tkinter.Label(rootia, text="Observação: para questões mais específicas é necessário uma descrição "
                                       "detalhada ou a IA trará questões genéricas sobre o assunto. ", fg="#5fa3f1",
                                                        bg="#a2d8f1", font="Helvetica 12 bold",wraplength=260)
    label.place(relx=7, rely=7, anchor='center')
    label.pack()

    rootia.mainloop()
