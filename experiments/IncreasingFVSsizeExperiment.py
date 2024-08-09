import sys
import os
from Experiment import Experiment
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from graph_generators.ErdosRenyiGenerator import ErdosRenyiGenerator
from python_implementation.GraphIO import GraphIO

class IncreasingFVSsizeExperiment(Experiment):

    _number_node : int  

    def __init__(self, number_node, output_csv):
        super().__init__(output_csv)
        self._number_node = number_node
    
    def generate_graphs(self):
        p = 1
        for i in range(10):
            generator = ErdosRenyiGenerator(self._number_node, p)
            graph = generator.erdos_renyi_generator()
            graph_name = f"doubling_fvs_{i}"
            my_dict = {"language": "", "graph_name": graph_name}
            self._graph_names.append(my_dict)
            writer = GraphIO(f"experimental_graphs/{graph_name}")
            writer.write_edge_list(graph)
            p /= 3
        
