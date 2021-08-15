"""
    Faça um Programa que leia um número e exiba o dia correspondente da semana.
    (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""
from unittest import TestCase, main, expectedFailure


def dia_da_semana(numero: int) -> str:
    dias_da_semana = {
        1: 'domingo',
        2: 'segunda',
        3: 'terca',
        4: 'quarta',
        5: 'quinta',
        6: 'sexta',
        7: 'sabado'
    }

    if numero in dias_da_semana:
        for key, value in dias_da_semana.items():
            if key == numero:
                return f"{value}"


class TestExercicio13(TestCase):

    def test_case_segunda(self):
        dia = dia_da_semana(2)
        self.assertEqual(dia, "segunda")

    def test_case_sabado(self):
        dia = dia_da_semana(7)
        self.assertEqual(dia, "sabado")

    @expectedFailure
    def test_case_erro(self):
        dia = dia_da_semana(3)
        self.assertEqual(dia, "quarta")


if __name__ == "__main__":
    main()
