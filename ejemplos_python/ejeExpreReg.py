import re

# Define el patrón regexCoordenadas_lnlt (Es una expresión regular)
regexCoordenadas_lnlt = r"^(La)(\:)(\s*)([-+]?)([\d]{1,2})(\:)([\d]{1,2})(\:)([\d]{1,2})((\.)(\d+))(\|+)(Lo)(\:)(\s*)(([-+]?)([\d]{1,2})(\:)([\d]{1,3})(\:)([\d]{1,3})((\.)(\d+))?)$"

# Define la variable
longitude = "La: 12:34:56|Lo: -123:45:67.89"

# Buscar una coincidencia del patrón regexCoordenadas_lnlt en la variable longitud
match_longitude = re.search(regexCoordenadas_lnlt, longitude)

print(match_longitude)

# Check if a match was found
if match_longitude:
    print("Match found!")
else:
    print("No match found.")




'''
Este pedazo de código reemplaza los caracteres especificados en una cadena.
En este caso, el código crea una tabla de traducción que asigna las vocales acentuadas (á, é, í, ó, ú, ü, Á, É, Í, Ó, Ú, Ü)
a sus correspondientes vocales no acentuadas (a, e, i, o, u, u, A, E, I, O, U, U).

a, b = 'áéíóúüÁÉÍÓÚÜ', 'aeiouuAEIOUU'
translation_table = str.maketrans(a, b) #El método str.maketrans() de Python devuelve una tabla de traducción

string_with_accents = 'Hállo wórld!'
string_without_accents = string_with_accents.translate(translation_table)

print(string_without_accents)
'''