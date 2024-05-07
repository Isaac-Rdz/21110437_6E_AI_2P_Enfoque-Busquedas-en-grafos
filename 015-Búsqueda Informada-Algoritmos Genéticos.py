
import random

class GeneticAlgorithm:
    def __init__(self, population_size, gene_length, crossover_rate, mutation_rate, fitness_func, selection_func):
        self.population_size = population_size
        self.gene_length = gene_length
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.fitness_func = fitness_func
        self.selection_func = selection_func

    def generate_population(self):
        return [[random.randint(0, 1) for _ in range(self.gene_length)] for _ in range(self.population_size)]

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, self.gene_length - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def mutate(self, individual):
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                individual[i] = 1 - individual[i]
        return individual

    def evolve(self, population):
        new_population = []
        while len(new_population) < self.population_size:
            parent1 = self.selection_func(population, self.fitness_func)
            parent2 = self.selection_func(population, self.fitness_func)
            if random.random() < self.crossover_rate:
                child1, child2 = self.crossover(parent1, parent2)
                new_population.append(self.mutate(child1))
                new_population.append(self.mutate(child2))
            else:
                new_population.append(self.mutate(parent1))
                new_population.append(self.mutate(parent2))
        return new_population

# Ejemplo de uso
def fitness(solution):
    return sum(solution)

def roulette_wheel_selection(population, fitness_func):
    total_fitness = sum(fitness_func(individual) for individual in population)
    selection_point = random.uniform(0, total_fitness)
    cumulative_fitness = 0
    for individual in population:
        cumulative_fitness += fitness_func(individual)
        if cumulative_fitness > selection_point:
            return individual

population_size = 100
gene_length = 10
crossover_rate = 0.8
mutation_rate = 0.01
generations = 100

genetic_algorithm = GeneticAlgorithm(population_size, gene_length, crossover_rate, mutation_rate, fitness, roulette_wheel_selection)
population = genetic_algorithm.generate_population()

for generation in range(generations):
    population = genetic_algorithm.evolve(population)
    best_individual = max(population, key=fitness)
    print("Generación {}: Mejor individuo: {}, Fitness: {}".format(generation + 1, best_individual, fitness(best_individual)))
