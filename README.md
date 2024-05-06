# Random Graphs

This project is a python webpage that generates Erdős-Rényi random graphs, displays their properties, and visualizes key metrics such as degree distribution, connectivity, and more.
Its goal is to provide a user-friendly interface for exploring random graph theory and being a nice introduction to the topic.

Find a live demo of the project [here](https://random-graphs.streamlit.app).

## Features

- **Generate Erdős-Rényi graphs**: Generate random graphs where each pair of nodes has an independent probability of being connected an display the expected average graph.
- **Visualize graph properties**: Visualize key properties of the generated graph, such as degree distribution, connectivity, and more.
- **Learn about random graphs**: Explore the fundamentals of random graph theory and further resources in the section "Deep Dive".

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/hotairballoon-04/random-graphs.git
    ```

2. Navigate to the project directory:

    ```bash
    cd random-graphs
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run Random_Graphs.py
    ```

## Technologies
- [Python](https://www.python.org/): The backbone of the project, facilitating data analysis, graph generation, and visualization.
- [NetworkX](https://networkx.org/): A Python library for the creation, manipulation, and study of complex networks, forming the core of the graph generation process.
- [Matplotlib](https://matplotlib.org/): Utilized for creating visualizations of the generated graphs and their properties.
- [Streamlit](https://streamlit.io/): Empowering the interactive web interface for exploring random graph properties and visualizations.

## License
This project is licensed under the terms of the [MIT license](LICENSE.md).
