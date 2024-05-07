
from pomdp_py import POMDP, BeliefState, DiscreteSpace, DiscreteDistribution

# Definir los estados, acciones, observaciones y recompensas
states = ['S0', 'S1', 'S2']
actions = ['A0', 'A1']
observations = ['O0', 'O1']
rewards = {
    ('S0', 'A0'): {'S0': 0, 'S1': 0, 'S2': 0},
    ('S0', 'A1'): {'S0': 0, 'S1': 0, 'S2': 0},
    ('S1', 'A0'): {'S0': 0, 'S1': 1, 'S2': 0},
    ('S1', 'A1'): {'S0': 0, 'S1': 0, 'S2': 1},
    ('S2', 'A0'): {'S0': 0, 'S1': 0, 'S2': 0},
    ('S2', 'A1'): {'S0': 0, 'S1': 0, 'S2': 0}
}
transitions = {
    ('S0', 'A0'): {'S0': 0.8, 'S1': 0.1, 'S2': 0.1},
    ('S0', 'A1'): {'S0': 0.1, 'S1': 0.8, 'S2': 0.1},
    ('S1', 'A0'): {'S0': 0.1, 'S1': 0.8, 'S2': 0.1},
    ('S1', 'A1'): {'S0': 0.1, 'S1': 0.1, 'S2': 0.8},
    ('S2', 'A0'): {'S0': 0.1, 'S1': 0.1, 'S2': 0.8},
    ('S2', 'A1'): {'S0': 0.8, 'S1': 0.1, 'S2': 0.1}
}
observations_prob = {
    ('S0', 'A0'): {'O0': 0.8, 'O1': 0.2},
    ('S0', 'A1'): {'O0': 0.2, 'O1': 0.8},
    ('S1', 'A0'): {'O0': 0.2, 'O1': 0.8},
    ('S1', 'A1'): {'O0': 0.8, 'O1': 0.2},
    ('S2', 'A0'): {'O0': 0.8, 'O1': 0.2},
    ('S2', 'A1'): {'O0': 0.2, 'O1': 0.8}
}

# Definir el POMDP
pomdp = POMDP(states, actions, observations, rewards, transitions, observations_prob)

# Crear un estado de creencia inicial uniforme
belief_space = DiscreteSpace(states)
initial_belief = BeliefState({s: 1/len(states) for s in states}, belief_space)

# Ejecutar la planificación POMDP
policy = pomdp.solve(100, initial_belief)
print("Política óptima:")
print(policy)
