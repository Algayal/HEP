#ifndef MET_H
#define MET_H
#include <iostream>
#include <vector>

class MET
{
public:
    MET();
    ~MET();

    // functions to access private variables and functions
    void printphi();
    void printx();
    void printy();

private:
    std::vector<int> x = {2,4,3}; //3D example values
    std::vector<int> y = {6,3,4}; //3D example values
    float phi();
};


#endif