'''
    Faça um algoritmo que calcule o valor de S, sendo que:
    S = 10! + 8! + 6! + ... + 2!
'''

soma = 0
fatorial = 1

for numero in range(10, 0, -2):

    for j in range(numero, 0, -1):
        fatorial *= j
    soma += fatorial
    
    print(f'Fatorial de {numero}!: {fatorial}')
    
    fatorial = 1

print(f'Soma total de todos fatoriais: {soma}')