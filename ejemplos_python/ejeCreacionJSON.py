import json

record = {'body': '[1, 2, 3]'}

'''

Esta manera de crear un JSON no es correcta del todo, es mejor hacer lo del segundo ejemplo.

message_all = json.loads(json.dumps(record)) #Convierte "record" en diccionario Python.
message_body = json.loads(json.dumps('{\"array_body\":'+message_all['body']+'}'))
body_json = json.loads(message_body)
'''

#Segundo ejemplo: 
message_all = json.loads(json.dumps(record))

message_body = {'array_body': json.loads(message_all['body'])}

#print(type(message_body))
print(message_body)

json_string = json.dumps(message_body) #cadena JSON

print(json_string)
