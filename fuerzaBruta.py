from itertools import permutations
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

def costoPermutacion(orden):
    tiempo_transcurrido = 0
    costo_total = 0
    for i in range(len(orden)):
        costo_total += int(costoRiego(orden[i], tiempo_transcurrido))
        tiempo_transcurrido += int(orden[i].tiempoRiego)
    return costo_total

def ordenOptimoFB(finca):
    permutaciones = permutations(finca)
    costos = []
    mejor_permutacion = None
    mejor_costo = float('inf')

    for permutacion in permutaciones:
        costo = costoPermutacion(permutacion)
        costos.append(costo)
        if costo < mejor_costo:
            mejor_permutacion = permutacion
            mejor_costo = costo
    return mejor_permutacion, mejor_costo, permutaciones, costos
       
finca = formatInput('BateriaPruebas/Prueba30.txt')
ordenOptimo, costoOptimo, permutaciones, costos = ordenOptimoFB(finca)

print("Orden óptimo:", ordenOptimo, "Costo óptimo:", costoOptimo)
