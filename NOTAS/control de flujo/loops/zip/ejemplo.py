'''Funcionamiento del método zip()

zip solo llega hasta el largo de la lista mas corta, es decir, si tenemos una lista de tamaño 3 y 
una de tamaño 4, zip solo llega hasta el tamaño de la lista de 3

zip pued combinar 2 o más listas
'''

nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 29, 42, 20]

#combinados = zip(bombre, edades)
combinados = list(zip(nombres, edades)) #Si no se pone en una lista solo imprime la direccion de memoria

print(combinados)