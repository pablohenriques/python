'''
    Faça um programa que leia dados de dois vetores A e B,
    com 10 elementos cada. Crie um vetor C, com 20 elementos,
    que é a junção de A e B.
'''

vetor_a = []
vetor_b = []
vetor_c = []
tam = 10

for i in range(tam):
    vet_a = int(input('Digite um número para o vetor A: '))
    vetor_a.append(vet_a)

print('\n')

for i in range(tam):
    vet_b = int(input('Digite um número para o vetor B: '))
    vetor_b.append(vet_b)

for v1 in vetor_a:
    vetor_c.append(v1)

for v2 in vetor_b:
    vetor_c.append(v2)

print('\n')

print(f'Elementos do vetor A: {vetor_a}')    
print(f'Elementos do vetor B: {vetor_b}')    
print(f'Junção dos vetores  : {vetor_c}')    