#include "GraphReader.h"
#include <iostream>
using namespace std;

GraphReader::GraphReader(const string& filePath) {
    this->filePath = filePath; 
}


 NetworKit::Graph GraphReader::readEdgesFormatGraph() const {
    
    char separator = ' ';        
    int firstNode = 0;           
    string commentPrefix = "#"; 
    bool continuous = true;      
    bool directed = false;      

    
    NetworKit::EdgeListReader reader(separator, firstNode, commentPrefix, continuous, directed);

    
    NetworKit::Graph graph = reader.read(filePath);

    return graph;
}
