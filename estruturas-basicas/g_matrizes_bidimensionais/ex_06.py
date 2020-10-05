"""
    Faça um programa que crie uma matriz, de ordem 8X8, preenchida com a seguinte formação:
        - Todos os elementos da primeira linha são preenchidos com 0;
        - Todos os elementos da segunda linha são preenchidos com 1;
        - Todos os elementos da terceira linha são preenchidos com 2;
        - E assim sucessivamente.
"""

matriz = []
cont = 0

for indice in range(8):
    linha = []
    for idx in range(8):
        linha.append(cont)
    cont += 1
    matriz.append(linha)

print(f'Matriz: {matriz}')