'''
    Foi realizada uma pesquisa de algumas características dos alunos de uma escola,
para a qual foram coletados os seguintes dados referentes a cada aluno:
    Turno ("D - Diurno", "N - Noturno");
    Salário - para indicar que o aluno não possui emprego deve ser atribuído 0 (zero) ao salário;
    Idade.
Faça um algoritmo que leia os dados dos alunos, sendo que a leitura é encerrada quando
a idade digitada for igual a -1, determine e escreva:
    A média dos salários dos alunos entre 18 e 25 anos;
    O percentual de indivíduos menores de idade que estudam no período noturno e possuem
    emprego.
'''
total_salario = 0
total_alunos = 0
qtd_aluno = 0
menor_idade = 0

idade = 0
while idade != -1:
    turno = input('\nPeríodo de aula, D - Diurno, N - Noturno:')
    salario = int(input('Possui emprego? Digite o salário, caso contrário digite 0:'))
    idade = int(input('Informe a idade do aluno ou -1 para finalizar:'))

    if idade == -1:
        break

    if idade >= 18 and idade <= 25:
        qtd_aluno += 1
        total_salario += salario

    if idade < 18 and salario > 0 and turno == 'N':
        menor_idade += 1

    total_alunos += 1

percentual_alunos = (100 * menor_idade) / total_alunos

print(f'Total de alunos: {total_alunos}')
print(f'Média salarial, entre 18 & 25 anos: {total_salario/qtd_aluno}')
print(f'Menores de idades, empregados do período noturno: {percentual_alunos}')
