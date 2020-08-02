"""
Fazer um algoritmo que calcule escreva o valor de S, que é a soma dos 15 primeiros termos da série:
S = (5/3) + (10/8) + (15/13) + (20/18) + (25/23) + ...
"""

somatorio = 0 
numerador = 5
denominador = 3

for indice in range(15):
    somatorio += numerador/denominador
    numerador += 5
    denominador += 5 

print(f'Resultado da soma: {somatorio}') 