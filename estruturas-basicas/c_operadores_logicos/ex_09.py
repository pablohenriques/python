'''
Construa um algoritmo para calcular o valor a ser pago pelo período de estacionamento de um
automóvel. O usuário deverá digitar a hora de entrada e a hora de saída. O valor cobrado pelo
estacionamento é:
    - R$ 4,00 para 1 hora de estacionamento
    - R$ 6,00 para 2 horas de estacionamento
    - R$ 1,00 por hora adicional (acima de 2 horas)
'''
from  datetime import datetime

valor = 0
extra = 0

e_hora = int(input('Digite o horário de entrada:'))
e_minutos = int(input('Digite os minutos de entrada:'))

s_hora = int(input('Digite o horário de saída:'))
s_minutos = int(input('Digite os minutos de saída:'))

calculo = (s_hora + (s_minutos/60)) - (e_hora + (e_minutos/60))

if calculo < 2:
    valor = 4.0
elif calculo < 3:
    valor = 6.0
else:
    extra = abs((calculo - 2) + 0.5)
    valor = 6.0 + (extra)

print(f'Variáveis - Cálculo:{calculo}, Valor:{valor}, Extra:{extra}')
print(f'Valor total do estacionamento: R${valor}')
