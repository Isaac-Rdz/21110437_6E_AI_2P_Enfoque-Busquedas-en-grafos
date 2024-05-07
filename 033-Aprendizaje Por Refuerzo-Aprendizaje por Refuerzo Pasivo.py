
import numpy as np

class PassiveRL:
    def __init__(self, num_states, num_actions, transitions, rewards, gamma, epsilon=0.01):
        self.num_states = num_states
        self.num_actions = num_actions
        self.transitions = transitions
        self.rewards = rewards
        self.gamma = gamma
        self.epsilon = epsilon

    def value_iteration(self):
        V = np.zeros(self.num_states)
        while True:
            delta = 0
            for s in range(self.num_states):
                v = V[s]
                V[s] = max(sum(self.transitions[s][a][s_next] * (self.rewards[s][a][s_next] + self.gamma * V[s_next])
                              for s_next in range(self.num_states)) for a in range(self.num_actions))
                delta = max(delta, abs(v - V[s]))
            if delta < self.epsilon:
                break
        return V

# Definir los parámetros del entorno
num_states = 3
num_actions = 2
transitions = {
    0: {0: {0: 0.9, 1: 0.1}, 1: {0: 0.8, 1: 0.2}},
    1: {0: {0: 0.6, 1: 0.4}, 1: {0: 0.3, 1: 0.7}},
    2: {0: {0: 0.5, 1: 0.5}, 1: {0: 0.1, 1: 0.9}}
}
rewards = {
    0: {0: {0: 0, 1: 1}, 1: {0: 0, 1: 1}},
    1: {0: {0: 0, 1: 1}, 1: {0: 0, 1: 1}},
    2: {0: {0: 0, 1: 1}, 1: {0: 0, 1: 1}}
}
gamma = 0.9

# Inicializar el aprendizaje por refuerzo pasivo
passive_rl = PassiveRL(num_states, num_actions, transitions, rewards, gamma)

# Realizar la iteración de valor para encontrar la política óptima
optimal_values = passive_rl.value_iteration()
print("Función de valor óptima:", optimal_values)
