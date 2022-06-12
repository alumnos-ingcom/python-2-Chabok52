################
# Valen Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio6 import cifrado_cesar, descifrado_cesar

"""
Test comprobando la función que realiza el cifrado
cesar rotando las letras una determinada cantidad de veces,
y la función que realiza el descifrado de ese texto
"""


def test_cifrado_cesar():
    """Test comprobando el cifrado cesar"""
    texto = "Hello123"
    rotaciones = 5
    resultado = cifrado_cesar(texto, rotaciones)
    assert isinstance (resultado, str), "El resultado debe ser un string"
    assert resultado == "Mjqqt678", "No se obtuvo el resultado esperado"


def test_descifrado_cesar():
    """Test comprobando el descifrado cesar"""
    texto = "Mjqqt678"
    rotaciones = 5
    resultado = descifrado_cesar(texto, rotaciones)
    assert isinstance (resultado, str), "El resultado debe ser un string"
    assert resultado == "Hello123", "No se obtuvo el resultado esperado"
