import streamlit as st

with open('./src/about.md', 'r') as file:
    markdown_content = file.read()

st.title("About this project")
st.markdown(markdown_content)
