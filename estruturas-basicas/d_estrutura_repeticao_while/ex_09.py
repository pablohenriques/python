'''
Faça um programa que leia um número e imprima uma mensagem indicando se ele é par ou não. Porém,
este programa deve se repetir até que o usuário digite zero.
'''

i = 1
while i != 0:
    num = int(input('Digite um número:'))

    if num % 2 == 0:
        print('Este número é par!')
    else:
        print('Este número é impar!')

    i = int(input('Continuar? Digite 1 - Finalizar? Digite 0: '))
