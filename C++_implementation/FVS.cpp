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

vector<int> naive_fvs (NetworKit::Graph* graph, int k, set<int>* F  ) {

	vector<int> myfvs;

	if (k < 0){
		myfvs.push_back(-1);
		return myfvs;
	}

	if (graph->numberOfNodes() == 0) {

		cout << "there are any node!" <<endl;
		myfvs.push_back(-1);
		return myfvs;
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
        				//cout << "Il vicino di"<< *node << "è:"<<*neighbor  <<endl;

				    if (F->find(*neighbor) != F->end()) {
				    	neighborCount ++;   
				    } 

			if (neighborCount == 2){

				cout << *node <<endl;

				graph->removeNode(*node);
				myfvs = naive_fvs(graph,k-1,F);
				myfvs.push_back(*node);
				return myfvs;
					
			}   		 
        	}
    }       
    }

    int maxDegree = 0;
    int NodeMaxDegree = -1;

    for (NetworKit::Graph::NodeIterator node = nodeRange.begin(); node != nodeRange.end(); ++node) {
    	
        if (F->find(*node) == F->end()) {
        	if (graph->degree(*node) >= maxDegree){
        		NodeMaxDegree = *node;
        		maxDegree = graph->degree(*node);
				}	
			}
        }
	    if (maxDegree == 2){

	    	vector<int> nodesCycle;

	    	while (true){

	    		nodesCycle = findCycle(graph);
	    		if (nodesCycle.size() == 0){
	    			break;
	    		}
	    		for (int node : nodesCycle){

	    			if (F->find(node) == F->end()){

	    				myfvs.push_back(node);
	    				graph->removeNode(node);
	    			} 
	    		}

	    	}
	    	if (myfvs.size()<=k){
	    		return myfvs;
	    	}
			else {
	    		vector<int> NotArray;
	    		NotArray.push_back(-1);
	    		return NotArray;
	    	}
	    }

    	graph->removeNode(NodeMaxDegree);
	    myfvs = naive_fvs(graph,k,F);

	    if (myfvs.size() != 1 && myfvs[0] != -1){

	    	myfvs.push_back(NodeMaxDegree);
	    	return myfvs;
	    }
	    F->insert(NodeMaxDegree);
		return naive_fvs(graph,k,F);
}
  
int main(int argc, char** argv) {
 
	set<int> *F = new set <int>;  
	NetworKit::Graph* graph = new NetworKit::Graph(10,false,false);
	graph->addEdge(0, 1);
    graph->addEdge(1, 2);
    graph->addEdge(2, 3);
    graph->addEdge(3, 4);
    graph->addEdge(4, 0);
/*
    vector<int> myVector;
   	NetworKit::Graph::NodeRange nodeRange = graph->nodeRange();
    //Now you can iterate over the nodes using the iterator range
    for (NetworKit::Graph::NodeIterator it = nodeRange.begin(); it != nodeRange.end(); ++it) {
    	
         myVector.push_back(*it);
    }
     for (int i=0; i<myVector.size(); i++){

     	cout << myVector[i] << endl;
     }
*/
	 vector<int> prova = naive_fvs(graph,10, F);
	 for (int node : prova){
	 	cout << node << endl;
	 }

	return 0;  
}