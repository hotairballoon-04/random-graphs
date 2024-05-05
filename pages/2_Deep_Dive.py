import streamlit as st

with open('./src/deep_dive.md', 'r') as file:
    markdown_content = file.read()

st.title("Deep Dive: Exploring Erdős-Rényi Random Graphs")
st.markdown(markdown_content)
