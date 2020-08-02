'''
    Faça um algoritmo para calcular
    a série Fibonacci até o N-ésimo termo. 
    A série tem a seguinte forma:
'''

n = int(input('Informe o número de termos da sequência de Fibonacci: '))

anterior = 1
proximo = 1
numero = 1

for i in range(n):
    print(numero)
    numero = anterior + proximo
    anterior = proximo
    proximo = numero