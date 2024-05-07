
import numpy as np

class GridWorld:
    def __init__(self, rows, cols, start, goal):
        self.rows = rows
        self.cols = cols
        self.start = start
        self.goal = goal
        self.actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Movimientos: derecha, izquierda, abajo, arriba
        self.num_actions = len(self.actions)

    def step(self, state, action):
        next_state = (state[0] + action[0], state[1] + action[1])
        if next_state[0] < 0 or next_state[0] >= self.rows or next_state[1] < 0 or next_state[1] >= self.cols:
            next_state = state  # Si la acción lleva fuera del GridWorld, el estado se mantiene igual
        if next_state == self.goal:
            reward = 1  # Recompensa si se alcanza la meta
        else:
            reward = 0
        return next_state, reward

def policy_iteration(gridworld, gamma=0.9, num_iterations=100):
    policy = np.random.randint(0, gridworld.num_actions, size=(gridworld.rows, gridworld.cols))  # Política inicial aleatoria
    for _ in range(num_iterations):
        value_function = evaluate_policy(gridworld, policy, gamma)
        policy = improve_policy(gridworld, value_function, gamma)
    return policy

def evaluate_policy(gridworld, policy, gamma):
    value_function = np.zeros((gridworld.rows, gridworld.cols))
    for i in range(gridworld.rows):
        for j in range(gridworld.cols):
            action = gridworld.actions[policy[i, j]]
            next_state, reward = gridworld.step((i, j), action)
            value_function[i, j] = reward + gamma * value_function[next_state[0], next_state[1]]
    return value_function

def improve_policy(gridworld, value_function, gamma):
    policy = np.zeros((gridworld.rows, gridworld.cols), dtype=int)
    for i in range(gridworld.rows):
        for j in range(gridworld.cols):
            max_action = None
            max_value = float('-inf')
            for k, action in enumerate(gridworld.actions):
                next_state, _ = gridworld.step((i, j), action)
                value = value_function[next_state[0], next_state[1]]
                if value > max_value:
                    max_value = value
                    max_action = k
            policy[i, j] = max_action
    return policy

# Ejemplo de uso
gridworld = GridWorld(rows=3, cols=3, start=(0, 0), goal=(2, 2))
optimal_policy = policy_iteration(gridworld)
print("Política óptima:")
print(optimal_policy)
