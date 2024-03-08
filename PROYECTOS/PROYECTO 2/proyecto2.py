nombre = input("Cuál es tu nombre? ")
ventas_mes = input("Cuáles fueron tus ventas de este mes? ")

def comisiones(ventas_mes):
    comisiones = float(ventas_mes) * 0.13
    return comisiones

print(f"{nombre} tus comisiones de este mes son ${comisiones(ventas_mes)}")

