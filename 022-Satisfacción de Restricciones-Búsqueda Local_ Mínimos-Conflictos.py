
import random

class MinimumConflicts:
    def __init__(self, variables, domains, constraints, max_steps=1000):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.max_steps = max_steps

    def minimum_conflicts_search(self):
        assignment = self.initial_assignment()
        for _ in range(self.max_steps):
            if self.is_solution(assignment):
                return assignment
            conflicted_variable = self.get_conflicted_variable(assignment)
            value = self.minimum_conflicts_value(conflicted_variable, assignment)
            assignment[conflicted_variable] = value
        return None

    def initial_assignment(self):
        return {variable: random.choice(self.domains[variable]) for variable in self.variables}

    def is_solution(self, assignment):
        return all(self.is_consistent(variable, assignment) for variable in self.variables)

    def is_consistent(self, variable, assignment):
        for other_variable, other_value in assignment.items():
            if (variable, other_variable) in self.constraints or (other_variable, variable) in self.constraints:
                if other_value == assignment[variable]:
                    return False
        return True

    def get_conflicted_variable(self, assignment):
        conflicted_variables = [variable for variable in self.variables if not self.is_consistent(variable, assignment)]
        return random.choice(conflicted_variables)

    def minimum_conflicts_value(self, variable, assignment):
        min_conflicts = float('inf')
        min_value = None
        for value in self.domains[variable]:
            conflicts = sum(not self.is_consistent(other_variable, {**assignment, variable: value}) for other_variable in self.variables)
            if conflicts < min_conflicts:
                min_conflicts = conflicts
                min_value = value
        return min_value

# Ejemplo de uso
variables = ['A', 'B', 'C']
domains = {'A': [1, 2, 3], 'B': [1, 2], 'C': [2, 3]}
constraints = [('A', 'B'), ('A', 'C')]
mc = MinimumConflicts(variables, domains, constraints)
solution = mc.minimum_conflicts_search()
print("Solución encontrada:", solution)
