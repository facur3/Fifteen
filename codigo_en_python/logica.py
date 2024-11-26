"""Parte logica de Fifteen"""

import random

def crear_tablero(filas, columnas):
    """"Creo un tablero NxM con un espacio en alguna posicion del tablero"""
    tablero = []
    numeros = 1
    for fila in range(filas):
        fila = []
        for columna in range(columnas):
            fila.append(numeros)
            numeros += 1
        tablero.append(fila)
    tablero[-1][-1] = " " #Reemplazo el ultimo numero del tablero con un espacio vacio
    return tablero

def encontrar_espacio(tablero):
    """Encuentro el espacio vacio en el tablero"""
    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            if tablero[fila][columna] == " ": #Si el espacio esta vacio hago un return de la fila y columna
                return fila, columna

def mover_derecha(tablero, fila):
    """Muevo el espacio vacio hacia la derecha"""
    espacio_fila, espacio_columna = encontrar_espacio(tablero) #Separo la fila y columna del espacio vacio
    if espacio_columna < len(tablero[0]) - 1:  #Me fijo si hay espacio a la derecha
        tablero[espacio_fila][espacio_columna], tablero[espacio_fila][espacio_columna + 1] = tablero[espacio_fila][espacio_columna + 1], tablero[espacio_fila][espacio_columna]
    else:  # Si no hay espacio a la derecha, muevo el espacio vacío a la primera columna
        tablero[espacio_fila][espacio_columna], tablero[espacio_fila][0] = tablero[espacio_fila][0], tablero[espacio_fila][espacio_columna]

def mover_izquierda(tablero, fila):
    """Muevo el espacio vacio hacia la izquierda"""
    espacio_fila, espacio_columna = encontrar_espacio(tablero) #Separo la fila y columna del espacio vacio
    if espacio_columna > 0:  #Me fijo si hay espacio a la izquierda
        tablero[espacio_fila][espacio_columna], tablero[espacio_fila][espacio_columna - 1] = tablero[espacio_fila][espacio_columna - 1], tablero[espacio_fila][espacio_columna]
    else:  # Si no hay espacio a la izquierda, muevo el espacio vacío a la última columna
        tablero[espacio_fila][espacio_columna], tablero[espacio_fila][-1] = tablero[espacio_fila][-1], tablero[espacio_fila][espacio_columna]

def mover_arriba(tablero, columna):
    """Muevo el espacio vacio hacia arriba"""
    espacio_fila, espacio_columna = encontrar_espacio(tablero) #Separo la fila y columna del espacio vacio
    if espacio_fila > 0:  #Me fijo si hay espacio arriba
        tablero[espacio_fila][espacio_columna], tablero[espacio_fila - 1][espacio_columna] = tablero[espacio_fila - 1][espacio_columna], tablero[espacio_fila][espacio_columna]
    else:  # Si no hay espacio arriba, muevo el espacio vacío a la última fila
        tablero[espacio_fila][espacio_columna], tablero[-1][espacio_columna] = tablero[-1][espacio_columna], tablero[espacio_fila][espacio_columna]

def mover_abajo(tablero, columna):
    """Muevo el espacio vacio hacia abajo"""
    espacio_fila, espacio_columna = encontrar_espacio(tablero) #Separo la fila y columna del espacio vacio
    if espacio_fila < len(tablero) - 1:  #Me fijo si hay espacio abajo
        tablero[espacio_fila][espacio_columna], tablero[espacio_fila + 1][espacio_columna] = tablero[espacio_fila + 1][espacio_columna], tablero[espacio_fila][espacio_columna]
    else:  # Si no hay espacio abajo, muevo el espacio vacío a la primera fila
        tablero[espacio_fila][espacio_columna], tablero[0][espacio_columna] = tablero[0][espacio_columna], tablero[espacio_fila][espacio_columna]

def mezclar_tablero(tablero):
    movimientos = [mover_derecha, mover_izquierda, mover_arriba, mover_abajo]
    Z = random.randint(5, 10)
    for mezcla in range(Z):
        movimiento_random = random.choice(movimientos)
        movimiento_random (tablero, 0)
    return tablero, Z

def tablero_ordenado(tablero):
    """Corroboro si el tablero esta ordenado para terminar el juego"""
    if tablero[-1][-1] != " ": #Si el ultimo numero no es un espacio vacio hago un return de False
        return False
    numeros = 1
    for fila in tablero:
        for numero in fila:
            if numeros == len(tablero)*len(tablero[0]):
                break
            if numero != numeros:
                return False
            numeros += 1
    return True