
import numpy as np

class QLearning:
    def __init__(self, num_states, num_actions, alpha, gamma, epsilon, max_steps):
        self.num_states = num_states
        self.num_actions = num_actions
        self.alpha = alpha  # Tasa de aprendizaje
        self.gamma = gamma  # Factor de descuento
        self.epsilon = epsilon  # Exploración vs. explotación
        self.max_steps = max_steps  # Máximo de pasos permitidos por episodio
        self.Q = np.zeros((num_states, num_actions))  # Matriz Q (valores de las acciones)

    def select_action(self, state):
        # Selección de acción basada en epsilon-greedy
        if np.random.uniform(0, 1) < self.epsilon:
            return np.random.randint(0, self.num_actions)  # Exploración
        else:
            return np.argmax(self.Q[state])  # Explotación

    def update_q_value(self, state, action, reward, next_state):
        # Actualización del valor Q usando la ecuación de Q-learning
        td_target = reward + self.gamma * np.max(self.Q[next_state])
        td_error = td_target - self.Q[state, action]
        self.Q[state, action] += self.alpha * td_error

    def train(self, env):
        # Entrenamiento del agente en el ambiente
        for episode in range(self.max_steps):
            state = env.reset()  # Reiniciar el estado del ambiente
            for step in range(self.max_steps):
                action = self.select_action(state)  # Selección de acción
                next_state, reward, done, _ = env.step(action)  # Ejecutar acción en el ambiente
                self.update_q_value(state, action, reward, next_state)  # Actualización de la matriz Q
                state = next_state  # Actualización del estado actual
                if done:  # Verificar si se ha alcanzado un estado terminal
                    break

# Ejemplo de ambiente simple
class Environment:
    def __init__(self):
        self.num_states = 2
        self.num_actions = 2

    def reset(self):
        return 0  # Reiniciar el estado a uno predeterminado

    def step(self, action):
        # Definir las recompensas y los estados siguientes basados en las acciones
        if action == 0:
            return 1, 0, False, {}  # Estado siguiente, recompensa, estado terminal, información adicional
        else:
            return 0, 1, False, {}

# Parámetros del algoritmo Q-Learning
num_states = 2
num_actions = 2
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento
epsilon = 0.1  # Tasa de exploración
max_steps = 1000  # Número máximo de pasos por episodio

# Inicializar el agente Q-Learning
q_learning_agent = QLearning(num_states, num_actions, alpha, gamma, epsilon, max_steps)

# Entrenar el agente en el ambiente
env = Environment()
q_learning_agent.train(env)

# Mostrar la matriz Q aprendida por el agente
print("Matriz Q aprendida:")
print(q_learning_agent.Q)
