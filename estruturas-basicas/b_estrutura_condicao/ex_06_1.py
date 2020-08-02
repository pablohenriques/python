'''
O IMC (índice de massa corporal) é calculado da seguinte forma: peso/altura 2 . Considera-se que o
IMC ideal para os homens é 22 e para as mulheres é 20.8. Escreva um algoritmo para ler os dados de
uma pessoa, imprimir o IMC desta e indicar se ela está no peso ideal, acima do peso ideal,
ou abaixo do peso ideal.
'''
sexo = input('Informe o sexo: "M" ou "F":')
peso = float(input('Informe o peso:'))
altura = float(input('Informe a altura:'))

imc = (peso / (altura * altura))

if sexo == 'M':
    if imc == 22:
        msg = 'Parabéns, você possui peso ideal !'
    else:
        msg = 'Continue se exercitando !'
elif sexo == 'F':
    if imc == 20.8:
        msg = 'Parabéns, você possui peso ideal !'
    else:
        msg = 'Continue se exercitando !'
else:
    msg ='Digite os dados corretamente.'

print(f' IMC: { imc }; { msg }')
