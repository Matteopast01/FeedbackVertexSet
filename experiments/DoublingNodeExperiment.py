import sys
import os
from Experiment import Experiment
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from graph_generators.AcyclicGraphGenerator import AcyclicGraphGenerator
from python_implementation.GraphIO import GraphIO

class DoublingNodeExperiment(Experiment):

    _starting_number_node : int 
    _max_number_node : int

    def __init__(self, starting_number_node, max_number_node, output_csv):
        super().__init__(output_csv)
        self._starting_number_node = starting_number_node
        self._max_number_node = max_number_node
    
    def generate_graphs(self):
        number_node = self._starting_number_node
        while number_node < self._max_number_node:
            generator = AcyclicGraphGenerator(number_node)
            graph = generator.generate()
            graph_name = f"doubling_{number_node}.graph"
            my_dict = {"language": "only C++" if number_node > 15000 else "", "graph_name": graph_name}
            self._graph_names.append(my_dict)
            writer = GraphIO(f"experimental_graphs/{graph_name}")
            writer.write_edge_list(graph)
            number_node *= 2
        
