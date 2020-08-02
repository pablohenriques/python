'''
Construa um algoritmo que leia o código de um determinado produto e mostre a sua classificação,
utilizando a seguinte tabela:

    Código do Produto     | Classificação
    ----------------------|-----------------------
    1                     | Alimento não perecível
    2, 3 ou 4             | Alimento perecível
    5 ou 6                | Material de limpeza
    Qualquer outro código | Inválido
'''

cod_produto = int(input('Digite o código do produto:'))

tipo_produto = ''

if cod_produto == 1:
    tipo_produto = 'Alimento não perecível'
elif cod_produto == 2 or cod_produto == 3 or cod_produto == 4:
    tipo_produto = 'Alimento perecível'
elif cod_produto == 5 or cod_produto == 6:
    tipo_produto = 'Material de limpeza'
else:
    tipo_produto = 'Código Inválido'

print(f'Classificação do produto: {tipo_produto}')