def costo_riego_tablon(ts, tr, p, t):
    """
    Calcula el costo de riego de un tablón en un tiempo dado.

    Parameters:
        ts (int): Tiempo de supervivencia del tablón.
        tr (int): Tiempo de riego del tablón.
        p (int): Prioridad del tablón.
        t (int): Tiempo transcurrido desde el inicio.

    Returns:
        int: El costo de riego del tablón.

    """
    if ts - tr >= t:
        return ts - (t + tr)
    else:
        return p * (t + tr - ts)

def programacionOptima(finca):
    n = len(finca)

    crf = [[0] * n for _ in range(n)]
    for i in range(n):
        crf[i][i] = costo_riego_tablon(finca[i][0], finca[i][1], finca[i][2], 0)
    
    print(crf)
    
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            print(l, i, j)
            crf[i][j] = float('inf')
            for k in range(i, j):
                crf_k = crf[i][k] + costo_riego_tablon(finca[k][0], finca[k][1], finca[k][2], crf[k][j]) #Costo de regar primero la plantacion que se esta evaluando
                crf_no_k = crf[i][k] + crf[k+1][j] #Costo de no regar primero la plantacion que se esta evaluando
                crf[i][j] = min(crf[i][j], crf_k, crf_no_k) #Se toma el minimo entre los dos costos
                print(crf)
    
    programacion = []

    def construir_programacion(i, j):
        if i > j:
            return
        elif i == j:
            programacion.append(i)
        else:
            for k in range(i, j):
                if crf[i][j] == crf[i][k] + costo_riego_tablon(finca[k][0], finca[k][1], finca[k][2], crf[k][j]):
                    programacion.append(k)
                    construir_programacion(i, k)
                    construir_programacion(k + 1, j)
                    break

    construir_programacion(0, n - 1)
    return programacion, crf[0][n - 1]

# finca = [(5, 2, 4), (10, 2, 2), (9, 4, 4), (7, 6, 1), (7, 6, 2)]
# programacion, costo_total = programacionOptima(finca)
# print("Programacion optima:", programacion)
# print("Costo total:", costo_total)
