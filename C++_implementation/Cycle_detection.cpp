#include <iostream>
#include <networkit/graph/Graph.hpp>
#include <vector>
#include "cycle_detection.h"

using namespace std;



void dfs(NetworKit::Graph* graph, int u, int parent, vector<int> *visited, vector<int> *cycle,  vector<vector<int>> *cycleNodes) {
    visited->push_back(u);
    cycle->push_back(u);

    NetworKit::Graph::NeighborRange neighborRange = graph->neighborRange(u);
    for (NetworKit::Graph::NeighborIterator neighbor = neighborRange.begin(); neighbor != neighborRange.end(); ++neighbor) {
        if (*neighbor != parent){

            if (find(cycle->begin(), cycle->end(), *neighbor) != cycle->end())
            {
                cycleNodes->push_back(*cycle);
            }
            else if(find(visited->begin(), visited->end(), *neighbor) == visited->end()){

                dfs(graph, *neighbor, u, visited, cycle, cycleNodes);


            }
        }
    }
    cycle->erase(std::remove(cycle->begin(), cycle->end(), u), cycle->end());
}


// Function to find a cycle in the graph
vector<vector<int>> findCycle(NetworKit::Graph* graph) {
   

    vector<vector<int>> *cycleNodes = new vector<vector<int>>;
    vector<int> *visited =  new vector<int>;   

    NetworKit::Graph::NodeRange nodeRange = graph->nodeRange();
    for (NetworKit::Graph::NodeIterator it = nodeRange.begin(); it != nodeRange.end(); ++it) {
        if (find(visited->begin(), visited->end(), *it) == visited->end()) {
            vector<int> *cycle = new vector<int>;
            dfs(graph, *it, -1, visited, cycle, cycleNodes);
        }
    }
    return *cycleNodes;  
}

