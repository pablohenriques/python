'''
Uma loja guarda os seguintes dados sobre cada um dos 150 produtos que revende: preço de custo, preço
de venda e tipo (V – vestuário e C – Calçado). Faça um algoritmo que leia os dados dos 150 produtos,
calcule e imprima:
    a.  Para cada produto, o lucro que proporciona.
    b.  Quantidade de calçados vendidos.
'''

preco_custo = 0
preco_venda = 0
qtd_calcado = 0

i = 0
while i < 5:
    tipo_prudoto = input('Digite o tipo do produto - V – vestuário e C – Calçado:')
    preco_custo = float(input('Digite o preço de custo:'))
    preco_venda = float(input('Digite o preço de venda:'))

    if tipo_prudoto == 'C':
        qtd_calcado += 1

    print(f'lucro: R$:{preco_venda - preco_custo}')
    i += 1

print('\nQuantidade de calçados vendidos:', qtd_calcado)