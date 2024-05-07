
class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def add_edge(self, node, neighbor):
        if node not in self.graph_dict:
            self.graph_dict[node] = []
        self.graph_dict[node].append(neighbor)

    def dls(self, start, goal, depth_limit, visited=None):
        if visited is None:
            visited = set()
        if depth_limit >= 0:
            visited.add(start)
            print(start)
            if start == goal:
                return True
            if depth_limit == 0:
                return False
            for neighbor in self.graph_dict.get(start, []):
                if neighbor not in visited:
                    if self.dls(neighbor, goal, depth_limit - 1, visited):
                        return True
        return False

    def ids(self, start, goal):
        depth_limit = 0
        while True:
            print(f"\nRecorrido DFS con límite de profundidad: {depth_limit}")
            if self.dls(start, goal, depth_limit):
                return True
            depth_limit += 1

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
print("Recorrido IDS:")
graph.ids(start_node, goal_node)
