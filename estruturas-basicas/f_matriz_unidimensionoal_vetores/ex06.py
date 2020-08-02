'''
    Faça um programa que leia um vetor A de 10
    posições e crie dois vetores B e C, de 5 
    elementos cada, preenchidos da seguintes forma:

        a) vetor B: conterá os valores que estão nas posições pares de A.

        b) vetor C: conterá a soma dos valores correspondentes de A e B.

        Exemplo:
            Índice:  0  - 1 - 2  - 3  - 4  - 5 - 6  - 7 - 8  - 9

            Vetor A: 45 - 8  - 20 - 13 - 15 - 9 - 10 - 8 - 51 - 14 
            Vetor B: 45 - 20 - 15 - 10 - 51
            Vetor C: 90 - 28 - 35 - 23 - 66
'''

vetor_a = []
vetor_b = []
vetor_c = []
soma = 0

for i in range(10):
    elemento = int(input('Digite um número: '))
    vetor_a.append(elemento)

for indice in range(10):
    if indice % 2 == 0:
        vetor_b.append(vetor_a[indice])

for indice in range(5):
    soma = vetor_a[indice] + vetor_b[indice]
    vetor_c.append(soma)

print(f'Elementos do Vetor A: {vetor_a}')
print(f'Elementos do Vetor B: {vetor_b}')
print(f'Elementos do Vetor C: {vetor_c}')


