"""
    Faça um Programa que verifique se uma letra digitada é "F" ou "M".
    Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

import unittest


def verificar_sexo(sexo):
    if sexo.lower() == "m":
        resultado = "masculino"
    elif sexo.lower() == "f":
        resultado = "feminino"
    else:
        resultado = "sexo invalido"
    return resultado


class TestExercicio03(unittest.TestCase):

    def test_caso_01(self):
        self.assertEqual(verificar_sexo("M"), f"masculino")

    def test_caso_02(self):
        self.assertEqual(verificar_sexo("f"), f"feminino")

    def test_caso_03(self):
        self.assertEqual(verificar_sexo("A"), f"sexo invalido")


if __name__ == "__main__":
    unittest.main()

