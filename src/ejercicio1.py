################
# Valen Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que retorne True cuando un
número entero es par y False cuando no lo sea, sin utilizar módulo. (%)
"""
# Precondición: Los números ingresados deben ser positivos


def es_par(numero):
    """La función recibe un número y
    mediante restas devuelve True cuando
    el número es par y False cuando no lo es"""
    valor = False
    while numero > 0:
        numero -= 2
    if numero == 0:
        valor = True
    return valor

# Postcondición: La función solo debe retornar True cuando el numero es par.


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese un número "))
    resultado = es_par(numero)
    if resultado is True:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")


if __name__ == "__main__":
    principal()
