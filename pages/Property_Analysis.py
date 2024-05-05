import streamlit as st
from utils.p_functions import p_functions
from utils.graph_properties import available_properties, calculate_expected_graph_properties, display_histogram


st.title("Detailed Graph Property Analysis")

# Sidebar controls
n = st.sidebar.slider("Number of Nodes", 50, 1000, 250)

# Select p function
selected_function = st.sidebar.selectbox("Select Threshold Function", list(p_functions.keys()))

# Select number of simulations
n_simulations = st.sidebar.slider("Number of Simulations", 100, 1000, 500)

# Calculate probability based on selected function and display
p = p_functions[selected_function](n)
st.sidebar.write(f"Probability (p) based on {selected_function}: {p:.4f}")

selected_properties = st.multiselect("Select Graph Properties", available_properties)

properties = calculate_expected_graph_properties(n, p, n_simulations, properties=selected_properties)

print(properties)

for prop in properties:
    if prop == 'isolated_vertices':
        display_histogram(properties[prop])

