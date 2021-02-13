"""
    Tendo como dado de entrada a altura (h) de uma pessoa,
    construa um algoritmo que calcule seu peso ideal,
    utilizando as seguintes fórmulas:
        a - Para homens: (72.7*h) - 58
        b - Para mulheres: (62.1*h) - 44.7
"""

altura_pessoa = float(input("Informe uma altura: "))
resultado_peso_ideal_homem = (72.7 * altura_pessoa) - 58
resultado_peso_ideal_mulher = (62.1 * altura_pessoa) - 44.7

print(f"Peso ideal para altura {altura_pessoa}m: -Homem: {resultado_peso_ideal_homem}")
print(f"Peso ideal para altura {altura_pessoa}m: -Mulher: {resultado_peso_ideal_mulher}")
