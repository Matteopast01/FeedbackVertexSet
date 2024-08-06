import networkit as nk
from networkit import graphio

class GraphIO:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_edges_format_graph(self):
        separator = ' '          # Separator for the edge list file
        first_node = 0           # Whether node numbering starts at 0
        comment_prefix = "#"     # Prefix for comment lines
        continuous = True        # Whether nodes are continuously numbered
        directed = False         # Whether the graph is directed

        reader = graphio.EdgeListReader(separator, first_node, comment_prefix, continuous, directed)
        G = reader.read(self.file_path)
        
        return G

    def write_edge_list(self, graph):
        with open(self.file_path, 'w') as f:
            for u, v in graph.iterEdges():
                f.write(f"{u} {v}\n")
