'''
Faça um programa que solicite ao usuário 10 números e, depois da leitura,
informe qual foi o maior valor informado
'''

maior = -99999

i = 0
while i < 5:
    num = int(input('Digite um número:'))
    if num > maior:
        maior = num
    i += 1

print('O maior número digitado:', maior)