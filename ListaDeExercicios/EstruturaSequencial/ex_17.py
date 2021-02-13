"""
    Faça um Programa para uma loja de tintas.
    O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
    Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
    e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros,
    que custam R$ 25,00.
    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
        -   comprar apenas latas de 18 litros;
        -   comprar apenas galões de 3,6 litros;
        -   misturar latas e galões, de forma que o desperdício de tinta seja menor. 
            Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias
    
    Exercicio resolvido com base na resolução do repositório abaixo:
        https://github.com/selatotal/pythonBrasilExercicios/blob/master/01_EstruturaSequencial/17_loja_tintas_2.py
"""

from math import ceil

area = float(input("Informe a área, em m², que será pintada:"))
litros = (area / 6) * 1.1

numero_latas = ceil(litros / 18)
numero_galoes = ceil(litros / 3.6)

numero_mix_latas = int(litros/18)
numero_mix_galoes = ceil((int(litros/18)) / 3.6)
#numero_mix_galoes = ceil(litros / 5)

custo_latas = numero_latas * 80
custo_galoes = numero_galoes * 25
custo_mix = (numero_mix_latas * 80) + (numero_mix_galoes * 25)

print(f'Área: {area} - Litros necessários: {litros}')
print(f'Número de Latas (18L): {numero_latas} - Custo total: {custo_latas} reais')
print(f'Número de Galões (3.6L): {numero_galoes} - Custo total: {custo_galoes} reais')
print(f'Mix - Número Latas: {numero_mix_latas} - Número Galões: {numero_mix_galoes} - Custo Total: {custo_mix} reais')