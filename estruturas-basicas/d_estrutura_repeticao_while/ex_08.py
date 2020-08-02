'''
Em uma pesquisa um cinema solicitou os seguintes dados para os entrevistados: sexo e a quantidade de
filmes que assistiu no segundo semestre de 2013. Faça um algoritmo que leia os dados de 50 pessoas,
calcule e imprima:
    a. Para cada pessoa, apresente a informação se é mulher ou homem.
    b. A quantidade de homens que assistiram mais que 10 filmes.
    c. O percentual de mulheres entrevistadas.
'''
h_filmes = 0
m_percentual = 0
total_mulheres = 0

i = 0
while i < 5:
    sexo = input('Informe o sexo do cliente: M - Masculino, F - Feminino:')
    qtd_filmes = int(input('Informe a quantidade de filmes assistido no semestre:'))

    if sexo == 'M':
        print('Participante do sexo masculino.')
        if qtd_filmes > 10:
            h_filmes += 1
    elif sexo == 'F':
        print('Participante do sexo feminino.')
        total_mulheres += 1
    i += 1

m_percentual = (100 * total_mulheres) / 5

print(f'Homens que assistiram a mais de 10 filmes: {h_filmes}')
print(f'Percentual de mulheres participantes: {m_percentual}%')