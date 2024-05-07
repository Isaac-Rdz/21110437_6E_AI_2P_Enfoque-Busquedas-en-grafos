
import random

class OnlineSearchAgent:
    def __init__(self):
        self.current_position = (0, 0)  # Posición inicial

    def move(self, maze):
        possible_moves = maze.get_possible_moves(self.current_position)
        if possible_moves:
            next_move = random.choice(possible_moves)
            self.current_position = next_move
            return next_move
        else:
            return None

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = set()

    def add_obstacle(self, position):
        self.obstacles.add(position)

    def get_possible_moves(self, position):
        possible_moves = []
        x, y = position
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) not in self.obstacles and 0 <= new_x < self.width and 0 <= new_y < self.height:
                    possible_moves.append((new_x, new_y))
        return possible_moves

# Ejemplo de uso
maze = Maze(10, 10)
maze.add_obstacle((1, 1))
maze.add_obstacle((2, 2))
maze.add_obstacle((3, 3))
maze.add_obstacle((4, 4))

agent = OnlineSearchAgent()
for _ in range(20):
    next_move = agent.move(maze)
    if next_move:
        print("El agente se mueve a la posición:", next_move)
    else:
        print("El agente no puede moverse más, ha alcanzado un callejón sin salida.")
        break
