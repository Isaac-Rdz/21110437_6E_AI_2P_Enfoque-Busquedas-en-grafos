
class ConflictDirectedBackjumping:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def backtracking_search(self):
        return self.backtrack({})

    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment

        unassigned_variables = [variable for variable in self.variables if variable not in assignment]
        variable = unassigned_variables[0]

        for value in self.domains[variable]:
            if self.is_consistent(variable, value, assignment):
                assignment[variable] = value
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                del assignment[variable]

        return None

    def is_consistent(self, variable, value, assignment):
        for other_variable, other_value in assignment.items():
            if (variable, other_variable) in self.constraints or (other_variable, variable) in self.constraints:
                if other_value == value:
                    return False
        return True

# Ejemplo de uso
variables = ['A', 'B', 'C']
domains = {'A': [1, 2, 3], 'B': [1, 2], 'C': [2, 3]}
constraints = [('A', 'B'), ('A', 'C')]
cb = ConflictDirectedBackjumping(variables, domains, constraints)
solution = cb.backtracking_search()
print("Solución encontrada:", solution)
