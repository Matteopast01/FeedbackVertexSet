from networkit import graphio
import networkit as nk
class GraphReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_edges_format_graph(self):
        separator = ' '          # Separator for the edge list file
        first_node = 0           # Whether node numbering starts at 0
        comment_prefix = "#"     # Prefix for comment lines
        continuous = True        # Whether nodes are continuously numbered
        directed = False         # Whether the graph is directed

        reader = graphio.EdgeListReader(" ", 0, "#", True, False)
    	G = reader.read(self.file_path)
        
        return G