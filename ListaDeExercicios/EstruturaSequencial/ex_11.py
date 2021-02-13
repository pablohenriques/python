"""
    Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
        a   -   o produto do dobro do primeiro com metade do segundo .
        b   -   a soma do triplo do primeiro com o terceiro.
        c   -   o terceiro elevado ao cubo.
"""

n1 = int(input("Digite o primeiro número inteiro:"))
n2 = int(input("Digite o segundo número inteiro:"))
nr1 = float(input("Digite um número real:"))

item_a = (n1*2) * (n2/2)
item_b = (n1*3) + nr1
item_c = (nr1**3)

print(f"O produto do dobro do primeiro com metade do segundo: {item_a}")
print(f"A soma do triplo do primeiro com o terceiro: {item_b}")
print(f"O terceiro elevado ao cubo: {item_c}")