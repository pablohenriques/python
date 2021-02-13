"""
    Faça um Programa que pergunte quanto você ganha por hora
    e o número de horas trabalhadas no mês. Calcule e mostre
    o total do seu salário no referido mês.
"""

valor_hora = float(input("Informe, em reais, o valor da sua hora de trabalho: "))
horas_trabalhdas = int(input("Informe, em números naturais, as horas trabalhadas, neste mês: "))
salario = valor_hora * horas_trabalhdas
print(f"Salário neste mês: {salario} reais")