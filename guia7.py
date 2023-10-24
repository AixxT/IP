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
    if (any((nota < 4) for nota in notas) | promedio(notas) < 4 ):
        res = 3
    elif ((all((nota >= 4) for nota in notas) & promedio(notas) in range(4,7))):
        res = 2
    else:
        res = 1
    return res

def promedio(lista: list[int]) -> int:
    sumaTotal = 0
    for num in lista:
        sumaTotal += num
    return round(sumaTotal / len(lista))



a = [7,1,9,10]
d = [5,2,5,1]
bocho = [10,9,8,10]

print(aprobado(a))
print(aprobado(d))
print(aprobado(bocho))


