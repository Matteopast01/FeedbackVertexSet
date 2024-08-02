#ifndef GRAPHREADER_HPP
#define GRAPHREADER_HPP

#include <networkit/graph/Graph.hpp>
#include <networkit/io/EdgeListReader.hpp>
#include <string>
using namespace std;

class GraphReader {
public:
    
    GraphReader(const string& filePath);

    NetworKit::Graph readEdgesFormatGraph() const;

private:
    string filePath;  
};

#endif 
