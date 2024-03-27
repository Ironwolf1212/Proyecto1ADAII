import copy

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

    def __init__(self, survTime, irriTime, priority):
        """
        Constructor de la clase Plantacion.

        Parámetros:
        - survTime (int): Tiempo de supervivencia de la plantacion.
        - irriTime (int): Tiempo de riego de la plantacion.
        - priority (int): Prioridad de la plantacion.
        """
        self.survTime = survTime
        self.irriTime = irriTime
        self.priority = priority

    def __str__(self):
        return f"Plantacion({self.survTime}, {self.irriTime}, {self.priority})"

def calculateCost(ranch, timings):
    """
    Calcula el costo total de riego para un rancho dado.

    Parámetros:
    - ranch (list): Lista de objetos Plantacion que representan los parches del rancho.
    - timings (list): Lista de tiempos de riego para cada plantacion.

    Retorna:
    - cost (int): Costo total de riego para el rancho.
    """
    cost = 0
    i = 0
    for plantacion in ranch:
        if (int(plantacion.survTime) - int(plantacion.irriTime)) > timings[i]:
            cost += int(plantacion.survTime) - (int(plantacion.irriTime) + timings[i])
        else:
            cost += int(plantacion.priority) * ((timings[i] + int(plantacion.irriTime)) - int(plantacion.survTime))
        i += 1
    return cost

#Lectura del archivo Input.txt y creación de la lista de objetos Plantacion
with open('Input.txt') as input:
    ranch = []
    input = input.readlines()[1:]
    for line in input:
        data = line.split(",")
        ranch.append(Plantacion(data[0], data[1], data[2]))
