"""
    Faça um Programa que calcule a área de um quadrado,
    em seguida mostre o dobro desta área para o usuário.
    Obs: Não há uma unidade específica para este exercício. Para este exercício
    a medida é a unidade (u) utilizada pelo usuário.
"""

lado = int(input("Digite o lado do quadrado: "))
area_quadrardo = lado * lado
dobro_area_quadrado = area_quadrardo * 2
print(f"Área do quadrado: {area_quadrardo} - Dobro da área do quadrado: {dobro_area_quadrado}")