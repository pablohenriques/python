'''
O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do
distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem
do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia
o custo de fábrica de um carro e escreva o custo ao consumidor.
'''

custo_fabrica = float(input('Digite o custo de fábrica do carro, em reais:'))
# 28% distribuidor + 45% impostos
custo_consumidor = (custo_fabrica * 0.73) + custo_fabrica
print(f'Porcentagem Distribuidor: 28% - R${custo_fabrica*0.28}')
print(f'Porcentagem Impostos: 45% - R${custo_fabrica*0.45}')
print(f'Valor final do veículo: R${custo_consumidor}')