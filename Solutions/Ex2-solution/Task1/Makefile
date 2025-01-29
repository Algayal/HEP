# Compiler
CXX = g++
# Compilation flags
CXXFLAGS = -O2 -Wall
# Source files
SRC = hello_world.cpp
# Object files
OBJ = hello_world.o
# Executable name
EXE = hello_world.exe

# Rule to build the executable
$(EXE): $(OBJ)
	$(CXX) $(CXXFLAGS) $(OBJ) -o $(EXE)

# Rule to compile .cpp files into .o files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean rule
clean:
	rm -f $(OBJ) $(EXE)
	rm -rf *.out
