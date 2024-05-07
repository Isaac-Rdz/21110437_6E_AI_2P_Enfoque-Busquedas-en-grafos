
class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def add_edge(self, node, neighbor):
        if node not in self.graph_dict:
            self.graph_dict[node] = []
        self.graph_dict[node].append(neighbor)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start)
        for neighbor in self.graph_dict.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

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
print("Recorrido DFS:")
graph.dfs(start_node)
