
import numpy as np
import nashpy as nash

# Definir las matrices de pago del juego
payoff_player1 = np.array([[3, 2], [0, 1]])
payoff_player2 = np.array([[3, 0], [2, 1]])

# Crear el juego
game = nash.Game(payoff_player1, payoff_player2)

# Encontrar el equilibrio de Nash
equilibria = game.support_enumeration()
for eq in equilibria:
    print("Equilibrio de Nash:", eq)
