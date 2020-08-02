'''
Faça um programa que leia sempre dois números e imprima o quadrado do menor número. O programa
deverá ser finalizado somente quando o usuário digitar o valor zero para os dois números.
'''

i = 1
j = 1
while i != 0 or j != 0:
    i = int(input('Digite um número:'))
    j = int(input('Digite outro número:'))

    if i < j:
        print('Quadrado do menor número:', i * i)
    elif j < i:
        print('Quadrado do menor número:', j * j)

    print('\n')