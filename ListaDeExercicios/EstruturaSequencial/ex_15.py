"""
    Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
    Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
    o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
        - salário bruto.
        - quanto pagou ao INSS.
        - quanto pagou ao sindicato.
        - o salário líquido.
        - calcule os descontos e o salário líquido, conforme a tabela abaixo:

        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$

        Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

valor_hora = float(input("Informe o valor da sua hora de trabalho, em reais: "))
horas_trabalhadas = int(input("Informe a quantidade de horas trabalhadas neste mês: "))
salario_bruto = valor_hora * horas_trabalhadas
desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (desconto_ir + desconto_inss + desconto_sindicato)

print(f"Salário Bruto: R${salario_bruto}")
print(f"IR (11%): R${desconto_ir}")
print(f"INSS (8%): R${desconto_inss}")
print(f"SINDICATO (5%): R${desconto_sindicato}")
print(f"Salário Líquido: R${salario_liquido}")