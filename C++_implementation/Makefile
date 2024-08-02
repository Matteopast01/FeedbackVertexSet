CXX = g++ -std=c++17
DBG = -g
OPT = -Ofast -DNDEBUG -march=native
VALGRIND = -g -DNDEBUG


OPTIONS = -lboost_serialization -lboost_program_options -lboost_system -lboost_filesystem -fopenmp -lnetworkit -lboost_timer

INCLUDEPATH = $(HOME)/networkit/include/ -I/usr/include/valgrind  -I$(HOME)/networkit/extlibs/tlx/ -I$(HOME)/networkit/extlibs/ttmath/
PATHLIB = $(HOME)/networkit/build/

TARGETS = FVS

debug:
	$(foreach var,$(TARGETS),$(CXX) $(DBG) -o $(var) -I$(INCLUDEPATH) -L$(PATHLIB) $(var).cpp Cycle_detection.cpp GraphReader.cpp $(OPTIONS);)

release:
	$(foreach var,$(TARGETS),$(CXX) $(OPT) -o $(var) -I$(INCLUDEPATH) -L$(PATHLIB) $(var).cpp Cycle_detection.cpp GraphReader.cpp $(OPTIONS);)

valgrind:
	$(foreach var,$(TARGETS),$(CXX) $(VALGRIND) -o $(var) -I$(INCLUDEPATH) -L$(PATHLIB) $(var).cpp Cycle_detection.cpp GraphReader.cpp $(OPTIONS);)


clean:
	$(foreach var,$(TARGETS),rm -rf $(var);)

