'''
Ana tem 5 anos e mende 1.15 metros. João tem 10 anos e mede 1.40 metros. Considerando que Ana
cresce 5 cm ao ano e que João cresce 3 cm ao ano, calcule e informe em quantos anos Ana ficará mais
alta que João.7
'''
ano = 0
altura_ana = 0#1.15
altura_joao = 1#1.40


cont = 0
while altura_ana != altura_joao and altura_joao != altura_ana:
    cont += 1
    altura_ana += 5
    ano += 1
    print('Altura Ana:', altura_ana)
    print('Altura joão:', altura_joao)
    print(ano)