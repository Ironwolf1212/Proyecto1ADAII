from itertools import permutations
from openInput import formatInput, costoRiego

def costoPermutacion(orden):
    tiempo_transcurrido = 0
    costo_total = 0
    for i in range(len(orden)):
        costo_total += int(costoRiego(orden[i], tiempo_transcurrido))
        tiempo_transcurrido += int(orden[i].tiempoRiego)
    return costo_total

def ordenOptimoFB(finca):
    permutaciones = permutations(finca)
    mejor_permutacion = None
    mejor_costo = float('inf')

    for permutacion in permutaciones:
        costo = costoPermutacion(permutacion)
        if costo < mejor_costo:
            mejor_permutacion = permutacion
            mejor_costo = costo
    return mejor_permutacion, mejor_costo
       
finca = formatInput('BateriaPruebas/Prueba1.txt')
ordenOptimo, costoOptimo = ordenOptimoFB(finca)

print("Orden óptimo:", ordenOptimo, "Costo óptimo:", costoOptimo)
