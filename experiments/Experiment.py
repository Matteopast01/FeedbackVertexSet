import subprocess
import re
import csv
import statistics
from abc import ABC, abstractmethod

class Experiment(ABC):
    # Define protected attributes
    _graph_names: list
    _results: list
    _output_csv: str

    def __init__(self, output_csv):
        self._graph_names = []  # Protected attribute initialized in constructor
        self._results = []  # Protected attribute initialized in constructor
        self._output_csv = output_csv  # Protected attribute initialized in constructor

    def parse_output(self, output):
        fvs_pattern = r"Feedback Vertex Set: (\{[^\}]*\})"
        size_pattern = r"Size FVS: (\d+)"
        edges_pattern = r"number_edges: (\d+)"
        nodes_pattern = r"number_nodes: (\d+)"
        time_pattern = r"elapsed_time: ([\d\.eE\-]+)"

        fvs_match = re.search(fvs_pattern, output)
        size_match = re.search(size_pattern, output)
        edges_match = re.search(edges_pattern, output)
        nodes_match = re.search(nodes_pattern, output)
        time_match = re.search(time_pattern, output)

        parsed_data = {
            "fvs_set": fvs_match.group(1) if fvs_match else "", 
            "size_fvs": int(size_match.group(1)) if size_match else "",
            "number_edges": int(edges_match.group(1)) if edges_match else "",
            "number_nodes": int(nodes_match.group(1)) if nodes_match else "",
            "elapsed_time": float(time_match.group(1)) if time_match else ""
        }
        return parsed_data

    def execute_and_retrieve_data(self, language, graph_name, number_repetitions):
        trials = []

        if language == "python":
            for _ in range(number_repetitions):
                python_result = subprocess.run(
                    ['python3', '../python_implementation/FVS.py', "--graph", graph_name, "--experiment"],
                    stdout=subprocess.PIPE, text=True
                ).stdout
                parsed_python = self.parse_output(python_result)
                trials.append(parsed_python["elapsed_time"])
            avg_python_time = sum(trials) / number_repetitions
            std_python_time = statistics.stdev(trials) if len(trials) > 1 else 0
            return ["Python", graph_name, parsed_python["size_fvs"], parsed_python["number_edges"], parsed_python["number_nodes"], avg_python_time, std_python_time]
        else:
            for _ in range(number_repetitions):
                cpp_result = subprocess.run(
                    ['../C++_implementation/FVS', "--graph", graph_name, "--experiment"],
                    stdout=subprocess.PIPE, text=True
                ).stdout
                parsed_cpp = self.parse_output(cpp_result)
                trials.append(parsed_cpp["elapsed_time"])
            avg_cpp_time = sum(trials) / number_repetitions
            std_cpp_time = statistics.stdev(trials) if len(trials) > 1 else 0
            return ["C++", graph_name, parsed_cpp["size_fvs"], parsed_cpp["number_edges"], parsed_cpp["number_nodes"], avg_cpp_time, std_cpp_time]

    def iterate_over_test_graphs(self):
        for graph in self._graph_names:
            if graph["language"] == "":
                self._results.append(self.execute_and_retrieve_data("python", graph["graph_name"], 3))
            self._results.append(self.execute_and_retrieve_data("c++", graph["graph_name"], 3))

    def save_test_results(self):
        with open(self._output_csv, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Language", "Graph Name", "Size FVS", "Number of Edges", "Number of Nodes", "Avg Elapsed Time", "Std Elapsed Time"])
            writer.writerows(self._results)
        print(f"Results have been written to {self._output_csv}")

    @abstractmethod
    def generate_graphs(self, *args, **kwargs):
        """Abstract method to be implemented by subclasses for graph generation."""
        pass

    def run(self, *args, **kwargs):
        """Method to generate graphs, run experiments, and save the results."""
        self.generate_graphs(*args, **kwargs)
        self.iterate_over_test_graphs()
        self.save_test_results()
