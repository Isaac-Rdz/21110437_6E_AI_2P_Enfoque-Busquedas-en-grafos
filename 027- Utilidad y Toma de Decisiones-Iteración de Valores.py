
import numpy as np

class ValueIteration:
    def __init__(self, num_states, num_actions, transitions, rewards, gamma, epsilon=0.01):
        self.num_states = num_states
        self.num_actions = num_actions
        self.transitions = transitions
        self.rewards = rewards
        self.gamma = gamma
        self.epsilon = epsilon

    def value_iteration(self):
        V = np.zeros(self.num_states)  # Inicializar los valores de los estados a cero
        while True:
            delta = 0
            for s in range(self.num_states):
                v = V[s]
                # Calcular el valor esperado para cada acción en el estado actual
                q_values = [sum(self.transitions[s][a][s_next] * (self.rewards[s][a][s_next] + self.gamma * V[s_next])
                                for s_next in range(self.num_states)) for a in range(self.num_actions)]
                # Actualizar el valor del estado como el máximo valor esperado entre todas las acciones
                V[s] = max(q_values)
                # Actualizar la diferencia máxima entre los valores de los estados
                delta = max(delta, abs(v - V[s]))
            # Verificar si la convergencia se ha alcanzado
            if delta < self.epsilon:
                break
        return V

# Definir los parámetros del entorno
num_states = 3
num_actions = 2
transitions = {
    0: {0: {0: 0.9, 1: 0.1}, 1: {0: 0.8, 1: 0.2}},
    1: {0: {0: 0.1, 1: 0.9}, 1: {0: 0.2, 1: 0.8}},
    2: {0: {0: 0.5, 1: 0.5}, 1: {0: 0.3, 1: 0.7}}
}
rewards = {
    0: {0: {0: 0, 1: 1}, 1: {0: 0, 1: 1}},
    1: {0: {0: 0, 1: 1}, 1: {0: 0, 1: 1}},
    2: {0: {0: 0, 1: 1}, 1: {0: 0, 1: 1}}
}
gamma = 0.9
epsilon = 0.01

# Inicializar la Iteración de Valores
value_iteration = ValueIteration(num_states, num_actions, transitions, rewards, gamma, epsilon)

# Realizar la Iteración de Valores para encontrar la función de valor óptima
optimal_values = value_iteration.value_iteration()

# Mostrar la función de valor óptima
print("Función de valor óptima:")
print(optimal_values)
