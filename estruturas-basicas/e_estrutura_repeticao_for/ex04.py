"""
Faça um algoritmo que calcule a média dos termos da seguinte série:
10, 15, 20, 25, 30, ..., 500.
"""

somatorio = 0
contador = 1
resultado = 0

for i in range(10, 501, 5):
    somatorio += i
    contador += 1

resultado = somatorio/contador

print(f'Contador: {contador} - Somatório: {somatorio} - Média dos Termos: {resultado}')