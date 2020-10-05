"""
    Elabore um programa que leia um vetor A de 5 posições. Após a leitura deste vetor construa uma
    matriz B (5 x 5), definida da seguinte forma:
        − A primeira linha da matriz é gerada pegando-se os elementos do vetor, e subtraindo cada um
          deles de 0;

        − A segunda linha da matriz é gerada pegando-se os elementos do vetor, e subtraindo cada
          uma deles de 1;

        −A terceira linha da matriz é gerada pegando-se os elementos do vetor, e subtraindo cada uma
         deles de 2;

        −E assim sucessivamente;

Depois, imprima o vetor e a matriz resultante.
"""
matriz = []
vetor = []
cont = 0
acm = 0

for i in range(5):
    elemento = int(input(f'Insira um número inteito na posição [{i}] do vetor:'))
    vetor.append(elemento)

for i in range(5):
    linha = []
    for j in vetor:
        valor = j - cont
        linha.append(valor)
        print(f'Valor: {valor}')
    matriz.append(linha)
    cont = 0
    acm += 1
    cont = acm

print(f'Matriz: {matriz}')