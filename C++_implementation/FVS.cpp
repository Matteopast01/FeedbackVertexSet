#include <iostream>
#include <boost/program_options.hpp>
#include <omp.h>
#include <networkit/graph/Graph.hpp>
#include <vector>
#include <set>
#include <string>
#include "cycle_detection.h"
#include "GraphReader.h"
#include "mytimer.h"

using namespace std;
namespace po = boost::program_options;

void printVector(const vector<int>* vec) {
    
    cout << "{";
    for (size_t i = 0; i < vec->size(); ++i) {
        cout << (*vec)[i];
        if (i != vec->size() - 1) {
            cout << ", ";
        }
    }
    cout << "}" << endl;
}

vector<int> provide_node_with_maximum_degree (NetworKit::Graph* graph, set<int>* F, NetworKit::Graph::NodeRange nodeRange){
	int maxDegree = 0;
    int NodeMaxDegree = -1;

    for (NetworKit::Graph::NodeIterator node = nodeRange.begin(); node != nodeRange.end(); ++node) {
    	
	    if (F->find(*node) == F->end()) {
	    	if (graph->degree(*node) > maxDegree){
	    		NodeMaxDegree = *node;
	    		maxDegree = graph->degree(*node);
			}	
		}
	}
    vector<int> *maximum_degree_information = new vector<int>;
    maximum_degree_information->push_back(maxDegree);
    maximum_degree_information->push_back(NodeMaxDegree);
    return *maximum_degree_information;
}


vector<int> naive_fvs (NetworKit::Graph* graph, int k, set<int>* F ) {

	vector<int> *result = new vector<int>;
	vector<int> myfvs;

	if (k < 0){
		result->push_back(-1);
		return *result;
	}

	if (graph->numberOfNodes() == 0) {
		return *result;
	}

	NetworKit::Graph::NodeRange nodeRange = graph->nodeRange();

	for (NetworKit::Graph::NodeIterator it = nodeRange.begin(); it != nodeRange.end(); ++it) {
  
         if (graph->degree(*it) < 2 ){
	         	graph->removeNode(*it);
	         	F->erase(*it);
	         	return naive_fvs(graph,k,F);	        
         }
    }

    for (NetworKit::Graph::NodeIterator node = nodeRange.begin(); node != nodeRange.end(); ++node) {
    	
	    if (F->find(*node) == F->end()) {
	    	
	    	NetworKit::Graph::NeighborRange neighborRange = graph->neighborRange(*node);
	    	int neighborCount = 0;       	 

	    	for (NetworKit::Graph::NeighborIterator neighbor = neighborRange.begin(); neighbor != neighborRange.end(); ++neighbor) {

			    if (F->find(*neighbor) != F->end()) {
			    	neighborCount ++;   
			    } 
				if (neighborCount == 2){
					graph->removeNode(*node);
					myfvs = naive_fvs(graph,k-1,F);
					if (find(myfvs.begin(), myfvs.end(), -1) == myfvs.end()){

				    	myfvs.push_back(*node);
						return myfvs;
				    }
				    else
				    {

				    	result->push_back(-1);
						return *result;
				    }				
				}   		 
	    	}
    	}       
    }
   
    vector<int> maximum_degree_information = provide_node_with_maximum_degree(graph, F, nodeRange);
	if (maximum_degree_information[0] == 2){

		vector<vector<int>> nodesCycle;
		vector<int> *X = new vector<int>;

		while (true){

			nodesCycle = findCycle(graph);
			if (nodesCycle.size() == 0){
				break;
			}

			for (int node : nodesCycle[0]){

				if (F->find(node) == F->end()){
				
					X->push_back(node);
					graph->removeNode(node);
					break;
				} 
	 		}		
		}
		if (X->size()<=k){
			return *X;
		}
		else 
		{
			result->push_back(-1);
			return *result;
		}
	}

	graph->removeNode(maximum_degree_information[1]);
    myfvs = naive_fvs(graph,k-1,F);

    if (find(myfvs.begin(), myfvs.end(), -1) == myfvs.end()){

    	myfvs.push_back(maximum_degree_information[1]);
    	return myfvs;
    }  
	    
    else {
			result->push_back(-1);
			return *result;
		}
}
  
int main(int argc, char** argv) {
 
 	set<int> *F = new set <int>;
 	po::options_description desc("Allowed options");
    desc.add_options()
        ("help", "produce help message")
                ("experiment", po::value<bool>()->default_value(false)->implicit_value(true), "optional experiment flag")
        ("graph", po::value<string>(), "set graph file");

    po::variables_map vm;
    po::store(po::parse_command_line(argc, argv, desc), vm);
    po::notify(vm);

    if (vm.count("help")) {
        cout << desc << endl;
        return 1;
    }

    if (!vm.count("graph")) {
        cerr << "Error: Graph file was not set." << endl;
        return 1;
    }
    string graphPath;
    if (vm["experiment"].as<bool>()) {
        graphPath = "../experiments/experimental_graphs/";
    } else {
        graphPath = "../public_graphs/";
    }

    string graphName = vm["graph"].as<std::string>();  
  	GraphReader graphReader(graphPath + graphName);

  	NetworKit::Graph readGraph = graphReader.readEdgesFormatGraph();
  	NetworKit::Graph *graph = &readGraph;
   	mytimer t_counter;
   	int k = 20000;
	int number_edges = graph->numberOfEdges();
	int number_nodes = graph->numberOfNodes();
	vector<int> prova = naive_fvs(graph, k, F);

	if (std::find(prova.begin(), prova.end(), -1) != prova.end()) {
	    cout << "Feedback Vertex Set: None" << endl;
	    cout << "There is no FVS of size " << k << endl;
	} else {
	    cout << "Feedback Vertex Set: ";
	    printVector(&prova);
	    cout << "Size FVS: " << prova.size() << endl;
	}

	cout << "number_edges: " << number_edges << endl;
	cout << "number_nodes: " << number_nodes << endl;
	cout << "elapsed_time: " << t_counter.elapsed() << "\n";

	return 0;
}
