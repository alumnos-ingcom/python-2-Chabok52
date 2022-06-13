################
# Valen Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio3 import superposicion

"""
Test comprobando el funcionamiento de la función
superposicion con dos casos de prueba, uno con elementos
superpuestos y otro con ningún elemento superpuesto
"""


def test_superposicion():
    """
    Test con dos listas con elementos superpuestos
    """
    lista = ['Hey', 'Martin', 'aprobame', 'plis']
    otra_lista = ['Hey', 'Martin', 'aprobame', 'copate']
    resultado = superposicion(lista, otra_lista)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == 3, "No se obtuvo el resultado esperado"


def test_superposicion_cero():
    """Test con dos listas sin elementos superpuestos"""
    lista = ['You', 'were', 'my', 'brother', 'Anakin!']
    otra_lista = ['I', 'HATE', 'YOU!!!']
    resultado = superposicion(lista, otra_lista)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == 0, "No se obtuvo el resultado esperado"
