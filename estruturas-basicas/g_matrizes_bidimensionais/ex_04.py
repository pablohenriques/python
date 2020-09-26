"""
    Uma loja controla o estoque de suas mercadorias armazenando em uma tabela (matriz) a quantidade
    em estoque e o valor unitário das mercadorias, como mostra o exemplo a seguir, sendo que a linha
    da matriz representa o código do produto. 
        *quantidade em estoqeu
        **valor unitário

  linha q*  v**
    0   10  5.00
    1   15  12.00
    2   25  2.00
    ...
        0   1   coluna

    Faça um programa que:
        a. Leia os dados de 50 mercadorias e armazene na matriz MERCADORIA.
        b. Calcule e imprima o código e o valor da mercadoria mais barata.
"""

menor_preco = 99999
numero_mercadorias = 5
mercadoria = []
total = []
dict_barato = {'codigo': 0, 'valor': 0}

for idx in range(numero_mercadorias):
    linha = []
    quantidade_produto = int(input(f"Informe a quantidade de produtos [{idx}]:"))
    preco_unitario = int(input(f"Digite o preco unitário do produto [{idx}]:"))
    linha.append(quantidade_produto)
    linha.append(preco_unitario)
    mercadoria.append(linha)

print(f"Matriz mercadoria: {mercadoria}")

for indice in range(numero_mercadorias):
    linha = mercadoria[indice]
    for i in range(len(linha)):
        if linha[1] < menor_preco:
            menor_preco = linha[1]
            dict_barato['codigo'] = indice
            dict_barato['valor'] = linha[1]

print(f"Produto {dict_barato['codigo']} tem o menor preço, {dict_barato['valor']} real (is)")

for indice in range(len(mercadoria)):
    linha = mercadoria[indice]
    for i in range(len(linha)):
        if i == 0:
            quantidade_mercadoria = []
            quantidade_mercadoria.append(indice)
            quantidade_mercadoria.append(linha[0])
            total.append(quantidade_mercadoria)

for linha in total:
    print(f"Código da mercadoria: {linha[0]} - Quantidade mercadoria: {linha[1]}")
