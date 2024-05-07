
class UtilityFunction:
    def __init__(self, weights):
        self.weights = weights

    def calculate_utility(self, outcome):
        utility = sum(w * x for w, x in zip(self.weights, outcome))
        return utility

# Ejemplo de uso
weights = [0.5, 0.3, 0.2]
utility_function = UtilityFunction(weights)
outcome1 = [10, 20, 30]
outcome2 = [5, 25, 35]

utility1 = utility_function.calculate_utility(outcome1)
utility2 = utility_function.calculate_utility(outcome2)

print("Utilidad de Outcome 1:", utility1)
print("Utilidad de Outcome 2:", utility2)

if utility1 > utility2:
    print("Outcome 1 es preferido sobre Outcome 2")
elif utility1 < utility2:
    print("Outcome 2 es preferido sobre Outcome 1")
else:
    print("Los outcomes son igualmente preferidos")
