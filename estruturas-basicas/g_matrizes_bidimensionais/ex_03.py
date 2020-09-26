"""
    Implementar um programa que leia uma matriz A (2x3) e crie uma matriz B (3x2), sendo que B é a
    matriz transposta de A. Transpor uma matriz significa transformar suas linhas em colunas e vice-
    versa.
"""

nova_linha = 0
nova_coluna = 0

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz_transposta = []

print(f'\nMatriz: {matriz}')
print(f'Número de Linhas: {len(matriz)} - Número de Colunas: {len(matriz[0])}')

print("\n ### \n")

nova_coluna = len(matriz)   #capturando número de linhas da matriz
nova_linha = len(matriz[0]) # capturando número de colunas da matriz
    
print(f'Nova Linha: {nova_linha} - Nova Coluna: {nova_coluna}')

for indice in range(nova_linha):
    lista = []
    matriz_transposta.append(lista)

print(f'Matriz Transposta: {matriz_transposta}')

print("\n ### \n")

for idx in range(len(matriz)):
    linha = matriz[idx]
    for clx in range(len(linha)):
        matriz_transposta[clx].append(linha[clx])

print(f'Matriz Transposta Preenchida: {matriz_transposta}')


