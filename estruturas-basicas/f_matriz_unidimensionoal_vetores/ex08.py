'''
    Faça um programa que leia os dados de dois vetores, NOTA1 e NOTA2,
    preenchidos com as notas de 10 alunos, sendo que o índice
    (posição no vetor) é o código do aluno. Depois, preencha
    um vetor MEDIAS com as médias dos alunos e informe o código
    de todos os alunos aprovados, considerando que a média
    mínima para aprovação é 6.0.
'''

nota1 = []
nota2 = []
medias = []
calculo = 0
aprovados = ''

for i in range(10):
    n1 = float(input(f'Digite a 1ª (primeira) nota do aluno {i}: '))
    nota1.append(n1)

print('\n')

for i in range(10):
    n2 = float(input(f'Digite a 2ª (segunda) nota do aluno {i}: ')) 
    nota2.append(n2)

for indice in range(10):
    calculo = (nota1[indice] + nota2[indice]) / 2
    medias.append(calculo)

for indice in range(10):
    if medias[indice] >= 6:
        aprovados += f' - {indice}'


print(f'\nVetor  de notas - NOTA1: {nota1}')  
print(f'Vetor de notas - NOTA2: {nota2}')  
print(f'Médias de notas - : {medias}')
print(f'Índice dos alunos aprovados: {aprovados}') 