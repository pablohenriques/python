'''
    Fazer um algoritmo que calcule o fatorial de 5
    Exemplo: 5! = 5*4*3*2*1
'''
resultado = 1

for i in range(5, 0, -1):
    resultado *= i
    print(f'Número: {i}')

print(f'Resultado: {resultado}')