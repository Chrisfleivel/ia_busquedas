import random
import time

# Generador de grafo completo aleatorio
def generar_grafo(N, distancia_max=100):
    grafo = [[0 if i == j else random.randint(1, distancia_max) for j in range(N)] for i in range(N)]
    return grafo

def tsp_nearest_neighbor(grafo, inicio):
    """
    Resuelve el Problema del Vendedor Viajero (TSP) utilizando el algoritmo del vecino más cercano.

    Args:
        grafo: Una matriz de adyacencia que representa el grafo. grafo[i][j] es la distancia entre la ciudad i y la ciudad j.
        inicio: El índice de la ciudad de inicio.

    Returns:
        Una tupla que contiene:
            - La ruta encontrada (lista de índices de ciudades).
            - El costo total de la ruta encontrada.
    """

    n = len(grafo)
    ruta = [inicio]
    nodos_visitados = {inicio}
    costo_total = 0

    while len(nodos_visitados) < n:
        ultimo_nodo = ruta[-1]
        siguiente_nodo = None
        distancia_minima = float('inf')

        for vecino in range(n):
            if vecino not in nodos_visitados and grafo[ultimo_nodo][vecino] < distancia_minima:
                distancia_minima = grafo[ultimo_nodo][vecino]
                siguiente_nodo = vecino

        if siguiente_nodo is not None:
            ruta.append(siguiente_nodo)
            nodos_visitados.add(siguiente_nodo)
            costo_total += distancia_minima

    costo_total += grafo[ruta[-1]][inicio]  # Regresar a la ciudad inicial
    ruta.append(inicio)

    return ruta, costo_total

if __name__ == '__main__':
    N = 5  # Número de ciudades
    grafo = generar_grafo(N)
    inicio = 0

    print("Grafo:")
    for fila in grafo:
        print(fila)

    ruta_nn, costo_nn = tsp_nearest_neighbor(grafo, inicio)

    print("\nRuta del vecino más cercano:", ruta_nn)
    print("Costo de la ruta:", costo_nn)