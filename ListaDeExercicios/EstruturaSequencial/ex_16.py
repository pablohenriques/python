"""
    Faça um programa para uma loja de tintas. O programa deverá
    pedir o tamanho em metros quadrados da área a ser pintada.
    Considere que a cobertura da tinta é de 1 litro para cada 3 metros
    quadrados e que a tinta é vendida em latas de 18 litros,
    que custam R$ 80,00. Informe ao usuário a quantidades de latas de
    tinta a serem compradas e o preço total.
"""
from math import ceil

area = int(input("Informe a área (em metros ²) que será pintada: "))
litros_necessarios = area / 3
numero_latas = ceil(litros_necessarios / 18)
preco_total = numero_latas * 80
print(f"1L -> 3m² - 1lata -> 18L")
print(f"Litros necessários: {litros_necessarios} - Número de Latas: {numero_latas} - Preço Total (Reais): {preco_total}")