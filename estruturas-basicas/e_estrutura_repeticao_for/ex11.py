'''
    Fazer um algoritmo que calcule o fatorial de 6
    Exemplo: 6! = 6*5*4*3*2*1
'''
resultado = 1

for i in range(6, 0, -1):
    resultado *= i
    print(f'Número: {i}')

print(f'Resultado: {resultado}')