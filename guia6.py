#  EJERCICIO 1
import math

def imprimirHolaMundo() :
    print ("Hola mundo!")

def imprimirUnVerso() :
    print ("Whoever said money can't solve your problems \n Must not have had enough money to solve 'em \n They say, 'Which one?' I say, 'Nah, I want all of 'em \n Happiness is the same price as red bottoms") 

def raizDe2() :
    return round(math.sqrt(2), 4)

def factorialDe2() :
    return 2

def perimetro() :
    return math.pi * 2


#  EJERCICIO 2
def imprimirSaludo(name:str) :
    print ("Hola " + name + "!" )

def raizCuadradaDe(num:float) :
    return math.sqrt(num)

def fahrenheitACelsius(temperature:int) :
    return (round(((temperature - 32) * 5)/9 , 3))

def imprimirDosVeces(estribillo: str) :
    print((estribillo + "\n") * 2)

def esMultiploDe (num1: float, num2: float):
    return num1%num2 == 0

def esPar(num: float) -> float:
    return esMultiploDe(num,2)

def cantidadDePizzas(comensales:int, minCantPorciones: int) :
    pizzasFloat = ((comensales * minCantPorciones) / 8)
    if (pizzasFloat > round(pizzasFloat)) :
        return round(pizzasFloat) + 1
    else:
        return round(pizzasFloat)

#  EJERCICIO 3
def algunoEs0(num1:float, num2: float) :
    return (num1 == 0) or (num2 == 0)

def ambosson0(num1:float, num2: float) :
    return (num1 == 0) and (num2 == 0)

def esNombreLargo(nombre: str) :
    return (len(nombre)>=3) and (len(nombre)<=8)    

def esBisiesto(year: int) :
    return (esMultiploDe(year,4) and not(esMultiploDe(year,100))) or (esMultiploDe(year,100) and esMultiploDe(year,400))

#  EJERCICIO 4
def pesoPino(altura:float) :
    if (min(altura, 3.01) == altura):
        return altura * 300
    else:
        return (3*3 + ((altura - 3)*2))* 100

def esPesoUtil(peso: float) :
    return ((min(1001,peso) == peso) and (max(399,peso)== peso))

def sirvePino(altura:float) :
    return esPesoUtil(pesoPino(altura))

#  EJERCICIO 5
def devolverElDobleSiEsPar(numero: int) :
    if (esPar(numero)):
        return numero * 2
    else :
        return numero

def devolverSiEsParSiNoElQueSigue(numero: int):
    if(esPar(numero)):
        return numero
    else:
        return numero + 1

def devolverElDobleSiEsMultiploDe3elTripleSiEsMultiploDe9(numero: int):
    if (esMultiploDe(numero,3)):
        return numero * 2
    elif (esMultiploDe(numero, 9)):
        return numero * 3
    else:
        return numero
    
def lindoNombre(nombre: str):
    if (len(nombre) >= 5):
        print("Tu nombre tiene muchas letras!")
    else:
        print("Tu nombre tiene menos de 5 caracteres")

def elRango(numero: float):
    if (numero < 5):
        print("Menor a 5")
    elif (numero > 10 & numero < 20):
        print("Entre 10 y 20")
    elif (numero > 20):
        print("Mayor a 20")
# Esto es un cancer pero la especificacion del ejercicio 
# no pide nada más ni dice como debe comportarse la función
# en los extremos :B

def jubiladoJovenOLaburante(genero: chr, edad: int):
    if (edad < 18):
        print("Andá de vacaciones")
    else:
        if((edad >= 60) & (genero == "F")):
            print("Andá de vacaciones")
        elif ( (edad >= 65) & (genero == "M")):
             print("Andá de vacaciones")
        else:
            print("Te toca trabajar")  

#  EJERCICIO 6
def naturalesHasta10():
    i = 1
    while (i < 11):
        print(i)
        i += 1

def paresEntre10Y40():
    i = 10
    while (i < 38):
        print((i + 2))
        i += 2

def eco():
    i = 0
    while (i < 10):
        print("eco ")
        i += 1

def cuentaRegresiva(numero: int):
    while (numero >= 1):
        print(numero)
        numero -= 1
    print("Despegue")

def viajeEnElTiempo(añoPartida: int, añoLlegada: int):
    while (añoLlegada < añoPartida):
        añoPartida -=1
        print("“Viajó un año al pasado, estamos en el año: ", añoPartida)
    print("Ha llegado a ", añoPartida)

def visitaAAristóteles(añoPartida: int):
    while (384 < añoPartida):
        añoPartida -=20
        print("“Viajó 20 años al pasado, estamos en el año: ", añoPartida)
    print("Ha llegado a ", añoPartida)


#  EJERCICIO 7

def naturales_hasta_10():
    for num in range(1,11,1):
        print(num)

def pares_entre_10_y_40():
    for num in range(12,42,2):
        print(num)

def eco10():
    for num in range(1,11,1):
        print("eco")

def cuenta_regresiva(numero: int):
    for num in range(numero,0,-1):
        print(num)

def viaje_en_el_tiempo(partida: int, llegada: int):
    for num in range(partida-1,llegada,-1):
        print("Viajó un año al pasado, estamos en el año:", num)
    print("Ha llegado al año", llegada)

def visita_a_aristóteles(partida: int):
    for num in range(partida-1,384,-20):
        print("Viajó 20 años al pasado, estamos en el año:", num)









