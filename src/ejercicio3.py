################
# Valentin Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Desarrollar una función que indique el grado de
superposición entre dos listas. Siendo 0 sin superposición
y uno para cada elemento superpuesto.
"""


def hacedor_de_listas():
    lista = []
    numero = int(input("Ingrese cuantos elementos contendrá la lista "))
    while numero > 0:
        elemento = input("Ingrese un elemento a la lista ")
        lista.append(elemento)
        numero -= 1
    return lista


def superposicion(lista, otra_lista):
    """La función recibe dos listas y las compara
    en busca de superposiciones, si las encuentra
    enumera cuantos elementos se superponen"""
    contador = len(lista)
    otro_contador = len(otra_lista)
    cero = 0
    cero_dos = 0
    super_puestos = 0
    if contador > otro_contador:
        while otro_contador > 0:
            if lista[cero] == otra_lista[cero_dos]:
                super_puestos += 1
            cero += 1
            cero_dos += 1
            otro_contador -= 1
    else:
        while contador > 0:
            if lista[cero] == otra_lista[cero_dos]:
                super_puestos += 1
            cero += 1
            cero_dos += 1
            contador -= 1
    return super_puestos


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    lista = hacedor_de_listas()
    otra_lista = hacedor_de_listas()
    resultado = superposicion(lista, otra_lista)
    if resultado == 0:
        print(f"Las listas no tienen elementos superpuestos")
    else:
        print(f"Las listas tienen {resultado} elementos superpuestos")


if __name__ == "__main__":
    principal()
