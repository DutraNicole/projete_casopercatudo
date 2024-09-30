import sqlite3
from datetime import datetime, timedelta
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def Banco_db(id_usuario):
    conexao = sqlite3.connect('comparativo.db')
    cursor = conexao.cursor()
    tabela_nome = f'horas_estudo{id_usuario}'

    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {tabela_nome} (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            data TEXT, 
            tempo_geral INTEGER,
            id_user INTEGER NOT NULL
    );
    """)
    return conexao, cursor, tabela_nome

def Ler_db(id_usuario):
    valor_aleatorio = 0
    dias_para_diminuir = 4  # Para inserir 5 dias

    conexao, cursor, tabela_nome = Banco_db(id_usuario)
    data_atual = datetime.now()

    for i in range(5):
        data_para_inserir = (data_atual - timedelta(days=dias_para_diminuir)).strftime('%Y-%m-%d')
        cursor.execute(f"INSERT INTO {tabela_nome} (tempo_geral, id_user, data) VALUES (?, ?, ?)", (valor_aleatorio, id_usuario, data_para_inserir))
        valor_aleatorio += 2
        dias_para_diminuir -= 1

    conexao.commit()
    cursor.execute(f"SELECT data, tempo_geral FROM {tabela_nome}")
    todos_registros = cursor.fetchall()
    conexao.close()

    return todos_registros

def plotar_grafico(dados):

    window = tk.Tk()
    window.title("Gráfico de Barras de Horas de Estudo")
    window.geometry("600x400")

    # Mudando a cor de fundo da janela
    window.config(bg='lightblue')  # Você pode mudar 'lightblue' para qualquer cor que desejar

    datas = [registro[0] for registro in dados]
    tempos = [registro[1] for registro in dados]

    fig = Figure(figsize=(5, 3), dpi=100)
    ax = fig.add_subplot(1, 1, 1)

    ax.bar(datas, tempos, color='skyblue')
    ax.set_title('Horas de Estudo por Data')
    ax.set_xlabel('Data')
    ax.set_ylabel('Tempo Geral (Horas)')
    ax.tick_params(axis='x', rotation=45)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    window.mainloop()

global dados
dados = Ler_db(1)
