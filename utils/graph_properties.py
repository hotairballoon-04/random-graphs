import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

available_properties = [
    'isolated_vertices',
    'average_degree',
    'connected',
]


def display_histogram(data):
    # Plot histogram
    fig, ax = plt.subplots()
    ax.hist(data, bins=np.arange(min(data), max(data) + 1.5) - 0.5, rwidth=0.8, color='skyblue', edgecolor='black')
    ax.set_xticks(np.arange(min(data), max(data) + 1))
    ax.set_xlabel('Number of Isolated Vertices')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Number of Isolated Vertices')
    st.pyplot(fig)


def number_of_isolated_vertices(graph):
    return len([node for node in graph.nodes() if graph.degree(node) == 0])


def calculate_expected_graph_properties(n, p, n_simulations, properties=available_properties):
    assert set(properties) <= set(available_properties), f"Invalid property name. Available properties: {available_properties}"

    calculated_properties = {}

    random_graphs = [nx.erdos_renyi_graph(n, p) for _ in range(n_simulations)]

    for prop in properties:
        if prop == 'isolated_vertices':
            calculated_properties[prop] = [number_of_isolated_vertices(graph) for graph in random_graphs]
        elif prop == 'average_degree':
            calculated_properties[prop] = [2 * graph.number_of_edges() / graph.number_of_nodes() for graph in random_graphs]
        elif prop == 'connected':
            calculated_properties[prop] = sum([nx.is_connected(graph) for graph in random_graphs]) / n_simulations

    return calculated_properties
