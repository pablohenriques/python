'''
Faça um algoritmo que leia os valores de dois lados adjacentes de uma figura geométrica e informe se
eles representam um quadrado perfeito ou um retângulo.

* https://brasilescola.uol.com.br/matematica/numero-quadrado-perfeito.htm
'''


l1 = int(input('Digite o primeiro lado da figura quadrangular:'))
l2 = int(input('Digite o segundo lado da figura quadrangular:'))

#considerando que os números digitados pelo usuário serão do conjuto naturais -
# a condição abaixo atende ao requisito para verificação de um quadrado perfeito

if l1 > 0 and l2 > 0:
    if l1 == l2:
        print('Esta figura é um quadrado perfeito.')
    else:
        print('Esta figura é um retângulo.')
else:
    print('Digite os lados corretamente')