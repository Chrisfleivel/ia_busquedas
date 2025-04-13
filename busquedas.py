import random
import time
import itertools
import math
from tsp_b import tsp_backtracking
from tsp_vegas import tsp_las_vegas
from tsp_g import *
from tsp_g_2p import *


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

    print(f"Backtracking:")
    print("\nRuta óptima:", ruta_optima)
    print("Costo óptimo:", costo_optimo)
    print("Estados expandidos:", estados_expandidos)
    print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")


    ruta_optima, costo_optimo, estados_expandidos, tiempo_ejecucion = tsp_las_vegas(grafo)
    print(f"\nVegas:")
    print("\nRuta encontrada:", ruta_optima)
    print("Costo de la ruta:", costo_optimo)
    print("Estados expandidos:", estados_expandidos)
    print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")

    print(f"\nGreedy:")
    ruta_nn, costo_nn = tsp_nearest_neighbor(grafo, 0)

    print("\nRuta del vecino más cercano:", ruta_nn)
    print("Costo de la ruta:", costo_nn)

    ruta_inicial = ruta_nn

    ruta_optimizada = dos_opt(grafo, ruta_inicial)
    costo_inicial = calcular_costo(grafo, ruta_inicial)
    costo_optimizada = calcular_costo(grafo, ruta_optimizada)
    print(f"\nGreedy + 2-opt:")
    print("\nRuta inicial:", ruta_inicial)
    print("Costo inicial:", costo_inicial)
    print("Ruta optimizada (2-opt):", ruta_optimizada)
    print("Costo optimizado:", costo_optimizada)
