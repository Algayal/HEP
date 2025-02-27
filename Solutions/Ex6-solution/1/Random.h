#ifndef RANDOM_H
#define RANDOM_H


#include "TFile.h"
#include "TTree.h"
#include "TRandom3.h"
#include "TObject.h"

class Random : public TObject {
public:
    Random();
    ~Random();
    void random_gaus();

private:
    ClassDef(Random,1)
};

#endif