'''
    Escreva um algoritmo para gerar os primeiros n
    termos de uma progressão aritmética de termo 
    inicial Ti e razão r. Todos estes valores 
    deverão ser lidos do teclado.
    Exemplo: Ti=10; r=2; n=5
    Resultado PA -> 10, 12, 14, 16, 18
'''

ti = int(input('Informe o termo incial para progessão (Aritmética): '))
r = int(input('Informe a razão da progessão (Aritmética): '))
n = int(input('Informe o número de termos da progessão (Aritmética): '))
progressao = ti

for i in range(n):
    print(f'valor da Progressão: {progressao}')
    progressao += r