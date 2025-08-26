import tkinter as tk
from math import *


funcoes_matematicas = {
    'sqrt': sqrt,
    'sin': sin,
    'cos': cos,
    'tan': tan,
    'log': log,
    'pi': pi,
    'e': e
}

janela = tk.Tk()
janela.title("Calculadora Científica")
janela.geometry("400x500")

entrada = tk.Entry(janela, font=("Arial", 18), borderwidth=5, relief="solid")
entrada.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

def inserir_valor(valor):
    entrada.insert(tk.END, valor)

def calcular():
    try:
        expressao = entrada.get()
       
        for nome_funcao, funcao in funcoes_matematicas.items():
            expressao = expressao.replace(nome_funcao, f'funcoes_matematicas["{nome_funcao}"]')
        
        
        resultado = eval(expressao, {"__builtins__": None}, funcoes_matematicas)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

def limpar():
    entrada.delete(0, tk.END)

botoes = [
    "7", "8", "9", "/", "sqrt",
    "4", "5", "6", "*", "sin",
    "1", "2", "3", "-", "cos",
    "0", ".", "(", ")", "tan",
    "pi", "e", "**", "+", "log"
]

linha = 1
coluna = 0
for botao in botoes:
    comando = lambda x=botao: inserir_valor(x)
    tk.Button(janela, text=botao, width=6, height=2, font=("Arial", 14),
              command=comando).grid(row=linha, column=coluna, padx=2, pady=2, sticky="nsew")
    coluna += 1
    if coluna > 4:
        coluna = 0
        linha += 1

tk.Button(janela, text="C", width=6, height=2, font=("Arial", 14), command=limpar).grid(row=linha, column=0, padx=2, pady=2, sticky="nsew")
tk.Button(janela, text="=", width=26, height=2, font=("Arial", 14), command=calcular).grid(row=linha, column=1, columnspan=4, padx=2, pady=2, sticky="nsew")

for i in range(6):
    janela.grid_rowconfigure(i, weight=1)
    janela.grid_columnconfigure(i, weight=1)

janela.mainloop()