from openInput import formatInput
import copy

def costoRiego(plantacion, tiempo_transcurrido):
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
    tiempo_supervivencia = plantacion.tiempoSuperv
    tiempo_regado = plantacion.tiempoRiego
    prioridad = plantacion.prioridad
    if int(tiempo_transcurrido) + int(tiempo_regado) <= int(tiempo_supervivencia):
        return int(tiempo_supervivencia) - (int(tiempo_transcurrido) + int(tiempo_regado))
    else:
        return int(prioridad) * ((int(tiempo_transcurrido) + int(tiempo_regado)) - int(tiempo_supervivencia))
    
def ordenOptimoDinamica(finca):
    #Arreglo para almacenar los costos de las soluciones a los subproblemas
    secuencias = [[]] * len(finca)
    print(secuencias)
    #Crear los costos de los casos bases (regar cada elemento de la finca en tiempo = 0) 
    for plantacion in finca:
        #print("Costo riego: ",costoRiego(plantacion,0))
        secuencias[0].append([[plantacion],plantacion.tiempoRiego,costoRiego(plantacion, 0)])
    indiceSecuencias = 0
    print("Secuencias[0]: ",secuencias[0])
    secuencias[1] = []
    secuencias[2] = []
    secuencias[3] = []
    secuencias[4] = []
    print("Secuencias[1]: ",secuencias[1])
    print("Secuencias[0]: ",secuencias[0])
    #Crear los costos de los casos recursivos
    #Que no combine las secuencias con su misma longitud sino con secuencias[0]
    for longitud in secuencias:
        print("Longitud: ", longitud)
        
        ##Calcular los costos para esa longitud
        #Buscar la forma de no combinarse con los elementos que ya combinó... quizá haciendo uso de las plantaciones que contiene y buscando en secuencias[0]
        longitudBackup = copy.copy(longitud)
        
        for secuenciaOptima in longitudBackup:
            print("Secuencia optima: ",secuenciaOptima)
            ## hallar el costo de poner este de primero y los demás de segundo, posteriormente expulsar del arreglo para evitar repetir
            ## probar orden en momento de hallar costo para escoger el minimo
            ## Guardar el tiempo que llevan acumuladas cada secuencia, calcular todas las secuencias de la siguiente longitud en un arreglo temporal y luego meterlas en costo?? no es necesario
            ## Guardar cada longitud de secuencia en un arreglo diferente??? podría ser
            ## Guardar las secuencias de cada longitud en una posición de un arreglo dinámico.
            plantacionesCombinar = copy.copy(secuencias[0])
            for plantaEscogida in secuenciaOptima[0]:
                print("Planta escogida: ", plantaEscogida)
                print("Secuencias[0]: ", secuencias[0])
                index = 0
                for plantacionOptima in plantacionesCombinar:
                    print("Planta escogida: ", plantaEscogida)
                    print("Plantacion optima: ", plantacionOptima)
                    print("Plantaciones combinar: ", plantacionesCombinar)
                    print("Indice: ", index)
                    if plantaEscogida in plantacionOptima[0]:
                        print("Planta escogida: ", plantaEscogida)
                        print("Plantacion optima: ", plantacionOptima)
                        print("Plantaciones combinar: ", plantacionesCombinar)
                        print("Indice: ", index)
                        plantacionesCombinar[index] = None
                    for plantacion in plantacionesCombinar:
                        if plantacion == None:
                            plantacionesCombinar.pop(plantacionesCombinar.index(plantacion))
                    index += 1
                #if plantaEscogida in secuencias[0]:
                    
                    #plantacionesCombinar.pop(plantacionesCombinar.index(plantaEscogida))
            print("plantacionesCombinar: ",plantacionesCombinar)
            #plantacionesCombinar.remove(secuenciaOptima)
            for nuevaPlantacion in plantacionesCombinar:
                print("Plantaciones a anadir: ",secuenciaOptima,nuevaPlantacion)
                #Marica rece unos 20 padre nuestros para entender este puto condicional oyo?
                #Basicamente, analiza si es mejor regar secuenciaOptima primero o regar nuevaPlantacion primero, esto lo hace sumando el costo de regar alguno de primero y el costo de regar el otro después, agarra el menor.
                print("nueva plantacion[0][0]: ",nuevaPlantacion[0][0])
                if indiceSecuencias == 0:
                    print("Secuencia optima: ", secuenciaOptima)
                    if secuenciaOptima[2]+costoRiego(nuevaPlantacion[0][0], secuenciaOptima[1]) < nuevaPlantacion[2]+costoRiego(secuenciaOptima[0][0], nuevaPlantacion[1]):
                        #secuencias[indiceSecuencias+1].append([[secuenciaOptima[0].append(nuevaPlantacion[0])], secuenciaOptima[1]+nuevaPlantacion[0].tiempoRiego, secuenciaOptima[2]+costoRiego(nuevaPlantacion[0], secuenciaOptima[1])])
                        secuencias[indiceSecuencias+1].append([[secuenciaOptima[0][0], nuevaPlantacion[0][0]],int(secuenciaOptima[1])+int(nuevaPlantacion[0][0].tiempoRiego), secuenciaOptima[2]+costoRiego(nuevaPlantacion[0][0], secuenciaOptima[1])])
                        #print("secuencias[",indiceSecuencias+1,"]: ", secuencias[indiceSecuencias+1])
                    else:
                        #secuencias[indiceSecuencias+1].append([[secuenciaOptima[0].insert(0,nuevaPlantacion[0])], secuenciaOptima[1]+nuevaPlantacion[0].tiempoRiego, secuenciaOptima[2]+costoRiego(nuevaPlantacion[0], secuenciaOptima[1])])
                        secuencias[indiceSecuencias+1].append([[nuevaPlantacion[0][0], secuenciaOptima[0][0]],int(secuenciaOptima[1])+int(nuevaPlantacion[0][0].tiempoRiego), nuevaPlantacion[2]+costoRiego(secuenciaOptima[0][0], nuevaPlantacion[0][0].tiempoRiego)])
                        #print("secuencias[",indiceSecuencias+1,"]: ", secuencias[indiceSecuencias+1])
                else:
                    secuenciaOptima[0].append(nuevaPlantacion[0][0])
                    secuencias[indiceSecuencias+1].append([secuenciaOptima[0],int(secuenciaOptima[1])+int(nuevaPlantacion[0][0].tiempoRiego), secuenciaOptima[2]+costoRiego(nuevaPlantacion[0][0], secuenciaOptima[1])])
                    print("secuencias[",indiceSecuencias+1,"]: ", secuencias[indiceSecuencias+1])
                    break

            #longitudBackup.remove(secuenciaOptima)
        indiceSecuencias+=1
        print("Indice secuencias: ",indiceSecuencias)
        if indiceSecuencias > 3:
            break
    return secuencias



finca = formatInput('BateriaPruebas/Prueba1.txt')
ordenOptimo = ordenOptimoDinamica(finca)
print("Orden optimo:")
tamano = 1
menor = float('inf')
for longitud in ordenOptimo:
    
    for secuenciaOptima in longitud:
        if tamano == 5 and (secuenciaOptima[2]<menor):
            menor = secuenciaOptima[2]
            print("Secuencia de tamano ",tamano,": ",secuenciaOptima , "\n")
    tamano += 1

#El dia de hoy me acostaré, con dos personas sabiendo cómo funciona este código, estas personas siendo yo y dios.
#Espero al levantarme mañana, que sólo dios recuerde.