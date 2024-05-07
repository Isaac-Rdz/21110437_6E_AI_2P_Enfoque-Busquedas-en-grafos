
class DecisionNode:
    def __init__(self, name, probabilities, children=None):
        self.name = name
        self.probabilities = probabilities
        self.children = children if children else []

class DecisionTree:
    def __init__(self):
        self.root = None

    def add_node(self, parent_name, node):
        if not self.root:
            self.root = node
        else:
            parent_node = self._find_node(self.root, parent_name)
            if parent_node:
                parent_node.children.append(node)
            else:
                print("Parent node not found.")

    def _find_node(self, current_node, name):
        if current_node.name == name:
            return current_node
        for child in current_node.children:
            result = self._find_node(child, name)
            if result:
                return result
        return None

    def expected_value(self, node):
        if not node.children:
            return 0  # Valor esperado para nodos finales
        else:
            expected_value = 0
            for i, child in enumerate(node.children):
                expected_value += node.probabilities[i] * self.expected_value(child)
            return expected_value

# Ejemplo de uso
root_node = DecisionNode("Inicio", [0, 0])  # Las probabilidades iniciales no tienen relevancia
decision_tree = DecisionTree()

# Definir los nodos de la red de decisión
distribuidor_node = DecisionNode("Distribuidor", [0.7, 0.3])
compra_mayorista_node = DecisionNode("Compra a Mayorista", [0.9, 0.1])
compra_minorista_node = DecisionNode("Compra a Minorista", [0.2, 0.8])
venta_mayorista_node = DecisionNode("Venta (Mayorista)", [0.6, 0.4])
venta_minorista_node = DecisionNode("Venta (Minorista)", [0.8, 0.2])

# Agregar nodos a la red de decisión
decision_tree.add_node("Inicio", distribuidor_node)
decision_tree.add_node("Distribuidor", compra_mayorista_node)
decision_tree.add_node("Distribuidor", compra_minorista_node)
decision_tree.add_node("Compra a Mayorista", venta_mayorista_node)
decision_tree.add_node("Compra a Minorista", venta_minorista_node)

# Calcular el valor esperado
expected_value = decision_tree.expected_value(root_node)
print("Valor esperado:", expected_value)
