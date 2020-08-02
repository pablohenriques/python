'''
Faça um algoritmo que leia um número inteiro e apresente uma das três mensagens: “Número igual a
zero”; “Número positivo”; ou “Número negativo”.
'''

num = int(input('Digite um número'))

if num > 0:
    print('Este número é positivo.')
elif num < 0:
    print('Este número é negativo.')
else:
    if num == 0:
        print('Este número é igual a zero')
