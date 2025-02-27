#ifndef PLOT_H
#define PLOT_H

#include "TFile.h"
#include "TTree.h"
#include "TH1F.h"
#include "TCanvas.h"
#include "TObject.h"

class Plot :  public TObject{
public:
    Plot();
    ~Plot();
    void hist_plot();


private:
    ClassDef(Plot,1)

};

#endif