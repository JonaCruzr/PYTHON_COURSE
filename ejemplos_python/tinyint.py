import numpy

string_num = "10" # ejemplo de string que representa el número 10
tinyint_num = numpy.int8(int(string_num))

print(type(tinyint_num)) # salida: <class 'numpy.int8'>
print(tinyint_num) # salida: 10