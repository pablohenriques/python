'''
Faça um algoritmo que solicite 10 números inteiros ao usuário, calcule e imprima:
    a. para cada número, informe se ele é negativo, positivo ou igual a 0 (zero);
    b. a quantidade de números negativos;
    c. o maior número positivo.
'''
qtd_num_negativo = 0
maior = -1

i = 0
while i < 5:
    n = int(input('Digite um número inteiro:'))
    if n > 0:
        if n > maior:
            maior = n
        print(f'Número {n} positivo!')
    elif n < 0:
        qtd_num_negativo += 1
        print(f'Número {n} negativo')
    else:
        print(f'Número {n} é igual a zero')
    i += 1

print(f'Quantidade números negativos: {qtd_num_negativo}')
print(f'Maior número positivo {maior}')