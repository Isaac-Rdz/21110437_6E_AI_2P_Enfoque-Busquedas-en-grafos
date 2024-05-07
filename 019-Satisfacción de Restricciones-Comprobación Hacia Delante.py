
def forward_checking(assignment, variables, domains, constraints):
    for variable in variables:
        if variable not in assignment:
            for value in list(domains[variable]):
                assignment[variable] = value
                if not is_consistent(variable, value, assignment, constraints):
                    domains[variable].remove(value)
            if not domains[variable]:
                return None
    return assignment

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
solution = forward_checking(assignment, variables, domains, constraints)
print("Asignación después de la comprobación hacia adelante:", solution)
