First download data at https://opendata.cern.ch/record/12353.

Open root and run: 
TFile *f = TFile::Open("DYJetsToLL.root");
TTree *t = (TTree*)f->Get("Events");
t->MakeSelector("MySelector");
Open the root file and create a Tree using the events then use MakeSelector method which creates MySelector.h and MySelector.C files. 
MySelector.h and MySelector.C define a class that inherits from TSelector.
Next edit the MySelector.h and MySelector.C files to select the trigger and pileup according to the exercise. 

Then run:
t->Process("MySelector.C+");


