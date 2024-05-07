import networkx as nx
import numpy as np


def calculate_average_degree_sequence(graphs: list[nx.Graph]) -> list[int]:
    degree_sequences = [sorted(list(dict(graph.degree()).values()), reverse=True) for graph in graphs]
    avg_degree_sequence = np.mean(degree_sequences, axis=0)

    return [round(degree) for degree in avg_degree_sequence]


def find_closest_valid_degree_sequence(avg_degree_sequence: list) -> list:
    """Finds the closest valid degree sequence to the average degree sequence using the Erdös-Gallai theorem."""

    avg_degree_sequence = sorted(avg_degree_sequence, reverse=True)

    if sum(avg_degree_sequence) % 2 != 0:
        avg_degree_sequence[0] -= 1

    sequence_valid = False

    while not sequence_valid:
        sequence_valid = True
        for k in range(1, len(avg_degree_sequence) + 1):
            sum_left = sum(avg_degree_sequence[1:k + 1])
            sum_right = k * (k - 1) + sum(
                min(avg_degree_sequence[i], k) for i in range(k + 1, len(avg_degree_sequence)))
            if sum_left > sum_right:
                avg_degree_sequence[np.argmax(avg_degree_sequence)] -= 1
                avg_degree_sequence[np.argmin(avg_degree_sequence)] += 1
                sequence_valid = False
                break

    closest_sequence = avg_degree_sequence
    return closest_sequence


def construct_graph_from_degree_sequence(degree_sequence: list) -> nx.Graph:
    """Constructs a random simple graph from a given degree sequence using the configuration model."""

    # Create an empty graph
    graph = nx.Graph()

    # Add nodes with degrees specified by the degree sequence
    for node, degree in enumerate(degree_sequence):
        graph.add_node(node)

    # Create a list of stubs (half-edges) for each node
    stubs = [node for node, degree in enumerate(degree_sequence) for _ in range(degree)]

    # Shuffle the stubs to create randomness
    np.random.shuffle(stubs)

    # Pair the stubs to form edges, avoiding self-loops and parallel edges
    while len(stubs) > 1:
        stub1 = stubs.pop()
        stub2 = np.random.choice(stubs)

        # Ensure no self-loops or parallel edges
        if stub1 != stub2 and not graph.has_edge(stub1, stub2):
            graph.add_edge(stub1, stub2)
            stubs.remove(stub2)

    return graph


def generate_expected_graph(n: int, p: float, n_simulations: int = 1000) -> nx.Graph:
    """Generates a random graph with the expected degree sequence of an Erdős-Rényi graph with parameters n and p."""

    # Generate a random graphs
    random_graphs = [nx.erdos_renyi_graph(n, p) for _ in range(n_simulations)]

    # Calculate the average degree sequence
    avg_degree_sequence = calculate_average_degree_sequence(random_graphs)

    # Find the closest valid degree sequence
    closest_sequence = find_closest_valid_degree_sequence(avg_degree_sequence)

    # Construct a graph from the closest valid degree sequence
    expected_graph = construct_graph_from_degree_sequence(closest_sequence)

    return expected_graph
