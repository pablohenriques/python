'''
Uma livraria está fazendo uma promoção para pagamento à vista em que o comprador pode escolher
entre dois critérios de desconto:
    Critério A: desconto de - R$ 0.25 por livro + R$ 7.50 fixo
    Critério B: desconto de - R$ 0.50 por livro + R$ 2.50 fixo
Faça um algoritmo em que o usuário entre com a quantidade de livros que deseja comprar e o programa
imprime uma das seguintes mensagens:
    As duas opções oferecem o mesmo desconto;
    A melhor opção de desconto é o critério A;
    A melhor opção de desconto é o critério B.
'''

qtd_livros = int(input('Digite a quantidade de livros para compra:'))

promocao = ''
criterio_a = (0.25 * qtd_livros) + 7.50
criterio_b = (0.5 * qtd_livros) + 2.50

if criterio_a > criterio_b:
    promocao = 'critério B'
elif criterio_b > criterio_a:
    promocao = 'critério A'
else:
    promocao = 'Ambos critérios'

print(f'Qtd de Livros: {qtd_livros}; Critério A: R${criterio_a}; Critério B: R${criterio_b}')
print(f'A melhor opção de compra é {promocao}')