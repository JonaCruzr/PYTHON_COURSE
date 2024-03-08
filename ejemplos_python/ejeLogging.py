'''
El nivel por defecto es WARNING, lo que significa que sólo los eventos de este nivel y 
superiores serán rastreados, a menos que el paquete de registro esté configurado para 
hacer lo contrario.

Los niveles estándar son los siguientes:
    - DEBUG
    - INFO
    - WARNING # Si no se especifica, WARNING es el nivel por defecto del Logger.
    - ERROR
    - CRITICAL
'''
import logging
logger = logging.getLogger('Spam Logger') # Obtiene un objeto Logger con el nombre "Spam Logger"
logger.setLevel(logging.DEBUG) #Se establece el nivel 'DEBUG'

'''
Al establecer el nivel de registro global en DEBUG, se habilita el registro de 
todos los eventos de registro, independientemente de su nivel de gravedad.
'''

logging.basicConfig(level=logging.DEBUG) #configura el registro global de la aplicación. todo el registro será de nivel 'DEBUG'
print(logger)