import copy

def costoRiego(plantacion, tiempo_transcurrido):
    """
    Calcula el costo de riego de una plantacion en funcion del tiempo transcurrido.

    Args:
        plantacion (tuple): Una tupla que contiene informacion sobre la plantacion.
            - tiempo_supervivencia (int): Tiempo maximo de supervivencia de la plantacion sin riego.
            - tiempo_regado (int): Tiempo necesario para regar la plantacion.
            - prioridad (int): Prioridad de la plantacion.
        tiempo_transcurrido (int): Tiempo transcurrido desde el inicio.

    Returns:
        int: El costo de riego de la plantacion.

    """
    tiempo_supervivencia = plantacion.tiempoSuperv
    tiempo_regado = plantacion.tiempoRiego
    prioridad = plantacion.prioridad
    if int(tiempo_transcurrido) + int(tiempo_regado) <= int(tiempo_supervivencia):
        return int(tiempo_supervivencia) - (int(tiempo_transcurrido) + int(tiempo_regado))
    else:
        return int(prioridad) * ((int(tiempo_transcurrido) + int(tiempo_regado)) - int(tiempo_supervivencia))

def costoMinimo(plantaciones):
    n = len(plantaciones)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        tiempoTranscurrido = 0
        for j in range(i):
            #tiempoTranscurrido += int(plantaciones[j - 1].tiempoSuperv)
            tiempoTranscurrido = sum(int(planta.tiempoSuperv) for planta in plantaciones[j:i])
            #costo = costoRiego(plantaciones[j - 1], tiempoTranscurrido)
            costo = sum(costoRiego(planta, tiempoTranscurrido) for planta in plantaciones[j:i])
            print("El costoo ",j," es ", costo)
            print("Comparando ",dp[i]," con ",dp[j-1] + costo)
            dp[i] = min(dp[i], dp[j] + costo)
        print("El costo ",i," es ",dp[i])

    return dp[n]

def ordenOptimo(plantaciones):
    print("Entrada: ",plantaciones)
    plantaciones2 = [0] * len(plantaciones)
    orden = copy.copy(plantaciones)
    menorCosto = float('inf')
    for i in range(len(plantaciones)):
        for plantacion in plantaciones:
            plantacionesBackup = copy.copy(plantaciones)
            print("Backup: ",plantacionesBackup)
            tiempoAcumulado = 0
            plantacionesBackup.remove(plantacion)
        ##Intentar reemplazar con Sum()
            for otraPlantacion in plantacionesBackup:
                tiempoAcumulado += int(otraPlantacion.tiempoRiego)
            #menorCosto = min(menorCosto,costoRiego(plantacion,tiempoAcumulado))
            if costoRiego(plantacion,tiempoAcumulado) < menorCosto:
                plantaEscogida = plantacion
                menorCosto = costoRiego(plantacion,tiempoAcumulado)
        
        orden.insert(0,plantaEscogida)
        print("Quitando: ", orden[0], " de ", plantaciones)
        plantaciones.remove(orden[0])
        plantaEscogida = None
        menorCosto = float('inf')
    return orden
        ##Calcular el costo en ese tiempo acumulado, escoger el de menor costo, hacer recursión con los demás.
'''
# Ejemplo de uso
plantaciones = [
    (10, 3, 4),
    (5, 3, 3),
    (2, 2, 1),
    (8, 1, 1),
    (6, 4, 2)
]

resultado = costoMinimo(plantaciones)
print("El costo minimo de regar todas las plantaciones es:", resultado)
'''