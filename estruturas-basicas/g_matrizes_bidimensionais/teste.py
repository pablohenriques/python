lista = [
    [1, 2],
    [2, 3]
]

print(f'Lista: {lista}')

for idx in range(len(lista)):
    print(f'Linha: {lista[idx]}')
    lista[idx].append(5)
    print(f'Linha: {lista[idx]}')

print(lista)
