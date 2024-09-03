import networkit as nk
import matplotlib.pyplot as plt
import networkx as nx
import sys
import os
import argparse
from GraphIO import GraphIO
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MyTimer import MyTimer

def draw_graph(G):
    G1 = nx.Graph()

    for i in range(G.numberOfNodes()):
        G1.add_node(i)

    for u, v in G.iterEdges():
        G1.add_edge(u, v)

    subax1 = plt.subplot(111)
    nx.draw(G1, with_labels=True, node_color='skyblue', edge_color='black', node_size=500, font_size=15)

    plt.show()


def find_cycles(G):
    cycles = []

    def dfs(v, parent, visited, cycle):
        visited.append(v)
        cycle.append(v)

        for u in G.iterNeighbors(v):
            if u != parent:
                if u in cycle:
                    cycles.append(list(cycle))
                elif u not in visited:
                    dfs(u, v, visited, cycle)

        cycle.remove(v)

    visited = []
    for v in G.iterNodes():
        if v not in visited:
            dfs(v, -1, visited, [])
    assert len(cycles) < G.numberOfNodes()

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
    assert max_degree >= 0
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
                X = naive_fvs(G, k - 1, F)
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
    assert max_degree_node >= 0
    G.removeNode(max_degree_node)
    X = naive_fvs(G, k - 1, F)
    if X != "no":
        return X.union({max_degree_node})
    else:
        return "no"


if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    k = 20000
    F = set()
    #F = F.union()

    parser = argparse.ArgumentParser(description='Process a graph file.')
    parser.add_argument('--graph', type=str, required=True, help='graph file')
    parser.add_argument('--experiment', action='store_true', help='Use experimental graphs')
    args = parser.parse_args()
    if args.experiment:
        graph_path = f"../experiments/experimental_graphs/{args.graph}"
    else:
        graph_path = f"../public_graphs/{args.graph}"

    
    graph_reader = GraphIO(graph_path)
    graph = graph_reader.read_edges_format_graph()
   
    timer = MyTimer()
    number_edges = graph.numberOfEdges()
    number_nodes = graph.numberOfNodes()
    fvs = naive_fvs(graph, k, F)
    elapsed_time = timer.get_elapsed_time()
    
    if fvs == "no":
        print(f"There is no FVS of size {k}")
    else:
        print("Feedback Vertex Set:", fvs)
        print("Size FVS:", len(fvs))

    print("number_edges:", number_edges)
    print("number_nodes:", number_nodes)
    print("elapsed_time:", elapsed_time)
   