def costo_riego(plantacion, tiempo_elapsado):
    tiempo_supervivencia, tiempo_regado, prioridad = plantacion
    if tiempo_elapsado + tiempo_regado <= tiempo_supervivencia:
        return tiempo_supervivencia - (tiempo_elapsado + tiempo_regado)
    else:
        return prioridad * ((tiempo_elapsado + tiempo_regado) - tiempo_supervivencia)

def orden_optimo(plantaciones):
    tiempo_elapsado = 0
    orden = []
    while plantaciones:
        mejor_costo = float('inf')
        mejor_plantacion = None
        for plantacion in plantaciones:
            costo = costo_riego(plantacion, tiempo_elapsado)
            if costo < mejor_costo:
                mejor_costo = costo
                mejor_plantacion = plantacion
        orden.append(mejor_plantacion)
        plantaciones.remove(mejor_plantacion)
        tiempo_elapsado += mejor_plantacion[1]
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