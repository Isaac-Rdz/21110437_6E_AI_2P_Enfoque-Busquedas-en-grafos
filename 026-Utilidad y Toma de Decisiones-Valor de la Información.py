
class ValueOfInformation:
    def __init__(self, utility_function):
        self.utility_function = utility_function

    def value_of_information(self, prior_prob, posterior_probs):
        prior_utility = self.utility_function.calculate_utility(prior_prob)
        expected_utility = sum(prob * self.utility_function.calculate_utility(post_prob) for prob, post_prob in zip(prior_prob, posterior_probs))
        return expected_utility - prior_utility

class UtilityFunction:
    def __init__(self, weights):
        self.weights = weights

    def calculate_utility(self, outcome):
        utility = sum(w * x for w, x in zip(self.weights, outcome))
        return utility

# Ejemplo de uso
prior_prob = [0.4, 0.6]  # Probabilidad a priori de los resultados
posterior_probs = [[0.7, 0.3], [0.2, 0.8]]  # Probabilidades posteriores para cada resultado
weights = [1, 2]  # Pesos para calcular la utilidad

utility_function = UtilityFunction(weights)
voi_calculator = ValueOfInformation(utility_function)

voi = voi_calculator.value_of_information(prior_prob, posterior_probs)
print("Valor de la información:", voi)
