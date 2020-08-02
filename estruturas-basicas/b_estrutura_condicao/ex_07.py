'''
Uma companhia de saneamento calcula o valor da conta de água de acordo com o tipo de consumidor:
    - Residencial: R$ 5.00 de taxa mais R$ 0.05 por m 3 gasto;
    - Comercial: R$ 500.00 para os primeiros 80 m 3 , acrescido de R$ 0.25 por m 3 gastos acima dos 80 m 3 ;
    - Industrial: R$ 800.00 para os primeiros 100 m 3 , acrescido de R$ 0.04 por m 3
      gastos acima dos 100 m 3 .

Baseando-se nessas informações, faça um algoritmo que leia o tipo do cliente e o seu consumo de água
em metros cúbicos. Depois, calcule e apresente a conta de água a ser paga pelo cliente.
'''

tipo_cliente = input('Informe a categoria do cliente: R - (Residencial), C - (Comercial), I - (Industrial):')
consumo_agua = int(input('Digite a quantidade de água consumida, em M³:'))
conta_agua = 0

if tipo_cliente == 'R':
    conta_agua = (consumo_agua * 0.05) + 5
elif tipo_cliente == 'C':
    if consumo_agua > 80:
        conta_agua = ((consumo_agua - 80) * 0.25) + 500
    else:
        conta_agua = 500
elif tipo_cliente == 'I':
    if consumo_agua > 100:
        conta_agua = ((consumo_agua - 100) * 0.04) + 800
    else:
        conta_agua = 800

print(f'Tipo de cliente: { tipo_cliente }\nValor total da conta: R${ conta_agua }')
