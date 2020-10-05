"""
    Faça um programa que crie uma matriz A, ordem 100x50, preenchida da seguinte forma:
                col0    col1    col2 ...
        lin0    0       1       2
        lin1    1       2       3
        lin2    2       3       4
        ...

    Depois imprima a matriz resultante.
"""

matriz = []
cont = 0
acumulador = 0

for i in range(100):
    linha = []
    for j in range(50):
        linha.append(cont)
        cont += 1
    matriz.append(linha)
    cont = 0
    acumulador += 1
    cont = acumulador

print(f'Matriz: {matriz}')    
    
