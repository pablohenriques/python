"""
    Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

import unittest


def vertificar_maior_numero(*args):
    return max(args), min(args)


class TestExercicio07(unittest.TestCase):

    def test_caso_01(self):
        maior_valor = vertificar_maior_numero(10, 1, 5)[0]
        self.assertEqual(maior_valor, 10)

    def test_caso_02(self):
        menor_valor = vertificar_maior_numero(10, 1, 5)[1]
        self.assertEqual(menor_valor, 1)
