'''
    Faça um programa que leia, preencha e imprima um vetor A
    de 10 elementos inteiros. Depois, troque o conteúdo das 
    posições pares com o conteúdo das posições ímpares. Por exemplo: 

     - O conteúdo da posição 0 do vetor deve ser inserido na 
       posição 1 e o conteúdo da posição 1 deve ser inserido
       na posição 0;

    - O conteúdo da posição 2 do vetor deve ser inserido na posição 3
      e o conteúdo da posição 3 deve ser inserido na posição 2;

    - E assim por diante.
'''

vetor = []
vetor_aux = []
tam = 10

for i in range(tam):
    elemento = int(input('Digite um número para o vetor: '))
    vetor.append(elemento)

print(f'\nVetor: {vetor}\n')

for indice in range(tam - 1):
    aux = vetor[indice]
    vetor[indice] = vetor[indice+1]
    vetor[indice+1] = aux
    print(f'Modificação... : {vetor}')

print(f'\nVetor modificado: {vetor}')
    

