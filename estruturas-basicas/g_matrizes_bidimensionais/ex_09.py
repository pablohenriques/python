"""
Faça um programa que leia uma matriz A, ordem 4x4, e imprima os seguintes dados:
    a. Produto dos elementos da diagonal principal.
    b. Soma dos elementos da diagonal secundária.

Exemplo: Na tabela a seguir, os elementos em negrito fazem 
parte da diagonal principal e os elementos sublinhados fazem 
parte da diagonal secundária.
"""

matriz = []
diagonal_principal = []
diagonal_secundaria = []
resultado_principal = 1
resultado_secundaria = 0

for i in range(4):
    linha = []
    for j in range(4):
        elemento = int(input(f'Insira um número para a posição [{i}][{j}] da matriz:'))
        linha.append(elemento)
    matriz.append(linha)

print(f'Matriz: {matriz}')

for i in range(4):
    linha = matriz[i]
    for j in range(4):
        if i==j:
            diagonal_principal.append(linha[j])
        elif i+j == 3:
            diagonal_secundaria.append(linha[j])

print(f'Diagonal Principal: {diagonal_principal}')
print(f'Diagonal Secundária: {diagonal_secundaria}')

for i in diagonal_principal:
    resultado_principal = i * resultado_principal

print(f'Produto dos elementos da diagonal principal: {resultado_principal}')

for j in diagonal_secundaria:
    resultado_secundaria += j

print(f'Soma dos elementos da diagonal secundária: {resultado_secundaria}')
