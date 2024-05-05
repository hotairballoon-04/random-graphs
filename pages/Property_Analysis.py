import streamlit as st
from utils.p_functions import p_functions
from utils.graph_properties import available_properties, calculate_expected_graph_properties, display_histogram, display_pie_chart


st.title("Detailed Graph Property Analysis")

st.sidebar.title("Configuration")

# Sidebar controls
n = st.sidebar.slider("Number of Nodes", 50, 1000, 250)

# Select p function
selected_function = st.sidebar.selectbox("Select Threshold Function", list(p_functions.keys()), index=5)

# Select number of simulations
n_simulations = st.sidebar.slider("Number of Simulations", 100, 1000, 500)

# Calculate probability based on selected function and display
p = p_functions[selected_function](n)
st.sidebar.write(f"Probability (p) based on {selected_function}: {p:.4f}")

selected_properties = st.multiselect("Select Graph Properties", available_properties, default=['isolated_vertices',])

properties = calculate_expected_graph_properties(n, p, n_simulations, properties=selected_properties)

# Create columns for dashboard view
num_cols = min(2, len(selected_properties))

columns = st.columns(num_cols)


for i, prop in enumerate(selected_properties):
    if prop == 'isolated_vertices':
        with columns[i % num_cols]:
            display_histogram(properties[prop], xlabel='#K1', ylabel='Frequency', title='Histogram of number of isolated vertices')
    if prop == 'average_degree':
        with columns[i % num_cols]:
            display_histogram(properties[prop], xlabel='d(G)', ylabel='Frequency', title='Histogram of average degree')
    if prop == 'connected':
        with columns[i % num_cols]:
            display_pie_chart({'Connected': properties[prop], 'Not Connected': 1 - properties[prop]}, title='Connected vs Not Connected')

