'''
    Faça um programa que leia, preencha e imprima um vetor A de 10 
    elementos inteiros. Depois, preencha e imprima um vetor B de 10
    elementos inteiros, que deverá conter os valores das posições
    pares de A em suas posições ímpares e os valores das posições
    ímpares de A em suas posições pares.
'''
tam = 10

vetor_a = []
vetor_b = []


for indice in range(tam):
  elemento = int(input('Informe um elemento:'))
  vetor_a.append(elemento)
  vetor_b.append(elemento)

print(f'Vetor "a": {vetor_a}')
print(f'Vetor "b": {vetor_b}')

for indice in range(tam-1):
  if indice % 2 == 0:
    vetor_b[indice] = vetor_a[indice+1]
    vetor_b[indice+1] = vetor_a[indice]

print(f'\nVetor "b": {vetor_b}')
