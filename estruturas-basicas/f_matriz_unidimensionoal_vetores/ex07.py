'''
    Faça um programa que leia dados de dois vetores A e B,
    de 5 elementos inteiros cada. Depois: 
        
        a) Construa um vetor C, no qual cada elemento é a
           diferença dos elementos correspondentes de A e B.

            Índice:   0 - 1 -  2 -  3 - 4
            Vetor A: 10 - 8 - 20 - 13 - 15
            Vetor B:  5 - 5 - 10 -  8 - 20
            Vetor C:  5 - 3 - 10 -  5 - -5 
        
        b) Informe quantos elementos negativos aparecem em C.
'''

vetor_a = []
vetor_b = []
vetor_c = []
subtracao = 0
negativos = 0

for i in range(5):
    elemento_a = int(input('Digite um valor para o vetor A: '))
    vetor_a.append(elemento_a)
    elemento_b = int(input('Digite um valor para o vetor B: '))
    vetor_b.append(elemento_b)

for indice in range(5):
    subtracao = vetor_a[indice] - vetor_b[indice]
    vetor_c.append(subtracao)
    if subtracao < 0:
        negativos += 1

print(f'Elementos do vetor A: {vetor_a}')
print(f'Elementos do vetor B: {vetor_b}')
print(f'Elementos do vetor C: {vetor_c}')
print(f'Número de Elementos negativos no vetor C: {negativos}')