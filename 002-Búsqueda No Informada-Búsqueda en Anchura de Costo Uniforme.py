
import heapq

class Node:
    def __init__(self, state, cost, path):
        self.state = state
        self.cost = cost
        self.path = path

    def __lt__(self, other):
        return self.cost < other.cost

def uniform_cost_search(graph, start, goal):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, Node(start, 0, [start]))

    while priority_queue:
        current_node = heapq.heappop(priority_queue)
        current_state, current_cost, current_path = current_node.state, current_node.cost, current_node.path

        if current_state == goal:
            return current_path

        if current_state not in visited:
            visited.add(current_state)

            for neighbor, neighbor_cost in graph[current_state].items():
                new_cost = current_cost + neighbor_cost
                heapq.heappush(priority_queue, Node(neighbor, new_cost, current_path + [neighbor]))

# Ejemplo de uso
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
goal_node = 'D'

path = uniform_cost_search(graph, start_node, goal_node)
print("Camino encontrado:", path)
