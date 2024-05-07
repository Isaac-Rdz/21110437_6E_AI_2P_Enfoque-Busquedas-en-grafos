
class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def add_edge(self, node, neighbor):
        if node not in self.graph_dict:
            self.graph_dict[node] = []
        self.graph_dict[node].append(neighbor)

    def bidirectional_search(self, start, goal):
        # Colas para la búsqueda desde el inicio y desde el objetivo
        queue_start = [start]
        queue_goal = [goal]
        visited_start = set([start])
        visited_goal = set([goal])

        while queue_start and queue_goal:
            # Búsqueda desde el inicio
            current_start = queue_start.pop(0)
            print("Desde el inicio:", current_start)
            if current_start in visited_goal:
                return True
            for neighbor in self.graph_dict.get(current_start, []):
                if neighbor not in visited_start:
                    visited_start.add(neighbor)
                    queue_start.append(neighbor)

            # Búsqueda desde el objetivo
            current_goal = queue_goal.pop(0)
            print("Desde el objetivo:", current_goal)
            if current_goal in visited_start:
                return True
            for neighbor in self.graph_dict.get(current_goal, []):
                if neighbor not in visited_goal:
                    visited_goal.add(neighbor)
                    queue_goal.append(neighbor)

        return False

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
print("Búsqueda bidireccional:")
result = graph.bidirectional_search(start_node, goal_node)
print("Se encontró un camino entre el nodo inicial y el objetivo:", result)
