
import math

class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def add_edge(self, node, neighbor, distance):
        if node not in self.graph_dict:
            self.graph_dict[node] = {}
        self.graph_dict[node][neighbor] = distance

def heuristic(node, goal):
    # Heurística de distancia euclidiana
    x1, y1 = node
    x2, y2 = goal
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def a_star(graph, start, goal):
    open_set = {start}
    closed_set = set()
    g_score = {node: float('inf') for node in graph.graph_dict}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph.graph_dict}
    f_score[start] = heuristic(start, goal)
    while open_set:
        current = min(open_set, key=lambda node: f_score[node])
        if current == goal:
            return True
        open_set.remove(current)
        closed_set.add(current)
        for neighbor, distance in graph.graph_dict[current].items():
            tentative_g_score = g_score[current] + distance
            if tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                if neighbor not in closed_set:
                    open_set.add(neighbor)
    return False

# Ejemplo de uso
graph = Graph({
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(0, 1): 1, (1, 0): 1}
})

start_node = (0, 0)
goal_node = (1, 1)
result = a_star(graph, start_node, goal_node)
print("¿Se encontró un camino al objetivo?", result)
