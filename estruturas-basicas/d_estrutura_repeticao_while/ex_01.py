'''
Faça um programa que leia a idade e o sexo (f – feminino ou m – masculino) de 15 pessoas, calcule e
imprima.
    a. A quantidade de mulheres.
    b. A quantidade de homens menores de idade.
'''
qtd_mulheres = 0
qtd_homens_menores_id = 0

i = 0
while i < 5: #utilizei 5 para facilitar os testes
    idade = int(input('Informe a idade da pessoa:'))
    sexo = input('Informe o sexe da pessoa; m-masculino, f-feminino:')
    if sexo == 'f':
        qtd_mulheres += 1
    elif idade < 18 and sexo == 'm':
        qtd_homens_menores_id += 1
    else:
        print('Verifique as informações digitadas!')
    i+=1

print(f'Quantidade total de mulheres: {qtd_mulheres}')
print(f'Quantidade de homens menores de idade: {qtd_homens_menores_id}')