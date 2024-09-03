import networkit as nk
import random

class AcyclicGraphGenerator:
    _number_nodes: int

    def __init__(self, number_nodes):
        self._number_nodes = number_nodes
    

    def generate(self):
        generator = nk.generators.ErdosRenyiGenerator(self._number_nodes + 100, 0.1)
        dense_graph = generator.generate()
        start_node = random.choice(range(dense_graph.numberOfNodes()))
        if dense_graph.numberOfNodes() < dense_graph.numberOfNodes():
            raise ValueError("The graph does not have enough nodes to extract a spanning tree.")
        visited = [False] * dense_graph.numberOfNodes()
        spanning_tree_edges = []
        bfs_queue = [start_node]
        visited[start_node] = True
        nodes_in_tree = 1
        node_mapping = {start_node: 0}  # Mapping of original node to new node index
        node_index = 1  # Start indexing for new nodes

        while bfs_queue and nodes_in_tree < self._number_nodes:
            u = bfs_queue.pop(0)
            for v in dense_graph.iterNeighbors(u):
                if not visited[v]:
                    visited[v] = True
                    bfs_queue.append(v)
                    spanning_tree_edges.append((u, v))
                    node_mapping[v] = node_index
                    node_index += 1
                    nodes_in_tree += 1
                    if nodes_in_tree >= self._number_nodes:
                        break
        
        # Create a new graph for the spanning tree
        spanning_tree = nk.graph.Graph(self._number_nodes, weighted=False, directed=False)
        
        # Add edges to the spanning tree with the new node indices
        for u, v in spanning_tree_edges:
            if u in node_mapping and v in node_mapping:
                new_u = node_mapping[u]
                new_v = node_mapping[v]
                if not spanning_tree.hasEdge(new_u, new_v):
                    spanning_tree.addEdge(new_u, new_v)
        
        return spanning_tree

       
            


            