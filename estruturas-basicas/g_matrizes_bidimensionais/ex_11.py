"""
    Faça um programa que leia dois vetores A e B com 3 elementos inteiros cada. Construir uma matriz
    C (3x2), com a seguinte formação: a primeira coluna deverá ser formada pelos elementos do vetor A
    e a segunda coluna pelos elementos do vetor B.
"""

vetor_a = []
vetor_b = []
matriz = []

for i in range(3):
    elemento = int(input(f'Digite um número inteiro para a posição [{i}] do vetor A:'))
    vetor_a.append(elemento)

print(f'Vetor A: {vetor_a}')

for i in range(3):
    elemento = int(input(f'Digite um número inteiro para a posição [{i}] do vetor B:'))
    vetor_b.append(elemento)

print(f'Vetor B: {vetor_b}')

for i in range(3):
    linha = []
    linha.append(vetor_a[i])
    linha.append(vetor_b[i])
    matriz.append(linha)

print(f'Matriz: {matriz}')