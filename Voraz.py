import copy
def costoRiego(plantacion, tiempo_transcurrido):
    """
    Calcula el costo de riego de una plantación en función del tiempo transcurrido.

    Args:
        plantacion (tuple): Una tupla que contiene información sobre la plantación.
            - tiempo_supervivencia (int): Tiempo máximo de supervivencia de la plantación sin riego.
            - tiempo_regado (int): Tiempo necesario para regar la plantación.
            - prioridad (int): Prioridad de la plantación.
        tiempo_transcurrido (int): Tiempo transcurrido desde el inicio.

    Returns:
        int: El costo de riego de la plantación.

    """
    tiempo_supervivencia = plantacion.tiempoSuperv
    tiempo_regado = plantacion.tiempoRiego
    prioridad = plantacion.prioridad
    if int(tiempo_transcurrido) + int(tiempo_regado) <= int(tiempo_supervivencia):
        return int(tiempo_supervivencia) - (int(tiempo_transcurrido) + int(tiempo_regado))
    else:
        return prioridad * ((int(tiempo_transcurrido) + int(tiempo_regado)) - int(tiempo_supervivencia))


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
    ordenFinal = [0]*len(orden)
    for i in range(len(orden)):
        #print("El elemento ",i," es: ",orden[i])
        #print("El elemento de backup ",i," es: ",orden[i])
        
        print("insertaré ", plantacionesBackup.index(orden[i]), "En backup",i)
        ordenFinal[i] = plantacionesBackup.index(orden[i])
    print("El orden final es: ", ordenFinal)
    return ordenFinal

# Ejemplo de uso
'''
plantaciones = [
    (10, 3, 4),
    (5, 3, 3),
    (2, 2, 1),
    (8, 1, 1),
    (6, 4, 2)
]

orden = orden_optimo(plantaciones)
print("Orden optimo de riego:")
for plantacion in orden:
    print(plantacion)
'''