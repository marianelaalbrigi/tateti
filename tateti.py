# %%
import numpy as np
from typing import List

# %%
# VALIDACION DE DATOS - SOLICITUD DE REINGRESO DE DATOS
def funcion_input_reentry(input_user:int, matriz_juego:List[int], name_user:str) -> int:
    """Verifica si la posicion elegida por el usuario ya fue
        marcada o si el dato ingresado dentro del rango de 
        las posiciones.

    Args:
        input_user (int): posición que quiere marcar el usuario
        matriz_juego (List[int]): posiciones enumeradas del tablero
        name_user (str): nombre del usuario

    Returns:
        int: posicion validada y verificada
    """

    input_reentry=input_user
    while input_reentry not in matriz_juego:
        if 0 < input_reentry < 10:
            input_reentry=int(input(f"Este lugar ya fue marcado. {name_user} introducí un número nuevamente:"))
        elif input_reentry > 9:
            input_reentry=int(input(f"El número ingresado es inválido. {name_user} introducí un número nuevamente:"))
    return input_reentry

# FUNCIONES PARA VALIDAR SI HAY JUGADA GANADORA (VERTICAL-HORIZONTAL-DIAGONAL)
def funcion_matriz_traspuesta(matriz_user:List[list[int]]) -> List[list[int]]:
    """Se genera una matriz traspuesta de la original.

    Args:
        matriz_user (List[list[int]]): matriz-tablero para el usuario

    Returns:
        List[list[int]]: matriz traspuesta de la original. Tablero con otro orden de numeros.
    """

    traspuesta=np.transpose(matriz_user)
    return matriz_user

def funcion_jugadas_verticales(matriz_user:List[list[int]], marca_user:str) -> bool:
    """Verifica si en cada columna de la matriz existen tres marcas iguales.

    Args:
        matriz_user (List[list[int]]): matriz-tablero para el usuario
        marca_user (str): la marca distintiva de cada usuario (X / O)

    Returns:
        bool: Verdadero si hay tres marcas iguales, Falso si no las hay
    """

    if all (lugar == marca_user for lugar in matriz_user [0]):
        hay_ganador=True
    elif all (lugar == marca_user for lugar in matriz_user [1]):
        hay_ganador=True
    elif all (lugar == marca_user for lugar in matriz_user [2]):
        hay_ganador=True
    else:
        hay_ganador=False
    return hay_ganador
    
def funcion_jugadas_horizontales(matriz_user:List[list[int]], marca_user:str) -> bool:
    """ Se genera una matriz traspuesta de la original y se verifica si en cada fila 
        de la matriz existen tres marcas iguales. 

    Args:
        matriz_user (List[list[int]]): matriz-tablero para el usuario
        marca_user (str): la marca distintiva de cada usuario (X / O)

    Returns:
        bool: Verdadero si hay tres marcas iguales, Falso si no las hay
    """

    traspuesta=np.transpose(matriz_user)
    hay_ganador=funcion_jugadas_verticales(traspuesta, marca_user)
    return hay_ganador
  
def funcion_jugadas_diagonales(matriz_user:List[list[int]], marca_user:str) -> bool:
    """Se verifica si en cada diagonal de la matriz existen tres marcas iguales. 

    Args:
        matriz_user (_type_): matriz-tablero para el usuario
        marca_user (str): la marca distintiva de cada usuario (X / O)

    Returns:
        bool: Verdadero si hay tres marcas iguales, Falso si no las hay
    """

    if matriz_user[0][0] == marca_user and matriz_user[1][1] == marca_user and matriz_user[2][2] == marca_user:
        hay_ganador=True
    elif matriz_user[0][2] == marca_user and matriz_user[1][1] == marca_user and matriz_user[2][0] == marca_user:
        hay_ganador=True
    else:
       hay_ganador=False
    return hay_ganador

def funcion_general_jugadas(matriz_user:List[list[int]], marca_user:str) -> bool:
    """ Se verifica si hay alguna jugada ganadora, ya sea horizontal, vertical o 
        diagonal. Si existe, el juego finaliza. 

    Args:
        matriz_user (List[list[int]]): matriz-tablero para el usuario
        marca_user (str): la marca distintiva de cada usuario (X / O)

    Returns:
        bool: Verdadero si hay jugada ganadora o Falso si no la ha
    """

    if funcion_jugadas_verticales(matriz_user, marca_user) or funcion_jugadas_horizontales(matriz_user, marca_user) or funcion_jugadas_diagonales(matriz_user, marca_user):
        juego_finalizado=True
    else: 
        juego_finalizado=False
    return juego_finalizado

# %%
# FUNCION PARA MARCAR JUGADAS EN EL TRABLERO PARA EL USUARIO
def funcion_marcador_user(marca_user:str, input:int, matriz_user:List[list[int]]) -> List[list[int]]:
    """Asienta una marca de acuerdo a la posición elegida por el usuario.

    Args:
        marca_user (str): la marca distintiva de cada usuario (X / O)
        input (int): la posicion elegida por el usuario
        matriz_user (List[list[int]]): la matriz/tablero del usuario

    Returns:
        List[list[int]]: una matriz con la nueva marca.
    """

    match input:
        case 1: 
            matriz_user [0][0] = marca_user
        case 2:
            matriz_user [0][1] = marca_user 
        case 3:
            matriz_user [0][2] = marca_user
        case 4:
            matriz_user [1][0] = marca_user
        case 5:
            matriz_user [1][1] = marca_user
        case 6:
            matriz_user [1][2] = marca_user
        case 7:
            matriz_user [2][0] = marca_user
        case 8:
            matriz_user [2][1] = marca_user
        case 9:
            matriz_user [2][2] = marca_user
    return matriz_user

# FUNCION PARA MARCAR JUGADAS EN EL TABLERO INTERNO DEL JUEGO
def funcion_marcador_intern (input:int, matriz_juego:list[int]) -> list[int]:
    """La posición/número elegido por el usuario, es reemplazado por un cero.
        De esta manera, se registra que la posición con ese número ya fue marcada.

    Args:
        input (int): posicion enumerada elegida por el usuario a marcar
        matriz_juego (list[int]): matriz/tablero del usuario

    Returns:
        list[int]: una nueva lista con el número o posición reemplazado por cero.
    """

    match input:
        case 1: 
            matriz_juego [0] = 0
        case 2:
            matriz_juego [1] = 0
        case 3:
            matriz_juego [2] = 0
        case 4:
            matriz_juego [3] = 0
        case 5:
            matriz_juego [4] = 0
        case 6:
            matriz_juego [5] = 0
        case 7:
            matriz_juego [6] = 0
        case 8:
            matriz_juego [7] = 0
        case 9:
            matriz_juego [8] = 0
    return matriz_juego

# %%
# Define colores ANSI
ROJO = "\033[91m"
AZUL = "\033[94m"
RESET = "\033[0m"

# FUNCION PARA IMPRIMIR EL TABLERO PARA LOS JUGADORES
def funcion_impresion_matriz_colores(matriz_user:List[List[int]]) -> None:
    """Imprime tablero para el usuario

    Args:
        matriz_user (List[List[int]]): matriz de numeros
    """

    print("+---+---+---+")
    for fila in matriz_user:
        fila_formateada = "|"
        for c in fila:
            if c == 'X':
                celda = f"{ROJO}{str(c):^3}{RESET}"
            elif c == 'O':
                celda = f"{AZUL}{str(c):^3}{RESET}"
            else:
                celda = f"{str(c):^3}"
            fila_formateada += celda + "|"
        print(fila_formateada)
        print("+---+---+---+")

# %%
# BIENVENIDA Y SOLICITUD DE NOMBRES DE USUARIO
name_user_1=input("Nombre usuario 1:\n").capitalize()
name_user_2=input("Nombre usuario 2:\n").capitalize()

print(f"Bienvenidos {name_user_1} y {name_user_2} al juego el TA-TE-TI!\n")
print(f"{name_user_1} tu serás X")
print(f"{name_user_2} tu serás O")

# SE IMPRIME EL TABLERO 
print(f"A continuación verán el tablero del juego. En sus respectivos turnos, deberán ingresar el número correspondiente al lugar que deseen marcar.\n")

matriz_user=[[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

funcion_impresion_matriz_colores(matriz_user)

print(f"¿Preparados para comenzar?")


# %%
juego_finalizado=False
matriz_juego=[1, 2, 3, 4, 5, 6, 7, 8, 9]

marca_user_1="X"
marca_user_2="O"
input_user1=""
input_user2=""
contardor_rondas=1

while not juego_finalizado:
    
    # TURNO USER 1
    input_user1=int(input(f"{name_user_1}, es tu turno. ¿Qué lugar deseas marcar? "))

    input_user1=funcion_input_reentry(input_user1, matriz_juego, name_user_1)           # Validar si el lugar ya esta ocupado o si el input esta dentro del rango
 
    matriz_juego=funcion_marcador_intern(input_user1, matriz_juego)                          # Marcar en el tablero interno la eleccion
    matriz_user=funcion_marcador_user(marca_user_1, input_user1, matriz_user)                # Marcar en el tablero del usuario la eleccion

    funcion_impresion_matriz_colores(matriz_user)
    print()  # Para dejar línea en blanco después del tablero                                             # Imprimir tablero para el usuario

    juego_finalizado=funcion_general_jugadas(matriz_user, marca_user_1)                     # Validar si la jugada es una jugada ganadora
    if juego_finalizado:
        print(f"El juego ha finalizado! {name_user_1} ha ganado!!!")
        break

    if contardor_rondas == 5:                                                                # Si no jugadas ganadoras anteriores y es la ronda N°5, entonces hay empate
        juego_finalizado=True
        print("Han empatado el juego! Les gustaría empezar un nuevo juego?")
        break  
    
    # TURNO USER 2
    input_user2=int(input(f"{name_user_2}, es tu turno. ¿Qué lugar deseas marcar? "))

    input_user2=funcion_input_reentry(input_user2, matriz_juego, name_user_2)           # Validar si el lugar ya esta ocupado o si el input esta dentro del rango

    matriz_juego=funcion_marcador_intern(input_user2, matriz_juego)                          # Marcar en el tablero interno la eleccion
    matriz_user=funcion_marcador_user(marca_user_2, input_user2, matriz_user)                # Marcar en el tablero del usuario la eleccion
    
    funcion_impresion_matriz_colores(matriz_user)
    print()  # Para dejar línea en blanco después del tablero                                              # Imprimir tablero para el usuario 

    juego_finalizado=funcion_general_jugadas(matriz_user, marca_user_2)                      # Validar si la jugada es una jugada ganadora
    if juego_finalizado:
        print(f"El juego ha finalizado! {name_user_2} ha ganado!!!")
        break
    
    contardor_rondas+=1                                                                      # contador de rondas