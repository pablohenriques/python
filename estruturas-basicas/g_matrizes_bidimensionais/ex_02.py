'''
    Faça um programa que leia os dados de uma matriz de inteiros 5x5
    e crie um vetor preenchido com os elementos da diagonal principal
    dessa matriz. Imprima a matriz e o vetor resultante.
'''

tam = 5
matriz = []
vetor = []

for linha in range(tam):
    vetor_linha = []
    for coluna in range(tam):
        elemento = int(input('Digite um número inteiro para a matriz: '))
        vetor_linha.append(elemento)
    matriz.append(vetor_linha)

print(f"Matriz: {matriz}")

for linha in range(tam):
    linha_matriz = matriz[linha]
    for coluna in range(tam):
        if coluna == linha:
            vetor.append(linha_matriz[coluna])
    print(f'Linha: [{linha}]: {linha_matriz}')

print(f'Vetor - Diagonal principal: {vetor}')