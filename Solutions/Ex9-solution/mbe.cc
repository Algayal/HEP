#include "Pythia8/Pythia.h"
#include <fstream> 
using namespace Pythia8;

int main(){
  Pythia pythia;
  
  //Simulating the proton-proton collision at LHC
  pythia.readString("Beams:idA = 2212");  
  pythia.readString("Beams:idB = 2212");  

  // Setting the center-of-mass energy
  pythia.readString("Beams:eCM = 13600.");

  // Minimum bias processes
  pythia.readString("SoftQCD:all = on");  
  pythia.init();


  int nEvent = 50000;

  std::ofstream outFile("muons.txt");  

  for (int iEvent = 0; iEvent < nEvent; ++iEvent) {
    if (!pythia.next()) continue; // Skips in event fails

    for (int i = 0; i < pythia.event.size(); ++i) {
      if (!pythia.event[i].isFinal()) continue;
      // Select muons only id=+-13
      if (abs(pythia.event[i].id()) != 13) continue; 

      double pT = pythia.event[i].pT();
      double eta = pythia.event[i].eta();

      outFile << pT << " " << eta << "\n";
    }
  }

  outFile.close();
  pythia.stat();
  return 0;
}