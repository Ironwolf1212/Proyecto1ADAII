import copy
from openInput import costoRiego, formatInput

def ordenOptimo(plantaciones):
    """
    Calcula el orden óptimo de riego de las plantaciones.

    Args:
        plantaciones (list): Una lista de tuplas que contienen información sobre las plantaciones.
            Cada tupla tiene la siguiente estructura:
            - tiempo_supervivencia (int): Tiempo máximo de supervivencia de la plantación sin riego.
            - tiempo_regado (int): Tiempo necesario para regar la plantación.
            - prioridad (int): Prioridad de la plantación.

    Returns:
        list: Una lista con el orden óptimo de riego de las plantaciones.

    """
    tiempo_transcurrido = 0
    orden = []
    plantacionesBackup = copy.copy(plantaciones)
    while plantaciones:
        mejor_costo = float('inf')
        mejor_plantacion = None
        for plantacion in plantaciones:
            costo = costoRiego(plantacion, tiempo_transcurrido)
            if int(costo) < float(mejor_costo):
                mejor_costo = costo
                mejor_plantacion = plantacion
        orden.append(mejor_plantacion)
        plantaciones.remove(mejor_plantacion)
        tiempo_transcurrido += int(mejor_plantacion.tiempoRiego)
    #Se crea un arreglo del mismo tamaño que orden
    ordenFinal = [0]*len(orden)
    #Se itera orden y se almacena el índice de cada elemento dentro de plantacionesBackup y orden en ordenFinal
    for i in range(len(orden)):
        ordenFinal[i] = plantacionesBackup.index(orden[i])
    return ordenFinal

def calcularCostoOrden(plantaciones, orden):
    print(orden)
    print(plantaciones)
    tiempoTranscurrido = 0
    costoTotal = 0
    for i in range(len(orden)):
        costoTotal += int(costoRiego(plantaciones[orden[i]], tiempoTranscurrido))
        print(costoTotal)
        tiempoTranscurrido += int(plantaciones[orden[i]].tiempoRiego)
    return costoTotal

finca = formatInput('BateriaPruebas/Prueba3.txt')
orden = ordenOptimo(copy.copy(finca))
costo = calcularCostoOrden(finca, orden)
print("Orden óptimo:", orden, "Costo óptimo:", costo)