'''
    Faça um programa que leia os dados de dois vetores A e B,
    com 5 caracteres cada, e depois crie e imprima um vetor C
    preenchido com os valores intercalados de A e B
'''

vetor_a = []
vetor_b = []
vetor_c = []
tam = 5

for i in range(tam):
    v1 = int(input('Informe um valor para o vetor A: '))
    vetor_a.append(v1)

print('\n')

for i in range(tam):
    v2 = int(input('Informe um valor para o vetor B: '))
    vetor_b.append(v2)

print('\n')

for indice in range(tam):
    vetor_c.append(vetor_a[indice])
    vetor_c.append(vetor_b[indice])

print(f'Valores vetor A: {vetor_a}')
print(f'Valores vetor B: {vetor_b}')
print(f'Valores vetor C: {vetor_c}')