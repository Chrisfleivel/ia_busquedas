import random
import time

# Generador de grafo completo aleatorio
def generar_grafo(N, distancia_max=100):
    grafo = [[0 if i == j else random.randint(1, distancia_max) for j in range(N)] for i in range(N)]
    return grafo

def tsp_las_vegas(grafo, tiempo_maximo=10):
    """
    Resuelve el Problema del Vendedor Viajero (TSP) utilizando el algoritmo de Las Vegas.

    Args:
        grafo: Una matriz de adyacencia que representa el grafo. grafo[i][j] es la distancia entre la ciudad i y la ciudad j.
        tiempo_maximo: Tiempo máximo en segundos para buscar una solución.

    Returns:
        Una tupla que contiene:
            - La ruta encontrada (lista de índices de ciudades) o None si no se encuentra.
            - El costo total de la ruta encontrada o None si no se encuentra.
            - El número de estados expandidos.
            - El tiempo que tardó en ejecutarse el algoritmo.
    """

    n = len(grafo)
    inicio = 0  # Ciudad de inicio
    inicio_tiempo = time.time()
    estados_expandidos = 0

    def calcular_costo(ruta):
        costo = 0
        for i in range(len(ruta) - 1):
            costo += grafo[ruta[i]][ruta[i+1]]
        costo += grafo[ruta[-1]][ruta[0]]  # Regresar a la ciudad inicial
        return costo

    def las_vegas(ruta_actual, nodos_visitados, costo_actual):
        nonlocal estados_expandidos

        estados_expandidos += 1

        if time.time() - inicio_tiempo > tiempo_maximo:
            return None, None  # Se agotó el tiempo

        if len(nodos_visitados) == n:
            ruta_completa = ruta_actual + [inicio]
            costo_total = calcular_costo(ruta_completa)
            return ruta_completa, costo_total

        nodos_no_visitados = list(set(range(n)) - nodos_visitados)
        if nodos_no_visitados:
            siguiente_nodo = random.choice(nodos_no_visitados)
            ruta_actual.append(siguiente_nodo)
            nodos_visitados.add(siguiente_nodo)
            resultado_ruta, resultado_costo = las_vegas(ruta_actual, nodos_visitados, costo_actual + grafo[ruta_actual[-2]][ruta_actual[-1]])
            if resultado_ruta:
                return resultado_ruta, resultado_costo
            else:
                ruta_actual.pop()
                nodos_visitados.remove(siguiente_nodo)
                return None, None
        else:
            return None, None  # No debería llegar aquí, pero por seguridad

    ruta, costo = las_vegas([inicio], {inicio}, 0)
    tiempo_ejecucion = time.time() - inicio_tiempo

    return ruta, costo, estados_expandidos, tiempo_ejecucion

if __name__ == '__main__':
    N = 5  # Número de ciudades
    grafo = generar_grafo(N)

    print("Grafo:")
    for fila in grafo:
        print(fila)

    ruta_optima, costo_optimo, estados_expandidos, tiempo_ejecucion = tsp_las_vegas(grafo)

    print("\nRuta encontrada:", ruta_optima)
    print("Costo de la ruta:", costo_optimo)
    print("Estados expandidos:", estados_expandidos)
    print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")