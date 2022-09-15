import random 
import time 
import colores 
import os

WHITE =    "\033[1;37m"
YELLOW =   "\033[1;33m"
GREEN=    "\033[1;32m"
BLUE=     "\033[1;34m"
CYAN=     "\033[1;36m"
RED=      "\033[1;31m"
MAGENTA=  "\033[1;35m"
BLACK=      "\033[1;30m"
DARKWHITE=  "\033[0;37m"
DARKYELLOW= "\033[0;33m"
DARKGREEN=  "\033[0;32m"
DARKBLUE=   "\033[0;34m"
DARKCYAN=   "\033[0;36m"
DARKRED=    "\033[0;31m"
DARKMAGENTA="\033[0;35m"
DARKBLACK=  "\033[0;30m"
OFF=       "\033[0;0m"

def nueva_trivia():

    carga(3, True)
    borrarPantalla()
    bienvenida()
    respuestas = []
    numero_de_pregunta = 1
    puntaje = 0
    #intentos = 0

    for i in preguntas: #imprimir las preguntas del diccionario
        print(i)
        for j in opciones[numero_de_pregunta-1]: # imprimir las opciones de opciones en manera ordenada
            print(j)
        print()
        intento = input("Escribe la letra de la alternativa correcta: ")
        intento = intento.upper()
        respuestas.append(intento)
        revisar_respuesta(preguntas.get(i), intento)

        if preguntas.get(i) == intento:
            puntaje += random.randint(1,15)
            print(CYAN + f"Tu puntaje es : {puntaje}" + OFF)
        elif numero_de_pregunta == 1 and intento == "X" :
            puntaje += 20
            print(DARKBLACK + "Fallaste, pero encontraste la respuesta secreta asi que tienes +20 puntos" + OFF) 
        else: 
            puntaje -= random.randint(1,15)
            print(CYAN +f"Tu puntaje es : {puntaje}" + OFF)
        print("--------------------------------------------")
        
        carga(0, False)
        numero_de_pregunta += 1
    
def bienvenida():
    print(MAGENTA + "HOLA!. Bienvenido a mi trivia, pondras a prueba tus conocimientos.")
    print("Espero que disfrutes de esta trivia tanto como yo al hacerla!!   ")
    print("***Atención*** ")
    print("Escribe solo la letra de las alternativas presentadas, de otra manera se te restará puntos.")
    print("Al final del juego. Tendrás un regalo especial. ")
    print("--------------------------------------------" + OFF)

def carga(segundos, mostrar_numeros): 
    for numero_carga in range (segundos, -1, -1):
        time.sleep(1)
        if mostrar_numeros == True:
            print(numero_carga)

def revisar_respuesta(respuesta, intento):
    if respuesta == intento:
        print (YELLOW+"Correcto!!" + OFF)
    else: 
        print(RED+ "Fallaste :(" + OFF)
    print("--------------------------------------------")
    carga(0, False)

def jugar_otra_vez():

    decision = str(input(DARKRED +"Quieres jugar de nuevo? (si o no):" + OFF))
    decision = decision.lower()
    if decision == "si" or decision == "Si":
        return True
    else: 
        return False

def borrarPantalla():  # borrar la pantalla de la consola
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

preguntas = {  # diccionario
 "Quien creó Python?: " : "A",
 "Creador de qué es Bjarne Stroustrup?: ": "C",
 "En que año Python fue creado?: ": "B",
 "John Romero y John Carmack son los fundadores de ID Sofware? ": "A"
}

opciones = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"], # lista de listas  
          ["A. Lua", "B. C", "C. C++", "D. C#"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Si","B. No", "C. No se"]]

nueva_trivia()

while jugar_otra_vez(): # volver a jugar
    nueva_trivia()

print("Hasta la proxima, espero que hayas disfrutado la trivia igual que yo al hacerla!")
