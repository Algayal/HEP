CXX = g++
CXXFLAGS = -Wall -fPIC

all: main

libMET.so: MET.cpp MET.h
	$(CXX) -shared $(CXXFLAGS) -o libMET.so MET.cpp

main: main.cpp libMET.so
	$(CXX) main.cpp -L. -lMET -Wl,-rpath,. -o main

clean:
	rm -f main libMET.so

cleanAll:
	rm -f *.o, *.so