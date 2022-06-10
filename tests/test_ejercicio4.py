################
# Valen Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio4 import sucesion_fibonacci

"""
Test comprobando si la posición indicada en la función
retorna el valor esperado en la sucesión fibonacci, teniendo
en cuenta que los dos primeros terminos son 1
"""


def test_sucesion_fibonacci():
    """
    Test comprobando si retorna el número esperado
    """
    numero = 5
    resultado = sucesion_fibonacci(numero)
    assert isinstance (resultado, int), "El resultado debe ser un entero"
    assert resultado == 5
