'''
Uma doceira levou pães de mel para vender em uma feira de gastronomia.
Faça um algoritmo que calcule o lucro obtido pela doceira na feira,
baseando-se na quantidade vendida e no preço de custo e preço de venda da unidade,
considerando que o valor gasto pela doceira com o aluguel do stand foi de R$ 500.00.
'''

preco_custo = float(input('Digite o preço de custo de uma unidade do produto:'))
preco_venda = float(input('Digite o preco venda de uma unidade do produto:'))
qtd_vendida = int(input('Digite a quantidade de produtos vendidos:'))
lucro = ((preco_venda - preco_custo)*qtd_vendida) - 500
print('Lucro final:', lucro)
