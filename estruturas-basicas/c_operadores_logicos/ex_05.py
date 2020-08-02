'''
Em uma universidade está sendo realizado um congresso internacional, no qual os inscritos,
no momento da inscrição, podem escolher se participarão dos minicursos e se precisarão
de tradução simultânea. O valor da inscrição é calculado da seguinte forma:

    • Valor base: R$ 50.00;
    • Valor para participar dos minicursos: acréscimo de R$ 20.00 ao valor base;
    • Valor para a tradução simultânea: acréscimo de R$ 10.00 ao valor base.

Faça um algoritmo em que o usuário informa se deseja participar dos minicursos (S ou N) e
se precisa de tradução simultânea (S ou N). Depois, calcule e informe o valor da
inscrição a ser pago pelo usuário.
'''

valor_total = 0
(minicurso, traducao) = ('N','N')

inscricao = input('Deseja realizar a inscrição no congresso internacional, S-sim/N-não:')

if inscricao == 'S':

    valor_total = 50

    minicurso = input('Deseja participar de algum minicurso, S-sim/N-não:')
    traducao = input('Deseja incluir tradução simultânea, S-sim/N-não:')

    if minicurso == 'S':
        valor_total = valor_total + 20
    elif traducao == 'S':
        valor_total = valor_total + 10
else:
    print('Ok - Até breve.')

print(f'Confirmação da Inscrição: {inscricao}')
print(f'Confirmação do Minucurso: {minicurso}')
print(f'Confirmação da Tradução: {traducao}')
print(f'Valor total, R${valor_total}')