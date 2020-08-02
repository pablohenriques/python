'''
Sabendo que cada quilowatt de energia custa um centésimo do salário mínimo, faça um programa que:
    - Receba inicialmente o valor do salário mínimo;
    - Leia um número indeterminado de linhas contendo cada uma a quantidade de quilowatts gasta
      em uma residência, sendo que o FLAG é a quantidade de quilowatts negativa.
    - Calcule e imprima:
        a) o valor a ser pago em cada residência;
        b) o valor total pago pelas residências.
'''
valor_kw = 0
custo_total = 0

salario_minimo = float(input('Digite o salário mínimo:'))

valor_kw = int(input('Informe o valor de Kw consumido ou digite um número negativo para sair:'))
while valor_kw >= 0:
    custo_kw = salario_minimo / 100
    custo_final = valor_kw * custo_kw
    custo_total += custo_final
    print(f'Valor da conta de Luz: R${ custo_final }')
    valor_kw = int(input('\nInforme o valor de Kw consumido ou digite um número negativo para sair:'))

print('\nValor total de todas residências:', custo_total)