"""
    As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram
    para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o
    reajuste segundo o seguinte critério, baseado no salário atual:
        salários até R$ 280,00 (incluindo) : aumento de 20%
        salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
        salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
        salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento.
"""

from unittest import TestCase, main, expectedFailure


def calcular_salario(salario: float) -> tuple:
    porcentagem_reajuste = {"20": 0.2, "15": 0.15, "10": 0.1, "5": 0.05}

    if salario <= 0:
        raise ValueError("Digite novamente valores acima de 0 para salário")

    else:
        if salario < 281:
            reajuste = porcentagem_reajuste["20"]
        elif salario < 701:
            reajuste = porcentagem_reajuste["15"]
        elif salario < 1501:
            reajuste = porcentagem_reajuste["10"]
        else:
            reajuste = porcentagem_reajuste["5"]

        valor_do_aumento = salario * reajuste
        novo_salario = salario + valor_do_aumento

        return salario, reajuste, valor_do_aumento, novo_salario


class TestExercicio11(TestCase):

    def test_caso_reajuste_20_porcento(self):
        resultado = calcular_salario(200)
        self.assertEqual(resultado, (200, 0.2, 40, 240))

    def test_caso_reajuste_15_porcento(self):
        resultado = calcular_salario(500)
        self.assertEqual(resultado, (500, 0.15, 75, 575))

    def test_caso_reajuste_10_porcento(self):
        resultado = calcular_salario(1500)
        self.assertEqual(resultado, (1500, 0.1, 150, 1650))

    def test_caso_reajuste_5_porcento(self):
        resultado = calcular_salario(10000)
        self.assertEqual(resultado, (10000, 0.05, 500, 10500))

    @expectedFailure
    def test_caso_erro_de_valor(self):
        resultado = calcular_salario(-1)
        self.assertRaises(ValueError, resultado)


if __name__ == "__main":
    main()
