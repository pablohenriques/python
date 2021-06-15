import unittest

"Faça um Programa que peça dois números e imprima o maior deles."


def verificar_maior_numero(n1, n2):
    if n1 > n2:
        resultado = f"{n1} maior que {n2}"
    elif n2 > n1:
        resultado = f"{n2} maior que {n1}"
    else:
        resultado = f"{n1} é igual a {n2}"
    return resultado


class TestExercicios(unittest.TestCase):

    def test_caso_01(self):
        self.assertEqual(verificar_maior_numero(10, 15), f"15 maior que 10")

    def test_caso_02(self):
        self.assertEqual(verificar_maior_numero(15, 10), f"15 maior que 10")

    def test_caso_03(self):
        self.assertEqual(verificar_maior_numero(15, 15), f"15 é igual a 15")


if __name__ == "__main__":
    unittest.main()
