"""
    Tendo como dados de entrada a altura de uma pessoa,
    construa um algoritmo que calcule seu peso ideal,
    usando a seguinte fórmula: (72.7*altura) - 58
"""

altura_pessoa = float(input("Informe sua altura:"))
resultado_peso_ideal = (72.7 * altura_pessoa) - 58
print(f"Peso ideal para altura {altura_pessoa}m: {resultado_peso_ideal}")