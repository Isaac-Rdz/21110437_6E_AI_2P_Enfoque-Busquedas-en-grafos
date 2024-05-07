
import numpy as np

class ExplorationExploitation:
    def __init__(self, epsilon):
        self.epsilon = epsilon

    def select_action(self, q_values):
        if np.random.uniform(0, 1) < self.epsilon:
            return np.random.randint(0, len(q_values))  # Exploración aleatoria
        else:
            return np.argmax(q_values)  # Explotación de la mejor acción estimada

# Ejemplo de uso
exploration_exploitation = ExplorationExploitation(epsilon=0.1)  # Epsilon-greedy con epsilon=0.1

# Q-values estimados para tres acciones
q_values = [0.2, 0.5, 0.8]

# Selección de acción basada en exploración vs. explotación
action = exploration_exploitation.select_action(q_values)

print("Acción seleccionada:", action)
