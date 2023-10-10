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

def tieneMinusculas(s: str) -> bool:
    




