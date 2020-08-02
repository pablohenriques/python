'''
Uma professora precisa calcular a média de um aluno.
O aluno realizou 3 provas, sendo que a primeira prova tem peso 1,
a segunda tem peso 2 e a terceira prova tem peso 3. Faça um algoritmo para calcular
e apresentar a média ponderada do aluno.
'''

n1 = float(input('Digite a primeira nota do aluno:'))
n2 = float(input('Digite a segunda nota do aluno:'))
n3 = float(input('Digite a terceira nota do aluno:'))
media = ((n1 * 1) + (n2 * 2) + (n3 * 3)) / 6
print('Média Final:', media)