################
# Valen Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio2 import maximo, minimo, promedio

"""
Test comprobando el retorno de las funciones
maximo, minimo, promedio y lista general
"""


def test_maximo():
    """
    Test de la función maximo
    """
    lista = [52, -52, 5, 2, -5, -2]
    resultado = maximo(lista)
    assert isinstance(resultado, int), "El resultado debe ser un número entero"
    assert resultado == 52


def test_minimo():
    """Test de la función minimo"""
    lista = [52, -52, 5, 2, -5, -2]
    resultado = minimo(lista)
    assert isinstance(resultado, int), "El resultado debe ser un número entero"
    assert resultado == -52


def test_promedio():
    """Test con la función promedio"""
    lista = [5, 2, 25, 52]
    resultado = promedio(lista)
    assert isinstance(resultado, int), "El resultado debe ser un número entero"
    assert resultado == 21
