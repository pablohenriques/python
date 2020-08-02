'''
Em uma eleição presidencial, existem 3 candidatos. Os votos foram registrados em fichas,
sendo que cada ficha contém um dos códigos a seguir:
 - 1, 2, 3 - Voto para os respectivos candidatos
 - 4 - Voto nulo
 - 5 - Voto em branco

Construa um algoritmo que leia as fichas, de forma que a última ficha (que não entre nos cálculos)
contém valor 0 (zero), calcule e apresente:
    a) a quantidade de eleitores que votaram;
    b) o total de eleitores que não escolheram um candidato (nulos ou brancos);
    c) o número candidato vencedor.
'''

cad_1 = 0
cad_2 = 0
cad_3 = 0
v_branco = 0
v_nulo = 0
qtd_eleitores = 0
vencedor = 0

i = 1
while i != 0:
    voto = int(input('Digite seu voto:'))

    if voto == 1:
        cad_1 += 1
    elif voto == 2:
        cad_2 += 1
    elif voto == 3:
        cad_3 += 1
    elif voto == 4:
        v_branco += 1
    elif voto == 5:
        v_nulo +=1

    qtd_eleitores += 1

    i = int(input('Digite 0 para terminar a eleição ou 1 para continuar:'))

if cad_1 > cad_2 and cad_1 > cad_3:
    vencedor = 1
elif cad_2 > cad_1 and cad_2 > cad_3:
    vencedor = 2
elif cad_3 > cad_1 and cad_3 > cad_2:
    vencedor = 3

print('Total de Eleitores:', qtd_eleitores)
print('Total de voto Branco e Nulos:', v_branco + v_nulo)
print('Candidato Vencedor:', vencedor)
