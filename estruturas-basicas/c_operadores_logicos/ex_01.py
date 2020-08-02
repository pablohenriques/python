"""
Escreva um algoritmo que leia dois números inteiros e apresente a mensagem "Os dois números devem
ser diferentes de zero!" se for digitado pelo menos um número igual a zero. Caso contrário, calcule e
apresente a soma dos números.
"""

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))

if n1 == 0 or n2 == 0:
    print('Os dois número devem ser diferentes de zero - 0!')
else:
    print('Soma dos números digitados:', n1 + n2)