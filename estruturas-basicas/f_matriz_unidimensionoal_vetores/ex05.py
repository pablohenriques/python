'''
    Faça um programa que leia 5 números inteiros diferentes
    (não repetidos) e guarde em um vetor, calcule e imprima:

        a) A posição de cada número par.

        b) A posição do maior elemento do vetor,
           considerando que não existem valores repetidos.
'''
vetor = []
indice_pares = ''
indice_maior = 0
maior_numero = -999999

for i in range(5):
    numero = int(input('Digite um número, (Difirente do número anterior): '))
    
    if numero in vetor:
        print('Este número já existe - Insira os número novamente !')
        break

    vetor.append(numero)

for indice in range(len(vetor)):
    if vetor[indice] % 2 == 0:
        indice_pares += f' - {indice}'

    if vetor[indice] > maior_numero:
        maior_numero = vetor[indice]


print('Números do vetor:', vetor)
print('Índice dos números pares: ', indice_pares)
print('Índice do maior número do vetor:', maior_numero)
