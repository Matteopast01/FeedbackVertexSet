import sys
import os
from Experiment import Experiment
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from graph_generators.ErdosRenyiGenerator import ErdosRenyiGenerator
from python_implementation.GraphIO import GraphIO
import random

class RandomGraphExperiment(Experiment):
  

    def __init__(self, output_csv):
        super().__init__(output_csv)
    
    def generate_graphs(self):
        for i in range(5):
            number_node = random.randint(5000, 14999)
            p = random.uniform(0.005, 0.1)
            generator = ErdosRenyiGenerator(number_node, p)
            graph = generator.erdos_renyi_generator()
            graph_name = f"random_graph{i}.graph"
            my_dict = {"language": "", "graph_name": graph_name}
            self._graph_names.append(my_dict)
            writer = GraphIO(f"experimental_graphs/{graph_name}")
            writer.write_edge_list(graph)
        
