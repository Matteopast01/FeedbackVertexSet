import sys
import os
from Experiment import Experiment
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from graph_generators.ErdosRenyiGenerator import ErdosRenyiGenerator
from python_implementation.GraphIO import GraphIO
import random

class RandomGraphExperiment(Experiment):
    _min_number_nodes : int 
    _max_number_nodes : int  
    _min_p : float 
    _max_p : float 
  

    def __init__(self, output_csv, min_number_nodes, max_number_nodes, min_p, max_p):
        super().__init__(output_csv)
        self._min_number_nodes = min_number_nodes
        self._max_number_nodes = max_number_nodes
        self._min_p = min_p
        self._max_p = max_p
    
    def generate_graphs(self):
        for i in range(4):
            number_node = random.randint(self._min_number_nodes, self._max_number_nodes)
            p = random.uniform(self._min_p, self._max_p)
            generator = ErdosRenyiGenerator(number_node, p)
            graph = generator.erdos_renyi_generator()
            graph_name = f"random_graph{i}.graph"
            my_dict = {"language": "", "graph_name": graph_name}
            self._graph_names.append(my_dict)
            writer = GraphIO(f"experimental_graphs/{graph_name}")
            writer.write_edge_list(graph)
        
