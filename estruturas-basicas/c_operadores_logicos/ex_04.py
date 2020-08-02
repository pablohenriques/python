'''
Dados três valores A, B e C, verificar e informar se eles podem ser os comprimentos dos lados de um
triângulo e, se forem, verificar se compõem um triângulo equilátero, isósceles ou escaleno,
sendo que:
    - Triângulo é uma figura geométrica de três lados, onde cada lado é menor do
      que a soma dos outros dois.
    - Triângulo equilátero: três lados iguais.
    - Triângulo isósceles: dois lados iguais.
    - Triângulo escaleno: todos os lados diferentes.
'''

def existencia(a, b, c):
    if a < (b + c):
        if b < (a + c):
            if c < (a + b):
                return True
    return False

def tipo_triangulo(a, b, c):
    if (a == b and a == c) and (b == a and b == c) and (c == a and c == b):
        tipo = 'Equilátero'
    elif (a == b and b == a and a != c) or (b == c and c == b and b != a) or (a == c and c == a and c != b):
        tipo = 'Isósceles'
    else:
        tipo = 'Escaleno'
    return tipo


l1 = int(input('Digite o primeiro lado do triângulo:'))
l2 = int(input('Digite o segundo lado do triângulo:'))
l3 = int(input('Digite o terceiro lado do triângulo:'))

if existencia(l1, l2, l3):
    print(f'Este triângulo é {tipo_triangulo(l1, l2, l3)}')
else:
    print('Estes valores não formam um triângulo. Digite os valores novamente.')