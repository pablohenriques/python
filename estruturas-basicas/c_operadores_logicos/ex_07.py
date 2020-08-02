'''
Uma loja está fazendo uma liquidação, sendo que o desconto é baseado nos seguintes dados dos
produtos: preço, possui desconto?
('S' - Sim ou 'N' - Não) e cor da etiqueta ('A' - Azul ou 'V' - Verde).
Faça um algoritmo que leia os dados do produto e informe se o
produto possui ou não possui desconto e o valor a ser pago pelo produto.
Caso haja desconto, esse é atribuído da seguinte forma:
    - Nos produtos com preço de R$ 100.00 ou mais e que possuem a etiqueta azul o cliente pagará a
      metade do preço;
    - Nos demais produtos o cliente receberá um desconto de 10%.
'''
preco_produto = float(input('Digite o preco do produto:'))
desconto = input('Possui desconto? S-Sim, N-Não:')

preco_final = 0

if desconto == 'S':
    cor_etiqueta = input('Informe a cor da etiqueta: A-Azul, V-Verde:')
    if preco_produto > 100 and cor_etiqueta == 'A':
        preco_final = preco_produto * 0.5
    else:
        preco_final = preco_produto - (preco_produto * 0.1)
else:
    preco_final = preco_produto

print(f'Preço final do produto: R${preco_final}')