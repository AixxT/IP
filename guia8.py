import random
from queue import LifoQueue as Pila
from queue import Queue

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
    copia = pila
    while (not copia.empty()):
        copia.get()
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
    pilaParentesis = Pila()
    for char in formula:
        if (char == "("):
            pilaParentesis.put("(")
        elif ((not pilaParentesis.empty()) & (char == ")")):
            pilaParentesis.get()
    return pilaParentesis.empty()

#print(estaBienBalanceada("1 + ( 2 x 3 = ( 2 0 / 5 ) )"))  
#print(estaBienBalanceada("10 * ( 1 + ( 2 * ( =1)))"))  
#print(estaBienBalanceada("1 + ) 2 x 3 ( ( )"))
# IT WOOORKS *bailecito de victoria*

#   EJERCICIO 12
def evaluarExpresion(postfix: str) -> int:
    pilaOperadores = Pila()
    operandos: list[chr] = ["+","-","*","/"]
    numero: str = ""
    total = 0
    for char in postfix:
        if ((char not in operandos) & (char != " ")):
            numero += char
        elif (((char == " ") & (numero != "")) & (Queue.qsize(pilaOperadores) < 2)):
            pilaOperadores.put(numero)
            numero = ""
        elif ((char in operandos) & (Queue.qsize(pilaOperadores) == 2)):
            operador2 = pilaOperadores.get()
            operador1 = pilaOperadores.get()
            total = calcular(operador1, operador2, char)
            pilaOperadores.put(total)
    return total
            
def calcular (num1: str, num2: str, operacion: str) -> int:
    operador1: int = int(num1)
    operador2:int = int(num2)
    total = 0
    match (operacion):
        case "+":
            total = operador1 + operador2
        case "-":
            total = operador1 - operador2
        case "*":
            total = operador1 * operador2
        case "/":
            total = operador1 / operador2
    return total

#print(evaluarExpresion("3 4 + 5 * 2 -"))


###### COLAS ######

#   EJERCICIO 13
def colaAzarosa(len: int, numDesde: int, numHasta: int) -> Queue:
    cola = Queue()
    pila = generarNumerosAlAzar(len,numDesde,numHasta)
    while (not pila.empty()):
        cola.put(pila.get())
    return cola

#   EJERCICIO 14
def cantidadElementosCola(cola: Queue) -> int:
    copia = cola
    contador = 0
    while (not copia.empty()):
        copia.get()
        contador += 1
    return contador

#   EJERCICIO 15
def buscarElMaximoCola(cola: Queue[int]) -> int:
    copia = cola
    max = 0
    while (not copia.empty()):
        num = copia.get()
        if (num > max):
            max = num
    return max

#print(buscarElMaximoCola(colaAzarosa(5,8,25)))

#   EJERCICIO 16
#16.1
def armarSecuenciaBingo() -> Queue[int]:
    secuenciaBingo: Queue[int] = Queue()
    numerosUsados: list[int] = []
    while (Queue.qsize(secuenciaBingo)<100):
        randomNum = random.randint(0,99)
        if (randomNum not in numerosUsados):
            secuenciaBingo.put(randomNum)
            numerosUsados.append(randomNum)
    return secuenciaBingo

#16.2
def generarCarton() -> list[int]:
    carton: list[int] = []
    i = 0
    while (i < 12):
        num = random.randint(0,99)
        if (num not in carton):
            carton.append(num)
            i += 1
    return carton

def jugarCartonDeBingo(carton: list[int], bolitas: Queue) -> int:
    faltantes = 12
    contador = 0
    i = 0
    while (faltantes > 0):
        bolita = bolitas.queue[i]
        contador += 1
        i += 1
        if (bolita in carton):
            faltantes -= 1
    return contador

#carton = generarCarton()
#carton2 = generarCarton()
#carton3 = generarCarton()
#bolitas = armarSecuenciaBingo()
#print(jugarCartonDeBingo(carton, bolitas))
#print(jugarCartonDeBingo(carton2, bolitas))
#print(jugarCartonDeBingo(carton3, bolitas))

#   EJERCICIO 17
def cantPacientesUrgentes(cola: Queue[(int, str, str)]) -> int:
    i = 0
    contadorPacientesUrgentes = 0
    while ( i < Queue.qsize(cola)):
        paciente = cola.queue[i]
        i += 1
        if (paciente[0] in range(1,4)):
            contadorPacientesUrgentes +=1
    return contadorPacientesUrgentes

#listaPacientes = Queue()
#listaPacientes.put((5,"Maria","Odontologia"))
#listaPacientes.put((1,"Renata","Podologia"))
#listaPacientes.put((3,"Marco","General"))
#listaPacientes.put((9,"Julio","Pediatria"))
#
#print(cantPacientesUrgentes(listaPacientes))

#   EJERCICIO 18
# TO DO

###### DICCIONARIOS ######
#   EJERCICIO 19
def agruparPorLongitud(nombreArchivo: str) -> dict:
    longitudEnLetras: dict = {}
    listaLetrasPorPalabra: list[int] = letrasPorPalabra(listarPalabras(nombreArchivo))
    
    for num in listaLetrasPorPalabra:
        cantidadDePalabras = listaLetrasPorPalabra.count(num)
        
        if num not in longitudEnLetras:
            longitudEnLetras.update({num:cantidadDePalabras})
    return longitudEnLetras 

def listarPalabras(nombreArchivo: str) -> list[str]:
    palabras: list[str] = []
    with open(nombreArchivo, "r") as archivo:
        for linea in archivo:
            palabra: str = ""
            for char in linea:
                if (char != " "):
                    palabra += char
                else:
                    palabras.append(palabra)
                    palabra = ""
        archivo.close()
    return palabras

def letrasPorPalabra(listaPalabras: list[str]) -> list[int]:
    letrasEnPalabra: list[int] = []
    for palabra in listaPalabras:
        letrasEnPalabra.append(len(palabra))
    return letrasEnPalabra

#print(letrasPorPalabra(listarPalabras("Prueba.txt")))
#print(agruparPorLongitud("Prueba.txt"))

#   EJERCICIO 20
def registroPromedios(alumnos: list[( str, list[int] )]):
    registro: dict[str, int] = {}

    for alumno in alumnos:
        promedioAlumno: int = promedio(alumno[1])
        registro.update({alumno[0]:promedioAlumno})
    return registro

def promedio(lista: list[int]) -> int:
    sumaTotal = 0
    for num in lista:
        sumaTotal += num
    return round(sumaTotal / len(lista))

#alumnos = [("103/20",[8,5,2,6]),("176/21",[7,6,9,3])]

#print(promedio(alumnos[0][1]))
#print(registroPromedios(alumnos)) 

#   EJERCICIO 21
def laPalabraMasFrecuente(nombreArchivo: str) -> str:
    palabras: list[str] = listarPalabras(nombreArchivo)
    repeticionPalabras: dict[str,int] = dictRepeticion(palabras)
    
    valorMax = max(repeticionPalabras.values())
    key: str = list(repeticionPalabras.keys())[list(repeticionPalabras.values()).index(valorMax)]

    return key

def dictRepeticion(listaPalabras: list[str]) -> dict[str,int]:
    dictRepeticiones: dict[str,int] = {}

    for palabra in listaPalabras:
        repeticiones = listaPalabras.count(palabra)

        if palabra not in dictRepeticiones:
            dictRepeticiones.update({palabra:repeticiones})
    return dictRepeticiones

#print(laPalabraMasFrecuente("Prueba.txt"))

#   EJERCICIO 22



























