'''
    Faça um programa que leia a idade de 10 pessoas
    e guarde em um vetor, calcule e imprima:
        a) A maior idade.
        b) A quantidade de pessoas que possuem idade igual a maior idade.
'''

lista_idades = []
maior_idade = 0
contador_idade = 0

for i in range(5):
    idade = int(input('Informe a idade da pessoa: '))
    lista_idades.append(idade)

for idade in lista_idades:
    if idade > maior_idade:
        maior_idade = idade

for idade in lista_idades:
    if idade == maior_idade:
        contador_idade += 1

print(f'Lista de Idades: {lista_idades}')
print(f'Maior idade na lista: {maior_idade}')
print(f'Número de passoas que possuem maior idade: {contador_idade}')
