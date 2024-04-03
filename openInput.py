import copy
import Voraz
import Dinamica

class Plantacion:
    """
    Clase que representa una plantacion en un rancho.

    Atributos:
    - survTime (int): Tiempo de supervivencia del plantacion.
    - irriTime (int): Tiempo de riego del plantacion.
    - priority (int): Prioridad del plantacion.

    Métodos:
    - __init__(self, survTime, irriTime, priority): Constructor de la clase Plantacion.
    - __str__(self): Método para representar un objeto Plantacion como string.
    """

    def __init__(self, tiempoSuperv, tiempoRiego, prioridad):
        """
        Constructor de la clase Plantacion.

        Parámetros:
        - survTime (int): Tiempo de supervivencia de la plantacion.
        - irriTime (int): Tiempo de riego de la plantacion.
        - priority (int): Prioridad de la plantacion.
        """
        self.tiempoSuperv = tiempoSuperv
        self.tiempoRiego = tiempoRiego
        self.prioridad = prioridad

    def __repr__(self):
        return f'Plantacion({self.tiempoSuperv}, {self.tiempoRiego}, {self.prioridad})'

def calcularCostoOrden(plantaciones, orden):
    tiempoTranscurrido = 0
    costoTotal = 0
    for i in range(len(orden)):
        costoTotal += int(Voraz.costoRiego(plantaciones[orden[i]], tiempoTranscurrido))
        print(costoTotal)
        tiempoTranscurrido += int(plantaciones[orden[i]].tiempoRiego)
    return costoTotal

#Lectura del archivo Input.txt y creación de la lista de objetos Plantacion
def formatInput(filePath):
    with open(filePath) as input:
        finca = []
        entrada = input.readlines()[1:]
        for linea in entrada:
            linea = linea.strip()
            datos = linea.split(",")
            finca.append(Plantacion(datos[0], datos[1], datos[2]))
    return finca

#print("Finca: ", formatInput('Input.txt'))
resultado =Dinamica.ordenOptimo(formatInput('BateriaPruebas/Prueba5.txt'))
print(resultado)
print("Costo: ", calcularCostoOrden(formatInput('BateriaPruebas/Prueba5.txt'), resultado))