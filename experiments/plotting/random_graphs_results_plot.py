import matplotlib.pyplot as plt
import pandas as pd

# Load the data
all_data = pd.read_csv("../experimental_results/random_graphs.csv", sep=",")

# Get unique graph names
graph_names = all_data['Graph Name'].unique()

# Define markers and colors
markers = ['o', 's', 'D', '^', 'v']  # Different markers for each graph
colors = ['blue', 'red']  # Blue for Python, Red for C++

plt.figure(figsize=(12, 8))

for i, graph_name in enumerate(graph_names):
    graph_data = all_data[all_data['Graph Name'] == graph_name]

    # Separate the data by language
    python_data = graph_data[graph_data['Language'] == 'Python']
    cpp_data = graph_data[graph_data['Language'] == 'C++']

    # Create x-axis labels as a combination of nodes, edges, and FVS size
    x_labels = python_data.apply(lambda row: f'n={row["Number of Nodes"]}, m={row["Number of Edges"]}, k={int(row["Size FVS"])}', axis=1)

    # Plot Python data
    plt.plot(x_labels, python_data['Avg Elapsed Time'], 
             marker=markers[i % len(markers)], color=colors[0], label=f'Python: {graph_name}')
    
    # Plot C++ data
    plt.plot(x_labels, cpp_data['Avg Elapsed Time'], 
             marker=markers[i % len(markers)], color=colors[1], linestyle='--', label=f'C++: {graph_name}')

plt.xlabel('Graph (n: Nodes, m: Edges, k: FVS Size)')
plt.ylabel('Average Elapsed Time (seconds)')
plt.title('Performance Comparison between Python and C++ for Different Graphs')
plt.legend()
plt.yscale('log')  # Use a logarithmic scale if there's a large difference in time
plt.xticks(rotation=45, ha='right')  # Rotate x labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()
