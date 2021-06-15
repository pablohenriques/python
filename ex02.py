import unittest

"""Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""


def verificar_numero_natural(numero: float):
    if numero > 0:
        resultado = "positivo"
    elif numero < 0:
        resultado = "negativo"
    else:
        resultado = "neutro"

    return resultado


class TestExercicios(unittest.TestCase):

    def test_caso_01(self):
        self.assertEqual(verificar_numero_natural(0), f"neutro")

    def test_caso_02(self):
        self.assertEqual(verificar_numero_natural(1), f"positivo")

    def test_caso_03(self):
        self.assertEqual(verificar_numero_natural(-1), f"negativo")


if __name__ == "__main__":
    unittest.main()
