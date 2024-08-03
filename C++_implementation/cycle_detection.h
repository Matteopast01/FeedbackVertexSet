#ifndef GRAPH_CYCLE_H
#define GRAPH_CYCLE_H

#include <iostream>
#include <networkit/graph/Graph.hpp>
#include <vector>


void dfs(NetworKit::Graph* graph, int u, int parent, std::vector<int> *visited, std::vector<int> *cycle,  std::vector<std::vector<int>> *cycleNodes);
std::vector<std::vector<int>> findCycle(NetworKit::Graph* graph);

#endif 
