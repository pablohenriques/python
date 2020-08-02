'''
Um grupo de investidores fez levantamento sobre os hábitos das mulheres que moram em uma pequena
cidade do interior, para saber se valia a pena abrir um novo salão de beleza na cidade. Para isso, para
cada entrevistada solicitou os seguintes dados: idade, renda mensal, valor gasto mensalmente com salão
de beleza e se acha que há necessidade de um novo salão na cidade ('s' - sim ou 'n' - não). Sabendo-se
que foram entrevistadas 1500 mulheres, fazer um algoritmo que calcule e escreva:

    a) a média dos valores gastos com salão por mulheres com idade entre 25 e 45 anos (inclusive as
    duas);
    b) o número de mulheres que respondeu não;
    c) a quantidade de mulheres que respondeu sim e que tem uma renda mensal menor que um salário
    mínimo.
    * O valor do salário mínimo deve ser lido antes da leitura dos dados da pesquisa
'''
cont  = 0
cont_n  = 0
cont_s = 0
renda_total = 0
media = 0

salario = float(input('Informe o valor do salário mínimo:'))

i = 0
while i < 2:

    idade = int(input('Informe sua idade:'))
    renda_mensal = float(input('Informe sua renda mensal, valor exato ou aproxamido:'))
    valor_gasto = float(input('Digite o valor gasto mensamente com salão de beleza:'))
    salao_confirmacao = input('Acredita que a cidade necessita de um novo salão de beleza? S ou N:')
    print('\n')

    if idade >= 25 and idade <= 45:
        cont += 1
        renda_total += renda_mensal

    if salao_confirmacao == 'N':
        cont_n += 1

    if salao_confirmacao == 'S' and renda_mensal < salario:
        cont_s += 1

    i += 1

if renda_total != 0 and cont != 0:
    media = renda_total / cont

print('A média dos valores gastos com salão por mulheres com idade entre 25 e 45 anos:', media)
print('Número de respostas negativas a construção de um novo salão:', cont_n)
print('Número de respostas postivas de mulheres que recebem menos de 1 salário mínimo:', cont_s)