'''
    Faça um programa que leia dados de um vetor A,
    com 10 elementos inteiros. Depois, calcule e imprima
    quantas vezes o primeiro elemento aparece no vetor.
'''

vetor = []
contador = 0

for i in range(10):
    elemento = int(input('Digite um número inteiro:'))
    vetor.append(elemento)

for elemento in vetor:
    if elemento == vetor[0]:
        contador += 1

print(f'Elementos do Vetor: {vetor}')
print(f'Número de elementos iguais ao primeiro elemento: {contador}')