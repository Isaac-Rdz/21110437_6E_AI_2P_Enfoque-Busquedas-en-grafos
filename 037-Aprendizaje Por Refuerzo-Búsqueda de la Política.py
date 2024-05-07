
import numpy as np

class PolicySearch:
    def __init__(self, num_states, num_actions, transitions, rewards, gamma):
        self.num_states = num_states
        self.num_actions = num_actions
        self.transitions = transitions
        self.rewards = rewards
        self.gamma = gamma
        self.policy = np.ones((num_states, num_actions)) / num_actions  # Inicializar una política aleatoria uniforme

    def evaluate_policy(self):
        # Evaluación de la política actual
        V = np.zeros(self.num_states)
        for _ in range(1000):  # Iteraciones de evaluación de la política
            for s in range(self.num_states):
                v = 0
                for a in range(self.num_actions):
                    v += self.policy[s][a] * sum(self.transitions[s][a][s_next] * (self.rewards[s][a][s_next] + self.gamma * V[s_next])
                                                 for s_next in range(self.num_states))
                V[s] = v
        return V

    def improve_policy(self, V):
        # Mejora de la política basada en los valores de estado-acción
        for s in range(self.num_states):
            q_values = np.zeros(self.num_actions)
            for a in range(self.num_actions):
                q_values[a] = sum(self.transitions[s][a][s_next] * (self.rewards[s][a][s_next] + self.gamma * V[s_next])
                                  for s_next in range(self.num_states))
            best_action = np.argmax(q_values)
            self.policy[s] = np.eye(self.num_actions)[best_action]  # Actualizar la política con la mejor acción

    def train(self):
        # Búsqueda de la política iterativa
        for _ in range(100):  # Número de iteraciones de mejora de política
            V = self.evaluate_policy()
            self.improve_policy(V)

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

# Inicializar la búsqueda de la política
policy_search = PolicySearch(num_states, num_actions, transitions, rewards, gamma)

# Entrenar la búsqueda de la política
policy_search.train()

# Mostrar la política aprendida
print("Política aprendida:")
print(policy_search.policy)
