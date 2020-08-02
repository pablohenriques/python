'''
Calcular a quantidade de litros de leite necessários e o custo para comprar o leite para alimentar as
crianças uma determinada creche que contém de três salas, sendo que é fornecida a quantidade de
crianças de cada sala e sabendo-se que:
    - cada litro de leite alimenta 5 crianças;
    - o litro de leite custa R$ 3.00.
'''
sala1 = int(input('Digite o número de crianças na sala 01:'))
sala2 = int(input('Digite o número de crianças na sala 02:'))
sala3 = int(input('Digite o número de crianças na sala 03:'))

total_criancas = sala1 + sala2 + sala3
total_litros = round(total_criancas / 5)
preco_total = total_litros * 3

print(f'Total de crinaças: {total_criancas}')
print(f'Total de litros necessários: {total_litros}L')
print(f'Custo total: R${preco_total}')