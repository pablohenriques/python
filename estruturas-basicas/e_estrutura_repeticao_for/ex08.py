"""
Faça um algoritmo que calcule e apresente a soma dos 30 primeiro termos da série:
480/10 - 475/11 + 470/12 - 465/13
"""

soma = 0
numerador = 480
denominador = 10
sinal = 1

# Valor 4 foi inserido no range apenas para teste
for indice in range(4): 
    #print(f'Numerador: {(numerador * sinal)} / Denominador: {denominador}')
    resultado = (numerador * sinal)/denominador
    #print(f'\t Resultado: {resultado}')
    soma += resultado
    #print(f'\t Soma: {soma}')
    numerador -= 5
    denominador += 1
    sinal *= -1

print(f'Soma Total: {soma}')