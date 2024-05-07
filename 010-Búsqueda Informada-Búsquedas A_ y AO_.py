
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

def aostar_search(graph, start, goal, heuristic):
    visited = set()
    priority_queue = [(0, start)]
    g_score = {node: float('inf') for node in graph.graph_dict}
    g_score[start] = 0
    
    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)
        if current_node == goal:
            return True
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbor, cost in graph.graph_dict[current_node]:
            new_cost = g_score[current_node] + cost
            if new_cost < g_score[neighbor]:
                g_score[neighbor] = new_cost
                priority_queue.append((max(new_cost + heuristic(neighbor, goal), current_cost), neighbor))
                heapq.heapify(priority_queue)
    
    return False

def astar_search(graph, start, goal, heuristic):
    visited = set()
    priority_queue = [(0, start)]
    g_score = {node: float('inf') for node in graph.graph_dict}
    g_score[start] = 0
    
    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)
        if current_node == goal:
            return True
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbor, cost in graph.graph_dict[current_node]:
            new_cost = g_score[current_node] + cost
            if new_cost < g_score[neighbor]:
                g_score[neighbor] = new_cost
                priority_queue.append((new_cost + heuristic(neighbor, goal), neighbor))
                heapq.heapify(priority_queue)
    
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
result_aostar = aostar_search(graph, start_node, goal_node, heuristic)
result_astar = astar_search(graph, start_node, goal_node, heuristic)
print("¿Se encontró un camino al objetivo utilizando AO*?", result_aostar)
print("¿Se encontró un camino al objetivo utilizando A*?", result_astar)
