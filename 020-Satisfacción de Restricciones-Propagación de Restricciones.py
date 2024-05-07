
def constraint_propagation(variables, domains, constraints):
    queue = [(variable, neighbor) for variable in variables for neighbor in variables if variable != neighbor]
    while queue:
        variable, neighbor = queue.pop(0)
        if revise(variable, neighbor, domains, constraints):
            if not domains[variable]:
                return None
            for other_neighbor in variables:
                if other_neighbor != neighbor and (variable, other_neighbor) in constraints:
                    queue.append((other_neighbor, variable))
    return domains

def revise(variable1, variable2, domains, constraints):
    revised = False
    for value1 in list(domains[variable1]):
        if not any(value2 for value2 in domains[variable2] if (value1, value2) in constraints):
            domains[variable1].remove(value1)
            revised = True
    return revised

# Ejemplo de uso
variables = ['A', 'B', 'C']
domains = {'A': [1, 2, 3], 'B': [1, 2], 'C': [2, 3]}
constraints = [((1, 2), (2, 1)), ((2, 2), (1, 1)), ((2, 3), (1, 3))]

reduced_domains = constraint_propagation(variables, domains, constraints)
print("Dominios reducidos después de la propagación de restricciones:", reduced_domains)
