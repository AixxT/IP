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




