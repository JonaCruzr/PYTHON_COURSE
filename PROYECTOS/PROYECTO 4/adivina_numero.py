import time
import random

nombre = input("Cuál es tu nombre? ")
print(f"Bueno {nombre}, he pensado un número entre 1 y 100\nTienes 8 intentos para adivinar\n")
time.sleep(2)

intentos = 0
numero_adivinar = random.randint(1, 101)
print(numero_adivinar)
numero = 0

while intentos < 8:
    numero = int(input("ingresa el numero que crees que es: "))
    intentos += 1

    if numero > 100 or numero < 0:
        print("Solo puedes ingresar numeros entre 1 y 100 \n")
    elif numero < numero_adivinar:
        print("respuesta incorrecta haz elegido un número menor al número secreto.\n")
    elif numero > numero_adivinar:
        print("respuesta incorrecta haz elegido un número mayor al número secreto.\n")
    else:
        print(f"Felicitaciones {nombre}! Has adivinado en {intentos} intentos\n")
        break

if numero != numero_adivinar:
    print(f"Lo siento, se han agotado los intentos. El numero secreto era {numero_adivinar}")