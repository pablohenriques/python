'''
Faça um algoritmo que leia um número inteiro. Caso o número digitado seja par e positivo, calcule e
apresente como resultado a metade deste número. Caso contrário, apresente o dobro do número.
'''

num = int(input('Digite um número inteiro qualquer:'))

if num > 0 and num % 2 == 0:
    resultado = num / 2
else:
    resultado = num * 2

print(f'Resultado: {resultado}')