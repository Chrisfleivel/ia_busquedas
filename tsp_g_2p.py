import random
import time

# Generador de grafo completo aleatorio
def generar_grafo(N, distancia_max=100):
    grafo = [[0 if i == j else random.randint(1, distancia_max) for j in range(N)] for i in range(N)]
    return grafo

def calcular_costo(grafo, ruta):
    """Calcula el costo total de una ruta."""
    costo = 0
    for i in range(len(ruta) - 1):
        costo += grafo[ruta[i]][ruta[i + 1]]
    costo += grafo[ruta[-1]][ruta[0]]  # Regresar a la ciudad inicial
    return costo

def dos_opt(grafo, ruta_actual):
    """Aplica la optimización local 2-opt a una ruta."""
    mejor_ruta = ruta_actual[:]  # Crear una copia para no modificar la original
    cambio = True

    while cambio:
        cambio = False
        for i in range(1, len(ruta_actual) - 1):
            for k in range(i + 1, len(ruta_actual)):
                nueva_ruta = ruta_actual[:i] + ruta_actual[i:k][::-1] + ruta_actual[k:]
                if calcular_costo(grafo, nueva_ruta) < calcular_costo(grafo, mejor_ruta):
                    mejor_ruta = nueva_ruta[:]
                    ruta_actual = nueva_ruta[:]  # Actualizar ruta_actual para la siguiente iteración
                    cambio = True

    return mejor_ruta

if __name__ == '__main__':
    N = 5  # Número de ciudades
    grafo = generar_grafo(N)
    inicio = 0

    print("Grafo:")
    for fila in grafo:
        print(fila)

    # Crear una ruta de ejemplo (puedes usar el vecino más cercano u otro algoritmo)
    ruta_inicial = [0, 1, 3, 2, 4, 0]

    ruta_optimizada = dos_opt(grafo, ruta_inicial)
    costo_inicial = calcular_costo(grafo, ruta_inicial)
    costo_optimizada = calcular_costo(grafo, ruta_optimizada)

    print("\nRuta inicial:", ruta_inicial)
    print("Costo inicial:", costo_inicial)
    print("Ruta optimizada (2-opt):", ruta_optimizada)
    print("Costo optimizado:", costo_optimizada)