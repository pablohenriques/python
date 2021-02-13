"""
    Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

n1 = float(input("Informe a primeira nota do aluno (a): "))
n2 = float(input("Informe a segunda nota do aluno (a): "))
n3 = float(input("Informe a terceira nota do aluno (a): "))
n4 = float(input("Informe a quarta nota do aluno (a): "))

media = (n1+n2+n3+n4) / 4
print(f"Média do aluno (a): {media}")