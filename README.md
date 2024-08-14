Algorithm Engineering Project:

This repository contains an implementation of an algorithm for finding a minimum feedback vertex set, of size almosto k, in undirected graphs, as described in the paper  [link](https://drops.dagstuhl.de/storage/01oasics/oasics-vol061_sosa2018/OASIcs.SOSA.2018.1/OASIcs.SOSA.2018.1.pdf). The algorithm is implemented in both Python and C++, and includes validation testing to ensure correctness. Additionally, the time complexity of the implementations is evaluated, with a comparison between the two programming languages.

Installation steps for running python implementation (Debian based OS):

1) installing python3 and pip3. 
2) installing the necessary python packages. (pip3 install -r requirements.txt)

Installation steps for running C++ implementation (Debian based OS):

1) installing g++:
(sudo apt install g++ )
2) installing cmake:
 (sudo apt install cmake)
3) installing gpp:
 (sudo apt install gpp)
5) installing libboost filesystem library:
 (sudo apt install libboost-filesystem-dev)
6) installing libboost serialization library:
 (sudo apt install libboost-serialization-dev) 
7) installing libboost_program_options library:
 (sudo apt install libboost-program-options-dev)
8) installing libboost_timer library:
 (sudo apt install libboost-timer-dev)
9) installing networkit, for graph managment:
	[installation link](https://networkit.github.io/)

10) In order to make the dynamic libraries (.so files) available to the running programm they must me moved to a system path, (for example /usr/lib, /lib, /usr/local/lib).
Otherwise we can set the LD_LIBRARY_PATH environment variable to networkit library build folder; To make the changes to library paths persistent on a Linux system, add the following line to the ~/.bashrc file:
export LD_LIBRARY_PATH=location/networkit/build/

then, source ~/.bashrc.

Once the initial setup is completed, you can run the python implementation on a choosen graph just following this steps:
1) Write the input_graph in a file (graph_name) within the public_graphs directory in edge-list format , every line of the file must be ad edge of the graph.
2) navigate to 'python_implementation' directory
3) python3 FVS.py --graph graph_name

To run the C++ implementation:
1) Write the input_graph in a file (graph_name) within the public_graphs directory in edge-list format , every line of the file must be ad edge of the graph.
2) compile the source code:
 To obtain an optimized version of the binary (make release)
 To obtain a ready to debug version of the binary (make debug)
3) ./FVS --graph graph_name

In the experiments directory, there is all the code for the experiments creation, is divided
into python classes, using the principles of OOP to make the tests
easily maintainable and replicable. 
In order to replicate an experiment just run the experiment_main.py script, present in this folder, the generated graphs for tests can be found in experimental_graphs folder and the  test results can be found under experimental_results one.