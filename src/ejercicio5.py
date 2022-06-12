################
# Valen Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una función que determine si una cadena con
corchetes está balanceada.

Es decir, si cada corchete que abre, tiene su par que cierra.
El resultado debe ser un valor lógico indicando si esta o no balanceado.
La funcion deberia de ignorar todo lo que no sean corchetes.
"""


def esta_balanceada(cadena):
    """La función recibe una cadena y
    retorna si la misma está balanceada o no
    mediante True o False"""
    lista = []
    for c in cadena:
        if c == "[":
            lista.append(c)
        elif c == "]":
            if len(lista) == 0:
                return False
            else:
                lista_top = lista.pop()
                if lista_top != "[":
                    return False
    return not len(lista)


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cadena = input("Ingrese una cadena ")
    resultado = esta_balanceada(cadena)
    if resultado is True:
        print(f"{cadena} está balanceada, ya que todos sus corchetes cierran")
    else:
        print(f"{cadena} no está balanceada")


if __name__ == "__main__":
    principal()
