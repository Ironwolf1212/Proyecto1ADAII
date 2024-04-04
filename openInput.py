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
# resultado = Dinamica.ordenOptimo(formatInput('BateriaPruebas/Prueba5.txt'))
# print(resultado)
# print("Costo: ", calcularCostoOrden(formatInput('BateriaPruebas/Prueba5.txt'), resultado))