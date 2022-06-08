import os
import random
from random import shuffle

LONGITUD_MAXIMA = 17119


def bienvenida():
    print("#" * 150)
    print("\033[1;32m"+"*** Bienvenido al juego del Ahorcado del grupo 'Aprobado' \U0001F606 \U0001F606 ***"+'\033[0;m')
    print("\033[;36m" + "A continuación, algunas indicaciones básicas del juego:  ")
    print("""    + El juego te permite multijugadores hasta un limite de 5. Inicialmente les solicitara los nombres de cada jugador
    + En cada carga les solicitara una confirmacion de si desea seguir ingresando nombres (jugadores). No pueden ingresar nombres repetidos
    + Luego tendran que elegir la longitud de la palabra que desean adivinar (mínimo 5 letras)
    + Todos los jugadores tendran la misma longitud de la palabra adivinar pero siendo otorgadas distintas palabras a cada jugador
    + Si ingresa una longitud mayor a la palabra mas larga, participaran las palabras con mas letras en el texto
    + Para elegir cualquier palabra sin importar la longitud presione 'enter'
    + Una vez elegida la longitud ya tendrá una palabra para adivinar 
    + Tiene hasta 7 intentos fallidos antes de perder la partida
    + Si estan participando mas de un jugador, el juego sera por turnos, pasando al siguiente jugador cuando se ingrese un desacierto
    + Cuando un jugador gane, finalizara inmediatamente el juego mostrando los puntajes por orden y con la palabra a adivinar
    + Cuando un jugador pierda pero siga existiendo participantes con intentos permitidos, la partida seguira normalmente
    + Para abandonar la partida, ingrese '0 (cero)' o 'FIN' 
    + Volver a ingresar una letra errónea contará como un nuevo desacierto
    + Las letras erróneas podrán visualizarse junto a la cantidad de desaciertos
    + Si vuelve a ingresar una letra ya acertada, el programa le pedirá un nuevo ingreso
    + Al finalizar el juego si decide no continuar, podrá visualizar su puntuación
    + Éxitos y que lo disfrute! """)
    print("#" * 150 + '\n'+ '\n'+'\033[0;m')

# <-- Bloque Escenario -->
def mostrar_interfaz(lista_palabra_oculta, aciertos, desaciertos, jugador):
    """"
    Funcion: mostar_interfaz
    Descripcion: Funcion parte del nucleo del escenario. Muestra el escenario a medida que se ejecuta cada intento
    ingresando letra por letra y la misma muestra la cantidad de aciertos
    o en su defecto desaciertos si el caracter ingresado no está en la palabra a adivinar
    Parametros:
    -palabra_oculta = invoca a la funcion lista_a_palabra junto con su parametro y lo muestra en la consola formateando
    la respuesta
    Salida: Muestra la letra en acierto o desacierto y la palabra oculta con signos de pregunta
    Autores: Mirko Pescio, Facundo Arce, Joaquin Dopazo, Tomas Barragan, Raul Gonzalez
    Funcion de la parte 1
    """
    palabra_oculta = lista_a_palabra(lista_palabra_oculta)
    return print("Turno de:",jugador,"\nPalabra a adivinar:", palabra_oculta, "Aciertos:", aciertos, "Desaciertos:", desaciertos)

def mostrar_interfaz_acierto(lista_palabra_oculta, aciertos, desaciertos, lista_letras_error):
    """"
    Funcion: mostrar_interfaz_acierto
    Descripcion: Funcion parte del nucleo del escenario. En caso de que la letra ingresada por el usuario esté en la
    palabra oculta, se imprime un mensaje de aprobación junto con la suma de un acierto por intento
    Precondicion: Acertar una letra de la palabra a adivinar
    PostCondicion: Aviso de acierto de una letra
    Autores: Mirko Pescio, Facundo Arce, Joaquin Dopazo, Tomas Barragan, Raul Gonzalez
    Funcion de la parte 1
    """
    palabra_oculta = lista_a_palabra(lista_palabra_oculta)
    return print("Muy bien!!! \U0001F60E →", palabra_oculta, "Aciertos:", aciertos, "Desaciertos:", desaciertos,
                 lista_letras_error)

def mostrar_interfaz_iniciada(lista_palabra_oculta, aciertos, desaciertos, lista_letras_error, jugador):
    palabra_oculta = lista_a_palabra(lista_palabra_oculta)
    return print("Turno de:",jugador,"\nPalabra a adivinar:", palabra_oculta, "Aciertos:", aciertos, "Desaciertos:", desaciertos,
                 lista_letras_error)

def mostrar_interfaz_error(lista_palabra_oculta, aciertos, desaciertos, lista_letras_error):
    """"
    Funcion: mostrar_interfaz_error
    Descripcion: Funcion parte del nucleo del escenario. El mensaje que se imprime por pantalla va a ser de
    desaprobación, junto con la suma de un desacierto por intento
    En esta se añade un parámetro lista_letras_error, la cual indica que si la letra ingresada es incorrecta, ésta se va
    a añadir a una lista para que el usuario pueda ver las letras que no corresponden con la palabra oculta
    Precondicion: Ingresar una letra erronea a adivinar
    PostCondicion: Mensaje informando el error
    Autores: Mirko Pescio, Facundo Arce, Joaquin Dopazo, Tomas Barragan, Raul Gonzalez
    Funcion de la parte 1
    """
    palabra_oculta = lista_a_palabra(lista_palabra_oculta)
    return print("Lo siento!!! \U0001F605 →", palabra_oculta, "Aciertos:", aciertos, "Desaciertos:", desaciertos,
                 lista_letras_error)

# <-- Bloque de procesamiento de los 3 archivos de texto (ETAPA 8)-->
def procesando_palabras_cuento():
    """Funcion: procesando_palabras_cuento
    Descripcion: En esta funcion cargamos en una lista las palabras correspondientes al texto: Cuentos.txt
                dicho texto se va a leer linea por linea con la función readline()
    PreCondicion: Texto original
    PostCondicion: Palabras del texto cargadas en una lista correspondientes al archivo procesado
    Autor: Mirko Pescio"""
    lista_palabras_cuento = []
    lineas_en_cuentos = open("Cuentos.txt")
    lineas = lineas_en_cuentos.readline()
    while lineas:
        for palabras in lineas.split():
            lista_palabras_cuento.append(palabras)
        lineas = lineas_en_cuentos.readline()
    lista_palabras_cuento = filtrar_listas(lista_palabras_cuento)
    lineas_en_cuentos.close()
    return lista_palabras_cuento

def procesando_palabras_la_araña_negra():
    """Funcion: procesando_palabras_la_araña_negra
    Descripcion: En esta funcion cargamos en una lista las palabras correspondientes al texto: La araña negra - tomo 1.txt
                dicho texto se va a leer linea por con la funcion readline()
    PreCondicion: Texto original
    PostCondicion: Palabras del texto cargadas en una lista correspondientes al archivo procesado
    Autor: Mirko Pescio"""
    lista_palabras_araña_negra = []
    lineas_en_araña_negra = open("La araña negra - tomo 1.txt")
    lineas = lineas_en_araña_negra.readline()
    while lineas:
        for palabras in lineas.split():
            lista_palabras_araña_negra.append(palabras)
        lineas = lineas_en_araña_negra.readline()
    lista_palabras_araña_negra = filtrar_listas(lista_palabras_araña_negra)
    lineas_en_araña_negra.close()
    return lista_palabras_araña_negra

def procesando_palabras_mil_y_una_noches():
    """Funcion: procesando_palabras_mil_y_una_noches
    Descripcion: En esta funcion cargamos en una lista las palabras correspondientes al texto: Las 1000 Noches y 1 Noche.txt
                dicho texto se va a leer linea por con la funcion readline()
    PreCondicion: Texto original
    PostCondicion: Palabras del texto cargadas en una lista correspondientes al archivo procesado
    Autor: Mirko Pescio"""
    lista_palabras_mil_y_una_noches = []
    lineas_en_mil_y_una_noches = open("Las 1000 Noches y 1 Noche.txt")
    lineas = lineas_en_mil_y_una_noches.readline()
    while lineas:
        for palabras in lineas.split():
            lista_palabras_mil_y_una_noches.append(palabras)
        lineas = lineas_en_mil_y_una_noches.readline()
    lista_palabras_mil_y_una_noches = filtrar_listas(lista_palabras_mil_y_una_noches)
    lineas_en_mil_y_una_noches.close()
    return lista_palabras_mil_y_una_noches

def quitar_simbolos_inicio(palabra):
    """Funcion: quitar_simbolos_inicio
    Descripcion: esta función filtra en todas las listas el primer caracter de las palabras que empiecen con un símbolo
    PreCondicion: haber generado las listas de palabras de cada archivo
    PostCondicion: seguimos teniendo las listas de palabras, pero las mismas sin símbolos al comienzo de las mismas
    Autor: Joaquin Dopazo"""
    indice = 0
    while not palabra[indice].isalpha() and indice < len(palabra)-1:
        indice += 1
    nueva_palabra = palabra[indice:len(palabra)]      
    return(nueva_palabra)

def quitar_simbolos_final(palabra):
    """Funcion: quitar_simbolos_final
    Descripcion: esta función filtra en todas las listas el último caracter de las palabras que terminen con un símbolo
    PreCondicion: haber generado las listas de palabras de cada archivo
    PostCondicion: seguimos teniendo las listas de palabras, pero las mismas sin símbolos al final de las mismas
    Autor: Joaquin Dopazo"""
    indice = 0
    simbolo_final = False
    while not simbolo_final and indice <= len(palabra)-1:
        if not palabra[indice].isalpha():
            simbolo_final = True
        indice += 1       
    if not simbolo_final:
        nueva_palabra = palabra
    else:
        nueva_palabra = palabra[0:indice-1]    
    return(nueva_palabra)

def quitar_tildes(palabra):
    """"
    Funcion: quitar_tildes
    Descripcion: En esta funcion principalmente, removemos las tildes asociadas a las vocales
    PreCondicion: Texto original
    PostCondicion: Letras con acentos son reemplazadas
    Autores: Mirko Pescio, Facundo Arce, Joaquin Dopazo, Tomas Barragan, Raul Gonzalez, Franco Scola
    Funcion de la parte 1
    """
    palabra = palabra.replace("á", "a")
    palabra = palabra.replace("é", "e")
    palabra = palabra.replace("í", "i")
    palabra = palabra.replace("ó", "o")
    palabra = palabra.replace("ú", "u")
    palabra = palabra.replace("ü", "u")
    
    return palabra

def filtrar_listas(lista):
    """Funcion: filtrar_listas
    Descripcion: esta función se ocupa de filtrar las palabras de las listas procesadas en cada archivo
                según las condiciones establecidas: longitud, quitar símbolos y tildes y tenerlas únicamente en minúsculas
    PreCondicion: Listas procesadas de cada archivo
    PostCondicion: 3 listas correspondientes a cada archivo de texto, pero con las palabras filtradas según las 
                condiciones planteadas
    Autor: Joaquin Dopazo"""
    lista_filtrada = []
    PALABRA_MAS_CORTA = 5
    for palabra in lista:
        palabra = palabra.lower()
        palabra = quitar_tildes(palabra)
        palabra = quitar_simbolos_inicio(palabra)
        palabra = quitar_simbolos_final(palabra)
        if palabra.isalpha() and len(palabra) >= int(PALABRA_MAS_CORTA):
            lista_filtrada.append(palabra)
    lista_filtrada.sort()
    return (lista_filtrada)

def lista_total_de_palabras():
    """Funcion: lista_total_de_palabras
    Descripcion: simplemente concatenamos las 3 listas filtradas de palabras obtenidas de cada texto para tener la
    lista de palabras candidatas
    PreCondicion: haber filtrado las listas de palabras de cada archivo de texto
    PostCondicion: obtenemos la lista de palabras candidatas para jugar
    Autores: Joaquin Dopazo
    """
    lista_total = []
    lista_1 = procesando_palabras_cuento()
    lista_2 = procesando_palabras_la_araña_negra()
    lista_3 = procesando_palabras_mil_y_una_noches()
    lista_total.extend(lista_1)
    lista_total.extend(lista_2)
    lista_total.extend(lista_3)
    return lista_total

# <-- Bloque Funciones de longitud -->
def verificar_longitud(lista_filtrada, longitud, longitud_maxima):
    """"
    Funcion: verificar_longitud
    Descripcion: Esta funcion se encarga de verificar la longitud especificada por el usuario generando asi una lista
    filtrada de las palabras candidatas que cumplen con la longitud previamente mencionada.
    PreCondicion: Recibir la lista de texto filtrada junto con las longitudes
    PostCondicion: Las palabras que cumplan con la condicion de longitud son agregadas a una nueva lista
    Autores: Mirko Pescio, Facundo Arce, Joaquin Dopazo, Tomas Barragan, Raul Gonzalez
    Funcion de la parte 1
    """
    nueva_lista_filtrada = []
    if longitud <= longitud_maxima:
        for palabra in lista_filtrada:
            if len(palabra) == longitud:
                nueva_lista_filtrada.append(palabra)
    else:
        for palabra in lista_filtrada:
            if len(palabra) == longitud_maxima:
                nueva_lista_filtrada.append(palabra)
    return nueva_lista_filtrada

def calculo_longitud_maxima(lista_filtrada):
    """"
    Funcion: calculo_longitud_maxima
    Descripcion: Corresponde a la longitud de cada palabra correspondiente en la lista de palabras candidatas con
    longitudes mayores a 5
    PreCondicion: Recibir lista filtrada
    PostCondicion: Se devuelve el valor de la palabra con la longitud mas grande
    Autores: Mirko Pescio, Facundo Arce, Joaquin Dopazo, Tomas Barragan, Raul Gonzalez, Franco Scola
    Funcion de la parte 1
    """
    longitud_maxima = 0
    for palabra in lista_filtrada:
        if longitud_maxima < len(palabra):
            longitud_maxima = len(palabra)
    return longitud_maxima

# <-- Bloque Funciones tratamiento de palabra - palabra candidata -->
def dicc_palabras_candidatas(longitud):
    """"
    Funcion: dicc_palabras_candidatas
    Descripcion: Cargamos la lista filtrada y la iteramos mediante compresion para asi formar un diccionario con las
    palabras candidatas, su cantidad de apariciones y ordenadas alfabeticamente
    PreCondicion: Recibir longitud y lista filtrada
    PostCondicion: Diccionario ordenado segun longitud especificada
    Autores: Mirko Pescio, Facundo Arce, Joaquin Dopazo, Tomas Barragan, Raul Gonzalez
    Funcion de la parte 1
    """
    lista_filtrada = lista_total_de_palabras()
    longitud_maxima = calculo_longitud_maxima(lista_filtrada)
    if longitud == "":
        print("Eligio el diccionario entero esto puede tomar unos segundos...")
        diccionario = {cantidad_apariciones: lista_filtrada.count(cantidad_apariciones) for cantidad_apariciones in
                       lista_filtrada}
        diccionario_vista_items = diccionario.items()
        diccionario_ordenado = {i: j for i, j in sorted(diccionario_vista_items)}
    else:
        nueva_lista_filtrada = verificar_longitud(lista_filtrada, longitud, longitud_maxima)
        diccionario = {cantidad_apariciones: nueva_lista_filtrada.count(cantidad_apariciones) for cantidad_apariciones
                       in nueva_lista_filtrada}
        diccionario_vista_items = diccionario.items()
        diccionario_ordenado = {i: j for i, j in sorted(diccionario_vista_items)}

    return diccionario_ordenado

def mostrar_lista(diccionario_ordenado):
    """
    Funcion: mostrar_lista
    Descripcion: Imprimimos por pantalla la cantidad total de palabras disponibles en el diccionario segun la longitud
    indicada por el usuario asi como tambien las palabras que cumplen con las condiciones especificadas
    PreCondicion: Recibir Longitud y diccionario
    PostCondicion: Muestra una lista de palabras de longitud X
    Autores: Mirko Pescio, Facundo Arce, Joaquin Dopazo, Tomas Barragan, Raul Gonzalez
    Funcion de la parte 1
    """
    longitud_diccionario = len(diccionario_ordenado.keys())
    print("Pool de palabras a elegir: ", longitud_diccionario)
    palabras = ""
    for i in diccionario_ordenado:
        palabras += i + ", "
    palabras_a_mostrar = palabras[:len(palabras) - 2]
    print("Diccionario de palabras:", palabras_a_mostrar)
    
def palabra_candidata(diccionario_ordenado):
    """
    Funcion: palabra_candidata
    Descripcion: Convertimos el diccionario a una lista que contenga solamente las claves y a partir de ella mediante la
    funcion de random elegimos al azar la palabra que sera asignada al juego para adivinar por el jugador
    Precondicion: Recibir un diccionario ordenado y una longitud
    PostCondicion: Una palabra al azar del diccionario es elegida segun la longitud especificada
    Autores: Mirko Pescio, Facundo Arce, Joaquin Dopazo, Tomas Barragan, Raul Gonzalez
    Funcion de la parte 1
    """
    lista_palabras_candidatas = diccionario_ordenado.keys()
    lista_palabras_candidatas = list(lista_palabras_candidatas)
    return random.choice(lista_palabras_candidatas).lower()
    
# <-- Bloque funciones tratamiento de letras y precondicondiciones de escenario -->
def lista_a_palabra(lista):
    """
    Funcion: lista_a_palabra
    Descripcion: Funcion que itera una lista de palabras y obtiene el caracter para luego permitir la visualizacion
    mediante la funciones de Escenarios
    PreCondicion: Recibir una lista
    PostCondicion: Devuelve una palabra en minusculas
    Autores: Franco Scola, Mirko Pescio, Facundo Arce, Joaquin Dopazo, Tomas Barragan, Raul Gonzalez
    Funcion de la parte 1
    """
    palabra = ""
    for caracter in lista:
        palabra += caracter
    return palabra.lower()

def palabras_en_listas(palabra):
    """
    Funcion: palabras_en_listas
    Descripcion: Funcion que permite la agregacion de las palabras en una lista que luego sera utilizado en la
    inicializacion de variables transformadola en la lista de palabras a adivinar
    Precondicion: Recibir una palabra
    PostCondicion: Retornar una lista con palabras
    Autores: Franco Scola, Mirko Pescio, Facundo Arce, Joaquin Dopazo, Tomas Barragan, Raul Gonzalez
    Funcion de la parte 1
    """
    lista = []
    for caracter in palabra:
        lista.append(caracter)
    return lista

def remplazar_por_letra(lista_palabra_1, lista_palabra_2, letra, cambio):
    """
    Funcion: remplazar_por_letra
    Descripcion:  Funcion que permite recorrer el escenario y reemplazar los signos de preguntas por las letras que
    conforman la palabra a adivinar
    PreCondicion: Recibir 2 listas y una letra ingresada por el usuario
    PostCondicion: retornar una lista con la letra cambiada en la posicion que corresponda
    Autores: Mirko Pescio, Facundo Arce, Joaquin Dopazo, Tomas Barragan, Raul Gonzalez
    Funcion de la parte 1
    """
    for caracter in range(0, len(lista_palabra_1)):
        if lista_palabra_1[caracter] == letra:
            lista_palabra_2[caracter] = letra
            cambio = True
    return lista_palabra_2, cambio

def busco_letra(lista_palabra_oculta, lista_palabra_adivinar, letra, cambio):
    """
    Función: busco_letra
    Descripción: Verifica que la letra ingresada por el jugador este dentro de la palabra a adivinar y en caso de
    volver a ingresar la misma letra imprime "Letra ya ingresada". En caso de error suma un desacierto
    PreCondicion: Recibir la palabra oculta a adivinar y la letra ingresada por el usuario
    PostCondicion: Retornar la letra cambiada en el escenario o un aviso de letra ya existente
    Autores: Joaquin Dopazo, Mirko Pescio, Tomas Barragan, Facundo Arce, Raul Gonzalez
    Funcion de la parte 1
    """
    cambio = False
    if letra in lista_palabra_adivinar:
        while letra in lista_palabra_oculta:
            print("Letra ya ingresada")
            letra = nuevo_ingreso()
    lista_palabra_oculta, cambio = remplazar_por_letra(lista_palabra_adivinar, lista_palabra_oculta, letra, cambio)
    return lista_palabra_oculta, cambio

def condicion_final(lista_palabra_oculta):
    """
    Función: condición_final
    Descripción: Al finalizar la partida revisa si la palabra a adivinar aun posee signos de pregunta(?), en caso de
    que los posea el jugador perdió, en caso de que no los posea, el jugador ganó
    PreCondicion: Recibir la palabra oculta en formato lista
    PostCondicion: Retornar el estado final del juego: "Ganaste o Perdiste"
    Autores: Joaquin Dopazo, Mirko Pescio, Tomas Barragan, Facundo Arce, Raul Gonzalez
    Funcion de la parte 1
    """
    if "?" in lista_palabra_oculta:
        ganaste = False
    else:
        ganaste = True
    return ganaste

def cargar_letras_erroneas(letra, lista_letras_error, letras_erroneas):
    """
    Función: cargar_letras_erroneas
    Descripción: Almacena las respuestas erróneas del jugador durante la partida y luego las muestra en la interfaz
    PreCondicion: Letras erroneas ingresadas por el usuario
    PostCondicion: Una lista de las letras erroneas
    Autores: Joaquin Dopazo, Mirko Pescio, Tomas Barragan, Facundo Arce, Raul Gonzalez
    Funcion de la parte 1
    """
    if letra not in lista_letras_error:
        lista_letras_error.append(letra)
        letras_erroneas += " - " + letra
    return lista_letras_error, letras_erroneas

def resultado_final(desaciertos, ganaste,lista_configuracion):
    """
    Función: resultado_final
    Descripción: Cuenta los errores del jugador durante la partida, en caso de llegar a los 8 desaciertos
    se da por finalizada y perdida la partida.
    PreCondicion: Recibir la cantidad de desaciertos y estado del tablero
    PostCondicion: Retornar mensaje de estado por pantalla "Ganaste o Perdiste"
    Autores: Franco Scola, Joaquin Dopazo, Mirko Pescio, Tomas Barragan, Facundo Arce, Raul Gonzalez
    Funcion de la parte 1
    """
    configuracion_remota = parametros_configuracion()
    dicc_parametros = validacion_configuracion(configuracion_remota)
    NUMERO_MAX_ERRORES = dicc_parametros['NUMERO_MAX_ERRORES']
    return "Perdiste" if (desaciertos == int(NUMERO_MAX_ERRORES) or not ganaste) else "Ganaste"

# <-- Bloque Funciones de validacion de Ingreso -->
def validar_caracter_numerico(longitud):
    """
    Funcion: validar_caracter_numerico
    Descripcion:  La función corresponde a la validación de caracter númerico ingresado por el usuario
    PreCondicion: Recibir una longitud
    PostCondicion: Retornar un estado valido o invalido dependiendo de la entrada del usuario
    Autores: Joaquin Dopazo, Mirko Pescio, Tomas Barragan, Facundo Arce, Raul Gonzalez
    Funcion de la parte 1
    """
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    caracteres_numericos = True
    indice = 0
    while caracteres_numericos and indice < len(longitud):
        if longitud[indice] not in numeros:
            caracteres_numericos = False
        indice += 1
    return caracteres_numericos

def validar_longitud(longitud):
    """
    Función: validar_longitud
    Descripción: Valua la longitud de la palabra que desea adivinar, evita que sea menor a 5 o
    un valor no numérico.
    PreCondicion: Recibir Longitud especifica por el usuario
    PostCondicion: retornar una longitud valida
    Autores: Joaquin Dopazo, Mirko Pescio, Tomas Barragan, Facundo Arce, Raul Gonzalez
    Funcion de la parte 1
    """
    caracteres_numericos = validar_caracter_numerico(longitud)
    if longitud != "" and caracteres_numericos:
        longitud = int(longitud)
        longitud = validar_longitud_minima(longitud, caracteres_numericos)
    elif longitud != "" and not caracteres_numericos:
        longitud = validar_ingreso_numerico(longitud, caracteres_numericos)
        if longitud != "":
            longitud = int(longitud)
            longitud = validar_longitud_minima(longitud, caracteres_numericos)
    return longitud

def validar_ingreso_numerico(longitud, caracteres_numericos):
    """
    Función: validar_caracter_numerico
    Descripción: Asegura que la longitud sea numerica al comparar una cadena con los números dentro de la lista de
    la función. Adicionalmente posee un manejo de excepciones especial en caso de que el usuario no especifique
    longitud luego de un ingreso erroneo
    Precondicion: Recibir Longitud y comprobar que la longitud ingresada sea valida
    PostCondicion: Retornar un mensaje para verificar dato ingresado
    Autores: Joaquin Dopazo, Facundo Arce, Mirko Pescio, Tomas Barragan, Raul Gonzalez
    Funcion de la parte 1
    """
    while caracteres_numericos == False and longitud != "":
        longitud = input("Ingrese solo valores numericos: ")
        try:
            caracteres_numericos = validar_caracter_numerico(longitud)
        except:
            longitud == ""
    return longitud

def validar_longitud_minima(longitud, caracteres_numericos):
    """
    Funcion: validar_longitud_minima
    Descripcion: Funcion que verifica que la longitud minima especifica por el usuario para la palabra a adivinar
    cumpla con las condiciones de ser mayores o igual 5. Adicionalmente posee un manejo de excepciones especial en caso
    de que el usuario no especifique longitud luego de un ingreso erroneo
    PreCondicion: Recibir longitud valida
    PostCondicion: Retornar mensaje de longitud esperable
    Autores: Joaquin Dopazo, Facundo Arce, Mirko Pescio, Tomas Barragan, Raul Gonzalez
    Funcion de la parte 1
    """
    configuracion_remota = parametros_configuracion()
    dicc_parametros = validacion_configuracion(configuracion_remota)
    PALABRA_MAS_CORTA = dicc_parametros['PALABRA_MAS_CORTA']
    while longitud != "" and longitud < int(PALABRA_MAS_CORTA):
        longitud = input("Ingrese una longitud mayor o igual a 5 caracteres: ")
        try:
            caracteres_numericos = validar_caracter_numerico(longitud)
            longitud = validar_ingreso_numerico(longitud, caracteres_numericos)
            longitud = int(longitud)
        except:
            longitud == ""
    return longitud

def validar_letra(letra, abandono):
    """"
    Funcion: validar_letra(letra,abandono)
    Descripción: La funcion verifica en partida que la letra ingresa sea de 1 solo caracter al mismo tiempo que verifica
    que el caracter ingresado no corresponda al "abandono" del juego
    PreCondicion: Recibir un ingreso por el usuario
    PostCondicion: Retornar si el ingreso es valido o una salida del juego
    Autores: Facundo Arce, Mirko Pescio, Tomas Barragan, Joaquin Dopazo, Raul Gonzalez
    Funcion de la parte 1
    """
    LONGITUD_RESPUESTA = 1
    while (len(letra) != LONGITUD_RESPUESTA or (not letra.isalpha())) and not abandono:
        print("Ingreso Inválido")
        letra = input("Ingrese Letra: ")
        letra = letra.lower()
        abandono = seguir_jugando(letra, abandono)
    return letra, abandono

# <-- Bloque Funciones para multijugador -->
def generar_jugadores():
    """
    Descripcion: Funcion que administra la carga de jugadores, valida la cantidad maxima y los almacena en una lista para su posterior
    tratamiento
    Autor: Mirko Pescio
    """
    configuracion_remota = parametros_configuracion()
    dicc_parametros = validacion_configuracion(configuracion_remota)
    MAX_USUARIOS = dicc_parametros['MAX_USUARIOS']
    validacion = "s"
    validacion = validacion.lower()
    contador = 0
    lista_jugador = []
    while validacion != "n" and validacion != "N" and contador < int(MAX_USUARIOS):
        cargar_nombre(lista_jugador)
        contador += 1
        if contador < 5:
            validacion = validar_ingreso_nombres()
    return lista_jugador

def validar_ingreso_nombres():
    """
    Decripcion: Funcion que valida si el usuario desea seguir ingresando nombres y verifica que los datos ingresados a modo de confirmacion sean correctos.
    Autor: Tomas Barragan
    """
    validacion = input("Desea seguir ingresando nombres? (s/n): ")
    validacion = validacion.lower()
    while validacion != "n" and validacion != "N" and validacion != "s" and validacion != "S":
        validacion = input("Por favor ingrese 's' o 'n': ")
    return validacion

def cargar_nombre(lista_jugador):
    """
    Descripcion: Funcion en el cual validamos que los ingresos de jugadores sean validos y con ello armamos una lista interna para el juego
    y sus operaciones
    Autor: Facundo Arce
    """
    nombre = input("Ingrese un nombre: ") 
    nombre = nombre.capitalize()
    while [nombre,0,"","","","","",False,"","",0,""] in lista_jugador or nombre == "" or nombre == " ":
        nombre = input("Ingrese un nombre que no se haya ingresado anteriormente ni sea un espacio vacio: ")
        nombre = nombre.capitalize()
    lista_jugador.append([nombre,0,"","","","","",False,"","",0,""])
    return lista_jugador
    
def iniciar_variables_multiplayer(lista_jugador,palabra_a_adivinar,contador):
    """
    Descripcion: Funcion en donde declaramos e iniciamos las variables para el juego y escenario con respecto a los multijugadores y sus estados iniciales
    Autor: Facundo Arce
    """
    lista_palabra_oculta = []
    lista_palabra_a_adivinar = palabras_en_listas(palabra_a_adivinar)
    aciertos = desaciertos = 0
    lista_letras_error = []
    letras_erroneas = ""
    ganaste = False
    abandono = False
    perdio = False
    for i in range (0, len(palabra_a_adivinar)):
        lista_palabra_oculta.append("?")
    lista_jugador = cargar_lista_jugador(lista_palabra_a_adivinar,lista_palabra_oculta,aciertos,desaciertos,letras_erroneas,ganaste,abandono,lista_letras_error,lista_jugador,contador,perdio)
    return lista_jugador

def cargar_lista_jugador(lista_palabra_a_adivinar,lista_palabra_oculta,aciertos,desaciertos,letras_erroneas,ganaste,abandono,lista_letras_error,lista_jugador,contador,perdio):
    """
    Descripcion: Funcion de generacion y carga de parametros de cada jugador en una lista para su posterior tratamiento y validacion durante y al finalizar la partida
    Autor: Facundo Arce
    """
    lista_jugador[contador][2] = lista_palabra_a_adivinar
    lista_jugador[contador][3] = lista_palabra_oculta
    lista_jugador[contador][4] = aciertos
    lista_jugador[contador][5] = desaciertos
    lista_jugador[contador][6] = letras_erroneas
    lista_jugador[contador][7] = ganaste
    lista_jugador[contador][8] = abandono
    lista_jugador[contador][9] = lista_letras_error
    lista_jugador[contador][11] = perdio
    return lista_jugador
    
def generar_diccionario_multiplayer(longitud):
    """
    Descripcion: Funcion de generacion de diccionario para los multijugadores respetando las longitudes especificadas
    Autor: Facundo Arce
    """
    diccionario_ordenado = dicc_palabras_candidatas(longitud)
    palabra_a_adivinar = palabra_candidata(diccionario_ordenado)
    mostrar_lista(diccionario_ordenado)
    if longitud == "":
        diccionario_ordenado,longitud = misma_longitud(diccionario_ordenado,palabra_a_adivinar)    
    return (diccionario_ordenado,palabra_a_adivinar,longitud)

def limpiar_lista(lista_jugador):
    """
    Descripcion: Funcion donde limpiamos la lista y sus estados para proximas rondas de juego
    Autor: Facundo Arce
    """
    for i in range(0,len(lista_jugador)):
        lista_jugador[i][2] = ""
        lista_jugador[i][3] = ""
        lista_jugador[i][4] = ""
        lista_jugador[i][5] = ""
        lista_jugador[i][6] = ""
        lista_jugador[i][7] = False
        lista_jugador[i][8] = ""
        lista_jugador[i][9] = ""
        lista_jugador[i][10] = 0
        lista_jugador[i][11] = ""
    return(lista_jugador)

# <-- Bloque Funciones Auxiliares para el multijugador -->
def guardar_puntajes_generales(lista_jugador):
    """
    Descripcion: Funcion que almacena los puntajes de las rondas para mostrarse luego como puntaje final de cada jugador
    Autor: Raul Gonzalez
    """
    for i in range(0,len(lista_jugador)):
        lista_jugador[i][1] += lista_jugador[i][10]
    return(lista_jugador)
        
def misma_longitud(diccionario_ordenado,palabra_a_adivinar):
    """
    Descripcion: Funcion que genera un subdiccionario con las palabras de la longitud elegida para ser utilizada en la asignacion al azar de palabras a los jugadores
    Autor: Tomas Barragan
    """
    nueva_longitud = 0
    longitud_diccionario = len(diccionario_ordenado.keys())
    if longitud_diccionario == LONGITUD_MAXIMA:
        nueva_longitud = len(palabra_a_adivinar)
        diccionario_ordenado = dicc_palabras_candidatas(len(palabra_a_adivinar))
    return(diccionario_ordenado,nueva_longitud)
           
def gano_la_maquina(lista_jugador):
    """
    Descripcion: Funcion de verificacion de estado de juego para cada jugador y asignando el puntaje correspondiente en 
    caso de la victoria de la maquina (todos los jugadores pierden)
    Autor: Tomas Barragan
    """
    configuracion_remota = parametros_configuracion()
    dicc_parametros = validacion_configuracion(configuracion_remota)
    PUNTOS_RESTA_GANA_PROGRAMA = dicc_parametros['PUNTOS_RESTA_GANA_PROGRAMA']
    for i in range(0,len(lista_jugador)):
        lista_jugador[i][10] -= int(PUNTOS_RESTA_GANA_PROGRAMA)
    return lista_jugador
        
def jugadores_participando(cant_jugadores,perdedores):
    """
    Descripcion: Funcion de validacion de jugadores activos en la ronda
    Autor: Mirko Pescio
    """
    cant_jugadores = cant_jugadores - perdedores
    return cant_jugadores

def longitud_multiplayer():
    """
    Descripcion: Funcion de ingreso de longitud de palabra a adivinar y su validacion para los multijugadores
    Autores: Facundo Arce, Mirko Pescio, Tomas Barrangan, Joaquin Dopazo, Raul Gonzalez
    Funcion de la parte 1 se cambio el nombre
    """
    longitud = input("Ingrese la longitud de su palabra (solo numericos): ")
    longitud = validar_longitud(longitud)
    return(longitud)

def quitar_perdedores(lista_jugador):
    """
    Descripcion: Funcion que remueve perdedores de la partida en curso
    Autor: Tomas Barragan
    """
    lista_jugador.sort(key = lambda item: item[11])
    return lista_jugador
    
def verifico_perdedor(desaciertos,perdedores,pierde):
    """
    Descripcion: Funcion auxiliar de declaracion de la condicion de derrota
    Autor: Tomas Barragan
    """
    configuracion_remota = parametros_configuracion()
    dicc_parametros = validacion_configuracion(configuracion_remota)
    NUMERO_MAX_ERRORES = dicc_parametros['NUMERO_MAX_ERRORES']
    if desaciertos == int(NUMERO_MAX_ERRORES) or desaciertos == "":
        perdedores +=1
        pierde = True
    return (perdedores,pierde)

def ordenar_lista(lista_jugador):
    """
    Descripcion: Funcion que ordena al azar la lista de jugadores respetando el ganador en cada ronda
    Autor: Raul Gonzalez
    """
    random.shuffle(lista_jugador)
    lista_jugador.sort(key=lambda item: item[7], reverse=True)
    return(lista_jugador)

# <-- Bloque Funciones de partida -->

def ingreso(abandono):
    """"
    Función: ingreso(abandono)
    Descripción: Función que corresponde cuando el ingreso de abandono sea verdadero y esto se va a cumplir cuando
    durante la asignación de caractéres, elija "FIN" o "0"
    PreCondicion: Recibir un ingreso por parte del usuario
    PostCondicion: Validar si el ingreso corresponde a un salida del juego
    Autores: Tomas Barragan, Facundo Arce, Mirko Pescio, Joaquin Dopazo
    Funcion de la parte 1
    """
    letra = input("Ingrese Letra: ")
    letra = letra.lower()
    abandono = seguir_jugando(letra, abandono)
    if not abandono:
        letra, abandono = validar_letra(letra, abandono)
        abandono = seguir_jugando(letra, abandono)
    return letra, abandono

def nuevo_ingreso():
    """"
    Función: nuevo_ingreso()
    Descripción: Ciclo para la repetición de asignación de caracteres, la cual corresponde con la condición de caracter
    válido, y su concatenación de Intentos
    PreCondicion: Recibir ingreso por parte del usuario
    PostCondicion: Validar y retornar la letra ingresada
    Autores: Tomas Barragan, Facundo Arce, Mirko Pescio, Joaquin Dopazo
    Funcion de la parte 1
    """
    letra = input("Ingrese Letra: ")
    letra = letra.lower()
    LONGITUD_RESPUESTA = 1
    while len(letra) != LONGITUD_RESPUESTA or not (letra.isalpha()):
        print("Ingreso Inválido")
        letra = input("Ingrese Letra: ")
        letra = letra.lower()
    return letra

def mostrar_resultados(lista_jugador):
    """
    Descripcion: Funcion que imprime por pantalla el resultado de las rondas, con el jugador ganador, puntajes, palabra a adivinar, etc
    Autor: Tomas Barragan
    """
    lista_jugador.sort(key = lambda item: item[1], reverse = True)
    for i in range(0,len(lista_jugador)):
        palabra = lista_a_palabra(lista_jugador[i][2])
        print("Jugador:",lista_jugador[i][0],"\tPuntos:",lista_jugador[i][10],"\tTotal:",lista_jugador[i][1],"\tPalabra:",palabra,"\tCantidad aciertos:",lista_jugador[i][4],\
            "\tCantidad desaciertos:",lista_jugador[i][5])
    print ("El Jugador con mejor puntaje es: ",lista_jugador[0][0])

def partida_multiplayer(jugador, lista_palabra_a_adivinar, lista_palabra_oculta, aciertos, desaciertos, \
                        letras_erroneas, ganaste, abandono, lista_letras_error, puntaje):
    """
    Descripcion: Funcion de partida adaptada para multijugadores, se invocan las funciones de escenario y palabras candidatas y se 
    itera a traves de ellas
    Autor: Facundo Arce
    """
    configuracion_remota = parametros_configuracion()
    dicc_parametros = validacion_configuracion(configuracion_remota)
    NUMERO_MAX_ERRORES = dicc_parametros['NUMERO_MAX_ERRORES']
    PUNTOS_ACIERTOS = dicc_parametros['PUNTOS_ACIERTOS']
    PUNTOS_DESACIERTOS = dicc_parametros['PUNTOS_DESACIERTOS']
    cambio=True
    while cambio == True and not ganaste and desaciertos < int(NUMERO_MAX_ERRORES):
        letra, abandono = ingreso(abandono)
        if not abandono:
            lista_palabra_oculta, cambio = busco_letra(lista_palabra_oculta, lista_palabra_a_adivinar, letra, cambio)
            if not cambio:
                desaciertos += 1
                puntaje -= int(PUNTOS_DESACIERTOS)
                lista_letras_error, letras_erroneas = cargar_letras_erroneas(letra, lista_letras_error, letras_erroneas)
                mostrar_interfaz_error(lista_palabra_oculta, aciertos, desaciertos, letras_erroneas)
            else:
                aciertos += 1
                puntaje += int(PUNTOS_ACIERTOS)
                mostrar_interfaz_acierto(lista_palabra_oculta, aciertos, desaciertos, letras_erroneas)
            ganaste = condicion_final(lista_palabra_oculta)
        else:
            desaciertos = int(NUMERO_MAX_ERRORES)           
    return jugador, lista_palabra_a_adivinar, lista_palabra_oculta, aciertos, desaciertos, \
                        letras_erroneas, ganaste, abandono, lista_letras_error, puntaje

def seguir_jugando(letra, abandono):
    """
    Función: seguir_jugando(letra,abandono)
    Descripción: Función de abandono concatenada con la variable de juego perdido (ganaste = False), la
    cual simplemente se refiere a que si el usuario ingresa "FIN" o "0", el juego se da por perdido junto con
    un mensaje por pantalla que diga: "perdiste" junto con sus puntos acumulados
    Autores: Facundo Arce, Mirko Pescio
    Funcion de la parte 1
    """
    if letra == "fin" or letra == "0":
        abandono = True
    return abandono

def validacion_final(jugar):
    """"
    Función: validacion_final(jugar)
    Descripción: Según el ingreso del caracter del usuario, si éste ingresa "n", Termina de jugar y por ende
    se muestra por pantalla sus puntos acumulados hasta su último juego.
    Si el usuario ingresa "s", sigue jugando y acumula sus puntos de los juegos anteriores
    Estos ingresos se cumplen como condición de un ciclo while en el cual si el usuario ingresa un caracter distinto
    de "s" o "n", se le pedirá nuevamente si quiere seguir jugando
    Autores: Facundo Arce, Mirko Pescio, Tomas Barragan, Joaquin Dopazo, Franco Scola, Raul Gonzalez
    Funcion de la parte 1
    """
    validacion = input("Desea seguir jugando? s/n: ")
    validacion = validacion.lower()
    while validacion != "n" and validacion != "s":
        validacion = input("Por favor ingrese 's' o 'n': ")
        validacion.lower()
    if validacion == "n":
        jugar = False
    elif validacion == "s":
        jugar = True
    return jugar

# <-- Bloque archivo configuracion externa -->

def parametros_configuracion():
    """
    Descripcion: Funcion que lee el archivo de configuracion externa, lo formatea y guarda los datos en un diccionario para luego ser validado
    Autor:Raul Gonzalez
    """
    configuracion_remota = {}
    if os.path.isfile("configuracion.csv"):
        with open("configuracion.csv") as configuracion_externa:
            for clave in configuracion_externa:
                variable,valor = clave.rstrip("\n").split(",")
                configuracion_remota[variable] = valor
    return configuracion_remota

def validacion_configuracion(configuracion_remota):
    """
    Descripcion: Funcion que valida el diccionario generado a partir del archivo de configuracion externa, verifica que la integracion de los datos
    comparandolo con un diccionario de variables por default. Dependiendo de su conformacion, se genera un diccionario final asegurandose que los 
    archivos de configuracion necesarios siempre esten presentes.
    Autor:Raul Gonzalez
    """
    variables_local = {'MAX_USUARIOS': '5','PALABRA_MAS_CORTA': '5 ', 'NUMERO_MAX_ERRORES': '8 ', 'PUNTOS_ACIERTOS': '2 ', \
         'PUNTOS_DESACIERTOS': '1', 'PUNTOS_ADIVINA_PALABRA': '10', 'PUNTOS_RESTA_GANA_PROGRAMA': '5'}
    dicc_parametros = {}
    if len(configuracion_remota.keys()) != 7:
        for clave,valor in variables_local.items():
            if clave not in configuracion_remota:
                configuracion_remota[clave] = valor
                dicc_parametros = configuracion_remota
    else:
        dicc_parametros = variables_local
    return dicc_parametros

def impresion_parametros(dicc_parametros):
    """
    Descripcion: Es una funcion auxiliar en el cual recorro el diccionario de parametros y lo formateo en columnas para mostrarlo
    en la carga del juego a modo de informacion.
    Autor:Raul Gonzalez
    """
    for clave, valor in dicc_parametros.items():
        print(clave, ' : ', valor)

# <-- Bloque crear el archivo de palabras.csv -->
def palabra_menor(palabra_1, palabra_2, palabra_3):
    """
    Descripcion: Crea una lista de tres palabras, que se ordena de menor a mayor por orden alfabetico, y luego devuelve la primer palabra de la lista
    Autor:Joaquin Dopazo
    """
    lista_palabras = [palabra_1, palabra_2, palabra_3]
    lista_palabras.sort()
    return(lista_palabras[0])

def leer_3_listas(lista_1, lista_2, lista_3):
    """
    Descripcion: Recibe tres listas ordenadas y abre un archivo palabras.csv de esas lista con la funciuon palabra
    menor encuentra una palabra para para contrastar. Luego recorre en paralelo las listas buscando si
    la palabra contrastada esta incluida y la cantidad de veces que aparece. En el archivo abierto escribe
    la palabra que se contrasto y la cantidad de veces que aparecio en las listas. Una vez que alcanza el
    final de la listas cierra y devuelve el archivo
    Autor:Joaquin Dopazo
    """
    contador_1 = contador_2 = contador_3 = 0
    pos_1 = pos_2 = pos_3 = 0
    fin_lista_1 = fin_lista_2 = fin_lista_3 = fin_todas_las_listas = False
    
    palabra_1 = lista_1[pos_1]
    palabra_2 = lista_2[pos_2]
    palabra_3 = lista_3[pos_3]
    palabras = open("palabras.csv","w")
    
    palabra_contrastada = palabra_menor(palabra_1, palabra_2, palabra_3)
    
    while not fin_todas_las_listas:
        
        
        while palabra_1 == palabra_contrastada and not fin_lista_1:
            contador_1 += 1
            if pos_1 < (len(lista_1)-1):
                pos_1 += 1
                palabra_1 = lista_1[pos_1]
            else:
                fin_lista_1 = True
                palabra_1 = "¿"
                
        while palabra_2 == palabra_contrastada and not fin_lista_2:
            contador_2 += 1
            if pos_2 < (len(lista_2)-1):
                pos_2 += 1
                palabra_2 = lista_2[pos_2]
            else:
                fin_lista_2 = True
                palabra_2 = "¿"
                
        while palabra_3 == palabra_contrastada and not fin_lista_3:
            contador_3 += 1
            if pos_3 < (len(lista_3)-1):
                pos_3 += 1
                palabra_3 = lista_3[pos_3]
            else:
                fin_lista_3 = True
                palabra_3 = "¿"
            
            
        if not fin_todas_las_listas:
            palabra_aux = palabra_contrastada
            palabra_nueva = palabra_menor(palabra_1, palabra_2, palabra_3)
            if palabra_nueva != palabra_aux:
                palabras.write(f"{palabra_contrastada},{contador_1},{contador_2},{contador_3}\n")
                palabra_contrastada = palabra_nueva
                contador_1 = contador_2 = contador_3 = 0
        
        if fin_lista_1 and fin_lista_2 and fin_lista_3:
            fin_todas_las_listas = True
    
    palabras.close()       
    return(palabras)

# <-- Bloque Main -->

def main():
    """
    Funcion: main
    Descripcion: Funcion de invocacion de las funciones que conforman la estructura del juego. Ejecuta en un while
    la funcion de Jugar pasandole todos los parametros que lo conforman. Al final invoca la funcion que valida si el
    usuario desea seguir jugando y muestra por pantalla el puntaje final.
    Autores: Facundo Arce, Mirko Pescio, Tomas Barragan, Joaquin Dopazo, Raul Gonzalez, Franco Scola
    """
    bienvenida()
    lista_1 = procesando_palabras_cuento()
    lista_2 = procesando_palabras_la_araña_negra()
    lista_3 = procesando_palabras_mil_y_una_noches()
    palabras = leer_3_listas(lista_1, lista_2, lista_3)
    jugar = True
    configuracion_remota = parametros_configuracion()
    dicc_parametros = validacion_configuracion(configuracion_remota)
    impresion_parametros(dicc_parametros)
    print('\n')
    lista_jugador = generar_jugadores()
    lista_jugador = ordenar_lista(lista_jugador)
    PUNTOS_ADIVINA_PALABRA = dicc_parametros['PUNTOS_ADIVINA_PALABRA']
    while jugar:
        nueva_partida = True
        todos_perdieron = alguien_gano = False
        cant_jugadores = len(lista_jugador) - 1
        perdedores = 0
        while todos_perdieron == False and alguien_gano == False:
            contador=0
            while contador <= cant_jugadores and alguien_gano == False:
                if nueva_partida and contador == 0:
                    longitud = longitud_multiplayer()
                    diccionario_ordenado,palabra_a_adivinar,longitud = generar_diccionario_multiplayer(longitud)
                    lista_jugador = iniciar_variables_multiplayer(lista_jugador,palabra_a_adivinar,contador)
                    mostrar_interfaz(lista_jugador[contador][3], lista_jugador[contador][4], lista_jugador[contador][5],lista_jugador[contador][0])
                elif nueva_partida == True:
                    palabra_a_adivinar = palabra_candidata(diccionario_ordenado)
                    lista_jugador = iniciar_variables_multiplayer(lista_jugador,palabra_a_adivinar,contador)
                    mostrar_interfaz(lista_jugador[contador][3], lista_jugador[contador][4], lista_jugador[contador][5],lista_jugador[contador][0])
                else:
                    mostrar_interfaz_iniciada(lista_jugador[contador][3], lista_jugador[contador][4], lista_jugador[contador][5], lista_jugador[contador][6], lista_jugador[contador][0])    
                lista_jugador[contador][0], lista_jugador[contador][2], lista_jugador[contador][3], \
                lista_jugador[contador][4], lista_jugador[contador][5], lista_jugador[contador][6], \
                lista_jugador[contador][7], lista_jugador[contador][8], lista_jugador[contador][9], \
                lista_jugador[contador][10] = partida_multiplayer(lista_jugador[contador][0],\
                lista_jugador[contador][2], lista_jugador[contador][3], lista_jugador[contador][4], \
                lista_jugador[contador][5], lista_jugador[contador][6], lista_jugador[contador][7], \
                lista_jugador[contador][8], lista_jugador[contador][9], lista_jugador[contador][10])
                if lista_jugador[contador][7] == True:
                    alguien_gano = True
                    lista_jugador[contador][10] += int(PUNTOS_ADIVINA_PALABRA)
                perdedores,lista_jugador[contador][11] = verifico_perdedor(lista_jugador[contador][5],perdedores,lista_jugador[contador][11])
                if contador == len(lista_jugador) - 1:
                    nueva_partida = False
                contador += 1
            if perdedores == cant_jugadores + 1:
                todos_perdieron = True
                lista_jugador = gano_la_maquina(lista_jugador)
            if not alguien_gano:
                cant_jugadores = jugadores_participando(cant_jugadores,perdedores)            
                lista_jugador = quitar_perdedores(lista_jugador)               
        lista_jugador = guardar_puntajes_generales(lista_jugador)
        mostrar_resultados(lista_jugador)
        lista_jugador = ordenar_lista(lista_jugador)
        lista_jugador = limpiar_lista(lista_jugador)
        jugar = validacion_final(jugar)
main()