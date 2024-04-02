def calcular_costo_riego(finca, permutacion):
    costo_total = 0
    tiempo_inicio_riego = 0
    for i in permutacion:
        tablon_actual = finca[i]
        tiempo_inicio_riego = max(tiempo_inicio_riego, tablon_actual.tiempoRiego)
        if tablon_actual.tiempoSuperv - tablon_actual.tiempoRiego >= tiempo_inicio_riego:
            costo_total += tablon_actual.tiempoSuperv - (tiempo_inicio_riego + tablon_actual.tiempoRiego)
        else:
            costo_total += tablon_actual.pFi * ((tiempo_inicio_riego + tablon_actual.tiempoRiego) - tablon_actual.tiempoSuperv)
        tiempo_inicio_riego += tablon_actual.tiempoRiego
    return costo_total

def calcular_riego_optimo(finca):
    mejor_permutacion = []
    mejor_costo = float('inf')
    n = len(finca)
    
    # Generar todas las permutaciones de los tablones
    def backtrack(permutacion_actual):
        nonlocal mejor_permutacion, mejor_costo
        if len(permutacion_actual) == n:
            costo_actual = calcular_costo_riego(finca, permutacion_actual)
            if costo_actual < mejor_costo:
                mejor_costo = costo_actual
                mejor_permutacion = permutacion_actual[:]
        else:
            for i in range(n):
                if i not in permutacion_actual:
                    permutacion_actual.append(i)
                    backtrack(permutacion_actual)
                    permutacion_actual.pop()
    
    backtrack([])
    return mejor_permutacion

def verificar_solucion_optima(finca, permutacion):
    costo_fuerza_bruta = calcular_costo_riego(finca, permutacion)
    # Calcular y comparar con la solución óptima conocida (si está disponible)
    # Solución óptima conocida
    # solucion_optima_conocida = ...
    # costo_optimo_conocido = calcular_costo_riego(finca, solucion_optima_conocida)
    # Comparar
    # if costo_fuerza_bruta == costo_optimo_conocido:
    #     print("La solución producida por fuerza bruta es óptima.")
    # else:
    #     print("La solución producida por fuerza bruta NO es óptima.")
    print("Costo total de riego con fuerza bruta:", costo_fuerza_bruta)

# Ejemplo de uso
# finca_ejemplo = [Tablon(8, 2, 3), Tablon(12, 4, 1), Tablon(10, 3, 2)]
# programacion_riego_optima = calcular_riego_optimo(finca_ejemplo)
# print("Programación de riego óptima:", programacion_riego_optima)
# verificar_solucion_optima(finca_ejemplo, programacion_riego_optima)