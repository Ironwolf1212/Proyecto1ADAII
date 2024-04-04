import copy
from openInput import costoRiego, formatInput

def ordenOptimo(finca):
    #aplicar la funcion riegoOptimo a la finca, en cada iteracion se elimina el elemento que se retorna en riegoOptimo
    costoTotal = 0
    orden = []
    while len(finca) > 0:
        costo, index = riegoOptimo(finca)
        orden.append(finca[index])
        costoTotal += costo
        finca.pop(index)
    return orden, costoTotal

def riegoOptimo(subarreglo):
    tiempoActual = sum([int(plantacion.tiempoRiego) for plantacion in subarreglo])
    costoST = 0
    temp = []
    for i in range(len(subarreglo)):
        costoST = costoRiego(subarreglo[i], tiempoActual - int(subarreglo[i].tiempoRiego))
        temp.append(costoST)
    elemento = min(temp)
    indiceElemento = temp.index(elemento)
    return elemento, indiceElemento

finca = formatInput('BateriaPruebas/Prueba5.txt')
costo, orden = ordenOptimo(copy.deepcopy(finca))
