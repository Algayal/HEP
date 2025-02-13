CXX = g++
CXXFLAGS = -Wall -fPIC
LDFLAGS = -shared

all: test

libMET.so: ReconstructedTrack.o Simulation.o
	$(CXX) $(LDFLAGS) -o libMET.so ReconstructedTrack.o Simulation.o

ReconstructedTrack.o: ReconstructedTrack.cpp ReconstructedTrack.h
	$(CXX) $(CXXFLAGS) -c ReconstructedTrack.cpp -o ReconstructedTrack.o

Simulation.o: Simulation.cpp Simulation.h ReconstructedTrack.h
	$(CXX) $(CXXFLAGS) -c Simulation.cpp -o Simulation.o

test: test.cpp libMET.so
	$(CXX) test.cpp -L. -lMET -Wl,-rpath,. -o test

clean:
	rm -f test libMET.so *.o
