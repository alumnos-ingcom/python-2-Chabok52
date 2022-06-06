################
# Valen Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una función que obtenga los máximos, mínimos y promedio
de una secuencia con números, retornando los valores como una tuple.

Sin utilizar lazos for o las funciones integradas del lenguaje que
procesan secuencias.
"""


def lista_general():
    lista = []
    cantidad = int(input("Ingrese la cantidad de números de la lista "))
    contador = 0
    while cantidad > contador:
        numero = int(input("Ingrese un número para añadirlo a la lista "))
        lista.append(numero)
        contador += 1
    return lista


def maximo(lista):
    contador = len(lista)
    mayor = lista[0]
    otro_contador = 0
    while contador > 0:
        if lista[otro_contador] > mayor:
            mayor = lista[otro_contador]
        contador -= 1
        otro_contador += 1
    return mayor


def minimo(lista):
    contador = len(lista)
    menor = lista[0]
    otro_contador = 0
    while contador > 0:
        if lista[otro_contador] < menor:
            menor = lista[otro_contador]
        contador -= 1
        otro_contador += 1
    return menor


def promedio(lista):
    contador = len(lista)
    otro_contador = 0
    suma = 0
    division = 0
    while contador > 0:
        suma += lista[otro_contador]
        contador -= 1
        otro_contador += 1
    division = suma // len(lista)
    return division


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    lista = lista_general()
    mayor = maximo(lista)
    menor = minimo(lista)
    prom = promedio(lista)
    print(f"El máximo de su lista es: {mayor}")
    print(f"El mínimo de su lista es: {menor}")
    print(f"El promedio de su lista es: {prom}")


if __name__ == "__main__":
    principal()
