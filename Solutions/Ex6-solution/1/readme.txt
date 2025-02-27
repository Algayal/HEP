The following commands produce the desired histograms:

make 
root 
gSystem->Load("libTree");
gSystem->Load("libHist");
gSystem->Load("libEvent.so");

Then one has access to the classes Random and Plot
Random r;
r.random_gaus();
Plot p;
p.hist_plot();

"I have some problems with conflicting versions of Root, so I cannot run make test"
