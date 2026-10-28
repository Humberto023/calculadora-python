import pytest

from calculadora import calcular, dividir, multiplicar, somar, subtrair


def test_somar():
    assert somar(2, 3) == 5


def test_subtrair():
    assert subtrair(10, 4) == 6


def test_multiplicar():
    assert multiplicar(3, 4) == 12


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(5, 0)


def test_calcular_com_operador():
    assert calcular(7, "+", 3) == 10
    assert calcular(7, "*", 3) == 21


def test_operador_invalido():
    with pytest.raises(ValueError):
        calcular(1, "%", 2)
