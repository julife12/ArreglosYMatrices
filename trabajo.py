import numpy as np
import funciones
a=np.random.randint(18,34,size=(5,7)) 
x=("  L  M  MI J  V  S  D")
a=funciones.cambio_ultimos(a)


funciones.mayor_semana(a)
funciones.menor_semana(a)
funciones.promedio(a)
funciones.mayor_menor_mes(a)
funciones.promediomax(a)
print("El mes sin cambios")
print(x)
print(a)
print("")
funciones.dia_cambiar(a)
print("El mes con cambios")
print("")
print(x)
print(a)
