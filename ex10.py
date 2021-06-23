"""
    Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino
    ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!",
    conforme o caso.
"""
from unittest import TestCase, main


def verificar_turno(turno):
    turnos = {"M": "Bom dia", "V": "Boa Tarde", "N": "Boa noite"}

    for key in turnos:
        if key == turno.upper():
            return turnos[key]
    return "valor inválido"


class TesteExercicio10(TestCase):

    def test_caso_01(self):
        resultado = verificar_turno("m")
        self.assertEqual(resultado, "Bom dia")

    def test_caso_02(self):
        resultado = verificar_turno("V")
        self.assertEqual(resultado, "Boa Tarde")

    def test_caso_03(self):
        resultado = verificar_turno("N")
        self.assertEqual(resultado, "Boa noite")

    def test_caso_04(self):
        resultado = verificar_turno("x")
        self.assertEqual(resultado, "valor inválido")


if __name__ == "__main":
    main()
