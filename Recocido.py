#carlos eduardoa arriaga yañez   2/02/24
#
import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la longitud de un recorrido (en este caso, TSP)
def calculate_length(order, distances):
    length = 0
    for i in range(len(order) - 1):
        length += distances[order[i]][order[i + 1]]
    length += distances[order[-1]][order[0]]  # Volver al punto inicial
    return length

# Función para intercambiar dos elementos en una lista
def swap(order):
    i, j = np.random.choice(len(order), 2, replace=False)
    order[i], order[j] = order[j], order[i]
    return order

# Implementación del algoritmo de recocido simulado
def simulated_annealing(distances, initial_order, temperature, cooling_rate, iterations):
    current_order = initial_order.copy()
    best_order = current_order.copy()
    current_length = calculate_length(current_order, distances)
    best_length = current_length

    length_list = [best_length]

    for iteration in range(iterations):
        new_order = swap(current_order.copy())
        new_length = calculate_length(new_order, distances)

        # Evaluar si aceptamos la nueva solución
        if new_length < current_length or np.random.rand() < np.exp((current_length - new_length) / temperature):
            current_order = new_order.copy()
            current_length = new_length

        # Actualizar la mejor solución encontrada
        if current_length < best_length:
            best_order = current_order.copy()
            best_length = current_length

        # Reducir la temperatura
        temperature *= 1 - cooling_rate

        length_list.append(best_length)

    return best_order, length_list

# Ejemplo de uso
# Define la matriz de distancias (puedes personalizarla según tu problema)
distances = np.array([
    [0, 2, 2, 5, 7],
    [2, 0, 4, 8, 2],
    [2, 4, 0, 1, 3],
    [5, 8, 1, 0, 2],
    [7, 2, 3, 2, 0]
])

# Punto de inicio (orden inicial)
initial_order = np.arange(len(distances))

# Parámetros del algoritmo
initial_temperature = 1000
cooling_rate = 0.001
iterations = 5000

# Aplicar el algoritmo de recocido simulado
best_order, length_list = simulated_annealing(distances, initial_order, initial_temperature, cooling_rate, iterations)

# Mostrar resultados
print("Mejor orden encontrado:", best_order)
print("Longitud del mejor recorrido:", length_list[-1])

# Graficar la evolución de la longitud durante las iteraciones
plt.plot(length_list)
plt.xlabel("Iteración")
plt.ylabel("Longitud del recorrido")
plt.title("Evolución del Recorrido - Recocido Simulado")
plt.show()
