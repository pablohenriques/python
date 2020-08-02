'''
Uma escola utiliza os seguintes critérios para a obtenção da nota do aluno:
    - O aluno faz duas provas, sendo que o cálculo da média é (Prova1 + Prova2)/2;
    - O aluno deve assistir, no mínimo, 15 aulas para não ser reprovado por falta;
    - O aluno deve atingir, no mínimo, a média 6.0 para ser aprovado.
Faça um algoritmo que leia duas notas e quantidade de aulas frequentadas e apresente a situação do aluno,
de acordo com as instruções abaixo:
    - APROVADO - atingiu média 6.0 e assistiu pelo menos 15 aulas;
    - REPROVADO POR FALTA - atingiu ou não a média 6.0, mas não assistiu o mínimo de 15 aulas;
    - VAI PARA EXAME - assistiu pelo menos 15 aulas, mas não atingiu a média 6.0.

Caso o aluno tenha ido para exame, deve ser solicitada a nota do exame e informado se o
aluno foi APROVADO ou REPROVADO, sendo que o cálculo da nota final é
(média+exame)/2 e que o aluno deve atingir média 6.0.
'''

def exame(nota_aluno, nota_exame):
    media = (nota_aluno + nota_exame)
    if media >= 6.0:
        return 'Aprovado'
    return 'Reprovado'

n1 = float(input('Digite a primeira nota do aluno:'))
n2 = float(input('Digite a segunda nota do aluno:'))
p = int(input('Digite o número de presenças do aluno:'))

media = (n1 + n2) / 2
situacao = ''
status = 'NÃO'


if p >= 15:
    if media >= 6.0:
        situacao = 'Aprovado'
    else:
        status = 'SIM'
        ne = float(input('Informe a nota do exame:'))
        if exame(media, ne) == 'Aprovado':
            situacao = 'Aprovado'
        else:
            situacao = 'Reprovado - Nota'
else:
    situacao = 'Reprovado - Falta'

print(f'\nResultado Final: {situacao} - Exame Final: {status}')
