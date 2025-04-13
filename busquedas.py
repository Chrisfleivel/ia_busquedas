import random
import time
import itertools
import math
from tsp_b import tsp_backtracking
from tsp_vegas import tsp_las_vegas

# Generador de grafo completo aleatorio
def generar_grafo(N, distancia_max=100):
    grafo = [[0 if i == j else random.randint(1, distancia_max) for j in range(N)] for i in range(N)]
    return grafo

# BACKTRACKING



if __name__ == '__main__':
    N = 5  # Número de ciudades
    grafo = generar_grafo(N)

    print("Grafo:")
    for fila in grafo:
        print(fila)

    ruta_optima, costo_optimo, estados_expandidos, tiempo_ejecucion = tsp_backtracking(grafo)

    print("\nRuta óptima:", ruta_optima)
    print("Costo óptimo:", costo_optimo)
    print("Estados expandidos:", estados_expandidos)
    print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")


    ruta_optima, costo_optimo, estados_expandidos, tiempo_ejecucion = tsp_las_vegas(grafo)

    print("\nRuta encontrada:", ruta_optima)
    print("Costo de la ruta:", costo_optimo)
    print("Estados expandidos:", estados_expandidos)
    print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")
