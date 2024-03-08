import random

aleatorio = random.randint(1, 5)
print("aleatorio entero: ", aleatorio)

aleatorio_f = round(random.uniform(1,100), 2) #round limita el numero a 2 decimales
print("aleatorio flotante:", aleatorio_f)

print(random.random())