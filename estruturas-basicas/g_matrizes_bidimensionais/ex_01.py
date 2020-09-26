'''
    Faça um programa que leia uma matriz, de ordem 3x3. Depois, calcule e imprima quantas vezes o
    último elemento aparece nessa matriz e em que posições (linha e coluna) ele está armazenado.
'''

matriz = []
indices = []
tam = 3
ultimo_elemento = 0
cont = 0

for i in range(tam):
    linha = []
    for j in range(tam):
        elemento = int(input('Digite um número:'))
        linha.append(elemento)
        ultimo_elemento = elemento
    matriz.append(linha)

print(f'\nUltimo_elemento: {ultimo_elemento}\n')

for i in range (len(matriz)):
    linha = matriz[i]
    for j in range(len(linha)):
        if linha[j] == ultimo_elemento:
            cont += 1
            indice = {'linha': i, 'coluna': j}
            indices.append(indice)
    print(f'linha [{i}]: {linha}')

print(f"\nÚltimo elemento {ultimo_elemento} aparece {cont} vezes no vetor")
print(f'\nIndice de elementos: {indices}')
print(f'\nMatriz:\n{matriz}')
