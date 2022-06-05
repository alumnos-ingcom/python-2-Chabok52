################
# Valen Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio1 import es_par

"""
Test con numeros pares e impares para
corroborar lo que retorna la función
"""


def test_es_par():
    """
    Test con un 52, debería retornar True
    """
    numero = 52
    resultado = es_par(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un booleano"
    assert resultado is True, "El resultado debe ser True"


def test_es_par_no():
    """Test con 5, debería retornar False"""
    numero = 5
    resultado = es_par(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un booleano"
    assert resultado is False, "El resultado debe ser False"
