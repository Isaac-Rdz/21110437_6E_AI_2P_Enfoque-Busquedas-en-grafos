
import random

class TabuSearch:
    def __init__(self, initial_solution, neighbors_func, objective_func, tabu_list_size=10, max_iterations=100):
        self.current_solution = initial_solution
        self.best_solution = initial_solution
        self.tabu_list = []
        self.tabu_list_size = tabu_list_size
        self.max_iterations = max_iterations
        self.neighbors_func = neighbors_func
        self.objective_func = objective_func

    def search(self):
        for _ in range(self.max_iterations):
            neighbors = self.neighbors_func(self.current_solution)
            best_neighbor = min(neighbors, key=self.objective_func)
            if best_neighbor not in self.tabu_list or self.objective_func(best_neighbor) < self.objective_func(self.best_solution):
                self.current_solution = best_neighbor
                self.best_solution = best_neighbor
            self.tabu_list.append(best_neighbor)
            if len(self.tabu_list) > self.tabu_list_size:
                self.tabu_list.pop(0)
        return self.best_solution

# Ejemplo de uso
def initial_solution():
    return random.randint(0, 100)

def neighbors(solution):
    return [solution + random.randint(-1, 1) for _ in range(10)]

def objective(solution):
    return abs(solution - 50)  # Objetivo: minimizar la diferencia entre la solución y 50

initial_solution = initial_solution()
tabu_search = TabuSearch(initial_solution, neighbors, objective)
best_solution = tabu_search.search()
print("Mejor solución encontrada:", best_solution)
print("Valor objetivo en la mejor solución:", objective(best_solution))
