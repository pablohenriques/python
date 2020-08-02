'''
    Faça um algoritmo que leia dois valores inteiros,
    X e Y, calcule e imprima X Y (elevar X à potência de Y).
    Exemplo: 3^4 = 3*3*3*3
'''

base = int(input('Informe a base: '))
expoente = int(input('Informe o expoente: '))
resultado=1

for i in range(expoente):
    resultado *= base

print(f'Base: {base} elevado a Expoente: {expoente} - Potência: {resultado}')