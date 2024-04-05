from openInput import formatInput
import copy

def costoRiego(plantacion, tiempo_transcurrido):
    """
    Calcula el costo de riego de una plantaci�n en funci�n del tiempo transcurrido.

    Args:
        plantacion (tuple): Una tupla que contiene informaci�n sobre la plantaci�n.
            - tiempo_supervivencia (int): Tiempo m�ximo de supervivencia de la plantaci�n sin riego.
            - tiempo_regado (int): Tiempo necesario para regar la plantaci�n.
            - prioridad (int): Prioridad de la plantaci�n.
        tiempo_transcurrido (int): Tiempo transcurrido desde el inicio.

    Returns:
        int: El costo de riego de la plantaci�n.

    """
    tiempo_supervivencia = plantacion.tiempoSuperv
    tiempo_regado = plantacion.tiempoRiego
    prioridad = plantacion.prioridad
    if int(tiempo_transcurrido) + int(tiempo_regado) <= int(tiempo_supervivencia):
        return int(tiempo_supervivencia) - (int(tiempo_transcurrido) + int(tiempo_regado))
    else:
        return int(prioridad) * ((int(tiempo_transcurrido) + int(tiempo_regado)) - int(tiempo_supervivencia))
    
def ordenOptimoDinamica(finca):
    #Arreglo para almacenar los costos de las soluciones a los subproblemas
    secuencias = []
    for i in range(len(finca)):
        secuencias.append([])
    print(secuencias)
    #Crear los costos de los casos bases (regar cada elemento de la finca en tiempo = 0) 
    for plantacion in finca:
        #print("Costo riego: ",costoRiego(plantacion,0))
        secuencias[0].append([[plantacion],plantacion.tiempoRiego,costoRiego(plantacion, 0)])
    indiceSecuencias = 0
    #Crear los costos de los casos recursivos
    #Que no combine las secuencias con su misma longitud sino con secuencias[0]
    for longitud in secuencias:
        #print("Longitud: ", longitud)
        
        ##Calcular los costos para esa longitud
        #Buscar la forma de no combinarse con los elementos que ya combin�... quiz� haciendo uso de las plantaciones que contiene y buscando en secuencias[0]
        longitudBackup = copy.copy(longitud)
        
        for secuenciaOptima in longitudBackup:
            #print("Secuencia optima: ",secuenciaOptima)
            
            ## hallar el costo de poner este de primero y los dem�s de segundo, posteriormente expulsar del arreglo para evitar repetir
            ## probar orden en momento de hallar costo para escoger el minimo
            ## Guardar el tiempo que llevan acumuladas cada secuencia, calcular todas las secuencias de la siguiente longitud en un arreglo temporal y luego meterlas en costo?? no es necesario
            ## Guardar cada longitud de secuencia en un arreglo diferente??? podr�a ser
            ## Guardar las secuencias de cada longitud en una posici�n de un arreglo din�mico.
            plantacionesCombinar = copy.copy(secuencias[0])
            if indiceSecuencias == 10:
                print("Plantaciones combinar: ", plantacionesCombinar)
            for plantaEscogida in secuenciaOptima[0]:
                #print("Planta escogida: ", plantaEscogida, "Secuencia Optima[0]: ",secuenciaOptima[0])
                #print("plantacionesCombinar: ", plantacionesCombinar)
                #print("Secuencias[0]: ", secuencias[0])
                index = 0
                encontrado = False
                for plantacionOptima in plantacionesCombinar:
                    #print("Planta escogida: ", plantaEscogida)
                    #print("Plantacion optima: ", plantacionOptima)
                    #print("Plantaciones combinar: ", plantacionesCombinar)
                    #print("Indice: ", index)
                    if str(plantaEscogida) == str(plantacionOptima[0][0]):
                        #print("Planta escogida: ", plantaEscogida)
                        #print("Plantacion optima: ", plantacionOptima)
                        #print("Plantaciones combinar: ", plantacionesCombinar)
                        #print("Indice: ", index)
                        plantacionesCombinar[index] = None
                        encontrado = True
                        if indiceSecuencias == 10:
                            print("Plantaciones combinar: ", plantacionesCombinar)
                    for plantacion in plantacionesCombinar:
                        if plantacion == None:
                            plantacionesCombinar.pop(plantacionesCombinar.index(plantacion))
                    if encontrado:
                        if indiceSecuencias == 10:
                            print("Plantaciones combinar: ", plantacionesCombinar)
                        break
                    index += 1
            
                #if plantaEscogida in secuencias[0]:
                    
                    #plantacionesCombinar.pop(plantacionesCombinar.index(plantaEscogida))
            #print("plantacionesCombinar: ",plantacionesCombinar)
            #plantacionesCombinar.remove(secuenciaOptima)
            for nuevaPlantacion in plantacionesCombinar:
                #print("Plantaciones a anadir: ",secuenciaOptima,nuevaPlantacion)
                #Si esta combinacion de plantaciones ya está en la secuencia objetivo, saltar el cálculo.
                secuenciaSaltar = copy.deepcopy(secuenciaOptima)
                #print("secuencia a saltar: ",secuenciaSaltar,"Secuencia optima: ", secuenciaOptima)
                secuenciaSaltar[0].append(nuevaPlantacion[0][0])
                secuenciaSaltar[2] += costoRiego(nuevaPlantacion[0][0], secuenciaSaltar[1])
                secuenciaSaltar[1] = int(secuenciaSaltar[1])
                secuenciaSaltar[1] += int(nuevaPlantacion[1])
                #print("secuencia a saltar: ",secuenciaSaltar,"Secuencia optima: ", secuenciaOptima)
                #print("secuencias[",indiceSecuencias+1,"]: ", secuencias[indiceSecuencias+1])
                

                #Está purgando de más, tiene que verificar que la que está es más barata que la que va a entrar? pero si tiene que encontrar match exactos... y las que están
                #Deberían ser óptimas... << sólo se cumple para los de longitud 2 para abajo, al resto se le tienen alternativas menos óptimas de manera temporal
                #Podría cambiar a que haga comparaciones aquí y sólo inserte las que mejoran, no sé qué tan bueno sea, creo que no es bueno... << Foreshadowing sí era bueno
                #A lo mejor estoy haciendo un mal enfoque, en vez de sacar los que tengan las mismas plantaciones, debería sacar...
                #TIENE QUE MIRAR SI HAY UNO EN EL MISMO ORDEN EN EL QUE EL ENTRARIA CLARROOOOOOO FUCK

                seEncontro = False
                for secuenciaOptimaComparar in secuencias[indiceSecuencias+1]:
                    if indiceSecuencias == 0:
                        if secuenciaSaltar[0][0] == secuenciaOptimaComparar[0][0] or secuenciaSaltar[0][0] == secuenciaOptimaComparar[0][1]:
                            if secuenciaSaltar[0][1] == secuenciaOptimaComparar[0][0] or secuenciaSaltar[0][1] == secuenciaOptimaComparar[0][1]:
                                seEncontro = True
                                break
                    
                    plantacionesRepetidas = 0
                    #print("Comparando ",secuenciaSaltar," con ",secuenciaOptimaComparar[0])
                    #if str(secuenciaSaltar) == str(secuenciaOptimaComparar[0]):
                    #    seEncontro = True
                    #   break
                    for plantacionSaltar in secuenciaSaltar[0]:
                        #print("Comparando ",plantacionSaltar, " con ",secuenciaOptimaComparar[0])
                        for plantacionComparar in secuenciaOptimaComparar[0]:
                            if str(plantacionSaltar) == str(plantacionComparar):
                                #print("Esta en ",plantacionSaltar, " con ",secuenciaOptimaComparar[0])
                                plantacionesRepetidas +=1
                    #print("PlantacionesRepetidas: ",plantacionesRepetidas," de ", len(secuenciaOptimaComparar[0]))
                    if plantacionesRepetidas == len(secuenciaOptimaComparar[0]):
                        #Todo está malo, no tocar secuencia optima
                        nuevaSecuenciaInsertar = copy.deepcopy(secuenciaSaltar)
                        #print("nuevaSecuenciaInsertar: ",nuevaSecuenciaInsertar, "Secuencia optima: ", secuenciaOptima)
                        #nuevaSecuenciaInsertar[0].append(nuevaPlantacion[0][0])
                        #nuevaSecuenciaInsertar[1] += int(nuevaPlantacion[1])
                        #nuevaSecuenciaInsertar[2] += costoRiego(nuevaPlantacion[0][0], int(secuenciaOptima[1]))
                        #print("nuevaSecuenciaInsertarPOST: ",nuevaSecuenciaInsertar)
                        #print("Evaluando mejor entre ",nuevaSecuenciaInsertar," y ",secuenciaOptimaComparar)
                        if nuevaSecuenciaInsertar[2] < secuenciaOptimaComparar[2]:
                            #secuenciaOptimaComparar = copy.deepcopy(nuevaSecuenciaInsertar)
                            #print("Secuencias: ", secuencias[indiceSecuencias+1])
                            for secuencia in secuencias[indiceSecuencias+1]:
                                #print("Comparando ",secuencia," con ",secuenciaOptimaComparar)
                                if str(secuencia) == str(secuenciaOptimaComparar):
                                    #print("iguales!! INSERTANDO ",nuevaSecuenciaInsertar," EN LUGAR DE ", secuencia)
                                    secuencias[indiceSecuencias+1][secuencias[indiceSecuencias+1].index(secuencia)] = copy.deepcopy(nuevaSecuenciaInsertar)
                                    #print("Secuencias: ", secuencias[indiceSecuencias+1])
                                    break
                            #secuencias[indiceSecuencias+1][secuencias.index(secuenciaOptimaComparar)] = copy.deepcopy(nuevaSecuenciaInsertar)
                            #print("nueva Secuencia optima comparar: ",secuenciaOptimaComparar)
                            #print("Secuencias: ", secuencias[indiceSecuencias+1])
                        seEncontro = True
                        break
                if seEncontro == True:
                    continue

                #Marica rece unos 20 padre nuestros para entender este puto condicional oyo?
                #Basicamente, analiza si es mejor regar secuenciaOptima primero o regar nuevaPlantacion primero, esto lo hace sumando el costo de regar alguno de primero y el costo de regar el otro despu�s, agarra el menor.
                #print("nueva plantacion[0][0]: ",nuevaPlantacion[0][0])
                if indiceSecuencias == 0:
                    #print("Secuencia optima: ", secuenciaOptima)
                    if secuenciaOptima[2]+costoRiego(nuevaPlantacion[0][0], secuenciaOptima[1]) < nuevaPlantacion[2]+costoRiego(secuenciaOptima[0][0], nuevaPlantacion[1]):
                        #secuencias[indiceSecuencias+1].append([[secuenciaOptima[0].append(nuevaPlantacion[0])], secuenciaOptima[1]+nuevaPlantacion[0].tiempoRiego, secuenciaOptima[2]+costoRiego(nuevaPlantacion[0], secuenciaOptima[1])])
                        secuencias[indiceSecuencias+1].append([[secuenciaOptima[0][0], nuevaPlantacion[0][0]],int(secuenciaOptima[1])+int(nuevaPlantacion[0][0].tiempoRiego), secuenciaOptima[2]+costoRiego(nuevaPlantacion[0][0], secuenciaOptima[1])])
                        #print("secuencias[",indiceSecuencias+1,"]: ", secuencias[indiceSecuencias+1])
                    else:
                        #secuencias[indiceSecuencias+1].append([[secuenciaOptima[0].insert(0,nuevaPlantacion[0])], secuenciaOptima[1]+nuevaPlantacion[0].tiempoRiego, secuenciaOptima[2]+costoRiego(nuevaPlantacion[0], secuenciaOptima[1])])
                        secuencias[indiceSecuencias+1].append([[nuevaPlantacion[0][0], secuenciaOptima[0][0]],int(secuenciaOptima[1])+int(nuevaPlantacion[0][0].tiempoRiego), nuevaPlantacion[2]+costoRiego(secuenciaOptima[0][0], nuevaPlantacion[0][0].tiempoRiego)])
                        #print("secuencias[",indiceSecuencias+1,"]: ", secuencias[indiceSecuencias+1])
                else:
                    #secuenciaOptima[0].append(nuevaPlantacion[0][0])
                    secuenciaNueva = copy.copy(secuenciaOptima[0])
                    secuenciaNueva.append(nuevaPlantacion[0][0])
                    secuencias[indiceSecuencias+1].append([secuenciaNueva,int(secuenciaOptima[1])+int(nuevaPlantacion[0][0].tiempoRiego), secuenciaOptima[2]+costoRiego(nuevaPlantacion[0][0], secuenciaOptima[1])])
                    #print("secuencias[",indiceSecuencias+1,"]: ", secuencias[indiceSecuencias+1])
                    #break

            #longitudBackup.remove(secuenciaOptima)
        indiceSecuencias+=1
        #print("Indice secuencias: ",indiceSecuencias)
        #if indiceSecuencias > 3:
        #    break
    return secuencias



finca = formatInput('BateriaPruebas/Prueba10.txt')
ordenOptimo = ordenOptimoDinamica(finca)
print("Orden optimo:")
tamano = 1
menor = float('inf')
for longitud in ordenOptimo:
    
    for secuenciaOptima in longitud:
        if tamano >= 11 and (secuenciaOptima[2]<menor):
            menor = secuenciaOptima[2]
            print("Secuencia de tamano ",tamano,": ",secuenciaOptima , "\n")
    tamano += 1

def devolverIndices(plantacionesResultado, finca):
    print(plantacionesResultado)
    orden = [0] * len(finca)
    for i in range(len(plantacionesResultado)):
        for plantacion in finca:
            if str(plantacion) == str(plantacionesResultado[i]):
                orden[i] = finca.index(plantacion)
    return orden
print(ordenOptimo[-1][0])
print(devolverIndices(ordenOptimo[-1][0][0],finca))
#El dia de hoy me acostaré, con dos personas sabiendo cómo funciona este código, estas personas siendo yo y dios.
#Espero al levantarme mañana, que sólo dios recuerde.

