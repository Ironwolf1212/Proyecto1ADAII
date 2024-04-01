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
        for j in range(1, i+1):
            tiempoTranscurrido += int(plantaciones[j - 1].tiempoSuperv)
            costo = costoRiego(plantaciones[j - 1], tiempoTranscurrido)
            print("El costoo ",j," es ", costo)
            print("Comparando ",dp[i]," con ",dp[j-1] + costo)
            dp[i] = min(dp[i], dp[j - 1] + costo)
        print("El costo ",i," es ",dp[i])

    return dp[n]
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