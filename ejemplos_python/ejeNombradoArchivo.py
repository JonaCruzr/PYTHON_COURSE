import time

# Obtener el número de milisegundos actuales desde 1970 y lo redondea
milisegundos = int(round(time.time() * 1000))

#Forma numero 1: 
# Generar el nombre de archivo único concatenando el número de milisegundos y la extensión de archivo
nombre_archivo = f"archivo_{milisegundos}.txt"
print(nombre_archivo)  # Salida: archivo_1618160172968.txt

#forma numero 2
#nombre_archivo = "archivo_{}.txt"
#print(nombre_archivo.format(milisegundos))