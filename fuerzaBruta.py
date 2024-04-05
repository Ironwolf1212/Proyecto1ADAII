from itertools import permutations
from openInput import formatInput, costoRiego

def costoPermutacion(orden):
    '''
    Calcula el costo total de una permutación de plantaciones.

    Parameters:
        orden (list): Una lista que representa el orden de las plantaciones.
        
    Returns:
        int: El costo total de la permutación de plantaciones.
    '''
    tiempo_transcurrido = 0
    costo_total = 0
    for i in range(len(orden)):
        #Se suma el costo de riego de la plantación actual al costo total, aplicando la funcion costoRiego
        costo_total += int(costoRiego(orden[i], tiempo_transcurrido))
        #Se actualiza el tiempo transcurrido
        tiempo_transcurrido += int(orden[i].tiempoRiego)
    return costo_total

def ordenOptimoFB(finca):
    '''
    Encuentra el orden óptimo de plantaciones en una finca, utilizando fuerza bruta.
    Es decir, generando todas las permutaciones posibles de las plantaciones de una finca
    Se calcula el costo de cada una de las permutaciones y se retorna la permutación con el menor costo.

    Parameters:
        finca (list): Una lista de plantaciones.

    Returns:
        tuple: Una tupla con la permutación óptima y el costo de la misma.
    '''

    #Se utiliza la función permutations de la librería itertools para generar todas las permutaciones posibles
    permutaciones = permutations(finca)
    mejor_permutacion = None #Se inicializa la mejor permutación
    mejor_costo = float('inf') #Se inicializa el mejor costo con infinito

    #Se recorren todas las permutaciones y se calcula el costo de cada una utilizando la función costoPermutacion
    for permutacion in permutaciones:
        costo = costoPermutacion(permutacion)
        #Si el costo de la permutación actual es menor al mejor costo encontrado hasta el momento, 
        #se actualiza el mejor costo y la mejor permutación
        if costo < mejor_costo:
            mejor_permutacion = permutacion
            mejor_costo = costo
    mejor_permutacion=devolverIndices(mejor_permutacion,finca)
    return mejor_permutacion, mejor_costo
       
def devolverIndices(plantacionesResultado, finca):
    print(plantacionesResultado)
    orden = [0] * len(finca)
    for i in range(len(plantacionesResultado)):
        for plantacion in finca:
            if str(plantacion) == str(plantacionesResultado[i]):
                orden[i] = finca.index(plantacion)
    return orden

'''
PRUEBAS
'''
finca = formatInput('BateriaPruebas/Prueba1.txt')
ordenOptimo, costoOptimo = ordenOptimoFB(finca)
print("Orden óptimo:", ordenOptimo, "Costo óptimo:", costoOptimo)