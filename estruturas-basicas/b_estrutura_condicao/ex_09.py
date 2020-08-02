'''
Escreva um algoritmo que leia dois números e apresente os seguintes resultados:
    - A média dos números.
    - Caso os números sejam diferentes:
        O quadrado do menor.
        O dobro do maior.
'''
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))

if n1 == n2:
    media = (n1 + n2)/2
    print('Média dos números digitados:', media)
else:
    if n1 > n2:
        dobro_maior = n1 * 2
        quadrado_menor = n2 * n2
        print(f'Dobro do maior número: { dobro_maior } - Quadrado do menor número: { quadrado_menor }')
    else:
        dobro_maior = n2 * 2
        quadrado_menor = n1 * n1
        print(f'Dobro do maior número: {dobro_maior} - Quadrado do menor número: {quadrado_menor}')
