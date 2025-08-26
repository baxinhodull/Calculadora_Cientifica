Calculadora Científica

Calculadora científica em Python com interface gráfica (GUI) utilizando Tkinter. Este projeto permite realizar operações matemáticas básicas e funções científicas de forma prática e intuitiva.

Visão Geral

A calculadora possui um visor para entrada de expressões e botões para números, operadores e funções científicas. O usuário pode montar expressões clicando nos botões ou digitando diretamente no visor. Ao pressionar "=", o resultado é calculado e exibido.

Funcionalidades

Operações Aritméticas Básicas: Adição (+), subtração (-), multiplicação (*), divisão (/), potência (**).

Funções Científicas: Raiz quadrada (sqrt), seno (sin), cosseno (cos), tangente (tan) e logaritmo (log).

Constantes Matemáticas: Pi (pi) e número de Euler (e).

Interface Gráfica: Layout simples e intuitivo desenvolvido com Tkinter.

Entrada de Expressões: Suporte a parênteses () para agrupar operações.

Limpeza: Botão "C" para limpar o visor e iniciar um novo cálculo.

Tecnologias Utilizadas

Python 3

Tkinter (GUI)

Módulo math (funções e constantes matemáticas)

Como Executar o Projeto

Pré-requisitos: Python 3 instalado. Tkinter já vem incluso na instalação padrão.

Salvar o Código: Salve o arquivo como calculadora.py (ou outro nome com extensão .py).

Executar:

Abra o terminal ou prompt de comando.

Navegue até a pasta do arquivo.

Execute:

<img width="230" height="61" alt="image" src="https://github.com/user-attachments/assets/3006fd24-b632-4992-8010-4805704ac34b" />


A janela da calculadora será aberta, pronta para uso.

Como o Código Funciona

Interface: A janela principal e os widgets (visor e botões) são criados e organizados em uma grade (grid), simulando o layout de uma calculadora real.

Entrada do Usuário: A função inserir_valor() adiciona o valor do botão pressionado ao visor.

Cálculo: A função calcular() processa a expressão do visor e utiliza eval() de forma segura, permitindo apenas funções matemáticas definidas, evitando execução de código indesejado.

Tratamento de Erros: Expressões inválidas ou operações impossíveis (como divisão por zero) são capturadas pelo try...except, exibindo "Erro" no visor.
