import networkit as nk
from random import choice, randint
import networkx as nx
import matplotlib.pyplot as plt

class CustomGenerator:
    _number_nodes: int
    _number_edges: int
    _connected: bool

    def __init__(self, number_nodes, number_edges, connected):
        self._number_nodes = number_nodes
        self._number_edges = number_edges
        self._connected = connected

    def custom_generator(self):
        # Check if the graph can be connected and if m is within valid range
        if self._number_edges < self._number_nodes - 1 and self._connected:
            raise ValueError('Graph must have at least n-1 edges to be connected')
        if self._number_edges > self._number_nodes * (self._number_nodes - 1) / 2:
            raise ValueError('Graph can have at most n*(n-1)/2 edges')
        # Initialize the graph
        G = nk.graph.Graph()
        G.addNodes(self._number_nodes)
        
        # Step 1: Connect nodes to ensure the graph is connected
        added_nodes = []
        number_edges = 0
        for node in G.iterNodes():
            if len(added_nodes) == 0:
                added_nodes.append(node)
            else:
                u = choice(added_nodes)
                # Ensure no self-loop is added
                if u != node:
                    G.addEdge(u, node)
                    added_nodes.append(node)
                    number_edges += 1
        
        # Step 2: Add additional edges
        while number_edges < self._number_edges:
            nodes = list(G.iterNodes())
            while len(nodes) > 0 and number_edges < self._number_edges:
                v = nodes.pop(randint(0, len(nodes) - 1))
                v_neighbors = [neighbor for neighbor in G.iterNeighbors(v)]
                possible_nodes = [node for node in G.iterNodes() if node != v and node not in v_neighbors]
                if len(possible_nodes) > 0:
                    u = choice(possible_nodes)
                    G.addEdge(u, v)
                    number_edges += 1
        
        return G
