"""
    Faça um Programa que leia três números e mostre o maior deles.
"""

import unittest


def vertificar_maior_numero(*args):
    return max(args)


class TestExercicio06(unittest.TestCase):

    def test_caso_01(self):
        maior_valor = vertificar_maior_numero(10, 1, 5)
        self.assertEqual(maior_valor, 10)
