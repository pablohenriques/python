"""
Faça um algoritmo que calcule a soma dos termos da seguinte série:
10, 20, 30, 40, 50, 60 ... 1000
"""

somatorio = 0
contador = 0
resultado = 0

for i in range(10, 1001, 10):
    somatorio += i
    contador += 1

resultado = somatorio/contador

print(f"Contador: {contador} - Somatório: {somatorio} - Resultado: {resultado}")