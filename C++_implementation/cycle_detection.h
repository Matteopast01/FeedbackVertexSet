#ifndef GRAPH_CYCLE_H
#define GRAPH_CYCLE_H

#include <iostream>
#include <networkit/graph/Graph.hpp>
#include <vector>

bool dfs(NetworKit::Graph* graph, int u, int parent, std::vector<bool>* visited, std::vector<int>& cycleNodes);
std::vector<int> findCycle(NetworKit::Graph* graph);

#endif // GRAPH_CYCLE_H
