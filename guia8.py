
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
    return control

#1.3
def cantidadApariciones(palabra: str, nombreArchivo: str) -> int:
    apariciones = 0
    with open(nombreArchivo, "r") as archivo:
        for linea in archivo:
            apariciones += linea.count(palabra)
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
            

            





#print(cantidadApariciones("manola", "Prueba.txt"))













