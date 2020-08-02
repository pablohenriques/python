'''
    Faça um programa que leia as 10 respostas do gabarito
    de uma prova e guarde em um vetor de caracteres G,
    sendo que a posição do vetor representa o número da questão.
    A seguir, leia as 10 respostas de um aluno e guarde
    em um vetor R. Depois, realize as seguintes ações:
        
        a. Imprima os números das questões que o aluno errou.

        b. Informe se o aluno foi aprovado, sendo que é aprovado
           o aluno que teve 6 ou mais acertos.
'''

gabarito = []  # Vetor G
respostas = [] # Vetor R
acertos = 0
status = 'reprovado'
numero_questoes = 10

for i in range(numero_questoes):
    questao = input(f'Digite: a, b, c, d, ou e para a questão {i}: ')
    gabarito.append(questao)

for i in range(numero_questoes):
    resposta = input(f'Digite: a, b, c, d, ou e para resposta da questão {i}: ')
    respostas.append(resposta)

for i in range(numero_questoes):
    if gabarito[i] == respostas[i]:
        acertos += 1

if acertos >= 6:
    status = 'aprovado'

print(f'\nGabarito: {gabarito}')
print(f'Respostas: {respostas}')
print(f'Número de acertos: {acertos}')
print(f'Status: {status}')