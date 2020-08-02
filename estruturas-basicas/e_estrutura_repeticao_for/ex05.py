"""
Faça um algoritmo que calcule o produto dos 10 primeiros termos da seguinte série:
5, 10, 15, 20, 25, 30, ...
"""

resultado = 1
multiplo = 5

for indice in range(10):
    numero = multiplo * (indice + 1)
    #print(f'Número: {numero}')
    resultado = numero * resultado
    #print(f'\tResultado: {resultado}')

print(f'Resultado Final da Multiplicação: {resultado}')