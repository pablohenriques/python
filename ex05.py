"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média
alcançada por aluno e apresentar:
    -   A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    -   A mensagem "Reprovado", se a média for menor do que sete;
    -   A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""


def calcular_nota(nota1, nota2):
    media = (nota1 + nota2) / 2

    if 0 < media < 11:
        if media == 10:
            resultado = "aprovado com distinção"
        elif media >= 7:
            resultado = "aprovado"
        else:
            resultado = "reprovado"
        return resultado
    else:
        raise ValueError("digite valores entre 0 e 10")



import unittest
class TestExercicio05(unittest.TestCase):

    def testAlunoAprovadoComDistinção(self):
        media = calcular_nota(10, 10)
        mensagem = "aprovado com distinção"
        self.assertEqual(media, mensagem)

    def testAlunoAprovado(self):
        media = calcular_nota(8, 7)
        mensagem = "aprovado"
        self.assertEqual(media, mensagem)

    def testAlunoReprovado(self):
        media = calcular_nota(4, 4)
        mensagem = "reprovado"
        self.assertEqual(media, mensagem)

    @unittest.expectedFailure
    def testErroDeValores(self):
        raise ValueError


if __name__ == "__main":
    unittest.main()
