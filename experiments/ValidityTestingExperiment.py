import sys
import os
from Experiment import Experiment
import subprocess
import re
import csv
import statistics
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class ValidityTestingExperiment(Experiment):
  

    def __init__(self, output_csv):
        super().__init__(output_csv)
    
    def read_public_graphs(self):
            path = "../public_graphs/"
            file_names = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
            for file in file_names:
                my_dict = {}
                my_dict["language"] = ""
                my_dict["graph_name"] = file
                self._graph_names.append(my_dict)


    def execute_and_retrieve_data(self, language, graph_name, number_repetitions):
        trials = []

        if language == "python":
            for _ in range(number_repetitions):
                python_result = subprocess.run(
                    ['python3', '../python_implementation/FVS.py', "--graph", graph_name],
                    stdout=subprocess.PIPE, text=True
                ).stdout
                parsed_python = self.parse_output(python_result)
                trials.append(parsed_python["elapsed_time"])
            avg_python_time = sum(trials) / number_repetitions
            std_python_time = statistics.stdev(trials) if len(trials) > 1 else 0
            return ["Python", graph_name, parsed_python["size_fvs"], parsed_python["fvs_set"], parsed_python["number_edges"], parsed_python["number_nodes"], avg_python_time]
        else:
            for _ in range(number_repetitions):
                cpp_result = subprocess.run(
                    ['../C++_implementation/FVS', "--graph", graph_name],
                    stdout=subprocess.PIPE, text=True
                ).stdout
                parsed_cpp = self.parse_output(cpp_result)
                trials.append(parsed_cpp["elapsed_time"])
            avg_cpp_time = sum(trials) / number_repetitions
            std_cpp_time = statistics.stdev(trials) if len(trials) > 1 else 0
            return ["C++", graph_name,parsed_cpp["size_fvs"],parsed_cpp["fvs_set"], parsed_cpp["number_edges"], parsed_cpp["number_nodes"],avg_cpp_time]

    def generate_graphs(self):
        pass

    def save_test_results(self):
        with open(f"experimental_results/{self._output_csv}", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Language", "Graph Name", "Size FVS", "FVS set", "Number of Edges", "Number of Nodes", "Avg Elapsed Time"])
            writer.writerows(self._results)
        print(f"Results have been written to {self._output_csv}")

    def run(self, *args, **kwargs):
        """Method to generate graphs, run experiments, and save the results."""
        self.read_public_graphs()
        self.iterate_over_test_graphs()
        self.save_test_results()

           