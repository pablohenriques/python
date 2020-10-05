"""
    Faça um programa que leia uma matriz de inteiros 3x4. Depois, crie e imprima 2 vetores, sendo que:
    o primeiro vetor é formado com os elementos da linha 0 da matriz; o segundo vetor é formado pelos
    elementos da coluna 1 da matriz.
"""

matriz = []
vetor0 = []
vetor1 = []

for i in range(3):
    linha = []
    for j in range(4):
        linha.append(j)
    matriz.append(linha)

print(f'Matriz preenchida {matriz}')

for i in matriz[0]:
    vetor0.append(i)

print(f'Vetor - Linha 0: {vetor0}')

for i in range(len(matriz)):
    linha = matriz[i]
    for j in range(len(linha)):
        if j == 1:
            vetor1.append(linha[j])

print(f'Vetor - Coluna 1: {vetor1}')
