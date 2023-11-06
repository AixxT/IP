#   EJERCICIO 1
def ultima_aparicion(listaNumerica: list[int], num: int) -> int:
    i = len(listaNumerica) - 1

    while (listaNumerica[i] != num):
        i -= 1
    
    return i

#   EJERCICIO 2
def elementos_exclusivos(seq1: list[int],seq2: list[int]) -> list[int]:
    diferenciaSimetrica: list[int] =[]

    for num in seq1:
        if ((num not in seq2) & (num not in diferenciaSimetrica)):
            diferenciaSimetrica.append(num)
    
    for num in seq2:
        if ((num not in seq1) & (num not in diferenciaSimetrica)):
            diferenciaSimetrica.append(num)
    
    return diferenciaSimetrica


#   EJERCICIO 3
def contar_traducciones_iguales(ing: dict[str:str], ale: dict[str:str]) -> int:
    coincidencias: int = 0
    
    valuesAleman: list[str] = list(ale.values())
    valuesIngles: list[str] = list(ing.values())

    for traduccion in valuesAleman:
        if (traduccion in valuesIngles):
            coincidencias += 1
    return coincidencias

#   EJERCICIO 4
def convertir_a_diccionario(listaNumerica: list[int]) -> dict[int:int]:
    apariciones: dict[int:int] = {}
    
    for num in listaNumerica:
        if num not in (apariciones.keys()):
            repeticiones: int = listaNumerica.count(num)
            apariciones.update( { num : repeticiones })

    return apariciones

lista = [-1, 0, 4, 100, 100, -1, -1]

#print(convertir_a_diccionario(lista) == {-1:3, 0:1, 4:1, 100:2})

    



