
from collections import deque

class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def add_edge(self, node, neighbor):
        if node not in self.graph_dict:
            self.graph_dict[node] = []
        self.graph_dict[node].append(neighbor)

    def bfs(self, start, goal):
        visited = set()
        queue = deque([(start, [start])])

        while queue:
            current_node, path = queue.popleft()
            visited.add(current_node)
            if current_node == goal:
                return path
            for neighbor in self.graph_dict.get(current_node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
                    visited.add(neighbor)

# Ejemplo de uso
graph = Graph({
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
})

start_node = 'A'
goal_node = 'F'
path = graph.bfs(start_node, goal_node)
print("Camino encontrado:", path)
