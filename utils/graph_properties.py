import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# available graph properties to choose from
available_properties = [
    'isolated_vertices',
    'average_degree',
    'degree_distribution',
    'connected',
    'components',
    'number_of_K4',
    'number_of_K5',

]


def display_histogram(data: np.array, xlabel: str, ylabel: str, title: str, scaling_parameter: int = 1):
    """
    Display histogram of data with given labels and title.
    """
    max_val = max(data)
    min_val = min(data)

    # If all values are the same, set bin size to 1 and extend the range
    if max_val == min_val:
        bin_size = 1
        min_val -= 1
        max_val += 1
    else:
        bin_size = (max_val - min_val) / 20.0

    num_bins = int((max_val - min_val) / bin_size)

    # Create histogram
    fig, ax = plt.subplots()
    ax.hist(data, bins=np.linspace(min_val, max_val, num_bins), rwidth=0.8, color='#A3E4D7', edgecolor='black')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    # If scaling parameter is not 1, scale the y-axis ticks. This is useful when displaying degree distribution.
    if scaling_parameter != 1:
        y_ticks = ax.get_yticks()
        scaled_y_ticks = [tick / scaling_parameter for tick in y_ticks]
        ax.set_yticklabels([f'{tick:.1f}' for tick in scaled_y_ticks])

    st.pyplot(fig)


def display_pie_chart(data: np.array, title: str):
    """
    Display pie chart of data with given title.
    """
    fig, ax = plt.subplots()
    ax.pie(data.values(), labels=data.keys(), colors=['#5499C7', '#A3E4D7'] ,autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title(title)
    st.pyplot(fig)


def number_of_isolated_vertices(graph: nx.Graph) -> int:
    """
    Calculate the number of isolated vertices in a graph.
    """
    return len([node for node in graph.nodes() if graph.degree(node) == 0])


def calculate_expected_graph_properties(n: int, p: float, n_simulations: int, properties: list) -> dict:
    """
    Calculate expected graph properties for a random graph with n nodes and probability p.
    """
    assert set(properties) <= set(available_properties), f"Invalid property name. Available properties: {available_properties}"

    calculated_properties = {}
    if properties:
        random_graphs = [nx.erdos_renyi_graph(n, p) for _ in range(n_simulations)]

        for prop in properties:
            if prop == 'isolated_vertices':
                calculated_properties[prop] = [number_of_isolated_vertices(graph) for graph in random_graphs]
            elif prop == 'average_degree':
                calculated_properties[prop] = [2 * graph.number_of_edges() / graph.number_of_nodes() for graph in random_graphs]
            elif prop == 'degree_distribution':
                calculated_properties[prop] = [degree[1] for graph in random_graphs for degree in graph.degree()]
            elif prop == 'connected':
                calculated_properties[prop] = sum([nx.is_connected(graph) for graph in random_graphs]) / n_simulations
            elif prop == 'components':
                calculated_properties[prop] = [nx.number_connected_components(graph) for graph in random_graphs]
            elif prop == 'number_of_K4':
                calculated_properties[prop] = [len([clique for clique in nx.find_cliques(graph) if len(clique) == 4]) for graph in random_graphs]
            elif prop == 'number_of_K5':
                calculated_properties[prop] = [len([clique for clique in nx.find_cliques(graph) if len(clique) == 5]) for graph in random_graphs]

    return calculated_properties
