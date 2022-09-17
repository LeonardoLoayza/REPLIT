import random
import time
import os
from colors import *
from data import *

def nueva_trivia():
    carga(3, True)
    borrarPantalla()
    bienvenida()
    respuestas = []
    numero_de_pregunta = 1
    puntaje = 0
    #intentos = 0

    for i in preguntas:  #imprimir las preguntas del diccionario
        print(i)
        for j in opciones[
                numero_de_pregunta -
                1]:  # imprimir las opciones de opciones en manera ordenada
            print(j)
        print()
        intento = input("Escribe la letra de la alternativa correcta: ").upper()
        respuestas.append(intento)
        revisar_respuesta(preguntas.get(i), intento)

        if preguntas.get(i) == intento:
            puntaje += random.randint(1, 15)
            print(CYAN + f"Tu puntaje es : {puntaje}" + OFF)
        elif numero_de_pregunta == 1 and intento == "X":
            puntaje += 20
            print(
                DARKBLACK +
                "Fallaste, pero encontraste la respuesta secreta asi que tienes +20 puntos"
                + OFF)
        else:
            puntaje -= random.randint(1, 15)
            print(CYAN + f"Tu puntaje es : {puntaje}" + OFF)
        print("--------------------------------------------")

        carga(0, False)
        numero_de_pregunta += 1


def bienvenida():
    print(MAGENTA +
          "HOLA!. Bienvenido a mi trivia, pondras a prueba tus conocimientos.")
    print("Espero que disfrutes de esta trivia tanto como yo al hacerla!!   ")
    print("***Atención*** ")
    print(
        "Escribe solo la letra de las alternativas presentadas, de otra manera se te restará puntos."
    )
    print("Al final del juego. Tendrás un regalo especial. ")
    print("--------------------------------------------" + OFF)


def carga(segundos, mostrar_numeros):
    for numero_carga in range(segundos, -1, -1):
        time.sleep(1)
        if mostrar_numeros == True:
            print(numero_carga)


def revisar_respuesta(respuesta, intento):
    if respuesta == intento:
        print(YELLOW + "Correcto!!" + OFF)
    else:
        print(RED + "Fallaste :(" + OFF)
    print("--------------------------------------------")
    carga(0, False)


def jugar_otra_vez():
    decision = input(DARKRED + "Quieres jugar de nuevo? (si o no):" + OFF).lower()
    return True if decision == "si" else False


def borrarPantalla():  # borrar la pantalla de la consola
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
