#include <iostream>
#include <networkit/graph/Graph.hpp>
#include <vector>
#include "cycle_detection.h"

using namespace std;



bool dfs(NetworKit::Graph* graph, int u, int parent, vector<bool> *visited, vector<int>& cycleNodes) {
    (*visited)[u] = true;

    NetworKit::Graph::NeighborRange neighborRange = graph->neighborRange(u);

    for (NetworKit::Graph::NeighborIterator neighbor = neighborRange.begin(); neighbor != neighborRange.end(); ++neighbor) {
        int v = *neighbor;

        if (!(*visited)[v]) {
            if (dfs(graph, v, u, visited, cycleNodes)) {
                return true;
            }
        } else if (v != parent) {
            // Found a back edge, indicating a cycle
            cycleNodes.push_back(v);
            cycleNodes.push_back(u);
            return true;
        }
    }

    return false;
}


vector<int> findCycle(NetworKit::Graph* graph) {
    if (!graph) {
        // Handle the case where the pointer is null
        return {};
    }

    vector<int> cycleNodes;
    vector<bool>* visited = new vector<bool>(graph->numberOfNodes(), false);
    bool Found = false;

    for (int u = 0; u < graph->numberOfNodes(); ++u) {
        if (!(*visited)[u]) {
            if (dfs(graph, u, -1, visited, cycleNodes)) {
            	Found = true;
                }
        }
    }

    for (int node : cycleNodes){

    	cout << node << endl;
    }

    if (Found){
    	delete visited;
    	return cycleNodes;
	}

    delete visited;
    return {};  
}

/*
int main() {
    // Create an undirected graph
    NetworKit::Graph* graph = new NetworKit::Graph(10,false,false); // Replace 5 with the number of nodes in your graph
    graph->addEdge(0, 1);
    graph->addEdge(1, 2);
    graph->addEdge(2, 3);
    graph->addEdge(3, 4);
    graph->addEdge(4, 1); // Introducing a cycle
    graph->addEdge(4, 2);

    // Find nodes in the cycle
    vector<int> cycleNodes = findCycle(graph);


    if (!cycleNodes.empty()) {
        cout << "Nodes in the cycle: ";
        for (int node : cycleNodes) {
            cout << node << " ";
        }
        cout << endl;
    } else {
        cout << "No cycle found." << endl;
    }

    return 0;
}

*/