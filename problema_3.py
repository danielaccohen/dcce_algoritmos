coordenada=input("Indique la coordenada: ")

def convertir_a_dms(coordenada):
    #Paso 1: Obtener el grado
    coordenada = coordenada.split(".")
    print(coordenada)
    grado=int(coordenada[0])
    #Paso 2: Obtener el minuto
    minuto_decimal=(coordenada-grado)*60
    minuto=int(minuto_decimal)
    #Paso 3: Obtener el segundo
    segundo_decimal=(minuto_decimal-minuto)*60
    segundo=round(segundo_decimal,2)
    return grado,minuto,segundo
grado, minuto, segundo = convertir_a_dms(coordenada)

print(f"{str(grado)}°{str(minuto)}{str(segundo)}")
#Al intentar correrlo me indica que hay un error en la línea 5, no se porque no corre.
                                                                                                                                                                                                                   