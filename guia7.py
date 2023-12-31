import random
import numpy as np

#  EJERCICIO 1
#1.1
def pertenece(s: list, e: int):
    return (s.count(e) > 0)
#1.2
def pertenece2(s: list, e: int):
    for num in s:
        if (num == e):
            return True
    return False

#1.3
def divideATodos(s: list, e: int):
    for num in s:
        if (num % e != 0):
            return False
    return True

#1.4
def sumaTotal(s: list):
    total = 0
    for num in s:
        total += num
    return total

#1.5
def ordenados(s: list):
    i = 0
    while (i< len(s)-1):
        if (s[i] > s[i+1]):
            return False
        i += 1
    return True

#1.6
def palabraLarga(s: str):
    return len(s) > 7

#1.7
def palindromo(s: str):
    listaSinEspacios = quitarEspacios(s.lower())
    if (esPar(len(listaSinEspacios))):
        i = 0
        while (i <= mitad(len(listaSinEspacios))):
            if (listaSinEspacios[i] != listaSinEspacios[len(listaSinEspacios)-i-1]):
                return False
            i += 1
        return True
    else:
        i = 0
        while ( i <= (round(mitad(len(listaSinEspacios))))):
            if (listaSinEspacios[i] != listaSinEspacios[len(listaSinEspacios)-i-1]):
                return False
            i += 1
        return True


def quitarEspacios(s: str) -> list:
    listaSinEspacios = []
    for letra in s:
        if (letra != " "):
            listaSinEspacios.append(letra)
    return listaSinEspacios

def esPar(num: int) -> bool:
    return (num % 2 == 0)

def mitad (num: int) -> int:
    return num / 2

#1.7
def fortaleza(pswd: str) -> str:
    if (len(pswd) < 5):
        return "ROJA"
    elif ((len(pswd) > 8) & tieneMinusculas(pswd) & tieneMayusculas(pswd) & tieneNumeros(pswd)):
        return "VERDE"
    else:
        return "AMARILLA"

def tieneMinusculas(pswd: str) -> bool:
    return any(char.islower() for char in pswd)

def tieneMayusculas(pswd: str) -> bool:
    return any(char.isupper() for char in pswd)

def tieneNumeros(pswd: str) -> bool:
    return any(char.isdigit() for char in pswd)

#1.8

def cuentaBancaria(movimientos: (str,int)) -> int:
    saldo = 0
    for movimiento in movimientos :
        if (movimiento[0] == "I"):
            saldo += movimiento[1]
        else:
            saldo -= movimiento[1]
    print("Saldo total: ", saldo)
    return saldo

# movimientos = [("I",2000), ("R", 20),("R", 1000),("I", 300)]


# 1.9

def tresVocalesDistintas(wrd: str) -> bool:
    tresVocales = []
    for char in wrd:
        if ((len(tresVocales) < 3) & esVocal(char) & (char not in tresVocales)):
            tresVocales.append(char)
    return len(tresVocales) == 3

def esVocal(char: chr) -> bool:
    vocales = ('a','e','i','o','u','A','E','I','O','U')
    return char in vocales



#  EJERCICIO 2

#1
def ceroEnParesInOut(lista: int) -> list:
    i = 0
    while (i < len(lista)):
        if esPar(i):
            lista[i + 1] = 0
        i += 1
    return lista

#2
def ceroEnParesIn(listaIn: int) -> list:
    i = 1
    listaOut = []
    while (i <= len(listaIn)):
        if esPar(i):
            listaOut.append(0)
        else:
            listaOut.append(listaIn[i -1])
        i += 1
    return listaOut

#3
def sinVocales(wrd: str) -> str:
    palabraSinVocales = ""
    for char in wrd:
        if (not esVocal(char)):
            palabraSinVocales += char
    return palabraSinVocales


#4
def reemplazaVocales(wrd: str) -> str:
    stringOut = ""
    for char in wrd:
        if esVocal(char):
            stringOut += "-"
        else:
            stringOut += char
    return stringOut


#5
def daVueltaStr(wrd: str) -> str:
    strAlReves = ""
    i = 0
    while (i < len(wrd)):
        strAlReves += wrd[len(wrd) - i - 1]
        i += 1
    return strAlReves

#6
def eliminarRepetidos(wrd: str) -> str:
    stringSinRepetidos = ""
    for char in wrd:
        if (char not in stringSinRepetidos):
            stringSinRepetidos += char
    return stringSinRepetidos


#  EJERCICIO 3

def aprobado(notas: list[int]) -> int:
    res = 0
    if ( (any((nota < 4) for nota in notas)) | (promedio(notas) < 4) ):
        res = 3
    elif ((all((nota >= 4) for nota in notas)) & (promedio(notas) in range(4,7))):
        res = 2
    else:
        res = 1
    return res

def promedio(lista: list[int]) -> int:
    sumaTotal = 0
    for num in lista:
        sumaTotal += num
    return round(sumaTotal / len(lista))


#  EJERCICIO 4

# 4.1
def misEstudiantes() -> list[str]:
    nombre = ""
    listaEstudiantes = []
    while (nombre != "listo"):
        nombre = input("Ingrese el nombre del estudiante: ")
        listaEstudiantes.append(nombre)
        print("Cuando finalice ingrese 'listo'")
    return listaEstudiantes

# 4.2
def billeteraVirtual() -> list[chr, int]:
    operacion = ""
    saldo = 0
    historial = []
    while (operacion != "X"):
        print("C: Cargar créditos \nD: Descontar créditos \nX: Finalizar")
        operacion = input("Ingrese la operación deseada: ")
        if (operacion == "C"):
            monto = int(input("Ingrese el monto a cargar: "))
            saldo += monto
            historial.append(("C",monto))
        elif (operacion == "D"):
            monto = int(input("Ingrese el monto a descontar: "))
            saldo -= monto
            historial.append(("D",monto))
    return historial

# 4.3
def sieteYMedio() -> list[int]:
    sumaTotal = 0
    plantarse = ""
    perdio = False
    historial: list[int] = []

    while ((plantarse != "P") & (not perdio)):
        carta = sacarCarta() #excluyo al 8 y al 9
        sumaTotal += valor(carta)
        historial.append(carta)
        if (sumaTotal < 7.5):
            plantarse = input("P: plantarte \nC: sacar otra carta \n Tú decides joven padawan: ")
        else:
            print("Perdiste.. Mejor ni vayas al casino")
            perdio = True
    if (not perdio):
        print("Ganaste! Jamás dudé de ti pequeño saltamontes")
    return historial
            
def sacarCarta() -> int:
    carta = 0
    control = True
    
    while control :
        carta = random.randint(1,13)
        if (carta not in range(8,10)):
            control = False
    return carta

def valor(carta: int) -> float:
    valor = 0
    if (carta in range(1,8)):
        valor = carta
    else:
        valor = 0.5
    return valor


#   EJERCICIO 5
#5.1
def perteneceACadaUno(lista1: list[list[int]], valor: int) -> list[bool]:
    listaPertenece: list[bool] = []
    for lista in lista1:
        listaPertenece.append(pertenece(lista,valor))
    return listaPertenece

ejemplo = [[1,2,3],[4,8,6],[1,6,9]]

#5.2
def esMatriz(lista: list[list[int]]) -> list[bool]:
    control = True
    i = 1
    
    while ((i < len(lista)) & control):
       control = ( len(lista[0]) == len(lista[i]) )
       i += 1
    
    return control

#5.3   
def filasOrdenadas(matriz: list[list[int]]) -> list[bool]:
    estanOrdenadas: list[bool] = []
    for lista in matriz:
        estanOrdenadas.append(ordenados(lista))
    return estanOrdenadas

#5.4 TO DO
