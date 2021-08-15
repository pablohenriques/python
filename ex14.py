"""
    Faça um programa que lê as duas notas parciais obtidas por um aluno
    numa disciplina ao longo de um semestre, e calcule a sua média.
    A atribuição de conceitos obedece à tabela abaixo:
"""

from unittest import TestCase, expectedFailure, main


def atribuir_conceito(nota1: float, nota2: float) -> str:
    media = (nota1 + nota2) / 2

    if media <= 10:
        if 0 <= media < 4:
            conceito = "E"

        elif 4 <= media < 6:
            conceito = "D"

        elif 6 <= media < 7.5:
            conceito = "C"

        elif 7.5 <= media < 9:
            conceito = "B"

        else:
            conceito = "A"

        return conceito

    else:
        raise ValueError("Validar medias inseridas")


class TestExercicio14(TestCase):

    def test_caso_conceito_a(self):
        resultado = atribuir_conceito(10, 10)
        self.assertEqual(resultado, "A")

    def test_caso_conceito_c(self):
        resultado = atribuir_conceito(7.5, 7.5)
        self.assertEqual(resultado, "B")

    @expectedFailure
    def test_caso_conceito_erro(self):
        resultado = atribuir_conceito(7.5, 7.5)
        self.assertEqual(resultado, "C")


if __name__ == "main":
    main()
