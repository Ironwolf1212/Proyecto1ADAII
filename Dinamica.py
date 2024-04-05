from openInput import formatInput, costoRiego

def calcularCostoOptimoPD(finca, tablones, vectorCostos):

    # Condicion de parada
    if len(tablones) == 0:
        return vectorCostos[0]
    
    # Convertir el subproblema en un número binario para indexar el vector de costos
    codSubproblema = '0'*len(finca)
    for idTablon in tablones:
        codSubproblema = codSubproblema[:idTablon-1] + '1' + codSubproblema[idTablon:]
    
    number = int(codSubproblema, 2)

    if vectorCostos[number] != float('inf'):
        return vectorCostos[number]

    ### En caso de que no exista el costo óptimo para el subproblema, se calcula
    # Se crea una lista con todas las posibles opciones de tablones para retirar
    listaSubproblemas = []
    for idTablon in tablones:
        tablonesCopy = tablones.copy()
        tablonesCopy.remove(idTablon)

        tiempoTranscurrido = sum([int(finca[idTablon-1].tiempoRiego) for idTablon in tablonesCopy])

        listaSubproblemas.append((tablonesCopy, idTablon, tiempoTranscurrido))

    # Se calcula el costo óptimo para el subproblema
    costoOptimo = min([calcularCostoOptimoPD(finca, tablonesCopy, vectorCostos) + costoRiego(finca[idTablon-1], tiempoTranscurrido) for tablonesCopy, idTablon, tiempoTranscurrido in listaSubproblemas])
    vectorCostos[number] = costoOptimo # Se guarda el costo óptimo en el vector de costos

    return costoOptimo


def calcularOrdenOptimoPD(finca, idsTablones, vectorCostos):

    ordenOptimo = [0] * len(finca)

    costoOptimoActual = vectorCostos[-1]
    for i in range(len(finca) - 1, -1, -1):
        # print("Costo optimo actual:", costoOptimoActual)

        # Se consiguen todos los subproblemas posibles para este punto
        listaSubproblemas = []
        for idTablon in idsTablones:
            tablonesCopy = idsTablones.copy()
            tablonesCopy.remove(idTablon)

            listaSubproblemas.append((tablonesCopy, idTablon, costoRiego(finca[idTablon-1], sum([int(finca[id-1].tiempoRiego) for id in tablonesCopy])))  )

        codigosSubproblemas = []
        for tablonesCopy, a, b in listaSubproblemas:
            codSubproblema = '0'*len(finca)
            for idTablon in tablonesCopy:
                codSubproblema = codSubproblema[:idTablon-1] + '1' + codSubproblema[idTablon:]
            codigosSubproblemas.append(int(codSubproblema, 2))
        
        subproblemaOptimo = None
        for i, subproblema in enumerate(listaSubproblemas):
            # print(vectorCostos[codigosSubproblemas[i]] + subproblema[2])
            if vectorCostos[codigosSubproblemas[i]] + subproblema[2] == costoOptimoActual:
                subproblemaOptimo = i

        ordenOptimo[i] = listaSubproblemas[subproblemaOptimo][1] - 1
        idsTablones = listaSubproblemas[subproblemaOptimo][0]
        costoOptimoActual = vectorCostos[codigosSubproblemas[subproblemaOptimo]]

    return ordenOptimo

def ordenOptimoPD(finca):

    idsTablones = { i+1 for i in range(len(finca)) }
    vectorCostos = [float('inf')] * 2**len(finca)
    vectorCostos[0] = 0

    costoOptimo = calcularCostoOptimoPD(finca, idsTablones, vectorCostos)
    ordenOptimo = calcularOrdenOptimoPD(finca, idsTablones.copy(), vectorCostos)

    return ordenOptimo, costoOptimo



if __name__ == '__main__':
    finca = formatInput('BateriaPruebas/Prueba5.txt')
    ordenOptimo, costoOptimo = ordenOptimoPD(finca)

    print("Orden óptimo:", ordenOptimo, "Costo óptimo:", costoOptimo)

    def calcularCostoOrden(plantaciones, orden):
        # print(orden)
        # print(plantaciones)
        tiempoTranscurrido = 0
        costoTotal = 0
        for i in range(len(orden)):
            costoTotal += int(costoRiego(plantaciones[orden[i]], tiempoTranscurrido))
            # print(costoTotal)
            tiempoTranscurrido += int(plantaciones[orden[i]].tiempoRiego)
        return costoTotal

