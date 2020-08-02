'''
    Escreva um algoritmo para gerar os primeiros
    n termos de uma progressão geométrica de
    termo inicial Ti e razão r. Todos estes
    valores deverão ser lidos do teclado.

    Ti=10; r=2; n=5
    Resultado PG -> 10 20 30 40 80 160
'''

ti = int(input('Informe o termo inicial da progressão (Geométrica): '))
r = int(input('Informe a razão da progressão (Geométrica): '))
n = int(input('Informe o número de termos da progessão (Geométrica): '))
progressao = ti

for i in range(n):
    print(f'Valor da progressão: {progressao}')
    progressao *= r