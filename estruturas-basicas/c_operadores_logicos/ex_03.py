'''
Uma loja está fazendo uma liquidação, sendo que o desconto é baseado nos seguintes dados dos
produtos: preço e cor da etiqueta ('P' – Preta, 'A' - Azul ou 'V' - Verde). Faça um algoritmo que leia os
dados do produto e informe se o produto possui ou não possui desconto e o valor a ser pago pelo
produto. Caso haja desconto, esse é atribuído da seguinte forma:
    • Não será fornecido desconto para os produtos com etiqueta preta;
    • Nos produtos com preço de R$ 200.00 ou mais e que possuem a etiqueta azul o cliente pagará a
      metade do preço;
    • Nos demais produtos o cliente receberá um desconto de 10%.
'''
preco_produto = float(input('Digite o preço do produto:'))
cor_etiqueta = input('Digite a cor da etiqueta: P – Preta, A - Azul ou V - Verde:')
preco_final = 0

if preco_produto >= 200 and cor_etiqueta == 'A':
    msg = 'Parabéns! Desconto de 50%'
    preco_final = preco_produto * 0.5
elif cor_etiqueta == 'P':
    msg = 'Este produto não possui desconto'
    preco_final = preco_produto
else:
    msg = 'Parabéns! Desconto de 10%'
    preco_final = preco_produto - (preco_produto * 0.1)

print(f'{msg}. Valor: R${preco_final}')