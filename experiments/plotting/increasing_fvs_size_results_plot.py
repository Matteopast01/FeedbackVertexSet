import matplotlib.pyplot as plt
import pandas as pd

# Load the data
all_data = pd.read_csv("../experimental_results/improving_fvs_size_results.csv", sep=",")

# Separate the data by language
python_data = all_data[all_data['Language'] == 'Python']
cpp_data = all_data[all_data['Language'] == 'C++']

# Plot for Python
plt.figure(figsize=(10, 6))
plt.plot(python_data['Size FVS'], python_data['Avg Elapsed Time'], marker='o', color='blue')
plt.xlabel('FVS Size')
plt.ylabel('Average Elapsed Time (seconds)')
plt.title('Python:')
plt.ylim(python_data['Avg Elapsed Time'].min(), python_data['Avg Elapsed Time'].max())  # Auto-adjust y-axis to data range
plt.show()

# Plot for C++
plt.figure(figsize=(10, 6))
plt.plot(cpp_data['Size FVS'], cpp_data['Avg Elapsed Time'], marker='o', color='red')
plt.xlabel('FVS Size')
plt.ylabel('Average Elapsed Time (seconds)')
plt.title('C++:')
plt.ylim(cpp_data['Avg Elapsed Time'].min(), cpp_data['Avg Elapsed Time'].max())  # Auto-adjust y-axis to data range
plt.show()
