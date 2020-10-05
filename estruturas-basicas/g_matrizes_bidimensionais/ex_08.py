"""
    Faça um programa que leia uma matriz, de ordem 3x3. Depois, calcule e imprima o maior elemento
    e quantas vezes ele aparece nessa matriz.
"""

matriz = []
maior_elemento = -99999
cont = 0

for i in range(3):
    linha = []
    for j in range(3):
        elemento = int(input("Digite um elemento:"))
        if elemento > maior_elemento:
            maior_elemento = elemento
        linha.append(elemento)
    matriz.append(linha)

for linha in matriz:
    for elemento in linha:
        if elemento == maior_elemento:
            cont += 1

print(f'Matriz: {matriz} \nMaior elemento: {maior_elemento} \nAparece {cont} vez (es) na matriz')