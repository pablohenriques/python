"""
    Faça um programa que leia uma matriz cujo conteúdo é a população dos 10 municípios mais
    populosos de cada um dos 26 estados brasileiros (i = estado, j = município)

        - Determine e imprima o número do município mais populoso e o número do estado a que ele
          pertence.

        - Considerando que a 1ª coluna contém sempre a população da capital do estado, calcular a média
          da população das capitais dos 26 estados.

        - Imprima a média da população de cada estado.
"""

maior = -99999
total_populacao_capitais = 0
maior_populacao = {'cidade': [], 'estado': [], 'populacao': []}
numero_estados = 2
numero_cidades = 3
matriz_populacao = []

for i in range(numero_estados):
    linha = []
    for j in range(numero_cidades):
        populacao_cidade = int(input(f"Informe o número de habitantes da cidade {j} do estado {i}:"))
        linha.append(populacao_cidade)
    matriz_populacao.append(linha)

print(f"\nMatriz populacional: {matriz_populacao}\n")

for i in range(len(matriz_populacao)):
    linha = matriz_populacao[i]
    for j in range(len(linha)):
        if linha[j] >= maior:
            maior = linha[j]
            maior_populacao['cidade'].append(j)
            maior_populacao['estado'].append(i)
            maior_populacao['populacao'].append(linha[i])

print(f"Município (s) mais populoso (s): {maior_populacao['cidade']} - População(ões): {maior_populacao['populacao']} - Estado (s) {maior_populacao['estado']}")

for i in range(len(matriz_populacao)):
    linha = matriz_populacao[i]
    for j in range(len(linha)):
        if j == 0:
            total_populacao_capitais += linha[j]

media_populacao_capitais = total_populacao_capitais / (len(matriz_populacao))
print(f'Média populacional das capitais: {media_populacao_capitais}')


for i in range(len(matriz_populacao)):
    linha = matriz_populacao[i]
    total_populacao = 0
    contador = 0
    for j in range(len(linha)):
        total_populacao += linha[j]
        contador += 1
    print(f"Média populacional do estado [{i}]: {total_populacao / contador}")
    
