
import random
import math

class SimulatedAnnealing:
    def __init__(self, initial_solution, neighbors_func, objective_func, temperature=100, cooling_rate=0.95, min_temperature=1, max_iterations=100):
        self.current_solution = initial_solution
        self.best_solution = initial_solution
        self.temperature = temperature
        self.cooling_rate = cooling_rate
        self.min_temperature = min_temperature
        self.max_iterations = max_iterations
        self.neighbors_func = neighbors_func
        self.objective_func = objective_func

    def search(self):
        for iteration in range(self.max_iterations):
            if self.temperature < self.min_temperature:
                break
            new_solution = random.choice(self.neighbors_func(self.current_solution))
            cost_diff = self.objective_func(new_solution) - self.objective_func(self.current_solution)
            if cost_diff < 0 or random.random() < math.exp(-cost_diff / self.temperature):
                self.current_solution = new_solution
            if self.objective_func(self.current_solution) < self.objective_func(self.best_solution):
                self.best_solution = self.current_solution
            self.temperature *= self.cooling_rate
        return self.best_solution

# Ejemplo de uso
def initial_solution():
    return random.randint(0, 100)

def neighbors(solution):
    return [solution + random.randint(-1, 1) for _ in range(10)]

def objective(solution):
    return abs(solution - 50)  # Objetivo: minimizar la diferencia entre la solución y 50

initial_solution = initial_solution()
simulated_annealing = SimulatedAnnealing(initial_solution, neighbors, objective)
best_solution = simulated_annealing.search()
print("Mejor solución encontrada:", best_solution)
print("Valor objetivo en la mejor solución:", objective(best_solution))
