
import random

def hill_climbing(problem, max_iterations):
    current_state = problem.initial_state()
    for _ in range(max_iterations):
        neighbors = problem.neighbors(current_state)
        next_state = max(neighbors, key=lambda state: problem.heuristic(state))
        if problem.heuristic(next_state) <= problem.heuristic(current_state):
            break
        current_state = next_state
    return current_state

class Problem:
    def __init__(self, initial_state, heuristic, neighbors):
        self.initial_state = initial_state
        self.heuristic = heuristic
        self.neighbors = neighbors

# Ejemplo de uso
def initial_state():
    return random.randint(0, 100)

def heuristic(state):
    return -state ** 2  # Objetivo: encontrar el máximo de la función cuadrática negativa

def neighbors(state):
    return [state + 1, state - 1]

problem = Problem(initial_state, heuristic, neighbors)
max_iterations = 1000
solution = hill_climbing(problem, max_iterations)
print("Máximo local encontrado:", solution)
print("Valor de la función objetivo en el máximo local:", heuristic(solution))
