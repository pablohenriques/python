"""
    Faça um Programa que peça a temperatura em graus Fahrenheit,
    transforme e mostre a temperatura em graus Celsius.
    Obs: C = 5 * ((F-32) / 9).
"""

temperatura_fahrenheit = int(input("Digite, em Fahrenheit, a temperatura para conversão em Celsius:"))
temperatura_convertida_celsius = 5 * ((temperatura_fahrenheit - 32) / 9)
print(f"{temperatura_fahrenheit}ºF = {temperatura_convertida_celsius}ºC")