
import heapq

class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def add_edge(self, node, neighbor, cost):
        if node not in self.graph_dict:
            self.graph_dict[node] = []
        self.graph_dict[node].append((neighbor, cost))

def greedy_best_first_search(graph, start, goal, heuristic):
    visited = set()
    priority_queue = [(heuristic(start, goal), start)]
    
    while priority_queue:
        _, current_node = heapq.heappop(priority_queue)
        if current_node == goal:
            return True
        visited.add(current_node)
        for neighbor, cost in graph.graph_dict[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic(neighbor, goal), neighbor))
    
    return False

# Ejemplo de uso
graph = Graph({
    'A': [('B', 5), ('C', 8)],
    'B': [('D', 12), ('E', 15)],
    'C': [('F', 10)],
    'D': [('G', 3)],
    'E': [('G', 20)],
    'F': [('G', 6)],
    'G': []
})

def heuristic(node, goal):
    # Heurística: distancia en línea recta hasta el nodo objetivo
    return abs(ord(node) - ord(goal))

start_node = 'A'
goal_node = 'G'
result = greedy_best_first_search(graph, start_node, goal_node, heuristic)
print("¿Se encontró un camino al objetivo?", result)
