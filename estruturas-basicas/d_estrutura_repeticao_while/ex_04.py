'''
Faça um algoritmo que solicite 10 números inteiros ao usuário, calcule e imprima:
    a. O dobro de cada número positivo.
    b. A quantidade de números negativos.

    * Considere que o usuário nunca digitará o número 0 (zero).
'''

qtd_numeros_negativos = 0

i = 0
while i < 10:
    num = int(input('Digite um número inteiro:'))

    if num > 0:
        print(f'Dobro do número digitado:{num * 2}\n')
    elif num < 0:
        qtd_numeros_negativos += 1

    i += 1

print('\nNúmero total de números negativos digitados:', qtd_numeros_negativos)