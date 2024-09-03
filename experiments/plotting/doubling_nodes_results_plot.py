import matplotlib.pyplot as plt
import pandas as pd

# Load the data
all_data = pd.read_csv("../experimental_results/doubling_nodes_results.csv", sep=",")

# Separate the data by language
python_data = all_data[all_data['Language'] == 'Python']
cpp_data = all_data[all_data['Language'] == 'C++']

# Plot for Python
plt.figure(figsize=(10, 6))
plt.plot(python_data['Number of Nodes'], python_data['Avg Elapsed Time'], marker='o', color='blue')
plt.xlabel('Number of Nodes')
plt.ylabel('Average Elapsed Time (seconds)')
plt.title('Python:')
plt.ylim(python_data['Avg Elapsed Time'].min(), python_data['Avg Elapsed Time'].max())  # Auto-adjust y-axis to data range
plt.savefig('python_plot.png')  # Save plot to file

# Plot for C++
plt.figure(figsize=(10, 6))
plt.plot(cpp_data['Number of Nodes'], cpp_data['Avg Elapsed Time'], marker='o', color='red')
plt.xlabel('Number of Nodes')
plt.ylabel('Average Elapsed Time (seconds)')
plt.title('C++:')
plt.ylim(cpp_data['Avg Elapsed Time'].min(), cpp_data['Avg Elapsed Time'].max())  # Auto-adjust y-axis to data range
plt.savefig('cpp_plot.png')  # Save plot to file
