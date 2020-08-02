'''
Sabendo que cada quilowatt de energia custa um centésimo do salário mínimo,
faça um algoritmo que receba o valor do salário mínimo e da quantidade de
quilowatts gasta em uma residência, calcule e imprima o valor pago pela residência em questão.
'''

salario_min = float(input('Digite o valor do salário mínimo:'))
qtd_qwatt = int(input('Digite a quantidade de quilowatts gasta:'))

valor_qwatt = salario_min / 100
conta_energia = qtd_qwatt * valor_qwatt

print(f'Valor da conta de luz: R${conta_energia}')