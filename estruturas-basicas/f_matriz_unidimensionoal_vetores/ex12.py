'''
    Faça um programa que leia, preencha e imprima um vetor A de 10 
    elementos inteiros. Depois, preencha e imprima um vetor B de 10
    elementos inteiros, que deverá conter os valores das posições
    pares de A em suas posições ímpares e os valores das posições
    ímpares de A em suas posições pares.
'''
vetor_a = []
vetor_b = []

vet_par = []
vet_impar = []

tam = 5
aux = 0

for i in range(tam):
    elemento = int(input(f'Informe um número para o vetor[{i}]: '))
    vetor_a.append(elemento)

for index in range(tam):
  if index % 2 == 0:
    vet_par.append(vetor_a[index])
  else:
    vet_impar.append(vetor_a[index])

for indice in range(tam):
  if indice % 2 == 0:
    vetor_b.append(vet_impar[indice])
  elif indice % 2 != 0:
    vetor_b.append(vet_par[indice])
  #else:
  #  vetor_b.append[vetor_a[index]]


print(f'\nVetor par: {vet_par}')
print(f'\nVetor impar: {vet_impar}')

print(f"\nVetor a: {vetor_a}")
print(f"\nVetor b: {vetor_b}")


