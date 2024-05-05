import streamlit as st
from utils.p_functions import p_functions
from utils.graph_properties import available_properties, calculate_expected_graph_properties, display_histogram, display_pie_chart


st.title("Detailed Graph Property Analysis")

# Sidebar controls
n = st.sidebar.slider("Number of Nodes", 50, 1000, 250)

# Select p function
selected_function = st.sidebar.selectbox("Select Threshold Function", list(p_functions.keys()), index=3)

# Select number of simulations
n_simulations = st.sidebar.slider("Number of Simulations", 100, 1000, 500)

# Calculate probability based on selected function and display
p = p_functions[selected_function](n)
st.sidebar.write(f"Probability (p) based on {selected_function}: {p:.4f}")

selected_properties = st.multiselect("Select Graph Properties", available_properties, default=['isolated_vertices',])

properties = calculate_expected_graph_properties(n, p, n_simulations, properties=selected_properties)


for prop in properties:
    if prop == 'isolated_vertices':
        display_histogram(properties[prop], xlabel='#Isolated Vertices', ylabel='Frequency', title='Histogram of number of isolated vertices')
    if prop == 'average_degree':
        display_histogram(properties[prop], xlabel='Average Degree', ylabel='Frequency', title='Histogram of average degree')
    if prop == 'connected':
        display_pie_chart({'Connected': properties[prop], 'Not Connected': 1 - properties[prop]}, title='Connected vs Not Connected')

