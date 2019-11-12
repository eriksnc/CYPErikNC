#import Modulos
#Modulos.mi_print("Hola")
#from Modulos import * el asterisco simula todos los modulos

from Modulos import mi_print, otro_print, sumar, restar
import time
import sys
from asciistuff import Banner

mi_print("Hola º0º")
otro_print("otro print usado")
print(sumar(4,5))
print(restar(10,7))

for i in range(10,0,-1):
    print(i,"...")
    time.sleep(.5) #Se pausa un tiempo asignado
print(Banner("BOOOOOOM !!!"))

print(sys.platform)
