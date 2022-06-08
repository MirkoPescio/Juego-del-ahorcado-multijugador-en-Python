#Palabras candidatas

def obtener_texto():
    from texto import obtener_texto
    texto_a_procesar = obtener_texto()
    return texto_a_procesar

def palabras_candidatas_a_obtener():
    texto = str(obtener_texto)
    texto.lower()
    palabras_candidatas = []
    for palabras in obtener_texto():
        for caracteres in palabras:
            if len(caracteres)>=5:
                palabras_candidatas.append(palabras)
    return palabras_candidatas

print(palabras_candidatas_a_obtener())