def costo_riego(plantacion, tiempo_transcurrido):
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
    tiempo_supervivencia, tiempo_regado, prioridad = plantacion
    if tiempo_transcurrido + tiempo_regado <= tiempo_supervivencia:
        return tiempo_supervivencia - (tiempo_transcurrido + tiempo_regado)
    else:
        return prioridad * ((tiempo_transcurrido + tiempo_regado) - tiempo_supervivencia)


def orden_optimo(plantaciones):
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
    while plantaciones:
        mejor_costo = float('inf')
        mejor_plantacion = None
        for plantacion in plantaciones:
            costo = costo_riego(plantacion, tiempo_transcurrido)
            if costo < mejor_costo:
                mejor_costo = costo
                mejor_plantacion = plantacion
        orden.append(mejor_plantacion)
        plantaciones.remove(mejor_plantacion)
        tiempo_transcurrido += mejor_plantacion[1]
    return orden

# Ejemplo de uso
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