
import networkx as nx

def cut_conditioning(graph):
    best_cut = set()
    max_cut_size = 0

    while True:
        cut_found = False
        for edge in graph.edges():
            cut = set(edge)
            cut_size = nx.cut_size(graph, cut)
            if cut_size > max_cut_size:
                max_cut_size = cut_size
                best_cut = cut
                cut_found = True

        if not cut_found:
            break

        for node in best_cut:
            graph.remove_node(node)

    return max_cut_size

# Ejemplo de uso
G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)])
initial_cut_size = nx.cut_size(G, {(0, 1), (2, 3)})
print("Tamaño inicial del corte:", initial_cut_size)

cut_size = cut_conditioning(G)
print("Tamaño del corte después del acondicionamiento:", cut_size)
