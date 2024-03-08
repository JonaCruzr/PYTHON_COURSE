import json
event = {'Records': [{'messageId': 'f4f9db05-e9a5-4ec4-87af-c434a2b16742', 'receiptHandle': 'AQEBzOwm9lL867Nd9GWFh+l5xJ+mSZm1KW51J7hDYZ0F7rBWY2DX5KjEb1kATDGCZVlCDSUz+LY4MLmpzM1y2xx0EBfqGV0Q37XsKHJid7SHo6wR0CGm/0Io70l99VsgQG18xH6vPK4shlujmM0100xupNZ9S2iPEGoOGjeBnb/nZQrQWSbI1IxwBEWUnzdSPJ9Copb7OZWpgF3a8eVeU1KuzxWzbhY+8IirB8YyEEc2UDslqa4AQJP0YYbtsksGngKs7v2oHKZLSAjjOrcDAYi6FC3iDaBkkaUnlsJCZY06HxVX9SblQJ1UgeYiPy44FNOqml4OIi67pcWVaeCWgjh/G0cNQswYJPWBeQpUm9aigqzgKyj9b0wPMfCJI94i5FNlZ1cMVT2HdSSGO6R0H+I5C/JLI8nAKkPdnARdsuWD28c=', 'body': '["software.amazon.payloadoffloading.PayloadS3Pointer",{"s3BucketName":"prep-edomex-dev-json-actas-sqs-521a","s3Key":"002bc6ad-cb21-4664-ab05-d9cc56dcc7ed"}]', 'attributes': {'ApproximateReceiveCount': '1', 'SentTimestamp': '1681757235364', 'SenderId': 'AIDA26BABLJOOGXK7R3OL', 'ApproximateFirstReceiveTimestamp': '1681757235369'}, 'messageAttributes': {'SQSLargePayloadSize': {'stringValue': '615043', 'binaryValue': None, 'stringListValues': [], 'binaryListValues': [], 'dataType': 'Number'}}, 'md5OfMessageAttributes': 'feb4c4d4d7de360c79a26ab047375f6e', 'md5OfBody': 'dfc9eb53aa29c58b354b741c2d1bb644', 'eventSource': 'aws:sqs', 'eventSourceARN': 'arn:aws:sqs:us-east-1:751686474332:prep-edomex-dev-queue-prep-casilla-521a', 'awsRegion': 'us-east-1'}]}
#print(type(event)) #Esto sale en pantalla al imprimir: <class 'dict'>

res = event["Records"]
#print(res)

if res is not None:
    for message in res:
        print()
        print(message) #imprime: <class 'dict'>

           
message_all = json.loads(json.dumps(message))
#print(type(message_all)) #imprime: <class 'dict'>

'''
a json.dumps() se le pasa unacadena de caracteres que parece ser un objeto JSON, 
pero en realidad es solo una cadena de caracteres que contiene texto en "formato" JSON.

Por lo tanto, la función json.dumps() devuelve una cadena de caracteres Python.
el resultado final de la siguiente línea de código es una cadena de caracteres Python.
'''
message_body = json.loads(json.dumps('{\"array_body\":'+message_all['body']+'}')) #únicamente almacena el "body" de lo obtenido en event["Records"]
#print(type(message_body)) #imprime: <class 'str'>   

body_json = json.loads(message_body) #Es un diccionario
#print(body_json['array_body'])

if 's3BucketName' in body_json['array_body'][1] and 's3Key'  in body_json['array_body'][1]:
    s3_bucket_name = body_json['array_body'][1]['s3BucketName'] 
    s3_key = body_json['array_body'][1]['s3Key']
else:
	s3_bucket_name = BUCKET_QUEUE
	s3_key = "01ff7b92-8e9f-4aea-9287-d1dba9703eee"
		