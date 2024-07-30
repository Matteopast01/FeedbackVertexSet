import networkit as nk
import matplotlib.pyplot as plt


def find_cycles(graph):
    cycles = []

    def dfs(v, parent, visited, cycle):
        visited.add(v)
        cycle.add(v)

        for u in graph.iterNeighbors(v):
            if u != parent:
                if u in cycle:
                    cycles.append(list(cycle))
                elif u not in visited:
                    dfs(u, v, visited, cycle)

        cycle.remove(v)

    visited = set()
    for v in graph.iterNodes():
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
    for v in list(G.iterNodes()):  # Iterate over a copy of the node list
        if G.degree(v) < 2:
            G.removeNode(v)
            if v in F:
                F.remove(v)
                return naive_fvs(G, k, F)

    # Remove vertices with two neighbors in the same component of G[F]
    for v in list(G.iterNodes()):  # Iterate over a copy of the node list
        neighbors = set(G.iterNeighbors(v))
        neighbors_in_F = neighbors.intersection(F)
        if v not in F and len(neighbors_in_F) == 2:
            G.removeNode(v)
            X = naive_fvs(G, k - 1, F)
            return X.union({v})



    max_degree_node, max_degree = provide_node_with_maximum_degree(G, F)
   

    if  max_degree == 2:
        X = set()
        while True:
            cycles = find_cycles(G)
            print(cycles)
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

    if max_degree_node != None:
        G.removeNode(max_degree_node)
    X = naive_fvs(G, k - 1, F)
    if X != "no":
        if max_degree_node != None:
            return X.union({max_degree_node})
        return X
    else:
        if max_degree_node != None:
            F = F.union({max_degree_node})
        return naive_fvs(G, k, F)




if __name__ =="__main__":
    
    G = nk.Graph(100)

    # Aggiunta dei nodi
    for i in range(100):
        G.addNode()

    # Aggiunta degli archi per formare cicli
    G.addEdge(0, 1)
    G.addEdge(1, 2)
    G.addEdge(2, 3)
    G.addEdge(3, 4)
    G.addEdge(4, 0)

    G.addEdge(5, 6)
    G.addEdge(6, 7)
    G.addEdge(7, 8)
    G.addEdge(8, 9)
    G.addEdge(9, 5)



    k = 15
    F = set()
    fvs = naive_fvs(G, k,F)

    print("Feedback Vertex Set:", fvs)
