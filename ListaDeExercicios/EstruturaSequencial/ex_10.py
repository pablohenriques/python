"""
    Faça um Programa que peça a temperatura em graus Celsius,
    transforme e mostre em graus Fahrenheit.
"""

temperatura_celsius = int(input("Digite, em Celsius, a temperatura para conversão em Fahrenheit:"))
temperatura_convertida_fahrenheit = (temperatura_celsius * (9/5)) + 32
print(f"{temperatura_celsius}ºF = {temperatura_convertida_fahrenheit}ºC")