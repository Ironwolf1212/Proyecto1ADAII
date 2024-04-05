import copy
from openInput import costoRiego, formatInput

def ordenOptimo(finca):
    '''
    Encuentra el orden óptimo de plantaciones en una finca, utilizando un algoritmo voraz.
    Siguiendo una subestructura óptima basada en CRF = CRF<t1, t2, ..., tn-1> + CRF<tn>
    Es decir, se calcula el costo de regar cada plantación de ultima, utilizando la función riegoOptimo
    Se selecciona la plantación que minimice el costo y se agrega al orden óptimo y se va "eliminando" de la finca.

    Parameters:
        finca (list): Una lista de plantaciones.

    Returns:
        tuple: Una tupla con la permutación óptima y el costo de la misma.
    '''
    costoTotal = 0 #Inicializa el costo total en 0
    orden = [] #Inicializa la lista de orden en vacío
    fincaBackup = copy.copy(finca)

    #Mientras haya plantaciones en la finca
    while len(finca) > 0:
        #Se calcula el costo de regar cada plantación de ultima
        costo, index = riegoOptimo(finca) 

        #Se agrega la plantación que minimice el costo al principio de la lista de orden
        orden.insert(0, finca[index]) 

        #Se actualiza el costo total
        costoTotal += costo

        #Se elimina de la finca a la plantación que se ha añadido al orden
        finca.pop(index) 
    print(orden)
    
    orden = devolverIndices(orden, fincaBackup)
    return orden, costoTotal

def riegoOptimo(subarreglo):
    '''
    Encuentra la plantación que al regarla de ultima minimice el costo de riego en un subarreglo de plantaciones.

    Parameters:
        subarreglo (list): Una lista de plantaciones.

    Returns:
        tuple: Una tupla con el costo de riego de la plantación que minimiza el costo y su índice en el subarreglo.
    '''
    #Se calcula el tiempo actual de riego sumando los tiempos de riego de todas las plantaciones en el subarreglo
    #De esta manera se deduce que al regar una plantación de ultima, ya se han regado todas las plantaciones anteriores
    tiempoActual = sum([int(plantacion.tiempoRiego) for plantacion in subarreglo])

    costoST = 0
    temp = []

    for i in range(len(subarreglo)):
        #Se calcula el costo de regar de ultima cada plantación, utilizando la función costoRiego
        #Se logra esto restando el tiempo actual de riego menos el tiempo de riego de la plantación que se esta evaluando
        costoST = costoRiego(subarreglo[i], tiempoActual - int(subarreglo[i].tiempoRiego))

        #Se agrega el costo al arreglo temporal
        temp.append(costoST)

    #Se obtiene el costo mínimo y su índice en el arreglo temporal    
    elemento = min(temp)
    indiceElemento = temp.index(elemento)
    
    return elemento, indiceElemento

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
orden, costo = ordenOptimo(copy.deepcopy(finca))
print("Orden optimo:", orden, "Costo optimo:", costo)


