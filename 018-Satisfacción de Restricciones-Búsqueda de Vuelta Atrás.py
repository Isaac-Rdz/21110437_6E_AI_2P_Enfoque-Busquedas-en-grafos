
def backtracking_search(assignment, variables, domains, constraints):
    if len(assignment) == len(variables):
        return assignment

    unassigned_variables = [variable for variable in variables if variable not in assignment]
    variable = unassigned_variables[0]

    for value in domains[variable]:
        if is_consistent(variable, value, assignment, constraints):
            assignment[variable] = value
            result = backtracking_search(assignment, variables, domains, constraints)
            if result is not None:
                return result
            del assignment[variable]

    return None

def is_consistent(variable, value, assignment, constraints):
    for other_variable, other_value in assignment.items():
        if (variable, other_variable) in constraints or (other_variable, variable) in constraints:
            if other_value == value:
                return False
    return True

# Ejemplo de uso
variables = ['A', 'B', 'C']
domains = {'A': [1, 2, 3], 'B': [1, 2], 'C': [2, 3]}
constraints = [('A', 'B'), ('A', 'C')]
assignment = {}
solution = backtracking_search(assignment, variables, domains, constraints)
print("Solución encontrada:", solution)
