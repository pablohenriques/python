'''
    Faça um algoritmo que calcule e apresente o valor de S,
    sendo que:
    S = 2/1 -4/2 + 6/3 -8/4 + ... -20/10
'''

soma = 0
denominador = 1
numerador = 2
sinal = 1
resultado = 0
soma = 0

for i in range(10):
    #print(f'Numeredor: {(sinal * numerador)} / Denominador: {denominador}')
    resultado = (sinal * numerador) / denominador
    #print(f'\t Resultado: {resultado}')
    soma += resultado
    #print(f'\t Soma: {soma}')
    numerador += 2
    denominador += 1
    sinal *= -1

print(f'Soma Total: {soma}')