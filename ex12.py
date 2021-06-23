"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto
de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS
corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido
corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua
hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas
    conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

    Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""

from unittest import TestCase, main, expectedFailure


def calcular_folha_de_pagamento(salario_bruto: float, desconto_imposto_de_renda: float) -> tuple:
    descontos_outros = {"sindicato": 0.03, "fgts": 0.11, "inss": 0.1}

    desconto_sindicato = salario_bruto * descontos_outros["sindicato"]
    desconto_inss = salario_bruto * descontos_outros["inss"]

    if salario_bruto <= 0:
        raise ValueError("Insira corretamente os valores, acima de 0")
    else:

        salario_liquido = salario_bruto - (desconto_inss + desconto_imposto_de_renda)
        fgts = salario_bruto * descontos_outros["fgts"]

        return salario_bruto, desconto_imposto_de_renda, desconto_inss, fgts, (desconto_imposto_de_renda + desconto_inss), salario_liquido


def calcular_desconto_imposto_de_renda(salario_bruto: float) -> float:
    descontos_ir = {"5": 0.05, "10": 0.1, "20": 0.2}

    if salario_bruto <= 0:
        raise ValueError("Insira corretamente os valores, acima de 0")
    else:
        if salario_bruto < 900:
            desconto = 0
        elif salario_bruto < 1501:
            desconto = salario_bruto * descontos_ir["5"]
        elif salario_bruto < 2501:
            desconto = salario_bruto * descontos_ir["10"]
        else:
            desconto = salario_bruto * descontos_ir["20"]

        return desconto


class TestExercicio12(TestCase):

    def test_caso_01(self):
        salario_bruto = 5 * 220
        desconto_ir = calcular_desconto_imposto_de_renda(salario_bruto)
        self.assertEqual(desconto_ir, 55.0)
        salario = calcular_folha_de_pagamento(salario_bruto, desconto_ir)
        self.assertEqual(salario, (1100, 55, 110, 121, 165, 935))

    @expectedFailure
    def test_caso_erro_01(self):
        resultado1 = calcular_desconto_imposto_de_renda(0)
        self.assertRaises(ValueError, resultado1)

    @expectedFailure
    def test_caso_erro_02(self):
        resultado2 = calcular_folha_de_pagamento(0)
        self.assertRaises(ValueError, resultado2)


if __name__ == "__main__":
    main()
