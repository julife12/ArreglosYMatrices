def cambio_ultimos(a):
    a[4][6]=0
    a[4][5]=0
    a[4][4]=0
    a[4][3]=0
    return a

def funcion_diccionario(x):
    diccionario= {0:"Lunes",1:"Martes",2:"Miercoles",3:"Jueves",4:"Viernes",5:"Sabado",6:"Domingo"}
    dia=diccionario[x]
    return dia


def mayor_semana(x):
    for i in range(5):
        mayor_1=max(x[i])
        for j in range(7):
            if mayor_1==x[i][j]:
                dia=funcion_diccionario(j)
        
        print("la mayor temperatura en la semana ", i+1, " es: ", mayor_1, "el ", dia)
    
    print("")


def menor_semana(x):
    for i in range(5):
        if i != 4:
            menor_1=min(x[i])
            for j in range(7):
                if menor_1==x[i][j]:
                    dia=funcion_diccionario(j)
        
            print("la menor temperatura en la semana ", i+1, " es: ", menor_1, "el ", dia)
        else:
            for j in range(3):
                n=x[i][j]

                if j==0:
                    numero_m=n
                    dia=funcion_diccionario(j)
                if numero_m>x[i][j]  :
                    numero_m=n
                    
                    dia=funcion_diccionario(j)

            print("la menor temperatura en la semana ", i+1, " es: ", numero_m, "el ", dia)    

    print("")
            

def promedio(a):
    for i in range(5):
        suma=0
        if i != 4:
            for j in range(7):
                suma+=a[i][j]

            print("el promedio de la semana ", i,"es", (suma/7) )

        else:
            for j in range(3):
                suma+=a[i][j]
            print("el promedio de la semana ", i, "es", (suma/3))

    print("")
    
def numero_dia_a_dia(x):
    if x%7==0:
        s=int(x/7)-1
    else:
        s=int(x/7)

    z=s*7
    ds= x-z
    if ds == 7:
        ds=0
    return ds

def mayor_menor_mes(a):
    import numpy as np
    valormx=a.max()
    numero=numero_dia_a_dia(np.argmax(a))
    dia=funcion_diccionario(numero)
    print("el valor maximo del mes fue: ",valormx, "un", dia)
    print("")
    valormn=a.min()
    numero2=numero_dia_a_dia(np.argmin(a))
    dia2=funcion_diccionario(numero2)
    print("el valor minimo del mes fue: ",valormn, "un", dia2)
    print("")


def promediomax(a):
    promediomx=0
    for i in range(5):
        suma=0
        
        if i != 4:
            for j in range(7):
                suma+=a[i][j]

            promedio=suma/7
        else:
            for j in range(3):
                suma+=a[i][j]
            promedio=suma/3

        if promediomx< promedio:
            promediomx=promedio
            semana=i

    print("la semana mas calurosa fue la semana ", semana, "con una temperatura promedio de: ", promediomx)
    print("")

def dia_cambiar(a):
    x=int(input("por favor digiteme el numero del dia que quiere cambiar: "))
    print("")
    valor=input("por favor ingrese la temperatura nueva: ")
    print("")

    if x%7==0:
        s=int(x/7)-1
    else:
        s=int(x/7)

    z=s*7
    ds= x-z-1
    a[s][ds]=valor


