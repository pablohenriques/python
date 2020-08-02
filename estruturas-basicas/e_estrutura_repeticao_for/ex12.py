'''
    Faça um algoritmo que solicite ao usuário
    dois números e imprima todos os números
    existentes entre o menor e o maior número
    digitado.

    * Obs: Testar sequência de números:
    -1 e -5; -5 e -1;
    1 e 10; 10 e 1;
    para compreender o funcionamento do range,
    neste exercício
'''

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))

if n1 == n2:
    print('Números iguais, não há sequência. Digite novamente')
else:
    print(f'Sequência de número entre {n1} e {n2}')
    for i in range((n1+1), n2, 1):
        print(f'Número: {i}')