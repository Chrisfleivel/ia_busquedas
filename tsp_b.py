import random
import time
import itertools
import math

# Generador de grafo completo aleatorio
def generar_grafo(N, distancia_max=100):
    grafo = [[0 if i == j else random.randint(1, distancia_max) for j in range(N)] for i in range(N)]
    return grafo

# BACKTRACKING
# Es un algoritmo exacto que intenta todas las posibles rutas que:Comienzan en la ciudad de origen (0),
# Visitan todas las demás ciudades una sola vez y regresan a la ciudad de origen.
# En cada paso
# A cada paso: Se elige una ciudad no visitada y se "visita". Se repite esto recursivamente.
# Si la ruta completa es válida, se calcula el costo total. Se compara con la mejor encontrada hasta ahora.
# Es como tratar todas las combinaciones posibles de caminos en una lista de entregas, y te quedaras con el que más cpnviene
# Es lento y no escalable pero óptimo

def tsp_backtracking(grafo):
    """
    Resuelve el Problema del Vendedor Viajero (TSP) utilizando el algoritmo de Backtracking.

    Args:
        grafo: Una matriz de adyacencia que representa el grafo. grafo[i][j] es la distancia entre la ciudad i y la ciudad j.

    Returns:
        Una tupla que contiene:
            - La ruta óptima (lista de índices de ciudades).
            - El costo total de la ruta óptima.
            - El número de estados expandidos.
            - El tiempo que tardó en ejecutarse el algoritmo.
    """

    n = len(grafo)
    inicio = 0  # Ciudad de inicio
    mejor_ruta = None
    costo_minimo = float('inf')
    estados_expandidos = 0

    def calcular_costo(ruta):
        costo = 0
        for i in range(len(ruta) - 1):
            costo += grafo[ruta[i]][ruta[i+1]]
        return costo

    def backtracking(ruta_actual, nodos_visitados, costo_actual):
        nonlocal mejor_ruta, costo_minimo, estados_expandidos

        estados_expandidos += 1

        if len(nodos_visitados) == n:
            ruta_completa = ruta_actual + [inicio]
            costo_total = calcular_costo(ruta_completa)
            if costo_total < costo_minimo or mejor_ruta is None:  # Modificado para manejar la primera solución
                costo_minimo = costo_total
                mejor_ruta = ruta_completa[:]  # Crear una copia de la lista
            return

        for siguiente_nodo in range(n):
            if siguiente_nodo not in nodos_visitados:
                ruta_actual.append(siguiente_nodo)
                nodos_visitados.add(siguiente_nodo)
                backtracking(ruta_actual, nodos_visitados, costo_actual + grafo[ruta_actual[-2]][ruta_actual[-1]])
                nodos_visitados.remove(siguiente_nodo)
                ruta_actual.pop()

    inicio_tiempo = time.time()
    backtracking([inicio], {inicio}, 0)
    tiempo_ejecucion = time.time() - inicio_tiempo

    return mejor_ruta, costo_minimo, estados_expandidos, tiempo_ejecucion

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