files = $(wildcard *.cc)
OBJS = $(addsuffix .o,$(basename $(files)))
garbage = $(wildcard *~ *.o)
felgergarb = $(wildcard eventdict* *.root *.so test)

OPT = -O -Wall -fPIC

ROOTINC := $(shell root-config --cflags)
ROOTLIBS := $(shell root-config --glibs)

INC = -I. $(ROOTINC)

LIBS = -L. -lEvent $(ROOTLIBS)

.cc.o:
	$(CXX) $(OPT) $(INC) -c $*.cc

.cpp.o:
	$(CXX) $(OPT) $(INC) -c $*.cpp

all:
	@$(MAKE) eventdict.cc; $(MAKE) compile; $(MAKE) libEvent.so

eventdict.cc: 
	rootcint -f eventdict.cc -c -I. Random.h Plot.h LinkDef.h

compile: $(OBJS)

libEvent.so: $(OBJS)
	$(CXX) -shared $(ROOTLIBS) -O *.o -o libEvent.so

test: test.o
	$(CXX) -O test.o $(LIBS) -o test

clean:
	rm $(garbage)

cleanAll:
	$(MAKE) clean; rm $(felgergarb)

