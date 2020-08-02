'''
Faça um programa que receba a data de aniversário de duas pessoas (pessoa1 e pessoa2), sendo que a
data consiste em dia, mês e ano (lidos separadamente). Baseando nestas datas, informe se as duas
pessoas têm a mesma idade ou qual é a mais velha.
'''

print('Digite as informações da primeira pessoa')
p1_dia = int(input('Digite o dia de nascimento:'))
p1_mes = int(input('Digite o número do mês de nascimento:'))
p1_ano = int(input('Digite o ano de nascimento:'))
print('\n')

print('Digite as informações da segunda pessoa')
p2_dia = int(input('Digite o dia de nascimento:'))
p2_mes = int(input('Digite o número do mês de nascimento:'))
p2_ano = int(input('Digite o ano do seu nascimento:'))
print('\n')

ano_p1 = 2018 - p1_ano
mes_p1 = 12 - p1_mes
dia_p1 = 30 - p1_dia

ano_p2 = 2018 - p2_ano
mes_p2 = 12 - p2_mes
dia_p2 = 30 - p2_dia

if ano_p1 > ano_p2:
    msg = 'Pessoa 01 eh mais velha!'
elif ano_p2 > ano_p1:
    msg = 'Pessoa 02 é mais velha!'
else:
    if mes_p1 > mes_p2:
        msg = 'Pessoa 01 é mais velha!'
    elif mes_p2 > mes_p1:
        msg = 'Pessoa 02 é mais velha!'
    else:
        if dia_p1 > dia_p2:
            msg = 'Pessoa 01 é mais velha!'
        elif dia_p2 > dia_p1:
            msg = 'Pessoa 02 é mais velha!'
        else:
            msg = 'Ambas pessoas possuem a mesma idade!'

print(f'Pessoa 01: { p1_dia }/{ p1_mes }/{ p1_ano }')
print(f'Pessoa 02: { p2_dia }/{ p2_mes }/{ p2_ano }')
print(f'{ msg }')