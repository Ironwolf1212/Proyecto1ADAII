from openInput import formatInput

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
        return int(prioridad) * ((int(tiempo_transcurrido) + int(tiempo_regado)) - int(tiempo_supervivencia))
    
def ordenOptimoDinamica(finca):
    #Arreglo para almacenar los costos de las soluciones a los subproblemas
    costos = []

    #Crear los costos de los casos bases (regar cada elemento de la finca en tiempo = 0) 
    for i in range(len(finca)):
        costos.append(costoRiego(finca[i], 0))
    
    #Crear los costos de los casos recursivos
    for i in range(len(costos)):
        temp = []


finca = formatInput('BateriaPruebas/Prueba10.txt')
ordenOptimo = ordenOptimoDinamica(finca)
print("Orden óptimo:", ordenOptimo)
