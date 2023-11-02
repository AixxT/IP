import random
from queue import LifoQueue as Pila
#   EJERCICIO 1

#1.1 
def contarLineas(nombreArchivo: str) -> int:
    archivo = open(nombreArchivo, "r")
    return len(archivo.readlines())

#1.2
def existePalabra(palabra: str, nombreArchivo: str) -> bool:
    control = False
    with open(nombreArchivo, "r") as archivo:
        for linea in archivo:
            if palabra in linea:
                control = True
        archivo.close()
    return control

#1.3
def cantidadApariciones(palabra: str, nombreArchivo: str) -> int:
    apariciones = 0
    with open(nombreArchivo, "r") as archivo:
        for linea in archivo:
            apariciones += linea.count(palabra)
        archivo.close()
    
    return apariciones

#   EJERCICIO 2

def clonarSinComentarios(nombreArchivo: str):
    archivoSinComentarios = open("sinComments.txt", "a")
    with open(nombreArchivo,"r") as archivoComentado:
        for linea in archivoComentado:
            if (not esComentario(linea)):
                archivoSinComentarios.writelines(linea)
    archivoSinComentarios.close()

def esComentario(linea:str) -> bool:
    comentario = False
    if ((linea[0] == "#") | comentarioTabuleado(linea)):
        comentario = True
    return comentario

def comentarioTabuleado(linea:str) -> bool:
    esCommentTabuleado = False

    if "#" in linea:
        recorte = linea[:linea.index("#")]
        if ( not any(char.isalpha() for char in recorte)):
            esCommentTabuleado = True
    
    return esCommentTabuleado

#   EJERCICIO 3
            
def reverso(nombreArchivo: str):
    with open(nombreArchivo, "r") as archivoOriginal:
        lineas: list[str] = archivoOriginal.readlines()
        archivoOriginal.close()
    with open("Reverso.txt", "w") as archivoReverso:
        for linea in reversed(lineas):
            archivoReverso.writelines(linea)
        archivoReverso.close()


#   EJERCICIO 4       
def agregarLineaFinal(nombreArchivo: str, linea: str):
    with open(nombreArchivo, "a") as archivo:
        archivo.write("\n")
        archivo.write(linea)
        archivo.close()

#   EJERCICIO 5
def agregarLineaComienzo(nombreArchivo: str, linea: str):
    with open(nombreArchivo) as archivo:
        contenido = archivo.read()
        archivo.close()

    with open(nombreArchivo, "w") as archivo:
        archivo.write(linea + "\n")
        archivo.write(contenido)
        archivo.close()

#   EJERCICIO 6
#consultar
def lectorBinario(nombreArchivo: str):

    with open(nombreArchivo, "r") as archivoBinario:
        contenidoBinario = archivoBinario.read()
        archivoBinario.close()
    
    palabras: list[str] = armarPalabras(contenidoBinario)
    
    return palabras

def armarPalabras(listaBinaria: list[int]):
    listaPalabras = []
    for byte in listaBinaria:
        palabra = ""
        if ((esCharValido(chr(byte))) & (chr(byte) != ' ')):
            palabra += chr(byte)
        else:
            listaPalabras.append(palabra)
            palabra = ""
    return listaPalabras

def esCharValido(char: chr):
    control = False
    if ( char.isalpha() | (esSimboloValido(char))):
        control = True
    return control

def esSimboloValido(char):
    control = False
    if ((ord(char) == 95) | (ord(char) == 32)):
        control = True
    return control   

#   EJERCICIO 7
#TO DO

###### PILAS ######

#   EJERCICIO 8
def generarNumerosAlAzar(num:int, desde: int, hasta: int) -> Pila:
    i = 0
    pila = Pila()
    while (i < num):
        pila.put(random.randint(desde,(hasta)))
        i += 1
    return pila

#   EJERCICIO 9
def cantidadDeElementos(pila: Pila) -> int:
    contador = 0
    while (not pila.empty()):
        pila.get()
        contador += 1
    return contador

#   EJERCICIO 10
def buscarElMaximo(pila: Pila) -> int:
    max = 0
    while( not pila.empty()):
        valor = pila.get()
        if (valor > max):
            max = valor
    return max

#   EJERCICIO 11
def estaBienBalanceada(formula: str) -> bool:
    operacionesBasicas = ["+","-","x","/"]
    



#print(buscarElMaximo(generarNumerosAlAzar(5,8,25)))















