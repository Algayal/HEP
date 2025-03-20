For installation run: make 
To run the program: make events
./test.job 

Event generator doesn't work as intended because I couldn't install CTEQ6L1 structure functions correctly.
This is why the output file is empty, but the idea would have been to generate the events, save it into txt file, then
write a pyroot code to do the plotting. Idealy, one could write one c++ code utilizing root a pythia, but I ran into problems with the Makefile 