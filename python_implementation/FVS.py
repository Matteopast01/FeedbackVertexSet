import networkit as nk
import matplotlib.pyplot as plt
import threading
import networkx as nx
from networkit import graphio
import sys

def draw_graph(G):

    G1 = nx.Graph()

    for i in range(G.numberOfNodes()):
        G1.add_node(i)

    for u, v in G.iterEdges():
        G1.add_edge(u,v)


    subax1 = plt.subplot(111)
    nx.draw(G1, with_labels=True, node_color='skyblue', edge_color='black', node_size=500, font_size=15)

    plt.show()
    



def find_cycles(G):
    cycles = []

    def dfs(v, parent, visited, cycle):
        visited.add(v)
        cycle.add(v)

        for u in G.iterNeighbors(v):
            if u != parent:
                if u in cycle:
                    cycles.append(list(cycle))
                elif u not in visited:
                    dfs(u, v, visited, cycle)

        cycle.remove(v)

    visited = set()
    for v in G.iterNodes():
        if v not in visited:
            dfs(v, -1, visited, set())

    return cycles


def provide_node_with_maximum_degree(G, F):
    max_degree_node = None
    max_degree = -1

    for node in G.iterNodes():
        if node not in F:
            degree = G.degree(node)
            if degree > max_degree:
                max_degree = degree
                max_degree_node = node

    return max_degree_node, max_degree


def naive_fvs(G, k, F):
    if k < 0:
        return "no"
    if G.numberOfNodes() == 0:
        return set()

    # Remove vertices with degree less than two
    for v in list(G.iterNodes()): 
        if G.degree(v) < 2:
            G.removeNode(v)
            if v in F:
                F.remove(v)
            return naive_fvs(G, k, F)

    # Remove vertices with two neighbors in the same component of G[F]
    for v in list(G.iterNodes()):
        if v not in F: 
            neighbors = set(G.iterNeighbors(v))
            neighbors_in_F = neighbors.intersection(F)
            if len(neighbors_in_F) == 2:
                G.removeNode(v)
                X = naive_fvs(G, k-1, F)
                if X != "no":
                    return X.union({v})
                else: 
                    return "no"

    max_degree_node, max_degree = provide_node_with_maximum_degree(G, F)

    if max_degree == 2:
        X = set()
        while True:
            cycles = find_cycles(G)
            if len(cycles) == 0:
                break
            cycle = cycles[0]
            x = next(v for v in cycle if v not in F)
            X.add(x)
            G.removeNode(x)
        if len(X) <= k:
            return X
        else:
            return "no"

    G.removeNode(max_degree_node)
    X = naive_fvs(G, k - 1, F)
    if X != "no":
        return X.union({max_degree_node})
    else:
        return "no"


if __name__ == "__main__":

    
    #to improve recursion
    sys.setrecursionlimit(100000)
    
    reader = graphio.EdgeListReader(" ", 0, "#", True, False)
    G = reader.read("../public_graphs/037.graph")
   
    k = 1000
    F = set()
    F = F.union()
    fvs = naive_fvs(G, k, F)

    print("Feedback Vertex Set:", fvs)
    print ("size:" + str(len(fvs)))
    
