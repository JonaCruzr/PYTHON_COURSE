import base64
from requests_toolbelt.__init__ import MultipartDecoder

coded_string = '''TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlz
IHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2Yg
dGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGlu
dWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRo
ZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4='''

datos = base64.b64decode(coded_string).decode('utf-8')

print(datos)

with open("h.txt", "rb") as f:
            img_base64 = base64.b64encode(f.read())
print(img_base64) #Imprime una cadena binaria en base64

valor = img_base64.decode('utf-8') 

print(valor) #Imprime la cadena en base64 (le quita el prefijo b'')

'''
archivo = open("h.txt", "rb")
print(base64.b64encode(archivo.read()))
'''