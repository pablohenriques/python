'''
    Faça um programa que leia dados de um vetor A,
    com 5 elementos inteiros. Depois, solicite um número
    ao usuário e informe quantas vezes esse número
    aparece no vetor.
'''
vetor = []
contador = 0

for i in range(5):
    numero = int(input('Digite um número:'))
    vetor.append(numero)

pesquisa = int(input('Digite um número para pesquisa no vetor: '))

for numero in vetor:
    if numero == pesquisa:
        contador += 1

print(f'Números do vetor: {vetor}')
print(f'Ocorrências do número ({pesquisa}) pesquisado: {contador}')

