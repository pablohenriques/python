"""
    Faça um Programa que peça os 3 lados de um triângulo.
    O programa deverá informar se os valores podem ser um triângulo.
    Indique, caso os lados formem um triângulo, se o mesmo é:
        equilátero, isósceles ou escaleno.

    Dicas:
    - Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    - Triângulo Equilátero: três lados iguais;
    - Triângulo Isósceles: quaisquer dois lados iguais;
    - Triângulo Escaleno: três lados diferentes;
"""


if __name__ == "__main__":
    # a, b, c = 10, 5, 9
    # a, b, c = 10, 9, 10
    # a, b, c = 10, 10, 10

    a = int(input("Digite o *primeiro* lado do triângulo: "))
    b = int(input("Digite o *segundo* lado do triângulo: "))
    c = int(input("Digite o *terceiro* lado do triângulo: "))

    condicao1 = abs(b-c) < a < (b+c)
    condicao2 = abs(a-c) < b < (a+c)
    condicao3 = abs(a-b) < c < (a+b)
    validacao = condicao1 and condicao2 and condicao3

    if validacao:
        if (a == b and b == a) and (b == c and c == b) and (c == a and c == b):
            print("Triângulo Equilátero")
        elif (
                (a == b and b == a and a != c and b != c) or
                (b == c and c == b and b != a and c != a) or
                (c == a and a == c and c != b and a != b)
        ):
            print(f"Triângulo Isóceles")
        else:
            print(f"Triângulo Escaleno")
    else:
        print(f"Lados não formam um triângulo")
