
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



            





#print(cantidadApariciones("manola", "Prueba.txt"))













