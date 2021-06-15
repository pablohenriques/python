"""
    Faça um Programa que verifique se uma letra digitada é vogal ou consoante
"""

import unittest


def verificar_letra(letra):
    vogais = ['a', 'e', 'i', 'o', 'u']
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

    if letra.lower() in vogais:
        resultado = "vogal"
    elif letra.lower() in consoantes:
        resultado = "consoante"
    else:
        resultado = "incorreta"

    return resultado


class TestExercicio04(unittest.TestCase):

    def test_caso_01(self):
        self.assertEqual(verificar_letra("A"), "vogal")

    def test_caso_02(self):
        self.assertEqual(verificar_letra("z"), "consoante")

    def test_caso_03(self):
        self.assertEqual(verificar_letra("?"), "incorreta")


if __name__ == "__main__":
    unittest.main()

