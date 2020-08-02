'''
Faça um algoritmo que leia a idade de uma pessoa expressa em anos,
meses e dias e mostre-a expressa apenas em dias.
    ∗ Considere o ano com 365 dias e o mês com 30 dias
'''

from datetime import datetime

ano_nasc = int(input('Digite sua ano de nascimento, exemplo "2001":'))
mes_nasc = int(input('Digite o número do seu mês de nascimento, exemplo "07":'))
dia_nasc = int(input('Digite o dia de nascimento, exemplo "15":'))

ano_atual = datetime.now().year
mes_atual = datetime.now().month
dia_atual = datetime.now().day

anos_dias = (ano_atual - ano_nasc) * 365
mes_dias  = (mes_atual - mes_nasc) * 30
dia_dias =  dia_atual - dia_nasc        # não tratei este dado intencionalmente, mas é necessário formatá-lo

idade_dias = anos_dias + mes_dias + dia_dias

print(f'Dados formatados - Idade:{anos_dias}, Mês:{mes_dias}, Dia:{dia_dias}')
print('Idade em dias:', idade_dias)