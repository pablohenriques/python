'''
Faça um algoritmo que leia a quantidade de mulheres e a quantidade de homens em uma turma e depois
calcule e:
    a. Imprima a quantidade total de pessoas.
    b. Informe ao usuário se a turma possui mais homens, mais mulheres ou se tem a mesma quantidade
    de homens e mulheres.
'''

n_homens = int(input('Digite o número de homens na turma:'))
n_mulheres = int(input('Digite o número de mulheres na turma:'))

total_pessoas = n_homens + n_mulheres
status_turma = ''

if n_homens > n_mulheres:
    status_turma = 'mais homens.'
elif n_mulheres > n_homens:
    status_turma = 'mais mulheres.'
else:
    status_turma = 'o mesmo número de homens e mulheres.'

print('Número total de alunos:', total_pessoas)
print('Nesta turma há:', status_turma)
