"""
Faça um algoritmo que calcule a soma dos 20 primeiros números da série:
5 -10 15 -20 25 -30 ...
"""

acumulador = 0
multiplo = 5
sinal = 1

for indice in range(20):
    numero = (multiplo * (indice + 1)) * sinal
    #print(f'Indice: {indice} - Numero: {numero}')
    acumulador += numero
    #print(f'\tAcumulador: {acumulador}')
    sinal = sinal * (-1)

print(f'Soma total dos números: {acumulador}')