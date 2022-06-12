################
# Valen Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
El cifrado César o cifrado de rotación usa una encriptación de sustitución
simple. Esto significa que cada caracter se sustituye por otro caracter de
acuerdo con un sistema especifico.

La codificación debe ser tal que la palabra codificada contenga unicamente
caracteres del tipo AZaz y 0 a 9, de manera que al codificar las ultimas letras
del abecedario se vuelva a las primeras letras.

Por ejemplo, el método conocido y muy utilizado ROT13 rota el alfabeto con 13
posiciones, resultando en A->N, B->O... Y->L y Z->M.

Implementar una funcion que codifique un texto rotandolo una cantidad de
posiciones ajustable.

Implementar la funcion que decodifique el texto rotado una cantidad de
posiciones ajustable.

Una buena forma para verificar este ejercicio es codificar y decodificar
un texto y compararlo con lo que fué ingresado originalmente.

Tip: Implementar las funciones utilizando las funciones ord y chr.
"""


def cifrado_cesar(texto, rotaciones):
    """La función recibe un texto,
    con letra de la A a la Z, sean minúscualas
    o mayúsculas, junto con numeros, y los rota una cierta
    cantidad de veces, encriptando el texto"""
    letra_a_numero = 0
    numero = 0
    rotacion = ""
    for c in texto:
        letra_a_numero = ord(c)
        if letra_a_numero >= 48 and letra_a_numero <= 57:
            if rotaciones > 10:
                while rotaciones > 10:
                    rotaciones -= 10
            letra_a_numero += rotaciones
            if letra_a_numero > 57:
                diferencia = letra_a_numero - 57
                letra_a_numero = 48
                letra_a_numero += diferencia - 1
            rotacion += chr(letra_a_numero)
        elif letra_a_numero >= 97 and letra_a_numero <= 122:
            if rotaciones > 26:
                while rotaciones > 26:
                    rotaciones -= 26
            letra_a_numero += rotaciones
            if letra_a_numero > 122:
                diferencia = letra_a_numero - 122
                letra_a_numero = 97
                letra_a_numero += diferencia - 1
            rotacion += chr(letra_a_numero)
        elif letra_a_numero >= 65 and letra_a_numero <= 90:
            if rotaciones > 26:
                while rotaciones > 26:
                    rotaciones -= 26
            letra_a_numero += rotaciones
            if letra_a_numero > 90 and letra_a_numero <= 122:
                diferencia = letra_a_numero - 90
                letra_a_numero = 65
                letra_a_numero += diferencia - 1
            rotacion += chr(letra_a_numero)
    return rotacion


def descifrado_cesar(texto, rotaciones):
    """La función recibe un texto, encriptado o no
    y lo rota una cierta cantidad de veces, de modo que
    si el mismo está encriptado y se lo decodifica con la
    función, volverá a su posición original"""
    letra_a_numero = 0
    numero = 0
    rotacion = ""
    for c in texto:
        letra_a_numero = ord(c)
        if letra_a_numero >= 48 and letra_a_numero <= 57:
            if rotaciones > 10:
                while rotaciones > 10:
                    rotaciones -= 10
            letra_a_numero -= rotaciones
            if letra_a_numero < 48:
                diferencia = 48 - letra_a_numero
                letra_a_numero = 57
                letra_a_numero -= diferencia - 1
            rotacion += chr(letra_a_numero)
        elif letra_a_numero >= 97 and letra_a_numero <= 122:
            if rotaciones > 26:
                while rotaciones > 26:
                    rotaciones -= 26
            letra_a_numero -= rotaciones
            if letra_a_numero < 97:
                diferencia = 97 - letra_a_numero
                letra_a_numero = 122
                letra_a_numero -= diferencia - 1
            rotacion += chr(letra_a_numero)
        elif letra_a_numero >= 65 and letra_a_numero <= 90:
            if rotaciones > 26:
                while rotaciones > 26:
                    rotaciones -= 26
            letra_a_numero -= rotaciones
            if letra_a_numero < 65:
                diferencia = 65 - letra_a_numero
                letra_a_numero = 90
                letra_a_numero -= diferencia - 1
            rotacion += chr(letra_a_numero)
    return rotacion


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    texto = input("Ingrese el texto a codificar: ")
    rotaciones = int(input("Ingrese la cantidad de rotaciones: "))
    codificado = cifrado_cesar(texto, rotaciones)
    decodificado = descifrado_cesar(codificado, rotaciones)
    print(f"Su texto codificado es: {codificado}")
    print(f"Su texto decodificado es: {decodificado}")


if __name__ == "__main__":
    principal()
