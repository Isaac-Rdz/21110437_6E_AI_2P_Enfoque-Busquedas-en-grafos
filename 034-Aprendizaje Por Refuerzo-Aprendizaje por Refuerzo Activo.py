
import numpy as np

class ActiveRL:
    def __init__(self, num_states, num_actions, alpha, gamma, epsilon, max_steps):
        self.num_states = num_states
        self.num_actions = num_actions
        self.alpha = alpha  # Tasa de aprendizaje
        self.gamma = gamma  # Factor de descuento
        self.epsilon = epsilon  # Exploración vs. explotación
        self.max_steps = max_steps  # Máximo de pasos permitidos por episodio
        self.Q = np.zeros((num_states, num_actions))  # Valor de la acción

    def select_action(self, state):
        if np.random.uniform(0, 1) < self.epsilon:
            return np.random.randint(0, self.num_actions)
        else:
            return np.argmax(self.Q[state])

    def update_q_value(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.Q[next_state])
        td_target = reward + self.gamma * self.Q[next_state, best_next_action]
        td_error = td_target - self.Q[state, action]
        self.Q[state, action] += self.alpha * td_error

    def train(self, env):
        for episode in range(self.max_steps):
            state = env.reset()
            for step in range(self.max_steps):
                action = self.select_action(state)
                next_state, reward, done, _ = env.step(action)
                self.update_q_value(state, action, reward, next_state)
                state = next_state
                if done:
                    break

# Ambiente simple de ejemplo
class Environment:
    def __init__(self):
        self.num_states = 2
        self.num_actions = 2
        self.state = 0

    def reset(self):
        self.state = 0
        return self.state

    def step(self, action):
        if self.state == 0 and action == 0:
            self.state = 1
            reward = 1
        elif self.state == 1 and action == 1:
            self.state = 0
            reward = 1
        else:
            reward = 0
        done = False
        return self.state, reward, done, {}

# Parámetros del algoritmo
num_states = 2
num_actions = 2
alpha = 0.1
gamma = 0.9
epsilon = 0.1
max_steps = 1000

# Inicializar el agente de aprendizaje por refuerzo activo
active_rl = ActiveRL(num_states, num_actions, alpha, gamma, epsilon, max_steps)

# Entrenar el agente en el ambiente
env = Environment()
active_rl.train(env)

# Mostrar la matriz Q aprendida por el agente
print("Matriz Q aprendida:")
print(active_rl.Q)
