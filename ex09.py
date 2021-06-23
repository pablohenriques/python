"""
    Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

from unittest import TestCase, main


def lista_de_numeros_em_ordem_decrescente(*args):
    return sorted(args, key=float, reverse=True)


class TestExecicioo9(TestCase):

    def test_caso_01(self):
        lista_reversa = lista_de_numeros_em_ordem_decrescente(1, 2, 3)
        self.assertEqual(lista_reversa, [3, 2, 1])


if __name__ == "__main":
    main()
