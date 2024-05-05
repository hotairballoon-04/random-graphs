import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from utils.p_functions import p_functions
from utils.graph_generation import generate_expected_graph


def display_graph(graph):
    fig, ax = plt.subplots()
    nx.draw(graph, with_labels=True, ax=ax)
    st.pyplot(fig)



def main():

    st.set_page_config(
        page_title="Random Graphs",
        page_icon="√"
    )

    st.title("Random Graphs")
    st.info("""
    This app generates [Erdős–Rényi random graphs](https://en.wikipedia.org/wiki/Erdős–Rényi_model) and calculates the
    expected graph based on the average degree sequence.
    Use the sidebar to control the number of nodes and the probability function to control the look of the graph.
    """)

    # Sidebar controls
    n = st.sidebar.slider("Number of Nodes", 10, 100, 20)

    # Select p function
    selected_function = st.sidebar.selectbox("Select Threshold Function", list(p_functions.keys()), index=3)

    # Calculate probability based on selected function and display
    p = p_functions[selected_function](n)
    st.sidebar.write(f"Probability (p) based on {selected_function}: {p:.4f}")

    # Generate a random graph
    graph = generate_expected_graph(n, p)

    # Display the graph
    display_graph(graph)


if __name__ == "__main__":
    main()