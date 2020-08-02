'''
Faça um algoritmo que, a partir da distância entre as cidades origem e destino,
calcule quantos litros de gasolina serão consumidos e quanto João vai gastar para
realizar uma viagem até a casa de sua tia. Considerando que:
    a) o carro de João tem um consumo médio de 10 km por litro;
    b) o preço da gasolina no posto em que João abastece o carro é de R$ 3.00.
Baseando-se nesses fatos, elabore um algoritmo que calcule as informações desejadas.
'''

distancia = int(input('Digite a distância total:'))
litros_necessario = distancia / 10
custo_final = litros_necessario * 3

print(f'Litros de gasolina necessários para viagem: {litros_necessario}L')
print(f'Custo final: R${custo_final}')