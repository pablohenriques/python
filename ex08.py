"""
    Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
    sabendo que a decisão é sempre pelo mais barato.
"""

import unittest


def encontar_menor_preco(*args):
    return min(args)


class TextExercicio08(unittest.TestCase):

    def test_caso_01(self):
        precos = encontar_menor_preco(100, 5, 1.5)
        self.assertEqual(precos, 1.5)


if __name__ == "__main":
    unittest.main()
