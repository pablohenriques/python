'''
Faça um algoritmo que receba uma quantidade de tempo representada em horas e minutos. Depois,
apresente esse tempo convertido em minutos.
'''
from datetime import datetime

hora = datetime.now().hour
minuto = datetime.now().minute

tempo_minutos = (hora * 60) + minuto

print(f'Horário atual em minutos: {tempo_minutos}')