'''
A administração de uma rodoviária anotou dados das 40 pessoas que chegaram em um
determinado ônibus na cidade. Para cada pessoa foi preenchida uma ficha
com a idade e a procedência (c - Capital, i - Interior, o - Outro estado).
Faça um algoritmo que leia os dados, calcule e imprima:
        a. a quantidade de pessoas maiores de idade.
        b. a quantidade de pessoas vindas da capital e que tem mais que 60 anos.
        c. o percentual de pessoas que vieram do interior.
'''

qtd_maior_idade = 0
qtd_idosos_capital = 0
qtd_interior = 0
i = 0
while i < 5: #numero total de passageiros
    idade = int(input('Digite a idade do passageiro:'))
    procedencia = input('Digite a regiao de origem - c - Capital, i - Interior, o - Outro estado:')

    if idade >= 18:
        qtd_maior_idade += 1
        if idade > 60 and procedencia == 'c':
            qtd_idosos_capital += 1

    if procedencia == 'i':
        qtd_interior += 1

    i+=1

porcentagem_interior = (100 * qtd_interior) / 5 #numero total de passageiros

print('Quantidade de pessoas maiores de idade:', qtd_maior_idade)
print('quantidade de pessoas vindas da capital e que tem mais que 60 anos:', qtd_idosos_capital)
print(f'Percentual de pessoas que vieram do interior: {porcentagem_interior}%')