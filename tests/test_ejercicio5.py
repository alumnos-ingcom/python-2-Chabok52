################
# Valen Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio5 import esta_balanceada

"""
Test comprobando ambos posibles retornos de la función
esta_balanceada.
"""


def test_esta_balanceada():
    """
    Test con un caso verdadero
    """
    cadena = "[Hola profe, may the force be with you]"
    resultado = esta_balanceada(cadena)
    assert isinstance (resultado, bool), "El resultado debe ser un booleano"
    assert resultado is True, "No se obtuvo el resultado esperado"


def test_no_esta_balanceada():
    """Test con un caso falso"""
    cadena = "[]]["
    resultado = esta_balanceada(cadena)
    assert isinstance (resultado, bool), "El resultado debe ser un booleano"
    assert resultado is False, "No se obtuvo el resultado esperado"