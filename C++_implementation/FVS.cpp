#include <iostream>
#include <boost/program_options.hpp>
#include <omp.h>
#include <networkit/graph/Graph.hpp>
#include <vector>
#include <set>
#include <string>
#include "cycle_detection.h"
#include "mytimer.h"

using namespace std;


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
				    else{

				    	result->push_back(-1);
						return *result;
				    }

							
				}   		 
	    	}
    	}       
    }
   
    vector<int> maximum_degree_information = provide_node_with_maximum_degree(graph, F, nodeRange);
	if (maximum_degree_information[0] == 2){

		vector<int> nodesCycle;
		vector<int> *X = new vector<int>;

		while (true){

			nodesCycle = findCycle(graph);
			if (nodesCycle.size() == 0){
				break;
			}
			
			int node = nodesCycle[0];
			for (int node : nodesCycle){

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
		else {
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

	//F->insert(2);
	NetworKit::Graph* graph = new NetworKit::Graph(15,false,false);
	
	graph->addEdge(0, 1);
    graph->addEdge(1, 2);
    graph->addEdge(2, 3);
    graph->addEdge(3, 4);
    graph->addEdge(4, 0);
    
   	graph->addEdge(4, 2);
   	/*
   
    graph->addEdge(0, 5);
    graph->addEdge(1, 5);
    graph->addEdge(1, 6);
    graph->addEdge(2, 6);
    graph->addEdge(3, 7);
    graph->addEdge(6, 7);
    graph->addEdge(7, 8);
    graph->addEdge(0, 9);
    graph->addEdge(0, 10);
    graph->addEdge(2, 10);
    graph->addEdge(7,11);
    graph->addEdge(8,11);
    graph->addEdge(8,12);
    graph->addEdge(12,13);
    graph->addEdge(5,13);
    graph->addEdge(14,13);
    graph->addEdge(14,12);
    */
   	

    /*
    graph->addEdge(0, 1);
    graph->addEdge(0, 2);
    graph->addEdge(0, 3);
    graph->addEdge(1 ,3);
    graph->addEdge(1, 4);
    graph->addEdge(1, 2);
    graph->addEdge(2, 3);
    graph->addEdge(2, 4);
    graph->addEdge(3, 4);
    graph->addEdge(4, 0);
  	*/
    
    

	 vector<int> prova = naive_fvs(graph,5, F);
	 for (int node : prova){
	 	cout << node << endl;
	 }

	return 0;  
}