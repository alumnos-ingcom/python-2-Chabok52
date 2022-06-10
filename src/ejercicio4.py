################
# Valen Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
La sucesión de Fibonacci es una sucesión infinita donde cada elemento
es la suma de los dos anteriores. En la misma, los dos primeros términos
son 1. (En algunos lugares se toma el primer término en 0 y el segundo en
1) Implementar una función que permita obtener el n-esimo termino de la
sucesión de Fibonacci. Siendo este número un entero positivo mayor a 2.
"""


def sucesion_fibonacci(numero):
    """La función recibe un número entero
    mayor a dos y retorna el termino de la
    sucesion fibonacci igual a ese número"""
    assert numero > 2, "El número debe ser mayor a 2"
    contador = 1
    otro_contador = 1
    total = 0
    clon_numero = numero
    while numero - 2 > 0:
        total = contador + otro_contador
        otro_contador = contador
        contador = total
        numero -= 1
    return total


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese un número mayor a dos "))
    resultado = sucesion_fibonacci(numero)
    print(f"Su número equivale a {resultado} en la sucesion fibonacci")


if __name__ == "__main__":
    principal()
