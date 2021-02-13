"""
    João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
    o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes
    maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
    deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que
    você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
    Gravar na variável excesso a quantidade de quilos além do limite
    e na variável multa o valor da multa que João deverá pagar.
    Imprima os dados do programa com as mensagens adequadas.
    Obs: Neste exercício não foi considerado um tratamento para valores de excesso menores
    que zero.
"""

peso_peixe = float(input("Digite, em quilogramas (Kg), a quantidade de peixe adquirido:"))
excesso_peixe = peso_peixe - 50
valor_multa = round(excesso_peixe * 4, 2)
print(f"Valor multa: R${valor_multa}0")
