import logica

def interfaz_tablero(tablero):
    """Creo la interfaz del tablero"""
    ancho = len(tablero[0])
    fifteen = ("="*ancho + "Fifteen" + "="*ancho)
    print(fifteen)
    for fila in tablero:
        linea = []
        for numeros in fila:
            linea.append(str(numeros).ljust(2))
        print("| " + "| ".join(linea) + "| ")
    separar = ("="*len(fifteen))
    print(separar)

def movimientos():
    """Creo la funcion de movimientos"""
    print("Controles: w , a, s, d")
    print("Salir del juego: o")
    while True:
        movimientos = input("Ingrese movimiento: ")
        movimientos = movimientos.lower()
        for mov in movimientos:
            if mov not in ["w", "a", "s", "d", "o"]:
                print("Movimiento invalido, ingrese una letra valida")
                break
            else:
                return movimientos

def filas_y_columnas():
    """Creo la funcion de filas y columnas"""
    while True:
        filas_columnas = input("Ingrese <filas> <columnas>: ").split()
        if len(filas_columnas) >= 2 and filas_columnas[0].isdigit() and filas_columnas[1].isdigit(): #Valido que se ingresen dos numeros
            filas = int(filas_columnas[0])
            columnas = int(filas_columnas[1])
            if 2 <= filas <= 15 and 2 <= columnas <= 15: #Para que el juego no sea muy grande, valido entre 2 y 15
                break
            else:
                print("Ingrese <filas> <columnas> enteros positivos entre 2 y 15.")
        else:
            print("Ingrese formato <filas> <columnas>")
    return filas, columnas

def main():
    """Creo la funcion principal""" #Llamo las funciones de logica y utilizo las funciones: Movimientos, filas_y_columnas e interfaz_tablero
    filas, columnas = filas_y_columnas()
    tablero = logica.crear_tablero(filas, columnas) #Creo el tablero
    tablero, Z = logica.mezclar_tablero(tablero) #Mezclo el tablero y defino Z
    interfaz_tablero(tablero)
    N = Z*5
    contador = 0
    restantes = N
    while not logica.tablero_ordenado(tablero):
        print(f"Movimientos realizados: {contador}")
        print(f"Movimientos restantes: {restantes}")
        movimientos_ingresados = movimientos()
        for movimiento in movimientos_ingresados:
            if movimiento == "o":
                print("Ababdonaste el juego")
                return
            if movimiento == "w":
                logica.mover_arriba(tablero, columnas)
                restantes -= len(movimiento)
            elif movimiento == "s":
                logica.mover_abajo(tablero, columnas)
                restantes -= len(movimiento)
            elif movimiento == "a":
                logica.mover_izquierda(tablero, filas)
                restantes -= len(movimiento)
            elif movimiento == "d":
                logica.mover_derecha(tablero, filas)
                restantes -= len(movimiento)
            contador += len(movimiento)
            if restantes <= 0:
                print("Perdiste, usaste muchos movimientos ):")
                return
        interfaz_tablero(tablero)
        if logica.tablero_ordenado(tablero):
            print("Ganaste (:")
main()