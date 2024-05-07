
import numpy as np

class MDP:
    def __init__(self, states, actions, transitions, rewards, gamma):
        self.states = states
        self.actions = actions
        self.transitions = transitions
        self.rewards = rewards
        self.gamma = gamma

    def value_iteration(self, epsilon=0.01):
        num_states = len(self.states)
        num_actions = len(self.actions)
        V = np.zeros(num_states)
        while True:
            delta = 0
            for s in range(num_states):
                v = V[s]
                V[s] = max(sum(self.transitions[s][a][s_next] * (self.rewards[s][a][s_next] + self.gamma * V[s_next])
                              for s_next in range(num_states)) for a in range(num_actions))
                delta = max(delta, abs(v - V[s]))
            if delta < epsilon:
                break
        return V

# Ejemplo de uso
states = ['S1', 'S2', 'S3']
actions = ['A1', 'A2']
transitions = {
    'S1': {'A1': {'S1': 0.1, 'S2': 0.9}, 'A2': {'S2': 1}},
    'S2': {'A1': {'S1': 0.8, 'S2': 0.2}, 'A2': {'S3': 1}},
    'S3': {'A1': {'S1': 0, 'S2': 0}, 'A2': {'S1': 1}}
}
rewards = {
    'S1': {'A1': {'S1': 0, 'S2': 0}, 'A2': {'S2': 1}},
    'S2': {'A1': {'S1': 0, 'S2': 0}, 'A2': {'S3': 10}},
    'S3': {'A1': {'S1': 0, 'S2': 0}, 'A2': {'S1': -1}}
}
gamma = 0.9

mdp = MDP(states, actions, transitions, rewards, gamma)
V = mdp.value_iteration()
print("Función de valor:")
print(V)
