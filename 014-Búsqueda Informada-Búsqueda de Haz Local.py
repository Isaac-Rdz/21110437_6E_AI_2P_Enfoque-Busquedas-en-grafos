
import random

class BeamSearch:
    def __init__(self, initial_solutions, neighbors_func, objective_func, beam_width=5, max_iterations=100):
        self.current_solutions = initial_solutions
        self.beam_width = beam_width
        self.max_iterations = max_iterations
        self.neighbors_func = neighbors_func
        self.objective_func = objective_func

    def search(self):
        for _ in range(self.max_iterations):
            next_solutions = []
            for solution in self.current_solutions:
                neighbors = self.neighbors_func(solution)
                next_solutions.extend(neighbors)
            next_solutions.sort(key=self.objective_func)
            self.current_solutions = next_solutions[:self.beam_width]
            if self.objective_func(self.current_solutions[0]) == 0:
                break
        return self.current_solutions[0]

# Ejemplo de uso
def initial_solutions():
    return [random.randint(0, 100)]

def neighbors(solution):
    return [solution + random.randint(-1, 1) for _ in range(10)]

def objective(solution):
    return abs(solution - 50)  # Objetivo: minimizar la diferencia entre la solución y 50

initial_solutions = initial_solutions()
beam_search = BeamSearch(initial_solutions, neighbors, objective)
best_solution = beam_search.search()
print("Mejor solución encontrada:", best_solution)
print("Valor objetivo en la mejor solución:", objective(best_solution))
