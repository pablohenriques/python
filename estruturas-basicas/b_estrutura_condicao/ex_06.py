'''
Faça um algoritmo que leia a velocidade máxima permitida em uma avenida e a velocidade de um carro
que passou por ela e:
    a. Caso o motorista esteja dentro da velocidade permitida, apresente a mensagem “Motorista está
    dentro da velocidade permitida!”;
    b. Caso contrário, apresente a mensagem “Motorista ultrapassou a velocidade máxima”, calcule e
imprima o valor da multa a ser paga por esse motorista.
    * são pagos R$ 10,00 para cada quilômetro que ultrapasse a velocidade máxima.
'''

velocidade_permitida = int(input('Digite a velocidade permitida:'))
velocidade_carro = int(input('Digite a velocidade do carro:'))

if velocidade_carro <= velocidade_permitida:
    print('Motorista está dentro da velocidade permitida!')
else:
    multa = (velocidade_carro - velocidade_permitida) * 10
    print('Motorista ultrapassou a velocidade máxima')
    print(f'Multa: R${ multa }')
